
async function cargarEstudios() {
    const contenedor = document.getElementById("contenedor-datos");

    try {
        const respuesta = await fetch("datos.json");

        if (!respuesta.ok) {
            throw new Error("No se pudo cargar el archivo JSON.");
        }

        const datos = await respuesta.json();
        const estudios = datos.estudios.estudio;

        contenedor.innerHTML = "";

        estudios.forEach((estudio) => {
            const tarjeta = document.createElement("article");
            tarjeta.className = "tarjeta-estudio";

            const fundadores = estudio.fundadores.join(", ");

            tarjeta.innerHTML = `
                <h2>${estudio.nombre}</h2>
                <p><strong>ID:</strong> ${estudio.id}</p>
                <p><strong>Fundadores:</strong> ${fundadores}</p>
                <p><strong>Fecha de fundación:</strong> ${estudio.fechaFundacion}</p>
                <p><strong>Activo:</strong> ${estudio.activo ? "Sí" : "No"}</p>
                <p><strong>Empresa matriz:</strong> ${estudio.empresaMatriz ?? "Ninguna"}</p>
                <p><strong>Ingresos:</strong> ${estudio.ingresosMillones} millones</p>
                <p><strong>Última actualización:</strong> ${estudio.ultimaActualizacion}</p>
            `;

            contenedor.appendChild(tarjeta);
        });

    } catch (error) {
        contenedor.innerHTML = `<p class="error">Error: ${error.message}</p>`;
    }
}

cargarEstudios();
