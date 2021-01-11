const registerForm = document.getElementById("registerForm");
const fname = document.getElementById("vorname");
const lname = document.getElementById("nachname");
const str = document.getElementById("strasse");
const sta = document.getElementById("hausnummer");
const post = document.getElementById("postleitzahl");
const residence = document.getElementById("ort");
const email = document.getElementById("email");
const psw1 = document.getElementById("password");
const psw2 = document.getElementById("password_repeat");

registerForm.addEventListener("submit", e => {
    
    checkInputs()

    function checkInputs() {
        // get the values from the input, remove all white spaces
        const fnameValue = fname.value.trim();
        const lnameValue = lname.value.trim();
        const strValue = str.value.trim();
        const staValue = sta.value.trim();
        const postValue = post.value.trim();
        const residenceValue = residence.value.trim();
        const emailValue = email.value.trim();
        const psw1Value = psw1.value.trim();
        const psw2Value = psw2.value.trim();
        
        if(fnameValue === "") {
            setErrorFor(fname, "Dieses Feld muss ausgefüllt sein!");
        } else {
            setSuccessFor(fname);
        }

        if(lnameValue === "") {
            setErrorFor(lname, "Dieses Feld muss ausgefüllt sein!");
        } else {
            setSuccessFor(lname);
        }

        if(strValue === "") {
            setErrorFor(str, "Dieses Feld muss ausgefüllt sein!");
        } else {
            setSuccessFor(str);
        }

        if(staValue === "") {
            setErrorFor(sta, "Dieses Feld muss ausgefüllt sein!");
        } else if (!isSta(staValue)) {
            setErrorFor(sta, "Dies ist keine gültige Hausnummer!")
        } else {
            setSuccessFor(sta);
        }

        if(postValue === "") {
            setErrorFor(post, "Dieses Feld muss ausgefüllt sein!");
        } else if (!isPost(postValue)) {
            setErrorFor(post, "Dies ist keine gültige Postleitzahl!")
        } else {
            setSuccessFor(post);
        }

        if(residenceValue === "") {
            setErrorFor(residence, "Dieses Feld muss ausgefüllt sein!");
        } else {
            setSuccessFor(residence);
        }

        if(emailValue === "") {
            setErrorFor(email, "E-Mail-Adresse muss ausgefüllt sein!");
        } else if (!isEmail(emailValue)) {
            setErrorFor(email, "Keine gültige E-Mail-Adresse!");
        } else {
            setSuccessFor(email);
        }

        if(psw1Value === "") {
            setErrorFor(psw1, "Passwort muss ausgefüllt sein!");
        } 
        else if (!pswAllowed(psw1Value)) {
            setErrorFor(psw1, "min. 8 Zeichen, Groß- und Kleinschreibung, eine Zahl und ein Sonderzeichen!");
        } 
        else {
            setSuccessFor(psw1);
        }

        if(psw2Value === "") {
            setErrorFor(psw2, "Passwort muss ausgefüllt sein!");
        } else if (psw1Value !== psw2Value) {
            setErrorFor(psw2, "Beide Passwörter müssen übereinstimmen!");
        } else {
            setSuccessFor(psw2);
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

    function isSta(sta) {
        return /[1-9][0-9]*[A-Za-z]*/.test(sta);
    }

    function isPost(post) {
        return /[0-9]{5}/.test(post);
    }

    function isEmail(email) {
        return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
    }

    function pswAllowed(psw) {
        return /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/.test(psw);
    }
});