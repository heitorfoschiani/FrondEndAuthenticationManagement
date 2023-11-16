const username_field = document.getElementById("username");
const password_field = document.getElementById("password");

username_field.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();
        password_field.focus();
    };
});

password_field.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        document.getElementById("form-login").submit();
    };
});

// floar label
const form_control = document.querySelectorAll(".text-field");

form_control.forEach(control => {
    const label = control.closest(".input-space").querySelector("label");

    control.addEventListener("focus", () => {
        label.classList.add("active");
    });

    control.addEventListener("blur", () => {
        if (control.value.trim() === "") {
            label.classList.remove("active");
        }
    });

    if (control.value.trim() !== "") {
        label.classList.add("active");
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
    }
});