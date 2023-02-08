// Funsi Button
function printName() {
    eel.name()
}
function datang() {
    eel.datang()
}
function pulang() {
    eel.pulang()
}

// Stream Video dan Data
// Video
eel.expose(set_elapsedtime);
function set_elapsedtime(elapsedtime) {
    document.getElementById("elapsedtime").innerHTML = "elapsedtime:" + elapsedtime + "s";
}
eel.expose(set_base64image);
function set_base64image(base64image) {
    document.getElementById("python_video").src = base64image;
}


// Data
// Images Name
function imgName(){
    eel.expose(imgName);
    function imgName(imgName){
        document.getElementById("imgName").innerHTML = imgName;
    }
}
// Time from Python
function pythonTime(){
    eel.expose(pythonTime);
    function pythonTime(realTime){
        document.getElementById("pythonTime").innerHTML = realTime;
    }
}
// Date from python
function pythonDate(){
    eel.expose(pythonDate);
    function pythonDate(realDate){
        document.getElementById("pythonDate").innerHTML = realDate;
    }
}
// Status from python
function pythonStatus(){
    eel.expose(pythonStatus);
    function pythonStatus(status){
        document.getElementById("pythonStatus").innerHTML = status;
    }
}

// Clock
function updateClock() {
    var now = new Date();
    var dname = now.getDay(),
        mo = now.getMonth(),
        dnum = now.getDate(),
        yr = now.getFullYear(),
        hou = now.getHours(),
        min = now.getMinutes(),
        sec = now.getSeconds(),
        pe = "AM";

    if (hou >= 12) {
        pe = "PM";
    }
    if (hou == 0) {
        hou = 12;
    }
    if (hou > 12) {
        hou = hou - 12;
    }

    Number.prototype.pad = function (digits) {
        for (var n = this.toString(); n.length < digits; n = 0 + n);
        return n;
    }

    var months = ["January", "February", "March", "April", "May", "June", "July", "Augest", "September", "October", "November", "December"];
    var week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    var ids = ["dayname", "month", "daynum", "year", "hour", "minutes", "seconds", "period"];
    var values = [week[dname], months[mo], dnum.pad(2), yr, hou.pad(2), min.pad(2), sec.pad(2), pe];
    for (var i = 0; i < ids.length; i++)
        document.getElementById(ids[i]).firstChild.nodeValue = values[i];
}

function initClock() {
    updateClock();
    window.setInterval("updateClock()", 1);
}

// style
var counter = 1;
setInterval(function () {
    document.getElementById('radio' + counter).checked = true;
    counter++;
    if (counter > 4) {
        counter = 1;
    }
}, 9000);