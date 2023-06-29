
(function () {
  /*
  summary: funcion autoejecutable que agrega un evento (mensaje de confirmación) de click a todos los elementos con clase "btnEliminacion"
  */
  const btnEliminacion = document.querySelectorAll(".btnEliminacion"); // Creamos una variable constante que almacena una lista de elementos con la clase .btnEliminación

  //A continuación para cada elemento de la lista aplicamos un evento de escucha.
  btnEliminacion.forEach((btn) => {
    btn.addEventListener("click", (eventClick) => {
      const confirmacion = confirm("¿Seguro que desea eliminar el usuario?");
      if (!confirmacion) { 
        eventClick.preventDefault(); //Si la confirmación devuelve false se cancelará el evento click
      }
    });
  });
})();
