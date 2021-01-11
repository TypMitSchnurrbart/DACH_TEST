const loginForm = document.getElementById("loginForm");
const email = document.getElementById("email");
const psw = document.getElementById("password");


loginForm.addEventListener("submit", e => {
    
    checkInputs()

    function checkInputs() {
        // get the values from the input, remove all white spaces
        const emailValue = email.value.trim();
        const pswValue = psw.value.trim();

        if(emailValue === "") {
            setErrorFor(email, "E-Mail-Adresse muss ausgefüllt sein!");
        } else if (!isEmail(emailValue)) {
            setErrorFor(email, "Keine gültige E-Mail-Adresse!");
        } else {
            setSuccessFor(email);
        }

        if(pswValue === "") {
            setErrorFor(psw, "Passwort muss ausgefüllt sein!");
        } else {
            setSuccessFor(psw);
        }
    }

    function setErrorFor(input, message) {
        e.preventDefault();
        const formControl = input.parentElement;
        const small = formControl.querySelector("small");

        // add error class
        formControl.className = "col-75 form-control error";

        // add error message insde small
        small.innerText = message;
    }

    function setSuccessFor(input) {
        const formControl = input.parentElement;
        formControl.className = "col-75 form-control success";
    }

    function isEmail(email) {
        return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
    }
});