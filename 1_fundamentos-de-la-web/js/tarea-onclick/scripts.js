document.addEventListener('DOMContentLoaded', function () {
    const loginButton = document.querySelector('header button');
    const addButton = document.querySelector('main form button');
    const likeButtons = document.querySelectorAll('.pet button');

    // Función 1: Cambiar "Iniciar sesión" a "Cerrar sesión"
    loginButton.addEventListener('click', function () {
        if (loginButton.textContent === 'Iniciar sesión') {
            loginButton.textContent = 'Cerrar sesión';
        } else {
            loginButton.textContent = 'Iniciar sesión';
        }
    });

    // Función 2: Desaparecer el botón "Agregar definición"
    addButton.addEventListener('click', function (event) {
        event.preventDefault(); // Previene la acción por defecto para demostración
        addButton.parentElement.style.display = 'none';
    });

    // Función 3 y 4: Manejo de los "Me gusta"
    likeButtons.forEach(button => {
        button.addEventListener('click', function () {
            const petName = this.parentNode.querySelector('h2').textContent;
            alert(petName + ' was liked');

            // Incrementa el contador de "Me gusta"
            let likesCount = parseInt(this.textContent.match(/\d+/)[0]);
            this.textContent = (likesCount + 1) + ' me gusta';
        });
    });
});
