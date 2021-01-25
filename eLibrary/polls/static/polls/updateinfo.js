function submitReqUpdate(email) {
    let pw = document.getElementById('password');
    let cpw = document.getElementById('cpassword');

    if (pw.value == cpw.value) {
        let form = document.getElementById('forms');
        form.setAttribute('method', 'POST');
        form.setAttribute('action', './requpdate');

        let hiddenField = document.createElement('input');
        hiddenField.setAttribute('type', 'hidden');
        hiddenField.setAttribute('name', 'email');
        hiddenField.setAttribute('value', email);
        form.appendChild(hiddenField);
        form.submit();
        alert('회원정보 수정완료 하였습니다.');
    }
    else{
        alert('비밀번호가 일치하지 않습니다.');
    }

}

function submitDeleteInfo(firstname, email) {
    let form = document.createElement('form');
    form.setAttribute('method', 'GET{% csrf_token %}');
    form.setAttribute('action', './deleteinfo');

    let hiddenField = document.createElement('input');
    hiddenField.setAttribute('type', 'hidden');
    hiddenField.setAttribute("name", "email");
    hiddenField.setAttribute("value", email);
    form.appendChild(hiddenField);

    hiddenField = document.createElement('input');
    hiddenField.setAttribute('type', 'hidden');
    hiddenField.setAttribute("name", "firstname");
    hiddenField.setAttribute("value", firstname);
    form.appendChild(hiddenField);

    document.body.appendChild(form);
    form.submit();
}