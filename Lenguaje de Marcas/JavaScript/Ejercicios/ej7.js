const form = document.getElementById("formDatos")
const resultado = document.getElementById("resultado")

form.addEventListener("submit", (event) => {
    event.preventDefault()

    const peso = document.getElementById("peso").value;
    const altura = document.getElementById("altura").value;
    const imc = peso / (altura * altura);

    if (imc < 18.5) {
        resultado.textContent = `Peso bajo`;
    }
    else if (imc >= 18.5 && imc <= 24.9) {
            resultado.textContent = `Peso normal`;
        }
    else if (imc >= 25) {
                resultado.textContent = `Sobrepeso`;
        }
})
