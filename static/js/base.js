window.addEventListener("load", inicio);
function inicio(){
    document.getElementById("buttonInput").addEventListener("click", getBotResponse);
}

function getBotResponse(){
    var rawText = $("#textInput").val();//almacenar lo que ingrese el usuario
    if (rawText!=""){
    var userHtml='<div class="messages__item messages__item--operator">'+rawText+'</div>';//variable para imprimir por pantalla lo que ingreso el usuario
    $("#textInput").val("");//cambia el valor del input a vacio porque su valor ya se imprimio
    $("#chatbox").append(userHtml);//añade el elemento al container
    document.getElementById('userInput').scrollIntoView({block:'start',behaviour:'smooth'});//solo para la barra de dezplazamiento
    $.get("/get",{msg:rawText}).done(function(data){//esto es para obtener el response del main
        if(data.includes("&")){
            link=data.substring(data.indexOf("&")+1);
            data=data.substr(0,data.indexOf("&"));
            var botHtml='<div class="messages__item messages__item--visitor">'+data+'</div>';//aqui se almacenara  la respuesta
            $("#chatbox").append(botHtml);//se  imprime la respuesta
            if (link.length<25){
                var linkHtml='<p class="messages__item messages__item--visitor">Para mayor información accede al siguiente link: <a href="'+link+'" target ="_blank">'+link+'</a></p>';//esto es  para el link
            }else{
                var linkHtml='<p class="messages__item messages__item--visitor">Para mayor información accede al siguiente link: <a href="'+link+'" target ="_blank">Press here</a></p>';//esto es  para el link
            }
            $("#chatbox").append(linkHtml)
        }
        else{
            var botHtml='<div class="messages__item messages__item--visitor">'+data+'</div>';//aqui se almacenara  la respuesta
            $("#chatbox").append(botHtml);//se  imprime la respuesta
        }

        //a partir de aqui se ddebe llamar al create
        $.get("/create",{answer:data}).done(function(lista){
            while(lista.includes("-")){
                final=lista.substr(0,lista.indexOf("-"));//esto hace un recorte de inicio a fin
                lista=lista.substring(lista.indexOf("-")+1);
                var alternative='<button  id="'+final+'" type="button" value="'+final+'" class="btn btn-green" onclick="alternative(id)" >'+final+'</button>'
                $("#chatbox").append(alternative)
                document.getElementById('userInput').scrollIntoView({block:'start', behaviour:'smooth'});
            }
        })
    });
    }
}
$("#textInput").keypress(function(e){//si presiona enter 
    if(e.which==13){
        getBotResponse();
    }
});
$("#buttonInput").click(function(){// si hace click en enviar
    getBotResponse();
})


