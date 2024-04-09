    //tarkista karkausvuosi
function checkLeapYear() {

//pyytää vuosi              //ID HTML
  const yearInput = document.getElementById("yearInput").value;
//saa käytäjältä tietoa luvuksi
  const year = parseInt(yearInput);
//osoitaa milloin onlarkausvuosi
  let isLeapYear = false;

  //onko jaettavissa 4llä
  if (year % 4 === 0) {
      //onko jaettavissa 100lla
    if (year % 100 === 0) {
        //jos on jaettavilla 400lla
      if (year % 400 === 0) {
          //on karkausvuosi
        isLeapYear = true;
      }
      //jos jaetavissa 4llä on karkausvusi vaikka ei jaettavissa 100lla
    } else {
      isLeapYear = true;
    }
  }
console.log("Onko karkausvuosi:", isLeapYear); // Tarkista, onko vuosi karkausvuosi

  const resultElement = document.getElementById("leapYearResult");
  //lisäätää ja päivitää palutaa teksti joka on Paragrafissa
  const resultText = isLeapYear ? `${year} is a leap year!` : `${year} is not a leap year.`;
  resultElement.textContent = resultText;
}