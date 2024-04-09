function getDogNames() {
  const dogNames = [];

  //  حلقه که نام شش سگ را می‌پرسد و آن‌ها را به آرایه اضافه می‌کند
  for (let i = 1; i <= 6; i++) {
    const nameInput = document.getElementById(`dogName${i}`);
    const name = nameInput.value;
    dogNames.push(name);
  }

  // مرتب‌سازی نام‌های سگ‌ها به ترتیب حروف الفبا و سپس برعکس کردن ترتیب
  dogNames.sort((a, b) => b.localeCompare(a));

  // ایجاد یک لیست و اضافه کردن نام‌های سگ‌ها به لیست
  const dogList = document.getElementById("dogList");
  dogList.innerHTML = ""; // Clear any existing list items

  // Create and add list items for each dog name
    //پیمایش// هر عنصر و اضافه کردن آن به لیست، داخل المان لیست
  for (const name of dogNames) {
    const listItem = document.createElement("li");
    listItem.textContent = name;

// قرار دادن لیست در المان مورد نظر در صفحه وب
    dogList.appendChild(listItem);
  }
}
