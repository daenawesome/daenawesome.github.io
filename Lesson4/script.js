function loadImages(img) {
    const imgSrc = img.getAttribute('data-src');
    img.src = imgSrc;
    img.removeAttribute('data-src');
}

let images = document.querySelectorAll("img[data-src]");
const imgObserver = new IntersectionObserver((entries, imgObserver) => {
    entries.forEach(entry => {
        if (!entry.isIntersecting) {
            return;
        } else {
            loadImages(entry.target);
            imgObserver.unobserve(entry.target);
        }
    });
});

images.forEach(img => {
    imgObserver.observe(img);
});