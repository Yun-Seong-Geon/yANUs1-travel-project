function checkInput(){
  const searchForm = document.getElementById("searchForm");
  const searchInput = document.getElementById("trans_text");
  searchForm.addEventListener("submit", function(event) {
    event.preventDefault();

    const searchTerm = searchInput.value;
    if (searchTerm === "") {
        alert("검색어를 입력해주세요.");
        return false
    } else {
        // 검색어를 쿼리 파라미터로 사용하여 결과 페이지로 이동
        // window.location.href = `result.html?search=${encodeURIComponent(searchTerm)}`;
        return true
    }
});
}

