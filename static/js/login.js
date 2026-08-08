// =================================
// Login Page JavaScript
// =================================


// Show / Hide Password

const togglePassword =
    document.getElementById("togglePassword");

const password =
    document.getElementById("password");


togglePassword.addEventListener("click", function () {

    if (password.type === "password") {

        password.type = "text";

        this.innerHTML =
            '<i class="fa-solid fa-eye-slash"></i>';

    } else {

        password.type = "password";

        this.innerHTML =
            '<i class="fa-solid fa-eye"></i>';

    }

});


// Login Form

const loginForm =
    document.getElementById("loginForm");


loginForm.addEventListener("submit", function (event) {

    event.preventDefault();

    const email =
        document.getElementById("email").value.trim();

    const passwordValue =
        document.getElementById("password").value.trim();


    if (email === "" || passwordValue === "") {

        alert("Please enter your email and password.");

        return;

    }


    alert("Login form submitted successfully!");

});