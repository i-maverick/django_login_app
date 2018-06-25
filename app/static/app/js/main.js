$().ready(function() {
    var id = 1;

    $("#id_load_test").click(function() {
        $.get('/app/load_test', {id: id}, function(data) {
            id = id + 1;
            $("#id_test").html(data);
        })
    });
});
