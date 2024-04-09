// Funktio ota nimi ja tervehdyttää nimellesi
function greetUser() {
  //se funktio pyyttää nimi prompt palaa viesti
  const name = prompt("Anna nimesi: ");
  const Terveisin = "Terve, " + name + "!";
  document.getElementById("terveisinViesti").textContent = Terveisin;
}

// varmista syöte näkyy
window.onload = greetUser;
