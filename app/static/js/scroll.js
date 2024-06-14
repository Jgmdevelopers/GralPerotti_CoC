
  document.addEventListener('DOMContentLoaded', function() {
    // Obtén los enlaces de navegación
    var inicioLink = document.querySelector('.M[href="#inicio"]');
    var historiaLink = document.querySelector('.M[href="#historia"]');
    var serviciosLink = document.querySelector('.M[href="#servicios"]');
    var obrasLink = document.querySelector('.M[href="#obras"]');
    var comerciosLink = document.querySelector('.M[href="#comercios"]');
    var contactoLink = document.querySelector('.M[href="#contacto"]');

    // Agrega un evento de clic a cada enlace de navegación
    inicioLink.addEventListener('click', scrollToSection);
    historiaLink.addEventListener('click', scrollToSection);
    serviciosLink.addEventListener('click', scrollToSection);
    obrasLink.addEventListener('click', scrollToSection);
    comerciosLink.addEventListener('click', scrollToSection);
    contactoLink.addEventListener('click', scrollToSection);

    // Función para desplazarse suavemente a la sección correspondiente
    function scrollToSection(event) {
      // Detener el comportamiento predeterminado del enlace
      event.preventDefault();

      // Obtener el ID de la sección objetivo del enlace
      var targetId = this.getAttribute('href');

      // Obtener la sección objetivo por su ID
      var targetSection = document.querySelector(targetId);

      // Realizar el desplazamiento suave hacia la sección objetivo
      if (targetSection) {
        targetSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }
  });


