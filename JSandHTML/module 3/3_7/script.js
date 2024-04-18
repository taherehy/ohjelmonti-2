const trigger = document.querySelector('#trigger');
const image = document.querySelector('img'); // Assuming there's only one image element

trigger.addEventListener("mouseenter", function(): void {
  image.src = "img/picB.jpg"; // Update image source on mouseenter
});

trigger.addEventListener("mouseleave", function(): void {
  image.src = "img/picA.jpg"; // Update image source on mouseleave (corrected filename)
});
