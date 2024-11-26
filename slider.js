// Array of background images
// img object
const images = [
    './img-1.jpg', // Replace with your image paths
    './img-2.jpg',
    './img-3.jpg'
];

let currentIndex = 0; // variable

// Function to change the background image
function changeBackground() {
    document.body.style.backgroundImage = `url('${images[currentIndex]}')`;
    currentIndex = (currentIndex + 1) % images.length; // Cycle through images
}

// Set an interval to change the background every 5 seconds
setInterval(changeBackground, 2000);

// Initialize the first background image
changeBackground(); // call functoin
