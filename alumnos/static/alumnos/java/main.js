document.addEventListener('DOMContentLoaded', function() {
    // Modal interaction
    const openModal = document.querySelector('.mi-boton');
    const modal = document.querySelector('.modal');
    const closeModal = document.querySelector('.modal__close');

    if (openModal && closeModal && modal) {
        openModal.addEventListener('click', (e) => {
            e.preventDefault();
            modal.classList.add('modal--show');
        });

        closeModal.addEventListener('click', (e) => {
            e.preventDefault();
            modal.classList.remove('modal--show');
        });
    } else {
        console.log('One of the modal elements is missing.');
    }

    // Validación de formulario de Contacto
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(event) {
            if (!validateContactForm()) {
                event.preventDefault(); // Prevent form submission if validation fails
            }
        });
    }

    function validateContactForm() {
        return validateContactName('nombre') && validateContactEmail('email-contact') && validateContactMessage('mensaje');
    }

    function validateContactName(id) {
        const contactName = document.getElementById(id).value;
        if (contactName.trim().length === 0) {
            alert('Por favor ingresa tu nombre.');
            return false;
        }
        return true;
    }

    function validateContactEmail(id) {
        return validateEmailRegister(id);  // Reuse the email validation function
    }

    function validateContactMessage(id) {
        const contactMessage = document.getElementById(id).value;
        if (contactMessage.trim().length === 0) {
            alert('Por favor ingresa tu mensaje.');
            return false;
        }
        return true;
    }

    // Función de cambio de tema claro y oscuro
    const themeToggler = document.getElementById('theme-toggler');
    if (themeToggler) {
        themeToggler.addEventListener('click', function() {
            const body = document.body;
            body.classList.toggle('dark-theme'); // Cambia la clase para aplicar el tema oscuro

            const icon = themeToggler.querySelector('i');  // Encuentra el ícono dentro del botón
            if (body.classList.contains('dark-theme')) {
                icon.classList.remove('bi-sun');
                icon.classList.add('bi-sun-fill');
            } else {
                icon.classList.remove('bi-sun-fill');
                icon.classList.add('bi-sun');
            }
        });
    }
});
