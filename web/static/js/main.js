function handleKeyPress(event) {
  // Enter 키의 keyCode는 13
  if (event.keyCode === 13) {
      var inputText = document.getElementById("inputText").value;{
      transBox();}
       alert("입력한 텍스트: " + inputText);
  }
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