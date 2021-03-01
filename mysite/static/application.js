$('#btnRewrite').click(function() {
    var strInput = $('#txt_Input').val();
    if (strInput.trim() == "") {
        alert("Please input text!");
        return;
    }
    var data = {
        'input': strInput
    };
    $('#txt_Result').val("rewriting...");
    $('#btnRewrite').prop('disabled', true);
    ajaxCall('/rewriter/onRewrite', data, "POST", handle_onRewrite);
});

function handle_onRewrite(data) {
    $('#txt_Result').val(data.result);
}