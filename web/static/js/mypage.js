const links_info = document.querySelectorAll('.link-info');
const pageContent_info = document.getElementById('pageContent-info');

links_info.forEach(function(link) {
  link.addEventListener('click', function() {
    // pageContent_search 창이 열려 있으면 닫기
    if (pageContent_search.classList.contains('show')) {
      pageContent_search.classList.remove('show');
    }
    pageContent_info.classList.toggle('show'); // 'show' 클래스를 토글
  });
});

const links_search = document.querySelectorAll('.link-search');
const pageContent_search = document.getElementById('pageContent-search');

links_search.forEach(function(link) {
  link.addEventListener('click', function() {
    // pageContent_info 창이 열려 있으면 닫기
    if (pageContent_info.classList.contains('show')) {
      pageContent_info.classList.remove('show');
    }
    pageContent_search.classList.toggle('show'); // 'show' 클래스를 토글
  });
});