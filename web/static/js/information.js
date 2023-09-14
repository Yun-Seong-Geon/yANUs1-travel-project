backToSearchButton.addEventListener("click", function() {
    // Redirect back to the search page
    window.location.href = "search.html";
});
// "backButton" 클릭 이벤트 핸들러
document.getElementById("backButton").addEventListener("click", function() {
    // "result.html" 페이지로 이동
    window.location.href = "result.html";
});



// 슬라이드 인덱스를 추적합니다.
let currentSlideIndex = 0;
const slides = document.getElementsByClassName("slideshow");

// 초기로드 시에 "travelInfo" 슬라이드를 숨깁니다.
for (let i = 1; i < slides.length; i++) {
    slides[i].style.display = "none";
}

// 다음 화살표 클릭 이벤트 핸들러
document.getElementById("nextArrow").addEventListener("click", function() {
    // 현재 슬라이드를 비활성화
    slides[currentSlideIndex].style.display = "none";

    // 다음 슬라이드를 활성화
    currentSlideIndex = (currentSlideIndex + 1) % slides.length;
    slides[currentSlideIndex].style.display = "block";
});

// 이전 화살표 클릭 이벤트 핸들러
document.getElementById("prevArrow").addEventListener("click", function() {
    // 현재 슬라이드를 비활성화
    slides[currentSlideIndex].style.display = "none";

    // 이전 슬라이드를 활성화
    currentSlideIndex = (currentSlideIndex - 1 + slides.length) % slides.length;
    slides[currentSlideIndex].style.display = "block";
});