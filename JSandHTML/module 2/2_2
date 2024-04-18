function getParticipantNames() {
  // مقدار ورودی تعداد شرکت‌کنندگان را از ورودی می‌گیرد
  var numParticipants = parseInt(document.getElementById("participantNum").value);
  var names = [];
  // در این حلقه، نام هر یک از شرکت‌کنندگان را از کاربر می‌گیرد و در آرایه‌ی names ذخیره می‌شود
  for (var i = 1; i <= numParticipants; i++) {
    var name = prompt("نام شرکت‌کننده " + i + " را وارد کنید:");
    names.push(name);
  }
  // تابع displayParticipantList برای نمایش لیست شرکت‌کنندگان صدا زده می‌شود
  displayParticipantList(names);
}

function displayParticipantList(names) {
  // لیست نام‌ها را بر اساس الفبا مرتب می‌کند
  names.sort();
  var listHtml = "<ol>";
  // برای هر نام، یک آیتم لیست در HTML ایجاد می‌شود
  for (var i = 0; i < names.length; i++) {
    listHtml += "<li>" + names[i] + "</li>";
  }
  listHtml += "</ol>";
  // لیست نام‌ها در داخل المان HTML مشخص شده نمایش داده می‌شود
  document.getElementById("participantNames").innerHTML = listHtml;
}
