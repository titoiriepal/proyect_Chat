//const {Console} = require("console");


function addMessages(msg_id, v) {
    // tempHtml = $("#textTemplate").html()
    const txt = this["txt"]
    const user = this["user"]
    const dateTime = this["datetime"]


    // let dateTimeParts = dateTime.split(/[- :]/); // regular expression split that creates array with: year, month, day, hour, minutes, seconds values
    // dateTimeParts[1]--; // monthIndex begins with 0 for January and ends with 11 for December so we need to decrement by one

    // const dateObject = new Date(...dateTimeParts); // our Date object
    // const humanTime = dateObject.toLocaleString("es-ES")

    const dateObject = new Date(dateTime)

    const humanTime =
        (
            (
                (dateObject.getHours() < 10 ? '0' : '') +
                dateObject.getHours()

            ) + ':' +
            (
                (dateObject.getMinutes() < 10 ? '0' : '') +
                dateObject.getMinutes()
            ) +
            ':' +
            (
                (dateObject.getSeconds() < 10 ? '0' : '') +
                dateObject.getSeconds()
            )
        )


    // const newMsg = `<p class= "mensajeEnChat" id="${msg_id}"><span>${user}: ${txt}</span></p>`
    const newMsg = `
        <div class="bubble" id="${msg_id}">
            <div class="txt">
                <p class="name">${user}</p>
                <p class="message">${txt}</p>
                <span class="timestamp">${humanTime}</span>
            </div>
        <div class="bubble-arrow"></div>`
    const ownMsg = `
        <div class="bubble alt" id="${msg_id}">
            <div class="txt">
                <p class="name alt">+353 87 1234 567<span>${user}</span></p>
                <p class="message">${txt}</p>
                <span class="timestamp">${humanTime}</span>
        </div>
        <div class="bubble-arrow alt"></div>`

    let msgToAppend = (Math.random() >= 0.5 ? newMsg : ownMsg)

    $(".speech-wrapper").append(msgToAppend)
}


window.onload = function() {


    $.getJSON("/recibir", function(json) {
        // inicio
        console.log(json); // this will show the info it in firebug console
        let i = 0
        $.each(json, function(index) {
            /// do stuff
            $.each(this, addMessages);
        });
        // fin
    });


    // $.ajax({
    //     url: "/ajax",
    //     type: "post",
    //     data: null,
    //     dataType: 'json',
    //     success: function(data) {
    //         console.log(data);
    //         console.log(data.id);
    //     }
    // });

    var formulario = document.getElementById('botonSend')
    formulario.addEventListener('click', function() {
        var usuario = document.getElementById("fname")
        var mensaje = document.getElementById("ftext")
        let jsonString = JSON.stringify({
            user: usuario.value,
            txt: mensaje.value
        })
        console.log(usuario.value)
        console.log(mensaje.value)
        $.post("/enviar", {
            jsonString
        }).success(console.log("bien")).fail(console.log("mal"));


    })

    //borrar mensaje después de enviar (POST)
    //mensaje.value = ""

}