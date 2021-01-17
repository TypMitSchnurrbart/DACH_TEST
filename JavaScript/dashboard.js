function doREQfetch(){
    var ident = document.getElementById("ident").value
    var data = { `ident=${ident}&next_param=from_testing`}

    fetch("./dashboard_json.py", {
        method: "POST",
        header: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `${data}`
    })
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
       lastRoom.innerHTML = "Raum " + data.lastRoom;
       }
       else{
       lastRoom.innerHTML = "-";
       }

       // room list
       var table = document.getElementById("tabelle");

       table.textContent = null;

       var row, raum, dt, zeit, pers;

       for (var i = 0; i < 5; i++) {
           if(data.roomHistory[i] != undefined) {
               row = table.insertRow(i);
               raum = row.insertCell(0);
               dt = row.insertCell(1);
               zeit = row.insertCell(2);
               pers = row.insertCell(3);
               raum.innerHTML = data.roomHistory[i].room;
               dt.innerHTML = data.roomHistory[i].date;
               zeit.innerHTML = data.roomHistory[i].begin;
               pers.innerHTML = data.roomHistory[i].end;
           } else {
               break;
           }
       }
    });
}

//nach Page-Load erstes Request, dann in 10Sek. Intervallen (JSON-GET)
window.onload = function() {
    //doREQ(); 
    //doREQfetch(); //beide Möglichkeiten funktionieren!

    setInterval(function() {
    //doREQ();
    doREQfetch();
}, 10 * 1000);
}