const translationResult = document.getElementById("translationResult");
const imageContainer = document.getElementById("imageContainer");

// 쿼리 파라미터를 파싱하여 검색어 가져오기
const urlParams = new URLSearchParams(window.location.search);
const searchTerm = urlParams.get("search");

let images = []; // 초기 빈 배열
let currentIndex = 0;

function updateImage() {
    const imageElements = document.querySelectorAll('#imageContainer img');
    imageElements.forEach((img, index) => {
        img.style.display = (index === currentIndex) ? 'block' : 'none';
    });
}

function nextImage() {
    currentIndex = (currentIndex + 1) % images.length;
    updateImage();
}

function prevImage() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    updateImage();
}

if (searchTerm) {
    // Fetching data from server
    fetch(`/get_prediction?search=${searchTerm}`).then(response => response.json()).then(data => {
        const translatedText = data.translated_text;
        images = data.img_src;
        
        // Updating the DOM
        translationResult.textContent = "번역된 결과: " + translatedText;

        images.forEach(src => {
            let imgElement = document.createElement("img");
            imgElement.src = src;
            imgElement.style.display = 'none';
            imageContainer.appendChild(imgElement);
        });

        updateImage();
    });
} else {
    // 검색어 없이 결과 페이지에 접근하려고 하면 검색 페이지로 리디렉션
    window.location.href = "search.html";
}

const backToSearchButton = document.getElementById("backToSearchButton");
const nextArrow = document.getElementById("nextArrow");
const prevArrow = document.getElementById("prevArrow");
const jButton = document.getElementById("jButton"); // 이 부분 추가

backToSearchButton.addEventListener("click", function() {
    window.location.href = "search.html";
});
jButton.addEventListener("click", function() {
    window.location.href = "information.html";
});
nextArrow.addEventListener("click", function() {
    nextImage();
});
prevArrow.addEventListener("click", function() {
    prevImage();
});
