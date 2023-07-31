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
document.addEventListener("DOMContentLoaded", function() {
  // Get all buttons with class "button"
  const buttons = document.querySelectorAll(".button");

  // Add click event listeners to each button
  buttons.forEach(button => {
      button.addEventListener("click", function() {
          // Get the data-target value from the button
          const targetId = button.getAttribute("data-target");

          // Get the div with the corresponding ID
          const targetDiv = document.getElementById(targetId);

          // Toggle the visibility of the div
          targetDiv.classList.toggle("show");
      });
  });
});