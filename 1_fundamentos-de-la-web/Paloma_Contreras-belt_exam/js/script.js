function searchPets() {
    alert('Buscando mascotas del tipo: ' + document.getElementById('pet-select').value);
}

function pet(name) {
    let pets = document.getElementById(name + '-pets');
    let count = parseInt(pets.textContent) + 1;
    pets.textContent = count + ' caricias';
}

document.getElementById('donate').addEventListener('click', function () {
    this.style.display = 'none';
});
