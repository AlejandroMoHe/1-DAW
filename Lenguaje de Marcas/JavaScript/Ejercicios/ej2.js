function aleatorioEntero(n, m) {
    return Math.floor(Math.random() * (m - n + 1)) + n;
}
const nAleatorio4 = aleatorioEntero(1, 4)
const spanD4 = document.getElementById("contador")
const boton = document.getElementById("d4")

boton.addEventListener("click", () => {
    spanD4.textContent = nAleatorio4;
});