// =================================
// Register Page JavaScript
// =================================


// Password Elements

const password =
    document.getElementById("password");

const confirmPassword =
    document.getElementById("confirmPassword");


// Toggle Password

const togglePassword =
    document.getElementById("togglePassword");


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


// Toggle Confirm Password

const toggleConfirmPassword =
    document.getElementById("toggleConfirmPassword");


toggleConfirmPassword.addEventListener("click", function () {

    if (confirmPassword.type === "password") {

        confirmPassword.type = "text";

        this.innerHTML =
            '<i class="fa-solid fa-eye-slash"></i>';

    } else {

        confirmPassword.type = "password";

        this.innerHTML =
            '<i class="fa-solid fa-eye"></i>';

    }

});


// Register Form

const registerForm =
    document.getElementById("registerForm");


registerForm.addEventListener("submit", function (event) {

    event.preventDefault();


    const fullName =
        document.getElementById("fullName").value.trim();

    const email =
        document.getElementById("email").value.trim();

    const phone =
        document.getElementById("phone").value.trim();

    const passwordValue =
        password.value.trim();

    const confirmPasswordValue =
        confirmPassword.value.trim();

    const terms =
        document.getElementById("terms").checked;


    // Check required fields

    if (
        fullName === "" ||
        email === "" ||
        phone === "" ||
        passwordValue === "" ||
        confirmPasswordValue === ""
    ) {

        alert("Please fill in all fields.");

        return;

    }


    // Check phone number

    if (!/^[0-9]{10}$/.test(phone)) {

        alert("Please enter a valid 10-digit phone number.");

        return;

    }


    // Check password length

    if (passwordValue.length < 6) {

        alert("Password must contain at least 6 characters.");

        return;

    }


    // Check passwords

    if (passwordValue !== confirmPasswordValue) {

        alert("Passwords do not match.");

        return;

    }


    // Check terms

    if (!terms) {

        alert("Please agree to the Terms & Conditions.");

        return;

    }


    // Success message

    alert(
        "Registration form submitted successfully!"
    );

});