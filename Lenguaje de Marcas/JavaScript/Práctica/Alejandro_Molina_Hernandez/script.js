let jugadaHumano = ""
let puntosHumano = 0
let puntosCPU = 0
let botonSeleccionado = null

let botonPiedra = document.getElementById("piedra")
let botonPapel = document.getElementById("papel")
let botonTijera = document.getElementById("tijera")
let botonLagarto = document.getElementById("lagarto")
let botonSpock = document.getElementById("spock")

let botonJugar = document.getElementById("jugar")

let marcador = document.getElementById("marcador")
let mensaje = document.getElementById("mensaje")

let jugadas = ["piedra", "papel", "tijera", "lagarto", "spock"]


botonPiedra.addEventListener("click", () => {

    if (botonSeleccionado != null) {
        botonSeleccionado.style.border = "1px solid #ccc"
    }

    jugadaHumano = "piedra"
    botonPiedra.style.border = "2px solid black"
    botonSeleccionado = botonPiedra

})

botonPapel.addEventListener("click", () => {

    if (botonSeleccionado != null) {
        botonSeleccionado.style.border = "1px solid #ccc"
    }

    jugadaHumano = "papel"
    botonPapel.style.border = "2px solid black"
    botonSeleccionado = botonPapel

})

botonTijera.addEventListener("click", () => {

    if (botonSeleccionado != null) {
        botonSeleccionado.style.border = "1px solid #ccc"
    }

    jugadaHumano = "tijera"
    botonTijera.style.border = "2px solid black"
    botonSeleccionado = botonTijera

})

botonLagarto.addEventListener("click", () => {

    if (botonSeleccionado != null) {
        botonSeleccionado.style.border = "1px solid #ccc"
    }

    jugadaHumano = "lagarto"
    botonLagarto.style.border = "2px solid black"
    botonSeleccionado = botonLagarto

})

botonSpock.addEventListener("click", () => {

    if (botonSeleccionado != null) {
        botonSeleccionado.style.border = "1px solid #ccc"
    }

    jugadaHumano = "spock"
    botonSpock.style.border = "2px solid black"
    botonSeleccionado = botonSpock

})


botonJugar.addEventListener("click", () => {

    if (jugadaHumano == "") {
        mensaje.textContent = "Elige una jugada primero."
        return
    }

    let numero = Math.floor(Math.random() * 5)
    let jugadaCPU = jugadas[numero]

    let texto = `Tú has sacado ${jugadaHumano} y la CPU ${jugadaCPU}.`

    if (jugadaHumano == jugadaCPU) {

        texto = `${texto} Empate.`

    }

    else if (jugadaHumano == "piedra" && jugadaCPU == "tijera") {
        texto = `${texto} Piedra rompe Tijera. Gana el jugador.`
        puntosHumano++
    }

    else if (jugadaHumano == "piedra" && jugadaCPU == "lagarto") {
        texto = `${texto} Piedra aplasta Lagarto. Gana el jugador.`
        puntosHumano++
    }

    else if (jugadaHumano == "papel" && jugadaCPU == "piedra") {
        texto = `${texto} Papel cubre Piedra. Gana el jugador.`
        puntosHumano++
    }

    else if (jugadaHumano == "papel" && jugadaCPU == "spock") {
        texto = `${texto} Papel refuta Spock. Gana el jugador.`
        puntosHumano++
    }

    else if (jugadaHumano == "tijera" && jugadaCPU == "papel") {
        texto = `${texto} Tijera corta Papel. Gana el jugador.`
        puntosHumano++
    }

    else if (jugadaHumano == "tijera" && jugadaCPU == "lagarto") {
        texto = `${texto} Tijera decapita Lagarto. Gana el jugador.`
        puntosHumano++
    }

    else if (jugadaHumano == "lagarto" && jugadaCPU == "papel") {
        texto = `${texto} Lagarto devora Papel. Gana el jugador.`
        puntosHumano++
    }

    else if (jugadaHumano == "lagarto" && jugadaCPU == "spock") {
        texto = `${texto} Lagarto envenena Spock. Gana el jugador.`
        puntosHumano++
    }

    else if (jugadaHumano == "spock" && jugadaCPU == "tijera") {
        texto = `${texto} Spock aplasta Tijera. Gana el jugador.`
        puntosHumano++
    }

    else if (jugadaHumano == "spock" && jugadaCPU == "piedra") {
        texto = `${texto} Spock vaporiza Piedra. Gana el jugador.`
        puntosHumano++
    }

    else {

        if (jugadaCPU == "piedra" && jugadaHumano == "tijera") {
            texto = `${texto} Piedra rompe Tijera. Gana la CPU.`
        }

        else if (jugadaCPU == "piedra" && jugadaHumano == "lagarto") {
            texto = `${texto} Piedra aplasta Lagarto. Gana la CPU.`
        }

        else if (jugadaCPU == "papel" && jugadaHumano == "piedra") {
            texto = `${texto} Papel cubre Piedra. Gana la CPU.`
        }

        else if (jugadaCPU == "papel" && jugadaHumano == "spock") {
            texto = `${texto} Papel refuta Spock. Gana la CPU.`
        }

        else if (jugadaCPU == "tijera" && jugadaHumano == "papel") {
            texto = `${texto} Tijera corta Papel. Gana la CPU.`
        }

        else if (jugadaCPU == "tijera" && jugadaHumano == "lagarto") {
            texto = `${texto} Tijera decapita Lagarto. Gana la CPU.`
        }

        else if (jugadaCPU == "lagarto" && jugadaHumano == "papel") {
            texto = `${texto} Lagarto devora Papel. Gana la CPU.`
        }

        else if (jugadaCPU == "lagarto" && jugadaHumano == "spock") {
            texto = `${texto} Lagarto envenena Spock. Gana la CPU.`
        }

        else if (jugadaCPU == "spock" && jugadaHumano == "tijera") {
            texto = `${texto} Spock aplasta Tijera. Gana la CPU.`
        }

        else if (jugadaCPU == "spock" && jugadaHumano == "piedra") {
            texto = `${texto} Spock vaporiza Piedra. Gana la CPU.`
        }

        puntosCPU++

    }

    mensaje.textContent = texto

    marcador.textContent = `Jugador ${puntosHumano} - ${puntosCPU} CPU`

    if ((puntosHumano >= 3 || puntosCPU >= 3) && Math.abs(puntosHumano - puntosCPU) >= 2) {

        if (puntosHumano > puntosCPU) {
            mensaje.textContent = `${mensaje.textContent} ¡Has ganado la partida!`
        }
        else {
            mensaje.textContent = `${mensaje.textContent} La CPU ha ganado la partida.`
        }

        botonJugar.disabled = true

    }

})
