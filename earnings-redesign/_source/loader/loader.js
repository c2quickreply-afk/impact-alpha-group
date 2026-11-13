/* ---------- preloader ---------- */
window.addEventListener("load", () => {
  setTimeout(() => {
    document.getElementById("loader").classList.add("done");
    document.getElementById("heroTitle").classList.add("play");
    document.querySelector(".hero").classList.add("play");
    if (window.__startTree) window.__startTree();   // tree begins growing as the curtain lifts
  }, prefersReduced ? 100 : 2650);   // bar hits 100% → emblem booms → curtain lifts
});
