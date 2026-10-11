// Reattach the catalog filter when Material replaces the page content.
(function () {
  function initializeCatalog() {
    if (!/\/catalog\/(?:index\.html)?$/.test(window.location.pathname)) return;
    var table = document.querySelector('.md-typeset table');
    var $ = window.jQuery;
    if (!table || !$ || !$.fn.dataTable || $.fn.dataTable.isDataTable(table)) return;
    $(table).DataTable({pageLength: 25, order: [[2, 'desc']]});
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
