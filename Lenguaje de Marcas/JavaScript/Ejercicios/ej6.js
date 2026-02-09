const form = document.getElementById("formDatos")
const resultado = document.getElementById("resultado")

form.addEventListener("submit", (event) => {
    event.preventDefault() // Evita que la página se recargue

    const num = document.getElementById("numero").value

    if (num % 2 === 0) {
        resultado.textContent = `Es primo`;
    } else {
        resultado.textContent = `No es primo`;
    }
})
