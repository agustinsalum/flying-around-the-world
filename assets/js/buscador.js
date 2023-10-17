       document.addEventListener("DOMContentLoaded", function() {
        //  DatePicker como forma de utilizar calendario, libreria utilizable de JS
        const picker = new Pikaday({
            field: document.getElementById('datepicker'),
            format: 'DD/MM/YYYY', // Pu
        });
    
        // 
        const numPasajeros = document.getElementById("num-pasajeros");
    
        // 
        numPasajeros.addEventListener("change", function() {
            // Asegúrate de que el valor esté en el rango de 0 a 6
            if (numPasajeros.value < 0) {
                numPasajeros.value = 0;
            } else if (numPasajeros.value > 6) {
                numPasajeros.value = 6;
            }
        });
    });
    
    document.addEventListener("DOMContentLoaded", function() {
        const fechaPartida = document.getElementById("fecha-partida");
        const fechaHoy = new Date().toISOString().split("T")[0]; // Obtiene la fecha actual en formato "YYYY-MM-DD"
        fechaPartida.setAttribute("min", fechaHoy);
    });





