// اضافه کردن یک مدیر رویداد برای ارسال فرم
document.getElementById('searchForm').addEventListener('submit', async function(event) {
  event.preventDefault(); // جلوگیری از عملیات پیش‌فرض فرم

  // دریافت مقدار ورودی از فیلد
  const query = document.getElementById('query').value.trim();

  // بررسی اینکه فیلد ورودی خالی نباشد
  if (query === '') {
    console.log('لطفاً نام سریال تلویزیونی را وارد کنید.');
    return;
  }

  try {
    // ارسال درخواست بر اساس نام سریال و دریافت پاسخ
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query}`);
    const data = await response.json();

    // پاک کردن نتایج قبلی
    document.getElementById('results').innerHTML = '';

    // بررسی هر سریال و اضافه کردن آن به نتایج
    data.forEach(tvShow => {
      // ساختار دهی مقدماتی
      const article = document.createElement('article');
      const heading = document.createElement('h2');
      const link = document.createElement('a');
      const image = document.createElement('img');
      const summary = document.createElement('div');

      // مقداردهی اطلاعات
      heading.textContent = tvShow.show.name;
      link.href = tvShow.show.url;
      link.target = '_blank';
      link.textContent = 'لینک جزئیات';
      image.src = tvShow.show.image?.medium || 'https://via.placeholder.com/210x295?text=No+Image';
      image.alt = tvShow.show.name;
      summary.innerHTML = tvShow.show.summary;

      // اضافه کردن به article
      article.appendChild(heading);
      article.appendChild(link);
      article.appendChild(image);
      article.appendChild(summary);

      // اضافه کردن article به نتایج
      document.getElementById('results').appendChild(article);
    });
  } catch (error) {
    console.error('خطا:', error);
  }
});
