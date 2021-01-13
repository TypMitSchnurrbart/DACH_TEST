// window.setInterval(function () {
//     var date = new Date();
//     alert(date.getMinutes();
//     if ((date.getMinutes() % 5) == 0) {

//         fetch("https://dhbwdach.ddns.net/dashboard.json")
//             .then(response => response.json())
//             .then(data => console.log(data));
//     }
// }, 60000);

// Funktion wird aufgrund von mehrfach-verwendung deklariert
function doREQ(){
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "test.json", true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            var data = JSON.parse(xhr.responseText);

            document.getElementById("state").innerHTML = "Status: " + data.status;
            document.getElementById("room").innerHTML = "Raum: " + data.room;
            document.getElementById("date").innerHTML = data.date;
        }
    }
    xhr.send(null);
}
function doREQfetch(){
    fetch("./test.json")
    .then(function(response) {
        return response.json();
    })
    .then(function(data){
        var a = document.getElementById("state");
        a.innerHTML = "Status: " + data.status;
    });
}



//nach Page-Load erstes Request, dann in 10Sek. Intervallen (JSON-GET)

// window.onload = function() {
//     var test = 1;
//     //doREQ(); 
//     doREQfetch(); //beide Möglichkeiten funktionieren!

//     setInterval(function() {
//     test += 1;
//     if (test == 3){
//         alert("It works!");
//     }
//     //doREQ();
//     doREQfetch();
// }, 10 * 1000);
// }