document.addEventListener('DOMContentLoaded', function () {
    const likeButtons = document.querySelectorAll('.like-section button');

    likeButtons.forEach(button => {
        button.addEventListener('click', function () {
            const likeCountSpan = this.previousElementSibling;
            let likes = parseInt(likeCountSpan.textContent.match(/\d+/)[0]);
            likeCountSpan.textContent = (likes + 1) + ' like(s)';
        });
    });
});
