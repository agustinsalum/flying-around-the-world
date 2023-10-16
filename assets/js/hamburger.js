document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('mobile-menu').addEventListener('click', function() {
        console.log('clic');
        let navMenu = document.querySelector('.nav-menu');
        navMenu.classList.toggle('active');
    });
});

