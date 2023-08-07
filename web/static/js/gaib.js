//joinform_check 함수로 유효성 검사
function joinform_check(){
    //변수에 담아주기
    var gaib_id = document.getElementById("gaib_id");
    var gaib_pw = document.getElementById("gaib_pw");
    var gaib_pw1 = document.getElementById("gaib_pw1");
    var phone = document.getElementById("phone");
    var email = document.getElementById("email");
    var gaib_nick = document.getElementById("gaib_nick");

    if (gaib_nick.value == "") { //해당 입력값이 없을 경우 같은말: if(!gaib_nick.value)
      alert("닉네임를 입력하세요.");
      gaib_nick.focus(); //focus(): 커서가 깜빡이는 현상, blur(): 커서가 사라지는 현상
      return false; //return: 반환하다 return false:  아무것도 반환하지 말아라 아래 코드부터 아무것도 진행하지 말것
    };
  
    if (gaib_id.value == "") { //해당 입력값이 없을 경우 같은말: if(!gaib_id.value)
      alert("아이디를 입력하세요.");
      gaib_id.focus(); //focus(): 커서가 깜빡이는 현상, blur(): 커서가 사라지는 현상
      return false; //return: 반환하다 return false:  아무것도 반환하지 말아라 아래 코드부터 아무것도 진행하지 말것
    };
  
    if (gaib_pw.value == "") {
      alert("비밀번호를 입력하세요.");
      gaib_pw.focus();
      return false;
    };
  
    //비밀번호 영문자+숫자+특수조합(8~20자리 입력) 정규식
    var gaib_pwCheck = /^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,20}$/;
  
    if (!gaib_pwCheck.test(gaib_pw.value)) {
      alert("비밀번호는 영문자+숫자+특수문자 조합으로 8~20자리 사용해야 합니다.");
      gaib_pw.focus();
      return false;
    };
  
    if (gaib_pw1.value !== gaib_pw.value) {
      alert("비밀번호가 일치하지 않습니다..");
      gaib_pw1.focus();
      return false;
    };

    if (email.value == "") {
      alert("이메일 주소를 입력하세요.");
      email.focus();
      return false;
    };

    if (phone.value == "") {
        alert("전화번호를 입력하세요.");
        phone.focus();
        return false;
      };

    var reg = /^[0-9]+/g; //숫자만 입력하는 정규식
  
    if (!reg.test(phone.value)) {
      alert("전화번호는 숫자만 입력할 수 있습니다.");
      phone.focus();
      return false;
    }
    
    return true;
}