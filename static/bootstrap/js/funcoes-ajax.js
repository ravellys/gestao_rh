function utilizouHoraExtra(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/horas-extras/utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function(result){
            console.log(result.horas)
            $("#mensagem").text(result.mensagem);
            $("#horas").text(result.horas);
        }
    });
}

function naoUtilizouHoraExtra(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/horas-extras/nao-utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function(result){
            console.log(result.horas)
            $("#mensagem").text(result.mensagem);
            $("#horas").text(result.horas);
        }
    });
}