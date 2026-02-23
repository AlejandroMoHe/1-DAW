const form = document.getElementById("formulario")
const costeTotal = document.getElementById("coste")
const consumo = document.getElementById("consumo")

form.addEventListener("submit", (event) =>{
    event.preventDefault()

    const kilometros = document.getElementById("km").value
    const litros = document.getElementById("litro").value
    const precio = document.getElementById("precio").value

    const consumoFinal = (litros / kilometros * 100)
    const costeFinal = (litros * precio)

    consumo.textContent = `Consumo: ${consumoFinal.toFixed(2)}L/100km`
    costeTotal.textContent = `Coste total: ${costeFinal.toFixed(2)}€`
})