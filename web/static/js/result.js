const translationResult = document.getElementById("translationResult");
const imageResult = document.getElementById("imageResult");
const imgCatResult = document.getElementById("imgCatResult");

let loadingTextElement = document.getElementById('loadingText');
let dots = 0;

setInterval(() => {
    dots = (dots + 1) % 4; // 4까지 증가하고 다시 0으로 돌아간다.
    let dotsStr = '.'.repeat(dots); // 반복된 점 문자열 생성
    loadingTextElement.textContent = "로딩 중" + dotsStr;
}, 500); // 0.5초마다 실행
// 쿼리 파라미터를 파싱하여 검색어 가져오기
const urlParams = new URLSearchParams(window.location.search);
const searchTerm = urlParams.get("search");

if (searchTerm) {
    // 서버에 예측 결과를 요청
    fetch('/get_prediction?search=' + encodeURIComponent(searchTerm))
    .then(response => response.json())
    .then(data => {
        // 결과 데이터를 사용하여 요소 업데이트
        translationResult.textContent = data.translated_text;
        imgCatResult.textContent = data.img_cat;
        imageResult.src = data.img_src;
        loadingContainer.style.display = 'none';
        results.style.display = 'block';
    })
    .catch(error => {
        console.error("Error fetching prediction:", error);
        // 에러 처리 및 사용자에게 메시지 표시 (옵션)
        alert("결과를 가져오는 데 실패했습니다. 다시 시도해 주세요.");
        loadingContainer.style.display = "none";
        results.innerHTML = "<p>결과를 가져오는데 문제가 발생했습니다. 페이지를 새로고침 하거나 다시 시도해 주세요.</p>";
        results.style.display = "block";
    });
} else {
    // 검색어 없이 결과 페이지에 접근하려고 하면 검색 페이지로 리디렉션
    window.location.href = "search.html";
}
