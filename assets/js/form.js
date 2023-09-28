
function sendMail() {
    const form_name = document.getElementById("name").value;
    const form_email = document.getElementById("email").value;
    const form_message = document.getElementById("message").value;

    if (!form_name || !form_email || !form_message) {
        alert("Por favor, complete todos los campos.");
        return;
    }

    var params = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        message: document.getElementById("message").value,
    };

    // Deben ingresar el serviceID y templateID
    const serviceID = 'service_yxvpl47';
    const templateID = 'template_8ldfder';

    emailjs.send(serviceID, templateID, params).then(function (res) {
        document.getElementById("name").value = "";
        document.getElementById("email").value = "";
        document.getElementById("message").value = "";
    })
    alert("Su mensaje se envio con exito!!")
    .catch (err => console.log(err));

}