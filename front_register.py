register_css = """
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Noto Sans KR", sans-serif;
  }
  
  a {
    text-decoration: none;
    color: black;
  }
  
  li {
    list-style: none;
  }
  
  .wrap {
    width: 100%;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(0, 0, 0, 0.1);
  }
  
  .gaib {
    width: 30%;
    height: 550px;
    background: white;
    border-radius: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }
  
  h2 {
    color: rgb(20, 180, 68);
    font-size: 2em;
  }
  
  .gaib_id {
    margin-top: 0px;
    width: 80%;
  }
  
  .gaib_id input {
    width: 100%;
    height: 35px;
    border-radius: 30px;
    margin-top: 10px;
    padding: 0px 20px;
    border: 1px solid lightgray;
    outline: none;
  }
  
  .gaib_pw {
    margin-top: 20px;
    width: 80%;
  }
  
  .gaib_pw input {
    width: 100%;
    height: 35px;
    border-radius: 30px;
    margin-top: 10px;
    padding: 0px 20px;
    border: 1px solid lightgray;
    outline: none;
  }
  .gaib_pw1 {
    margin-top: 20px;
    width: 80%;
  }
  
  .gaib_pw1 input {
    width: 100%;
    height: 35px;
    border-radius: 30px;
    margin-top: 10px;
    padding: 0px 20px;
    border: 1px solid lightgray;
    outline: none;
  }

  .email{
    margin-top: 20px;
    width: 80%;
  }
  
  .email input {
    width: 100%;
    height: 35px;
    border-radius: 30px;
    margin-top: 10px;
    padding: 0px 20px;
    border: 1px solid lightgray;
    outline: none;
  }
  
  .phone{
    margin-top: 20px;
    width: 80%;
  }
  
  .phone input {
    width: 100%;
    height: 35px;
    border-radius: 30px;
    margin-top: 10px;
    padding: 0px 20px;
    border: 1px solid lightgray;
    outline: none;
  }

  .membergaib {
    margin-top: 40px;
    width: 80%;
  }

  .membergaib input {
    width: 100%;
    height: 50px;
    border: 0;
    outline: none;
    border-radius: 40px;
    background-color: rgb(20, 180, 68);
    color: white;
    font-size: 1.2em;
    letter-spacing: 2px;
  }
"""
register_js = '''
//joinform_check 함수로 유효성 검사
function joinform_check(){
    //변수에 담아주기
    var gaib_id = document.getElementById("gaib_id");
    var gaib_pw = document.getElementById("gaib_pw");
    var gaib_pw1 = document.getElementById("gaib_pw1");
    var phone = document.getElementById("phone");
    var email = document.getElementById("email");
  
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
    
    alert("회원가입이 완료되었습니다.");
    location.href="main.html"
  
}
'''

register_html = (f'''
<script>{register_js}</script>
<style>{register_css}</style>
<!DOCTYPE html>
<html lang="ko"> <!-- 코드언어 표시 == 웹 표준지침 준수 -->
<head>
<meta charset="UTF-8">
<title>올리브 회원가입</title> 
<link rel="stylesheet" href="./gaib.css">
<script src="gaib.js"></script>
</head>
<body>
    <form name="join_form">
        <div class="wrap">
            <div class="gaib">
                <h2>All-Leave</h2>
                
                <div class="gaib_id">
                    <h5>아이디</h5>
                    <input type="text" name="gaib_id" id="gaib_id" maxlength="20" placeholder="아이디를 입력하세요">
                </div>
                <div class="gaib_pw">
                    <h5>비밀번호</h5>
                    <input type="password" name="gaib_pw" id="gaib_pw"  maxlength="20" placeholder="비밀번호를 입력하세요">
                </div>
                <div class="gaib_pw1">
                    <h5>비밀번호 재확인</h5>
                    <input type="password" name="gaib_pw1" id="gaib_pw1" maxlength="20" placeholder="비밀번호를 재입력하세요">
                </div>

                <div class="email">
                    <h5>이메일</h5>
                    <input type="text" name="email" id="email" maxlength="20" class="check" placeholder="이메일을 입력하세요">
                    
                </div>

                <div class="phone">
                    <h5>전화번호</h5>
                    <input type="text" name="phone" id="phone" class="check" placeholder="-를 제외하고 입력하세요">
                    
                </div>
    
                <div class="membergaib">
                    <input type="button"  onclick="joinform_check();" value="가입하기">
                </div>
        
        
            </div>
        </div>
    </form>
</body>
</html>
    '''   
)