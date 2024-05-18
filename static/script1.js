const slider = document.querySelector('.slider');
const images = document.querySelectorAll('.slider img');

let currentIndex = 0;
const slideWidth = images[0].clientWidth;

function nextSlide() {
  currentIndex++;
  if (currentIndex >= images.length-1) {
    currentIndex = 0;
  }
  updateSliderPosition();
  nextSlide1()
}
function nextSlide1() {
    currentIndex++;
    if (currentIndex >= images.length-1) {
      currentIndex = 0;
    }
    updateSliderPosition();
    nextSlide()
  }

function previousSlide() {
  currentIndex--;
  if (currentIndex < 0) {
    currentIndex = images.length - 1;
  }
  updateSliderPosition();
}

function updateSliderPosition() {
  slider.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
}

setInterval(nextSlide, 1000); // Change slide every 3 seconds (adjust as needed)
