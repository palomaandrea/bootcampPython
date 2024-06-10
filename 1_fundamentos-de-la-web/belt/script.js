function findPet() {
    // Placeholder for find pet functionality
}

function pet(name) {
    let petButton = document.querySelector(`button[onclick="pet('${name}')"]`);
    let petCount = petButton.nextElementSibling;
    let count = parseInt(petCount.textContent) + 1;
    petCount.textContent = count + ' petting(s)';
}

document.getElementById('donate').addEventListener('click', function () {
    this.style.display = 'none';
});
