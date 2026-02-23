function chisteAleatorio(n, m) {
    return Math.floor(Math.random() * (m - n + 1)) + n;
}

const boton = document.getElementById("btn")
const parrafo = document.getElementById("texto")

boton.addEventListener("click", () =>{
    const chistes = [
  "—¿Cuál es el colmo de un jardinero? —Que siempre lo dejen plantado.",
  "—¿Cuál es el animal más antiguo? —La cebra, porque está en blanco y negro.",
  "—¿Por qué el libro de matemáticas estaba triste? —Porque tenía demasiados problemas.",
  "—¿Qué le dice un semáforo a otro? —No me mires, que me estoy cambiando.",
  "—¿Qué hace un pez? —Nada.",
  "—¿Qué hace un perro con un taladro? —Taladrando.",
  "—¿Cómo se despiden los químicos? —Ácido un placer."
]

    parrafo.textContent = chistes[aleatorioEntero(1, 7)]
})