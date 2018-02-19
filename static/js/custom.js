var path = window.location.pathname;
var page = path.split("/").pop();
var reqHeader = document.getElementById("requests-header");
var reqButton = document.getElementById("requests-button")
if (page=="index.html") {
  reqHeader.innerHTML = "Свежие заявки"
  reqHeader.style.textAlign = "center"
  reqButton.innerHTML = "Посмотреть все заявки"
  reqButton.href="requests.html"
}
