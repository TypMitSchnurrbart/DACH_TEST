// const { doc } = require("prettier");

//Funktion wird aufgrund von mehrfach-verwendung deklariert
function doREQ(){
     var xhr = new XMLHttpRequest();
     xhr.open("GET", "test.json", true);
     xhr.onreadystatechange = function() {
         if (xhr.readyState == 4) {
             var data = JSON.parse(xhr.responseText);

             var a = document.getElementById("state");
             a.innerHTML = "Status: " + data.status;
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
        // Deklarieren von Variablen notwendig? ==> direkter Edit?
        //upper Elements
        var status = document.getElementById("state");
        var lastRoom = document.getElementById("lastR"); 
        
        status.innerHTML = "Status: " + data.state;
        if (data.roomHistory[0] != undefined){
        lastRoom.innerHTML = "Raum " + data.roomHistory[0].room;
        }
        else{
        lastRoom.innerHTML = "-";
        }
        
        // room list
        var table = document.getElementById("tabelle");
        var row, raum, dt, zeit, pers;
        for (var i = 0; i < 5; i++)
        {
            if(data.roomHistory[i] != undefined)
            {
            row = table.insertRow(i);
            raum = row.insertCell(0);
            dt = row.insertCell(1);
            zeit = row.insertCell(2);
            pers = row.insertCell(3);
            raum.innerHTML = data.roomHistory[i].room;
            dt.innerHTML = data.roomHistory[i].date;
            zeit.innerHTML = data.roomHistory[i].time;
            pers.innerHTML = data.roomHistory[i].nrUser;
            }
            else{
                break;
            }
        }
     });
 }

 //nach Page-Load erstes Request, dann in 10Sek. Intervallen (JSON-GET)
 window.onload = function() {
     //doREQ(); 
     doREQfetch(); //beide Möglichkeiten funktionieren!

     setInterval(function() {
     //doREQ();
     doREQfetch();
 }, 60 * 1000);
 }