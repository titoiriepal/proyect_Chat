//const {Console} = require("console");

window.onload = function() {


    $.getJSON("./mensajes.json", function(json) {
        // inicio
        console.log(json); // this will show the info it in firebug console
        let i = 0
        $.each(json, function(index) {
            /// do stuff
            $.each(this, function(msg_id, v) {
                // tempHtml = $("#textTemplate").html()
                const txt = this["txt"]
                const user = this["user"]

                // const newMsg = `<p class= "mensajeEnChat" id="${msg_id}"><span>${user}: ${txt}</span></p>`
                const newMsg = `
                    <div class="bubble" id="${msg_id}">
                        <div class="txt">
                            <p class="name">${user}</p>
                            <p class="message">${txt}</p>
                            <span class="timestamp">10:20 pm</span>
                        </div>
                    <div class="bubble-arrow"></div>`
                const ownMsg = `
                    <div class="bubble alt" id="${msg_id}">
                        <div class="txt">
                            <p class="name alt">+353 87 1234 567<span>${user}</span></p>
                            <p class="message">${txt}</p>
                            <span class="timestamp">10:22 pm</span>
                    </div>
                    <div class="bubble-arrow alt"></div>`

                let msgToAppend = (Math.random() >= 0.5 ? newMsg : ownMsg)

                $(".speech-wrapper").append(msgToAppend)
            });
        });
        // fin
    });


    $.ajax({
        url: "/ajax",
        type: "post",
        data: null,
        dataType: 'json',
        success: function(data) {
            console.log(data);
            console.log(data.id);
        }
    });

    var formulario = document.getElementById('botonSend')
    formulario.addEventListener('click', function() {
        var usuario = document.getElementById("fname")
        //    var mensaje = document.getElementById("ftext")
        //    console.log(usuario.value)
        //    console.log(mensaje.value)
        // $.post("127.0.0.1", {
        //     json_string: JSON.stringify({
        //         user: usuario.value,
        //         txt: mensaje.value
        //     })
    });

    //borrar mensaje después de enviar (POST)
    mensaje.value = ""
};