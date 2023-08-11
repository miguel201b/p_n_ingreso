function obtenerPrimeraLetra(apellido) {
    return apellido.charAt(0).toUpperCase();
}

document.querySelector("#boton").addEventListener("click", function() {
        var apellido = document.getElementById("apellido").value;
        var primeraLetra = obtenerPrimeraLetra(apellido);
        var cuenta = document.getElementById("ncuenta").value;

        alert("Apellido: " + primeraLetra + "\nNúmero de cuenta: " + cuenta);
    });