function sendPOSTRequest() {
    var form = document.createElement("form");
    form.setAttribute("method", "POST");
    form.setAttribute("action", "url");
    form.style.display = "hidden";
    document.body.appendChild(form);
    form.submit();
}
