function colorChange(id) {

    var elem = document.getElementById(id).style.fill;
    console.log(elem);
    console.log(id.charAt(7));
    if (elem == "rgb(255, 255, 255)" || elem == ""){
        console.log('t2');
        if (id.charAt(7) == '0' )
            document.getElementById(id).style.fill = "teal";
        if (id.charAt(7) == '1' )
            document.getElementById(id).style.fill = "pink";
        if (id.charAt(7) == '2' )
            document.getElementById(id).style.fill = "blue";
        if (id.charAt(7) == '3' )
            document.getElementById(id).style.fill = "red";
        if (id.charAt(7) == '4' )
            document.getElementById(id).style.fill = "green";
        if (id.charAt(7) == '5' )
            document.getElementById(id).style.fill = "orange";
        if (id.charAt(7) == '6' )
            document.getElementById(id).style.fill = "yellow";
        if (id.charAt(7) == '7' )
            document.getElementById(id).style.fill = "violet";
    }
    else {
        console.log('t1');
        document.getElementById(id).style.fill = "#fff";
    } 

}