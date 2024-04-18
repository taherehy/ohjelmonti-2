// Sample data
const picArray = [
  { title: "Title 1", image: "https://via.placeholder.com/300", caption: "Caption 1", description: "Description 1" },
  { title: "Title 2", image: "https://via.placeholder.com/300", caption: "Caption 2", description: "Description 2" },
  { title: "Title 3", image: "https://via.placeholder.com/300", caption: "Caption 3", description: "Description 3" }
];

// Selecting the section element
const section = document.getElementById('articles');

// Looping through picArray and creating articles
picArray.forEach(pic => {
  // Creating elements
  const article = document.createElement('article');
  const heading = document.createElement('h2');
  const figure = document.createElement('figure');
  const image = document.createElement('img');
  const figcaption = document.createElement('figcaption');
  const description = document.createElement('p');

  // Setting content and attributes
  heading.textContent = pic.title;
  image.src = pic.image;
  image.alt = pic.title;
  figcaption.textContent = pic.caption;
  description.textContent = pic.description;

  // Appending elements
  figure.appendChild(image);
  figure.appendChild(figcaption);
  article.appendChild(heading);
  article.appendChild(figure);
  article.appendChild(description);

  // Adding class to article
  article.classList.add('card');

  // Appending article to section
  section.appendChild(article);
});
