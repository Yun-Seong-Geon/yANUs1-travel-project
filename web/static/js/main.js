function handleKeyPress(event) {
  // Enter 키의 keyCode는 13
  if (event.keyCode === 13) {
      var inputText = document.getElementById("inputText").value;{
      transBox();}
       alert("입력한 텍스트: " + inputText);

       translateAndDisplayImage(inputText); // 이미지 표시 함수 호출
  }
}

async function translateAndDisplayImage(translated_text) {
  const imageUrl = await searchImage(translated_text);
  const imageContainer = document.getElementById("imageContainer");
  imageContainer.innerHTML = `<img src="${imageUrl}" alt="이미지">`;
}

async function searchImage(query) {
  // 이 부분에서 실제 이미지 검색 API를 사용하여 이미지 URL을 가져오는 코드를 작성해야 합니다.
  // 여기서는 가상의 이미지 URL을 반환하도록 가정합니다.
  return "https://via.placeholder.com/300";
}

function transBox() {
  var box = document.getElementById('transBox');
  if (box.style.display === 'none') {
    box.style.display = 'block';
  } else {
    box.style.display = 'none';
  }
}

function checkInput() {
    var text = document.getElementById("trans_text").value;
    if (text == "") { //해당 입력값이 없을 경우 같은말: if(!trans_text.value)
        alert("번역할 글을 입력해주세요.");
        document.getElementById("trans_text").focus(); //focus(): 커서가 깜빡이는 현상, blur(): 커서가 사라지는 현상
        return false; //return: 반환하다 return false:  아무것도 반환하지 말아라 아래 코드부터 아무것도 진행하지 말것
      };

    return true;
}