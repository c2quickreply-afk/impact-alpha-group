/* Runs in <head> before first paint (tiny, blocking on purpose).
   - adds .js so reveal styles only apply when JavaScript is running
   - skips the loader on every page after the first one in a visit */
(function () {
  var d = document.documentElement;
  d.classList.add("js");
  try { if (sessionStorage.getItem("ie_loader_seen") === "1") d.classList.add("no-loader"); } catch (e) {}
})();
