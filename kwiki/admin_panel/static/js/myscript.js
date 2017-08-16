'use strict'

$("#auth_form").submit(function(e){
    e.preventDefault();
    $.ajax({
        headers: { "X-CSRFToken": readCookie("csrftoken") },
        url: 'auth/',
        type: "POST",
        data: $.param({
            username: $("#login").val(),
            password: $("#password").val(),
            }),
        success: function(data){
            if (data.status == 1)
                location.href = '/'
            else
                $("#error").text('Invalid login or password')
                $("#login").val('')
                $("#password").val('')
            }
        })
    })


function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}