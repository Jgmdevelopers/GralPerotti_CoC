document.addEventListener('DOMContentLoaded', function() {
  document.querySelector('.contacto-formulario').addEventListener('submit', function(event) {
      // Obtener todos los campos del formulario
      var campos = this.elements;

      // Variable para rastrear si hay algún campo vacío
      var camposVacios = false;

      // Verificar que todos los campos obligatorios estén completos
      for (var i = 0; i < campos.length; i++) {
          if (campos[i].name === 'contactos' || campos[i].name === 'nombre' || campos[i].name === 'apellido' || campos[i].name === 'telefono' || campos[i].name === 'email' || campos[i].name === 'mensaje') {
              if (campos[i].value === '') {
                  // Si el campo está vacío y no hay mensaje de error, agregar uno
                  if (!campos[i].parentNode.querySelector('.error-message')) {
                      camposVacios = true;
                      mostrarError(campos[i].parentNode, 'El campo ' + campos[i].getAttribute('name') + ' es obligatorio.');
                  }
              } else {
                  // Si el campo no está vacío, eliminar cualquier mensaje de error existente
                  ocultarError(campos[i].parentNode);
              }
          }
      }

      // Validar el formato del correo electrónico
      if (campos['email'].value !== '' && !validarEmail(campos['email'].value)) {
          mostrarError(campos['email'].parentNode, 'Por favor, introduzca un correo electrónico válido.');
          camposVacios = true;
      }

      // Prevenir el envío del formulario si hay campos vacíos o errores de validación
      if (camposVacios) {
          event.preventDefault();
      } else {
          // Mostrar mensaje de alerta si el formulario se envía correctamente
          alert('Mensaje enviado correctamente');
          // Limpiar campos del formulario
          this.reset();
      }
  });

  // Función para mostrar un mensaje de error
  function mostrarError(elemento, mensaje) {
      var mensajeError = document.createElement('p');
      mensajeError.textContent = mensaje;
      mensajeError.classList.add('error-message');
      mensajeError.style.color = '#C40C0C'; // Establecer color de texto en rojo
      mensajeError.style.fontSize = '0.85rem'; // Tamaño de fuente
      mensajeError.style.marginTop = '0.25rem'; // Margen superior
      elemento.appendChild(mensajeError);
  }

  // Función para ocultar un mensaje de error
  function ocultarError(elemento) {
      var errorExistente = elemento.querySelector('.error-message');
      if (errorExistente) {
          errorExistente.remove();
      }
  }

  // Función para validar el formato del correo electrónico
  function validarEmail(email) {
      var re = /\S+@\S+\.\S+/;
      return re.test(email);
  }
});
