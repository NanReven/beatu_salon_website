// script.js

// Function to handle appointment booking
function bookAppointment() {
    // Add your appointment booking logic here
    alert("Appointment booked successfully!");
}

// Function to handle image slider
let currentSlide = 0;

function showSlide(slideIndex) {
    const slides = document.getElementsByClassName("slide");
    if (slideIndex >= slides.length) {
        currentSlide = 0;
    } else if (slideIndex < 0) {
        currentSlide = slides.length - 1;
    } else {
        currentSlide = slideIndex;
    }

    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    slides[currentSlide].style.display = "block";
}

function nextSlide() {
    showSlide(currentSlide + 1);
}

function prevSlide() {
    showSlide(currentSlide - 1);
}

// Event listener for appointment button
const appointmentButton = document.getElementById("book-appointment");
if (appointmentButton) {
    appointmentButton.addEventListener("click", bookAppointment);
}

// Event listeners for image slider controls
const prevButton = document.getElementById("prev-slide");
const nextButton = document.getElementById("next-slide");

if (prevButton && nextButton) {
    prevButton.addEventListener("click", prevSlide);
    nextButton.addEventListener("click", nextSlide);
}
