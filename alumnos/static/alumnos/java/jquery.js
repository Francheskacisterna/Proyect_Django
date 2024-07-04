$(document).ready(function() {
    // Validación del formulario de inicio de sesión
    $('#login-form').submit(function(event) {
        var email = $('#email-login').val();
        var password = $('#password-login').val();
        var emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        var passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w]).{8,}$/;

        // Validación del correo electrónico
        if (!emailRegex.test(email)) {
            alert('Por favor ingresa un correo electrónico válido.');
            event.preventDefault(); // Detiene la presentación del formulario
        }

        // Validación de la contraseña
        if (!passwordRegex.test(password)) {
            alert('La contraseña debe tener al menos 8 caracteres, incluir al menos un número, una letra mayúscula, una letra minúscula, y un carácter especial.');
            event.preventDefault(); // Detiene la presentación del formulario
        }
    });

    // Botón de mensaje motivacional del día
    $('#show-message-btn').click(function() {
        alert('Nueva cita del día: "La vida es 10% lo que te ocurre y 90% cómo reaccionas a ello." - Charles R. Swindoll');
    });
});



