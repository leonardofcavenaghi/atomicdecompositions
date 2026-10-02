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
  var requested = false;
  var previousArticle = null;

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
    requested = true;
    var math = window.MathJax;
    if (typesetting || !math || typeof math.typesetPromise !== "function") return;
    typesetting = true;

    // Startup and all later typesets share one queue. A navigation that
    // arrives during rendering must be processed after the active render.
    Promise.resolve(math.startup.promise).then(async function () {
      while (requested) {
        requested = false;
        revealHash();
        var article = document.querySelector('[data-md-component="content"]');
        if (!article) continue;
        if (previousArticle && previousArticle !== article) {
          math.typesetClear([previousArticle]);
        }
        previousArticle = article;
        var pending = Array.from(article.querySelectorAll('.arithmatex')).filter(function (node) {
          return !node.querySelector('mjx-container');
        });
        if (pending.length) await math.typesetPromise(pending);
        revealHash();
      }
    }).catch(function (error) {
      console.error("Formula rendering failed", error);
    }).finally(function () {
      typesetting = false;
      if (requested) typesetArticle();
    });
  }

  // Render through the same queue even if the initial navigation event
  // arrives before the MathJax runtime has finished loading.
  window.MathJax.startup = {
    typeset: false,
    ready: function () {
      MathJax.startup.defaultReady();
      MathJax.startup.promise.then(typesetArticle);
    }
  };

  // `document$` is supplied by the Material bundle.  The fallback keeps the
  // script usable when a page is opened as a plain static file.
  if (typeof document$ !== "undefined" && document$ && document$.subscribe) {
    document$.subscribe(typesetArticle);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", typesetArticle);
  } else {
    typesetArticle();
  }
  if (typeof location$ !== "undefined" && location$ && location$.subscribe) {
    location$.subscribe(typesetArticle);
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
