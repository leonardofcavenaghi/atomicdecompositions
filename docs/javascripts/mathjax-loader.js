(function () {
  if (window.geoatomsMathjax) { window.geoatomsMathjax.refresh(); return; }
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
  },
  svg: {fontCache: 'local'}
};

// Material for MkDocs replaces the article body during instant navigation.
// MathJax observes the first page load automatically, but it does not know
// about those later DOM replacements unless we ask it to typeset the new body.
(function () {
  var typesetting = false;
  var requested = false;
  var previousArticle = null;
  var loading = false;
  var loadAttempts = 0;
  var renderAttempts = 0;
  var loaderURL = document.currentScript && document.currentScript.src;
  var sources = [
    new URL('../assets/mathjax/tex-mml-svg.js', loaderURL || document.baseURI).href,
    'https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-mml-svg.js',
    'https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-svg.js'
  ];

  function clearNotice() {
    var notice = document.getElementById('math-render-status');
    if (notice) notice.remove();
  }

  function showRetry() {
    if (document.getElementById('math-render-status') || !document.querySelector('.arithmatex')) return;
    var notice = document.createElement('p');
    notice.id = 'math-render-status';
    notice.setAttribute('role', 'status');
    notice.appendChild(document.createTextNode('Mathematical formulas could not load. '));
    var retry = document.createElement('button');
    retry.type = 'button';
    retry.textContent = 'Retry';
    retry.addEventListener('click', function () {
      loadAttempts = 0;
      renderAttempts = 0;
      clearNotice();
      typesetArticle();
    });
    notice.appendChild(retry);
    var article = document.querySelector('[data-md-component="content"]');
    if (article) article.prepend(notice);
  }

  function loadRuntime() {
    if (loading || (window.MathJax && typeof window.MathJax.typesetPromise === 'function')) return;
    if (loadAttempts >= sources.length) { showRetry(); return; }
    loading = true;
    var script = document.createElement('script');
    script.id = 'MathJax-script';
    script.async = true;
    script.src = sources[loadAttempts % sources.length];
    loadAttempts += 1;
    var settled = false;
    var timeout = setTimeout(failed, 8000);
    function failed() {
      if (settled) return;
      settled = true;
      clearTimeout(timeout);
      loading = false;
      script.remove();
      if (loadAttempts < sources.length) setTimeout(loadRuntime, 300 * loadAttempts);
      else showRetry();
    }
    script.addEventListener('load', function () {
      if (settled) return;
      settled = true;
      clearTimeout(timeout);
      loading = false;
      typesetArticle();
    });
    script.addEventListener('error', failed);
    document.head.appendChild(script);
  }

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
    // Published pages already contain complete SVG and accessible MathML.
    // The browser runtime is needed only for newly inserted source content.
    var pendingSource = Array.from(document.querySelectorAll('.arithmatex')).some(function (node) {
      return !node.querySelector('mjx-container');
    });
    if (!pendingSource) { clearNotice(); return; }
    requested = true;
    var math = window.MathJax;
    if (!math || typeof math.typesetPromise !== "function") { loadRuntime(); return; }
    if (typesetting) return;
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
        renderAttempts = 0;
        clearNotice();
        revealHash();
      }
    }).catch(function (error) {
      console.error("Formula rendering failed", error);
      renderAttempts += 1;
      if (renderAttempts <= 2) setTimeout(typesetArticle, 500 * renderAttempts);
      else showRetry();
    }).finally(function () {
      typesetting = false;
      if (requested) typesetArticle();
    });
  }

  window.geoatomsMathjax = {refresh: typesetArticle};

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
  window.addEventListener("pageshow", typesetArticle);
  window.addEventListener('online', function () {
    loadAttempts = 0;
    renderAttempts = 0;
    typesetArticle();
  });
  // Content can arrive after startup or outside Material's document$ event.
  // Observe new source containers, ignoring MathJax's own generated children.
  var observer = new MutationObserver(function (mutations) {
    var addedMath = mutations.some(function (mutation) {
      return Array.from(mutation.addedNodes).some(function (node) {
        return node.nodeType === 1 && (node.matches('.arithmatex') || node.querySelector('.arithmatex'));
      });
    });
    if (addedMath) typesetArticle();
  });
  observer.observe(document.body, {childList: true, subtree: true});
  typesetArticle();
})();

})();
