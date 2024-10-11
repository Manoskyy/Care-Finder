function confirmPass(){
    var ini_p;
    ini_p = document.getElementById("initial").value;

    var fin_p;
    fin_p = document.getElementById("final").value;

    if (ini_p == fin_p) {
        window.alert('passwords match')
    } else {
        window.alert('passwords do not match')
    }
}