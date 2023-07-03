
(function () {
  /*
  summary: funcion autoejecutable que agrega un evento (mensaje de confirmación) de click a todos los elementos con clase "btnEliminacion"
  */
  
  // Seleccionamos todos los elementos que tengan la clase "btnEliminacion" y los almacenamos en la constante "btnEliminacion".
  const btnEliminacion = document.querySelectorAll(".btnEliminacion"); 
  
  // Usamos el método "forEach" para iterar sobre cada botón con la clase "btnEliminacion".
  btnEliminacion.forEach((btn) => {
    // Agregamos un evento "click" a cada botón seleccionado.
    btn.addEventListener("click", (eventClick) => {
      // Cuando se hace clic en el botón, se muestra un cuadro de diálogo de confirmación con el mensaje "¿Seguro que desea eliminar el usuario?".
      const confirmation = confirm("¿Seguro que desea eliminar el usuario?");
      
      // Si el usuario hace clic en "Aceptar" (es decir, confirma la eliminación), no hacemos nada y el proceso de eliminación continuará normalmente.
      // Si el usuario hace clic en "Cancelar" (es decir, niega la eliminación), ejecutamos "eventClick.preventDefault()" para evitar que el evento de clic del botón se propague y realice la eliminación.
      if (!confirmation) { 
        eventClick.preventDefault();
      }
    });
  });
})();
