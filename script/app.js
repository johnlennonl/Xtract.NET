var swiper = new Swiper('.swiper-container', {
    loop: true, // Hace que el carrusel sea infinito
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    autoplay: {
        delay: 3000, // Cambia cada 3 segundos
        disableOnInteraction: false,
    },
    allowTouchMove: false, // Desactiva el scroll manual
    simulateTouch: false, // Desactiva la simulación de arrastre en dispositivos táctiles
});