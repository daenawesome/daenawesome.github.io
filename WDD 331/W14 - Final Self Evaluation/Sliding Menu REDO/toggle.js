function toggleNav() {
    var updateElement = document.getElementById("menu-icon");
    updateElement.classList.toggle("open");
    var updateElement = document.getElementById("menu");
    updateElement.classList.toggle("list");
    var updateElement = document.getElementById("main-page");
    updateElement.classList.toggle("move");
}