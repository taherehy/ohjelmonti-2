
//Tämä funktio etsii karkausvuodet
function findLeapYears() {
    //käyttäjältä aloitusvuosi
    const startYear = parseInt(prompt("Enter the start year:"));
    //lopetusvuosi          #muunnetaan se kokonaisluvuksi
    const endYear = parseInt(prompt("Enter the end year:"));
//tyhjä lista karkausvuosille
    const leapYears = [];

    // تمام سال‌ها را از سال شروع تا سال پایانی بررسی می‌کند
    for (let year = startYear; year <= endYear; year++) {
        //laskee onko karkausvuosi
        if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {

            //jos on push to list
            leapYears.push(year);
        }
    }
//tekee uusi elementiluento
    const ul = document.createElement("ul");
//Käydään läpi kaikki joka vuosi ussilistaelementi
    leapYears.forEach(function(year) {
        const li = document.createElement("li");
       //tekee vuosilista
        li.textContent = year;
        ul.appendChild(li);
    });
 //Etsitään HTML-dokumentista elementti, jonka id on "leapYearsResult"
    const resultElement = document.getElementById("leapYearsResult");
    //// Lisätään luetteloelementti (ul) tuloksena näytettävään elementtiin (div)
    resultElement.appendChild(ul);
}
