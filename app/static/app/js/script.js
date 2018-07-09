$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

$().ready(function() {
    $('#button-enter').click(function() {
        var text = $('#input-text').val();
        $.post('app/input_text/', {data: text}, function (data) {
            console.log(data)
        });
    });

    $('#id_main').click(function() {
        $.get('app/main/', {}, function (data) {
            console.log(data);
        })
    });

    $('#id_form').submit(function () {
        var obj = $(this).serializeJSON();
        var jsonString = JSON.stringify(obj);
        $.post('app/submit_form/', {data: jsonString}, function(data) {
            console.log(data.data);
        });
        return false;
    });
});
