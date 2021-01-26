function submitReqMember() {
  let mesg = "{{msg}}";
  let pw = document.getElementById('password');
  let cpw = document.getElementById('cpassword');
  let email = document.getElementById('mail');
  let phone = document.getElementById('phonein');
  let firstName = document.getElementById('firstn');
  let lastName = document.getElementById('lastn');
  let address = document.getElementById('address');

  if (firstName.value == '' || lastName.value == '') alert('이름을 입력해주세요.');
  else if (email.value == '') alert('이메일을 입력해주세요.');
  else if (phone.value == '') alert('핸드폰 번호를 입력하세요.');
  else if (phone.value.indexOf('-') != -1) alert('-없이 핸드폰번호를 입력하세요.');
  else if (isNaN(phone.value)) alert('핸드폰 번호에 숫자를 입력하세요');
  else if (pw.value == '') alert('비밀번호를 입력해주세요.');
  else if (pw.value != cpw.value) alert('비밀번호가 일치하지 않습니다.');
  else if (address.value == '') alert('주소를 입력해주세요.');
  //else if(mesg != 'available') alert('이메일 중복 확인하세요.');
  else {
    alert('회원가입이 완료됐습니다.')
    let forms = document.getElementById('forms');
    forms.setAttribute('method', 'post');
    forms.setAttribute('action', './reqmember');
    forms.submit();
  }
}

function checkMail() {
  let form = document.getElementById('forms');
  form.setAttribute('method', 'post');
  form.setAttribute('action', './checkmail');
  form.submit();
}