// Reattach the catalog filter when Material replaces the page content.
(function () {
  function initializeCatalog() {
    var dimensionPage = /\/catalog\/(?:points-curves|surfaces|threefolds|fourfolds|fivefolds|higher-dimensional)\/(?:index\.html)?$/.test(window.location.pathname);
    var atomicPage = /\/catalog\/atomic-invariants\/(?:index\.html)?$/.test(window.location.pathname);
    if (!dimensionPage && !atomicPage && !/\/catalog\/(?:index\.html)?$/.test(window.location.pathname)) return;
    var table = document.querySelector(atomicPage ? '.atomic-index table' : '.md-typeset table');
    var $ = window.jQuery;
    if (!table || !$ || !$.fn.dataTable || $.fn.dataTable.isDataTable(table)) return;
    $(table).DataTable({pageLength: 25, order: atomicPage ? [[1, 'desc'], [0, 'asc']] : [[2, 'desc'], [3, 'desc'], [0, 'asc']]});
  }
  if (typeof document$ !== 'undefined' && document$.subscribe) {
    document$.subscribe(initializeCatalog);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeCatalog);
  } else {
    initializeCatalog();
  }
})();

