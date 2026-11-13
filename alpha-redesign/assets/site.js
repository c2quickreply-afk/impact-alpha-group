/* ==========================================================================
   IMPACT — shared script for both sites (no dependencies)
   0. Motion control   1. Loader   2. Nav & mobile menu   3. Scroll reveals
   4. Counters   5. Hero visuals   6. Scroll-lit statement   7. Feature visuals
   8. Topics accordion   9. Contact form
   No inline scripts anywhere, so the CSP can stay at script-src 'self'.
   ========================================================================== */
(function () {
  "use strict";
  var root = document.documentElement;
  var reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;
  var finePointer = matchMedia("(hover: hover) and (pointer: fine)").matches;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------- 0. MOTION CONTROL -----------------------------------------
     Anything that moves on its own (hero sequences, call timer, looping CSS
     animations) stops for visitors who ask for reduced motion, and the
     footer "Pause animations" button stops it for everyone else (WCAG 2.2.2). */
  var motion = {
    paused: reduced,
    subs: [],
    set: function (p) {
      this.paused = p;
      root.classList.toggle("motion-paused", p);
      this.subs.forEach(function (fn) { fn(p); });
      $$(".motion-toggle").forEach(function (b) {
        b.setAttribute("aria-pressed", p ? "true" : "false");
        b.textContent = p ? "Play animations" : "Pause animations";
      });
    }
  };
  $$(".motion-toggle").forEach(function (b) { b.addEventListener("click", function () { motion.set(!motion.paused); }); });
  motion.set(motion.paused);

  /* ---------- 1. LOADER --------------------------------------------------
     Original timing preserved: window.load + 2650ms (100ms reduced motion).
     Extras: first page of a visit only, hard fallback so it always lifts. */
  var started = false;
  var startHandlers = [];
  function onStart(fn) { started ? fn() : startHandlers.push(fn); }
  function startPage() {
    if (started) return;
    started = true;
    var hero = $(".hero");
    if (hero) hero.classList.add("play");
    startHandlers.forEach(function (fn) { fn(); });
  }

  var loader = document.getElementById("loader");
  if (!loader || root.classList.contains("no-loader")) {
    if (loader) loader.remove();
    startPage();
  } else {
    var dismissed = false;
    var dismiss = function () {
      if (dismissed) return;
      dismissed = true;
      loader.classList.add("done");
      try { sessionStorage.setItem("ie_loader_seen", "1"); } catch (e) {}
      startPage();
      setTimeout(function () { loader.remove(); }, 900);
    };
    var afterLoad = function () { setTimeout(dismiss, reduced ? 100 : 2650); };
    if (document.readyState === "complete") afterLoad();
    else addEventListener("load", afterLoad);
    setTimeout(dismiss, reduced ? 1500 : 6000);   // never wait on a slow asset
  }

  /* ---------- 2. NAV & MOBILE MENU -------------------------------------- */
  var nav = document.getElementById("nav");
  var onScrollNav = function () { if (nav) nav.classList.toggle("scrolled", scrollY > 8); };
  addEventListener("scroll", onScrollNav, { passive: true });
  onScrollNav();

  var burger = document.getElementById("burger");
  var menu = document.getElementById("mobileMenu");
  /* Menu behaves like a dialog: focus moves in, Tab stays inside (menu +
     burger), Esc closes, focus returns to the burger. Page behind is inert. */
  var mainEl = document.getElementById("main"), footEl = $(".footer");
  function setMenu(open) {
    var was = root.classList.contains("menu-open");
    root.classList.toggle("menu-open", open);
    if (burger) {
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      burger.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    }
    [mainEl, footEl].forEach(function (el) { if (el) { if (open) el.setAttribute("inert", ""); else el.removeAttribute("inert"); } });
    if (open && !was) { var first = $("a", menu); if (first) setTimeout(function () { first.focus(); }, 50); }
    if (!open && was && burger && menu.contains(document.activeElement)) burger.focus();
  }
  if (burger && menu) {
    burger.addEventListener("click", function () { setMenu(!root.classList.contains("menu-open")); });
    $$("a", menu).forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });
    addEventListener("keydown", function (e) {
      if (!root.classList.contains("menu-open")) return;
      if (e.key === "Escape") { setMenu(false); burger.focus(); return; }
      if (e.key !== "Tab") return;
      var f = [burger].concat($$("a, button", menu));
      var i = f.indexOf(document.activeElement);
      if (e.shiftKey && i <= 0) { e.preventDefault(); f[f.length - 1].focus(); }
      else if (!e.shiftKey && i === f.length - 1) { e.preventDefault(); f[0].focus(); }
      else if (i === -1) { e.preventDefault(); f[0].focus(); }
    });
    addEventListener("resize", function () { if (innerWidth > 1024) setMenu(false); });
  }

  /* ---------- 3. SCROLL REVEALS ------------------------------------------
     Toggle (not one-shot): elements play in every time they enter, in either
     direction, and fade out only once they are essentially off-screen. */
  $$("[data-stagger]").forEach(function (g) {
    Array.prototype.forEach.call(g.children, function (c, i) { c.style.setProperty("--i", i); });
  });
  var revealEls = $$("[data-reveal],[data-stagger]");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { e.target.classList.toggle("in", e.isIntersecting); });
    }, { threshold: 0, rootMargin: "-5% 0px -5% 0px" });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  }

  /* run fn(true) when el enters view, fn(false) when it leaves */
  function watch(el, fn, threshold) {
    if (!("IntersectionObserver" in window)) { fn(true); return; }
    new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { fn(e.isIntersecting); });
    }, { threshold: threshold || 0.3 }).observe(el);
  }

  /* ---------- 4. COUNTERS ------------------------------------------------ */
  $$("[data-count]").forEach(function (el) {
    var end = +el.dataset.count, raf = 0;
    if (reduced) return;
    watch(el, function (inView) {
      cancelAnimationFrame(raf);
      if (!inView) { el.textContent = "0"; return; }
      var t0 = performance.now(), dur = 1600;
      (function tick(t) {
        var p = Math.min((t - t0) / dur, 1);
        el.textContent = Math.round(end * (1 - Math.pow(1 - p, 4)));
        if (p < 1) raf = requestAnimationFrame(tick);
      })(t0);
    }, 0.6);
  });

  /* ---------- 5. HERO VISUAL --------------------------------------------- */
  var pipe = document.getElementById("pipe");
  var heroVisible = true;
  if (pipe) {
    var nodes = $$(".pn", pipe), fill = $(".pipe-fill", pipe);
    var detail = document.getElementById("pipeDetail");
    var stepText = [
      "Data streams in from the market: prices, volume and news.",
      "An AI model looks for patterns in that data.",
      "Your rules decide what\u2019s allowed: position size, limits, stop points.",
      "Only then is an order placed, and every step is logged for review."
    ];
    var phase = 0, timer = 0;
    var setPhase = function (n) {
      phase = n % 4;
      nodes.forEach(function (el, i) { el.classList.toggle("on", i === phase); el.classList.toggle("done", i < phase); });
      fill.style.width = (phase / 3 * 100) + "%";
      detail.classList.add("swap");
      setTimeout(function () {
        $(".pd-n", detail).textContent = "0" + (phase + 1);
        $("p", detail).textContent = stepText[phase];
        detail.classList.remove("swap");
      }, reduced ? 0 : 250);
    };
    var loop = function () {
      clearInterval(timer);
      pipe.classList.toggle("run", !motion.paused);
      if (motion.paused || !heroVisible) return;
      timer = setInterval(function () { setPhase(phase + 1); }, 2600);
    };
    onStart(function () { setTimeout(loop, 1200); });
    motion.subs.push(function () { if (started) loop(); });
    watch(pipe, function (v) { heroVisible = v; if (started) loop(); }, 0.1);

    /* call timer in the window's title bar */
    var clock = document.getElementById("callTime");
    if (clock) onStart(function () {
      var secs = 0;
      setInterval(function () {
        if (motion.paused || !heroVisible) return;
        secs++;
        var m = Math.floor(secs / 60), s = secs % 60;
        clock.textContent = (m < 10 ? "0" : "") + m + ":" + (s < 10 ? "0" : "") + s;
      }, 1000);
    });

    /* gentle pointer parallax: the heaviest effect stays in the hero */
    var hv = document.getElementById("heroVisual");
    if (hv && finePointer && !reduced) {
      var tx = 0, ty = 0, cx = 0, cy = 0, running = false;
      var heroEl = $(".hero");
      var step = function () {
        cx += (tx - cx) * 0.08; cy += (ty - cy) * 0.08;
        hv.style.transform = "perspective(1400px) rotateY(" + (cx * 4).toFixed(2) + "deg) rotateX(" + (cy * -3).toFixed(2) + "deg)";
        if (Math.abs(tx - cx) > 0.001 || Math.abs(ty - cy) > 0.001) requestAnimationFrame(step); else running = false;
      };
      heroEl.addEventListener("mousemove", function (e) {
        var r = heroEl.getBoundingClientRect();
        tx = (e.clientX - r.left) / r.width - 0.5;
        ty = (e.clientY - r.top) / r.height - 0.5;
        if (!running) { running = true; requestAnimationFrame(step); }
      });
      heroEl.addEventListener("mouseleave", function () { tx = 0; ty = 0; if (!running) { running = true; requestAnimationFrame(step); } });
    }
  }

  /* Alpha: initiative alignment map. Partners light up one by one, the stage
     bar advances, and the caption explains each step. Illustrative only. */
  var amap = document.getElementById("amap");
  if (amap) {
    var anodes = $$(".am-node", amap), alines = $$(".am-line", amap), astages = $$(".am-stage", amap);
    var adetail = document.getElementById("amDetail");
    var acap = anodes.map(function (n) { return n.getAttribute("data-cap"); });
    var ak = 0, atimer = 0, amapVisible = true;
    var aset = function (k) {
      ak = k;
      anodes.forEach(function (n, i) { n.classList.toggle("on", i < k); n.classList.toggle("now", i === k - 1); });
      alines.forEach(function (l, i) { l.classList.toggle("on", i < k); });
      var st = Math.min(astages.length, Math.ceil(k / anodes.length * astages.length));
      astages.forEach(function (s, i) { s.classList.toggle("on", i < st); });
      if (adetail) adetail.textContent = k === 0 ? adetail.getAttribute("data-start") : acap[k - 1];
    };
    var aloop = function () {
      clearInterval(atimer);
      if (motion.paused) { aset(anodes.length); return; }   // still: show the finished map
      if (!amapVisible) return;
      atimer = setInterval(function () { aset(ak >= anodes.length ? 0 : ak + 1); }, 1700);
    };
    onStart(function () { setTimeout(aloop, 900); });
    motion.subs.push(function () { if (started) aloop(); });
    watch(amap, function (v) { amapVisible = v; if (started) aloop(); }, 0.1);
    if (reduced) aset(anodes.length);
  }

  /* ---------- 6. SCROLL-LIT STATEMENT ------------------------------------ */
  var st = document.getElementById("statement");
  if (st) {
    var em = (st.dataset.em || "").split(/\s+/).filter(Boolean);
    var words = st.textContent.trim().split(/\s+/);
    st.innerHTML = words.map(function (w) {
      return '<span class="w' + (em.indexOf(w) > -1 ? " em" : "") + '">' + w + "</span>";
    }).join(" ");
    var spans = $$(".w", st);
    if (reduced) spans.forEach(function (s) { s.classList.add("lit"); });
    else {
      var ticking = false;
      var paint = function () {
        ticking = false;
        var r = st.getBoundingClientRect();
        var p = (innerHeight * 0.88 - r.top) / (r.height + innerHeight * 0.35);
        p = Math.min(Math.max(p, 0), 1);
        var lit = Math.ceil(p * spans.length);
        spans.forEach(function (s, i) { s.classList.toggle("lit", i < lit); });
      };
      addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(paint); } }, { passive: true });
      addEventListener("resize", paint);
      paint();
    }
  }

  /* ---------- 7. FEATURE VISUALS (replay each time they enter) ---------- */
  $$('[data-anim="eval"]').forEach(function (card) {
    var rows = $$(".eval-row", card), timers = [];
    var labels = ["Covered", "Covered", "Covered"];
    watch(card, function (v) {
      timers.forEach(clearTimeout); timers = [];
      rows.forEach(function (r, i) {
        var state = $(".eval-state", r);
        if (!v) { r.classList.remove("done"); state.textContent = "Up next"; return; }
        timers.push(setTimeout(function () { r.classList.add("done"); state.textContent = labels[i]; }, reduced ? 0 : 450 + i * 550));
      });
    }, 0.35);
  });

  $$('[data-anim="checks"]').forEach(function (card) {
    var items = $$(".checks li", card), fg = $(".ring .fg", card), n = $(".ring-n", card), timers = [];
    var C = 163.4;
    var set = function (k) { n.textContent = k; fg.style.strokeDashoffset = C - (C * k) / items.length; };
    watch(card, function (v) {
      timers.forEach(clearTimeout); timers = [];
      if (!v) { items.forEach(function (li) { li.classList.remove("on"); }); set(0); return; }
      items.forEach(function (li, i) {
        timers.push(setTimeout(function () { li.classList.add("on"); set(i + 1); }, reduced ? 0 : 350 + i * 260));
      });
    }, 0.35);
  });

  /* ---------- 8. TOPICS ACCORDION (phones only) -------------------------- */
  var phone = matchMedia("(max-width: 760px)");
  $$(".topic").forEach(function (t) {
    var btn = $(".topic-btn", t), panel = $(".topic-panel", t);
    btn.addEventListener("click", function () {
      if (!phone.matches) return;
      var open = !t.classList.contains("open");
      t.classList.toggle("open", open);
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      panel.style.maxHeight = open ? panel.scrollHeight + "px" : "0px";
    });
  });
  phone.addEventListener && phone.addEventListener("change", function () {
    $$(".topic").forEach(function (t) {
      t.classList.remove("open");
      $(".topic-btn", t).setAttribute("aria-expanded", "false");
      $(".topic-panel", t).style.maxHeight = "";
    });
  });

  /* ---------- 9. CONTACT FORM ------------------------------------------
     Posts in the page to FormSubmit, which emails Francene. FORM_ENDPOINT:
     once FormSubmit's random-string alias is activated, put it in place of
     the address (see README). _honey is FormSubmit's spam trap: a hidden
     field people never see; FormSubmit discards anything that fills it in. */
  var FORM_ENDPOINT = "https://formsubmit.co/ajax/francene@impactearnings.com";
  $$(".contact-form").forEach(function (f) {
    var status = $(".form-status", f);
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      status.classList.remove("err");
      var btn = $("button[type=submit]", f), orig = btn.innerHTML;
      btn.disabled = true; btn.textContent = "Sending…"; status.textContent = "Sending your message…";
      fetch(FORM_ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify({
          name: f.cname.value, email: f.cemail.value, message: f.cmessage.value,
          _honey: f._honey ? f._honey.value : "",
          _subject: "Website inquiry from " + f.cname.value, _replyto: f.cemail.value,
          _template: "table"
        })
      }).then(function (r) {
        if (!r.ok) throw new Error("send failed");
        btn.textContent = "Message sent \u2713"; f.reset();
        status.textContent = "Thank you, your message was sent.";
      }).catch(function () {
        btn.innerHTML = orig; btn.disabled = false;
        status.classList.add("err");
        status.textContent = "Something went wrong sending your message \u2014 please email francene@impactearnings.com directly.";
      });
    });
  });
})();
