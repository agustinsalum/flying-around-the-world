document.addEventListener("DOMContentLoaded", function() {
    const botonMostrarUbicacion = document.getElementById("mostrar-ubicacion");
    const ubicacion = document.getElementById("ubicacion");

    botonMostrarUbicacion.addEventListener("click", function() {
        ubicacion.style.display = "block";
    });
});
