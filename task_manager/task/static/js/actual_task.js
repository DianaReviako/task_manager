function deleteSelectedTr () {
    let dict = {'selected': []}
    let csrf =(document.cookie).split('=')[1];
    dict['csrfmiddlewaretoken'] = csrf
    let form = $("#task_status");
    let tbody = $("tbody", form);
    let tds = $("td", tbody)
    for (let td of tds) {
        let input = $("input[type=checkbox]", td)
        if (input.prop("checked")) {
        let id = input.attr("id");
        dict['selected'].push(id)
        $.ajax({
        url: $("#task_status").attr("action"),
        method: $("#task_status").attr('method'),
        data: dict,
        }).done(function() {
            $("#" + id).closest("tr").remove();
            console.log(id)

        });
        }
    }
}




$(document).ready(function () {
    $("#button").on("click", function(){
        deleteSelectedTr ()
    });
});
