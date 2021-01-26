function reqUpdate(firstname, email) {
    let form = document.createElement('form');
    form.setAttribute('charset', 'utf-8')
    form.setAttribute('method', 'get{{ csrf_token }}');
    form.setAttribute('action', './updateinfo');

    hiddenField = document.createElement('input');
    hiddenField.setAttribute('type', 'hidden');
    hiddenField.setAttribute('name', 'firstname');
    hiddenField.setAttribute('value', firstname);
    form.appendChild(hiddenField);

    hiddenField = document.createElement('input');
    hiddenField.setAttribute('type', 'hidden');
    hiddenField.setAttribute('name', 'email');
    hiddenField.setAttribute('value', email);
    form.appendChild(hiddenField);

    document.body.appendChild(form);
    form.submit();
}

function clickImage(src){
    let form = document.createElement('form');
    form.setAttribute('method', 'GET{{ csrf_token }}');
    form.setAttribute('action', './bookinfo');

    let hiddenField = document.createElement('input');
    hiddenField.setAttribute('type', 'hidden');
    hiddenField.setAttribute('name', 'imgurl');
    hiddenField.setAttribute('value', src);
    form.appendChild(hiddenField);
    
    document.body.appendChild(form);
    form.submit();
}