const date = new Date();
const year = date.getFullYear();

document.querySelector('#copyrightyear').innerHTML = year;
document.querySelector('#lastupdated').innerHTML = document.lastModified;