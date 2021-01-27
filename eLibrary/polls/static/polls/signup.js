function goMain() {
  let form = document.createElement('form');
  form.setAttribute('action', './');
  form.setAttribute('method', 'get');
  document.body.appendChild(form);
  form.submit();
}