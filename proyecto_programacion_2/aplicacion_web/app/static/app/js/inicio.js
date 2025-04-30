(function () {

const btnEliminacion = document.querySelectorAll('.btnEliminacion');
btnEliminacion.forEach((btn) => {
    btn.addEventListener('click', (e) => {
       const confirmacion = confirm("¿Está seguro de que desea eliminar este curso?");
       if(!confirmacion){
         e.preventDefault();
        }
        // Evita que el formulario se envíe si el usuario no confirma
       });
    });
})();