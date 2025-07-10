// Inicializar MixItUp
let mixerProyectos = mixitup('.proyectocontainer', {
    selectors: {
        target: '.proyectoitem'
    },
    animation: {
        duration: 300
    }
});

// Efecto de reveal al hacer scroll
document.addEventListener("DOMContentLoaded", function() {
    const habItems = document.querySelectorAll('.habitem');

    const revealItems = () => {
        const windowHeight = window.innerHeight;
        const revealPoint = 150; // Punto de revelación

        habItems.forEach(item => {
            const itemTop = item.getBoundingClientRect().top;

            if (itemTop < windowHeight - revealPoint) {
                item.classList.add('active');
            } else {
                item.classList.remove('active');
            }
        });
    };

    window.addEventListener('scroll', revealItems);
    revealItems(); // Llamar a la función al cargar la página
});

// Enviar correo electrónico
const contactoform = document.getElementById('contactoform'),
    contactonombre = document.getElementById('contactonombre'),
    contactoemail = document.getElementById('contactoemail'),
    mensaje = document.getElementById('mensaje'),
    contactomensaje = document.getElementById('contactomensaje');

const sendEmail = (e) => {
    e.preventDefault();

    if (contactonombre.value === '' || contactoemail.value === '' || mensaje.value === '') {
        contactomensaje.classList.remove('color-light');
        contactomensaje.classList.add('color-dark');
        contactomensaje.textContent = 'No puedes dejar celdas vacías';
    } else {
        emailjs.sendForm('service_3gjd272', 'template_88ctyru', 'contactoform', 'S2Y4k7G1Ue7EABt0n')
            .then(() => {
                contactomensaje.classList.add('color-light');
                contactomensaje.textContent = 'Mensaje enviado';
                
                setTimeout(() => {
                    contactomensaje.textContent = '';
                }, 5000);
            })
            .catch((error) => {
                console.error('Error al enviar el mensaje:', error);
                contactomensaje.classList.remove('color-light');
                contactomensaje.classList.add('color-dark');
                contactomensaje.textContent = 'Error al enviar el mensaje';
            });
    }
};

contactoform.addEventListener('submit', sendEmail);
