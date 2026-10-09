/* Bot-safe contact links.
 *
 * The e-mail address is never present in the served HTML as a plain string or
 * mailto: URL. Elements carry the local part and domain in separate data
 * attributes and are wired up at render time, which defeats naive harvesters
 * while staying one click for humans.
 */
(function () {
  "use strict";

  function activate() {
    var nodes = document.querySelectorAll("a.email-link");
    Array.prototype.forEach.call(nodes, function (el) {
      var user = el.getAttribute("data-user");
      var domain = el.getAttribute("data-domain");
      if (!user || !domain) {
        return;
      }
      var address = user + String.fromCharCode(64) + domain;
      el.href = "mai" + "lto:" + address;
      el.setAttribute("title", address);
      if (el.hasAttribute("data-plain")) {
        el.textContent = address;
      }
    });
  }

  /* Material for MkDocs instant navigation re-renders pages client side. */
  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(activate);
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", activate);
  } else {
    activate();
  }
})();
