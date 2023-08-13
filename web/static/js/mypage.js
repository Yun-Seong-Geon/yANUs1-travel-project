const links = document.querySelectorAll('.link');
const pageContent = document.getElementById('pageContent');

links.forEach(function(link) {
  link.addEventListener('click', function() {
    pageContent.classList.toggle('show'); // 'show' 클래스를 토글
  });
});
