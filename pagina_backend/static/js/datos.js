document.querySelector("#boton").addEventListener("click", function(event) {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente

    var apellido = document.getElementById("apellido").value;
    var cuenta = document.getElementById("ncuenta").value;

    // Crear un objeto FormData para enviar los datos al servidor
    var formData = new FormData();
    formData.append("apellido", apellido);
    formData.append("cuenta", cuenta);

    // Realizar la solicitud POST al servidor
    fetch("/horario", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Aquí puedes manejar la respuesta del servidor
        if (data.success) {
            showAlert(data.message);
            window.location.href = '/'; // Redirecciona al inicio (o donde quieras) después de mostrar el mensaje
        } else {
            showAlert(data.message);
        }
    })
    .catch(error => {
        console.error("Error:", error);
        showAlert("Hubo un error al enviar los datos. Por favor, inténtalo de nuevo.");
    });
});

function showAlert(message) {
    alert(message);
}
