function submitReqDelete(firstname, email) {
    let form = document.getElementById('forms');
    form.setAttribute('action', './reqdelete');
    form.setAttribute('method', 'post');

    let hiddenField = document.createElement('input');
    hiddenField.setAttribute('type', 'hidden');
    hiddenField.setAttribute('name', 'email');
    hiddenField.setAttribute('value', email);
    form.appendChild(hiddenField);

    hiddenField = document.createElement('input');
    hiddenField.setAttribute('type', 'hidden');
    hiddenField.setAttribute('name', 'firstname');
    hiddenField.setAttribute('value', firstname);
    form.appendChild(hiddenField);
    form.submit();
}

function submitIndex() {
    let form = document.getElementById('forms');
    form.setAttribute('action', './');
    form.setAttribute('method', 'get');
    form.submit();
}