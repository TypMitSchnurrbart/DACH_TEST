function doREQfetch(){
    var ident = document.getElementById("ident").value
    var data = `ident=${ident}&next_param=from_testing`

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
       var table = document.getElementById("tabelle");
       var row, raum, dt, zeit, pers;
    
       table.textContent = null;

       status.innerHTML = "Status: " + data.state;
       
       if (data.lastRoom !== "$false$") {
           lastRoom.innerHTML = `Raum: ${data.lastRoom}`;

           // room list
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
        } else { 
            lastRoom.innerHTML = `Raum: ---`;
            row = table.insertRow(0);
            raum = row.insertCell(0);
            raum.innerHTML = "Kein Raum in den letzten 14 Tagen!";
        }
    });
}

//nach Page-Load erstes Request, dann in 10Sek. Intervallen (JSON-GET)
window.onload = function() {
    // doREQfetch();

    setInterval(function() {
    doREQfetch();
    }, 60 * 1000);
}