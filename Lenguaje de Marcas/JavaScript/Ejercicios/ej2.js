function aleatorioEntero(n, m) {
    return Math.floor(Math.random() * (m - n + 1)) + n;
}

const dado4 = document.getElementById(d4);
const resultado4 = document.getElementById(r4);

dado4.addEventListener('click', () =>{
    resultado4.textContent = aleatorioEntero(1, 4)
})