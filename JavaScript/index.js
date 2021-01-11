const openNav = document.getElementById("openNav");

openNav.onclick = function() {
    document.getElementById("topNav").style.width = "100%";
}

const closeNav = document.getElementById("closeNav");

closeNav.onclick = function() {
    document.getElementById("topNav").style.width = "0%";
}
