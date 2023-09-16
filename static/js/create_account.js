const full_name_field = document.getElementById('full_name');
const email_field = document.getElementById('email');
const phone_field = document.getElementById('phone');
const username_field = document.getElementById('username');
const password_field = document.getElementById('password')
const password_confirm_field = document.getElementById('password_confirm');

full_name_field.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        email_field.focus();
    };
});

email_field.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        phone_field.focus();
    }
});

phone_field.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        username_field.focus();
    };
});

username_field.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        password_field.focus();
    };
});

password_field.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        password_confirm_field.focus();
    };
});

password_confirm_field.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        document.getElementById('form-create-account').submit();
    };
});

// floar label
const form_control = document.querySelectorAll('.text-field');

form_control.forEach(control => {
    const label = control.closest('.input-space').querySelector('label');

    control.addEventListener('focus', () => {
        label.classList.add('active');
    });

    control.addEventListener('blur', () => {
        if (control.value.trim() === '') {
            label.classList.remove('active');
        }
    });

    if (control.value.trim() !== '') {
        label.classList.add('active');
    }
});

// password vizualization
const password_view_button = document.getElementById("password-view-button");
const password_view = document.getElementById("password-view");
const password = document.getElementById("password");

password_view_button.addEventListener("click", function () {
    if (password.type === "password") { 
        password.type = "text";
        password_view.classList.remove("fa-eye-slash");
        password_view.classList.add("fa-eye");
    } else {
        password.type = "password";
        password_view.classList.add("fa-eye-slash");
        password_view.classList.remove("fa-eye");
    };
});

// password vizualization
const password_confirm_view_button = document.getElementById("password-confirm-view-button");
const password_confirm_view = document.getElementById("password-confirm-view");
const password_confirm = document.getElementById("password_confirm");

password_confirm_view_button.addEventListener("click", function () {
    if (password_confirm.type === "password") {
        password_confirm.type = "text";
        password_confirm_view.classList.remove("fa-eye-slash");
        password_confirm_view.classList.add("fa-eye");
    } else {
        password_confirm.type = "password";
        password_confirm_view.classList.add("fa-eye-slash");
        password_confirm_view.classList.remove("fa-eye");
    };
});