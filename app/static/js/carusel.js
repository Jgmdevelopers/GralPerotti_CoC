document.addEventListener('DOMContentLoaded', function() {
// Inicializar el carousel cuando el documento esté listo
document.addEventListener('DOMContentLoaded', function () {
// Seleccionar el carousel por su ID y inicializarlo
var myCarousel = document.getElementById('carouselExampleInterval');
var carousel = new bootstrap.Carousel(myCarousel, {
    interval: 5000, // Cambia el intervalo en milisegundos si lo deseas
    wrap: true // Permite que el carousel se repita
});
});
});
