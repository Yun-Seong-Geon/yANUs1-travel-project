const translationResult = document.getElementById("translationResult");
const imageResult = document.getElementById("imageResult");

// 쿼리 파라미터를 파싱하여 검색어 가져오기
const urlParams = new URLSearchParams(window.location.search);
const searchTerm = urlParams.get("search");

if (searchTerm) {
    // 번역 및 이미지 URL을 가져오는 것을 가정합니다 (실제 API로 대체)
    const translatedText = "번역된 결과: " + searchTerm;
    const imageUrl = "https://via.placeholder.com/300"; // 예시 이미지 URL

    translationResult.textContent = translatedText;
    imageResult.src = imageUrl;
} else {
    // 검색어 없이 결과 페이지에 접근하려고 하면 검색 페이지로 리디렉션
    window.location.href = "search.html";
}

