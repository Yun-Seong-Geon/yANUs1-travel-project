import streamlit as st
import streamlit.components.v1 as components
import front_register as fs
login_id = None
login_css = (
    '''
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
    # background: rgba(0, 0, 0, 0.1)
    margin : 0, auto;
  }
  
  .login {
    width: 30%;
    height: 500px;
    background: white;
    border-radius: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    margin : 0, auto;
  }
  
  h2 {
    color: rgb(20, 180, 68);
    font-size: 2em;
  }
  
  .login_id {
    margin-top: 20px;
    width: 80%;
  }
  
  .login_id input {
    width: 100%;
    height: 50px;
    border-radius: 30px;
    margin-top: 10px;
    padding: 0px 20px;
    border: 1px solid lightgray;
    outline: none;
  }
  
  .login_pw {
    margin-top: 20px;
    width: 80%;
  }
  
  .login_pw input {
    width: 100%;
    height: 50px;
    border-radius: 30px;
    margin-top: 10px;
    padding: 0px 20px;
    border: 1px solid lightgray;
    outline: none;
  }
  
  .submit-login {
    margin-top: 30px;
    width: 80%;
  }

  .submit-login button {
    width: 100%;
    height: 50px;
    border: 0;
    outline: none;
    border-radius: 40px;
    background-color:rgb(26, 223, 85);
    color: white;
    font-size: 1.2em;
    letter-spacing: 2px;
  }.submit-gaib button {
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
    '''
)
login_js = '''
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

    alert("로그인이 되었습니다.");
    location.href="main.html"
}

'''
logins_css = "login.css"
login_html = (f'''
    <script>{login_js}</script>
    <style>{login_css}</style>
    <form class="join_form">
    <div class="wrap">
        <div class="login">
            <h2>All-Leave</h2>
            
            <div class="login_id">
                <h4>아이디</h4>
                <input type="text" name="login_id" id="login_id" placeholder="아이디를 입력하세요">
            </div>
            <div class="login_pw">
                <h4>비밀번호</h4>
                <input type="password" name="login_pw" id="login_pw" placeholder="비밀번호를 입력하세요">
            </div>

            <div class="submit-login">
                <button type="button" onclick="joinform_check();">로그인</button>
            </div>
        </div>
    </div>
</form>
    '''   
)
