let prevScrollPos = window.pageYOffset;
window.onscroll = function() {
  const currentScrollPos = window.pageYOffset;
  const navbar = document.getElementById("navbar");
  
  if (prevScrollPos > currentScrollPos) {
    document.body.classList.remove("scrolling-down");
    document.body.classList.add("scrolling-up");
  } else {
    document.body.classList.remove("scrolling-up");
    document.body.classList.add("scrolling-down");
  }
  
  prevScrollPos = currentScrollPos;
};
const textContainer = document.getElementById("typing-text");
const text = textContainer.innerText;
textContainer.innerText = "";
let charIndex = 0;

function type() {
  const currentText = text.slice(0, charIndex);
  textContainer.innerHTML = `${currentText}<span class="cursor"></span>`;
  charIndex++;
  if (charIndex <= text.length) {
    setTimeout(type, 50);
  }
}

type();

// const slider = document.querySelector('.slider');
// const images = document.querySelectorAll('.slider img');

// let currentIndex = 0;
// const slideWidth = images[0].clientWidth;

// function nextSlide() {
//   currentIndex++;
//   if (currentIndex >= images.length-1) {
//     currentIndex = 0;
//   }
//   updateSliderPosition();
//   nextSlide1()
// }
// function nextSlide1() {
//     currentIndex++;
//     if (currentIndex >= images.length-1) {
//       currentIndex = 0;
//     }
//     updateSliderPosition();
//     nextSlide()
//   }

// function previousSlide() {
//   currentIndex--;
//   if (currentIndex < 0) {
//     currentIndex = images.length - 1;
//   }
//   updateSliderPosition();
// }

// function updateSliderPosition() {
//   slider.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
// }

// setInterval(nextSlide, 1000); // Change slide every 3 seconds (adjust as needed)
