let cadenas = ["Hola", "Perro", "Sol", "Gato", "Pájaro"]
let letra = "p"
function EmpiezaPorLetra(cadenas, letra){
    let palabraInicia = []
    for (let palabra of cadenas){
        if (palabra.startsWith(letra)){
            palabraInicia.push(palabra)
        }
    }
    return palabraInicia
}