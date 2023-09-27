document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("contact-form");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const nombre = document.getElementById("nombre").value;
        const email = document.getElementById("email").value;
        const mensaje = document.getElementById("mensaje").value;

        if (!nombre || !email || !mensaje) {
            alert("Por favor, complete todos los campos.");
            return;
        }

        alert(nombre);
        alert(email);
        alert(mensaje);

        const subject = `Mensaje de ${nombre}`;
        const mailtoLink = `mailto:correo_destino@example.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(mensaje)}`;

        window.location.href = mailtoLink;
    });
});