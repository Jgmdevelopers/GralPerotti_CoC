// Obtén el header para que al moverlo se trasparente
document.addEventListener("DOMContentLoaded", function() {
const mainHeader = document.querySelector('header');

// Agrega un evento de desplazamiento
window.addEventListener('scroll', function() {
    // Si el desplazamiento vertical es mayor que 50px
    if (window.scrollY > 50) {
        // Agrega la clase "sticky" al header
        mainHeader.classList.add('sticky');
    } else {
        // De lo contrario, elimina la clase "sticky" del header
        mainHeader.classList.remove('sticky');
    }
});
});


// Esperar a que se cargue completamente el contenido del DOM
document.addEventListener("DOMContentLoaded", () => {
    // Obtener referencias a los elementos del DOM después de que se haya cargado
    const menuBtn = document.querySelector(".nav-menu-btn");
    const closeBtn = document.querySelector(".nav-close-btn");
    const navigation = document.querySelector(".navigation");
    const navItemsLinks = document.querySelectorAll(".navigation .nav-items a");

    // Verificar si se encontraron los elementos antes de agregar eventos
    if (menuBtn && closeBtn && navigation && navItemsLinks) {
        // Agregar evento para mostrar la navegación al hacer clic en el botón de menú
        menuBtn.addEventListener("click", () => {
            navigation.classList.add("active");
            // Iterar sobre cada enlace y modificar su estilo
            navItemsLinks.forEach(link => {
                link.style.color = "#fff";
                link.style.fontSize = "1em";
                link.style.transition = "none";
                link.style.webkitTextStroke = "none";
            });
        });

        // Agregar evento para ocultar la navegación al hacer clic en el botón de cierre
        closeBtn.addEventListener("click", () => {
            navigation.classList.remove("active");
        });
    } else {
        console.error("No se encontraron elementos en el DOM");
    }


});
