const links_info = document.querySelectorAll('.link-info');
const links_my = document.querySelectorAll('.link-my');
const links_search = document.querySelectorAll('.link-search');
const pageContent_info = document.getElementById('pageContent-info');
const pageContent_my = document.getElementById('pageContent-my');
const pageContent_search = document.getElementById('pageContent-search');
function showPageContent(pageElement) {
  // 우선 모든 페이지를 숨깁니다.
  pageContent_info.style.display = 'none';
  pageContent_my.style.display = 'none';
  pageContent_search.style.display = 'none';

  // 선택된 페이지만 보여줍니다.
  pageElement.style.display = 'block'; 
  pageElement.classList.add('show');
}


function setActivePage(pageName) {
    localStorage.setItem('activePage', pageName);
    switch(pageName) {
        case 'info':
            showPageContent(pageContent_info);
            break;
        case 'my':
            showPageContent(pageContent_my);
            break;
        case 'search':
            showPageContent(pageContent_search);
            break;
    }
}
// 페이지 로딩 시 활성화되어 있던 페이지를 로드하는 함수
function loadActivePage() {
  const savedPageName = localStorage.getItem('activePage');
  if (savedPageName) {
      setActivePage(savedPageName);
  }
}

// 페이지 로딩 시 실행되게 합니다.
loadActivePage();
links_info.forEach(function(link) {
    link.addEventListener('click', function() {
        setActivePage('info');
    });
});

links_my.forEach(function(link) {
    link.addEventListener('click', function() {
        setActivePage('my');
    });
});

links_search.forEach(function(link) {
    link.addEventListener('click', function() {
        setActivePage('search');
    });
});

pageContent_info.addEventListener('click', function() {
    window.scrollTo(0, 0);
});

pageContent_my.addEventListener('click', function() {
    window.scrollTo(0, 0);
});

pageContent_search.addEventListener('click', function() {
    window.scrollTo(0, 0);
});


const links = document.querySelectorAll(".my-container h1, .my-container h3");

links.forEach(link => {
    link.addEventListener("click", function() {
        if (this.classList.contains("clicked")) {
            this.classList.remove("clicked");
        } else {
            // 먼저 모든 항목에서 clicked 클래스를 제거
            links.forEach(item => item.classList.remove("clicked"));
            // 현재 항목에 clicked 클래스 추가
            this.classList.add("clicked");
        }
    });
});

function deleteRecord(recordId) {
  fetch(`/delete-history/${recordId}`, {
      method: 'DELETE',
  }).then(response => {
      if (response.ok) {
          // 성공적으로 삭제되면 해당 항목을 DOM에서 제거
          const item = document.querySelector(`.history-item[data-record-id="${recordId}"]`);
          if (item) {
              item.remove();
          }
          location.reload();
      } else {
          alert("Failed to delete record.");
      }
  });
}
// 버튼 클릭 이벤트 리스너 추가
document.querySelectorAll('.history-delete-btn').forEach(button => {
  button.addEventListener('click', function() {
      const recordId = this.getAttribute('data-record-id');
      deleteRecord(recordId);
  });
});

function fetchSearchHistoryResultByTimestamp(timestamp) {
  fetch('/search-history-result-by-timestamp', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ timestamp: timestamp })
  })
  .then(response => response.json())
  .then(data => {
      if (data.error) {
          alert(data.error);
      } else {
          document.getElementById('translationResult').textContent = data.translated_text;
          document.getElementById('imgCatResult').textContent = data.img_cat;
          const imageResultElem = document.getElementById('imageResult');
          imageResultElem.src = data.image_url;
          imageResultElem.alt = "이미지 결과";

          document.getElementById('results').style.display = 'block';
      }
  })
  .catch(error => {
      console.error("Error fetching search history result:", error);
  });
}

// 검색 기록 항목을 클릭하면 해당 함수를 호출
document.querySelectorAll('.history-item').forEach(item => {
  item.addEventListener('click', function() {
      const timestamp = item.querySelector('.history-timestamp').textContent;
      fetchSearchHistoryResultByTimestamp(timestamp);
  });
});
