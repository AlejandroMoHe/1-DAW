let contador = 0

const spanContador = document.getElementById("contador")
const boton = document.getElementById("btnIncrementar")

boton.addEventListener("click", () => {
    contador++;
    spanContador.textContent = contador;
});