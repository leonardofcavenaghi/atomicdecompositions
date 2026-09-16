window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

// Material for MkDocs replaces the article body during instant navigation.
// MathJax observes the first page load automatically, but it does not know
// about those later DOM replacements unless we ask it to typeset the new body.
(function () {
  var typesetting = false;

  function revealHash() {
    var raw = window.location.hash.slice(1);
    if (!raw) return;
    var id;
    try {
      id = decodeURIComponent(raw);
    } catch (error) {
      id = raw;
    }
    var target = document.getElementById(id);
    if (!target) return;
    var details = target.closest("details");
    if (!details) {
      // Catalog anchors are emitted immediately before their collapsible card:
      // <p><span id="...">...</span></p><details>...</details>.
      var parent = target.parentElement;
      while (parent && !details) {
        var sibling = parent.nextElementSibling;
        if (sibling && sibling.matches("details")) details = sibling;
        parent = parent.parentElement;
      }
    }
    if (details) details.open = true;
  }

  function typesetArticle() {
    revealHash();
    if (!window.MathJax || typeof window.MathJax.typesetPromise !== "function") {
      return;
    }
    var article = document.querySelector('[data-md-component="content"]');
    if (!article || typesetting) return;

    // Do not run MathJax repeatedly on an already-rendered article.  Repeated
    // calls append duplicate <mjx-container> nodes, which is especially easy
    // to trigger when a hard load and an instant navigation finish together.
    var pending = false;
    article.querySelectorAll('.arithmatex').forEach(function (node) {
      if (!node.querySelector('mjx-container')) pending = true;
    });
    if (!pending) return;

    typesetting = true;
    window.MathJax.typesetPromise([article]).catch(function () {
      // A transient navigation or a malformed third-party fragment must not
      // break the rest of the site; the next navigation will retry typesetting.
    }).then(function () {
      typesetting = false;
    });
  }

  // `document$` is supplied by the Material bundle.  The fallback keeps the
  // script usable when a page is opened as a plain static file.
  if (typeof document$ !== "undefined" && document$ && document$.subscribe) {
    document$.subscribe(typesetArticle);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", typesetArticle);
  } else {
    typesetArticle();
  }
  window.addEventListener("hashchange", function () {
    revealHash();
    typesetArticle();
  });
  // The Material document$ event can occur before the blocking MathJax CDN
  // script has loaded on a hard refresh.  The load callback covers that first
  // page while document$ handles all later instant-navigation replacements.
  window.addEventListener("load", typesetArticle);
})();
