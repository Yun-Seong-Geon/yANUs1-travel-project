//joinform_check 함수로 유효성 검사
function joinform_check(){
    //변수에 담아주기
    var login_id = document.getElementById("login_id");
    var login_pw = document.getElementById("login_pw");
  
    if (login_id.value == "") { //해당 입력값이 없을 경우 같은말: if(!login_id.value)
      alert("아이디를 입력하세요.");
      gaib_id.focus(); //focus(): 커서가 깜빡이는 현상, blur(): 커서가 사라지는 현상
      return false; //return: 반환하다 return false:  아무것도 반환하지 말아라 아래 코드부터 아무것도 진행하지 말것
    };
  
    if (login_pw.value == "") {
      alert("비밀번호를 입력하세요.");
      login_pw.focus();
      return false;
    };
    return true;
}