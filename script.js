const form = document.querySelector('.form');
const nextButton = form.querySelector('#nextButton'); // Using form as the context

// Add a click event listener to the button
nextButton.addEventListener('click', function(event) {
    window.location.href = 'home.html';
});

// Add a submit event listener to the form
form.addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent the default form submission behavior
  window.location.href = 'home.html';
});
