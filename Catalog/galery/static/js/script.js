let slideIndex = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;

document.getElementById('btn-next').addEventListener('click', () => {
    slideIndex = (slideIndex + 1) % totalSlides;
    updateSlidePosition();
});

document.getElementById('btn-prev').addEventListener('click', () => {
    slideIndex = (slideIndex - 1 + totalSlides) % totalSlides;
    updateSlidePosition();
});

function updateSlidePosition() {
    for (let slide of slides) {
        slide.style.transform = 'translateX(' + (-slideIndex * 100) + '%)';
    }
}