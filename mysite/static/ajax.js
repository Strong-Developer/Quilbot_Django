// var appURL = "https://localhost:44301/";

function ajaxCall(uri, data, verb = "GET", callback, errorCallback) {

    $.ajax({
        cache: false,
        async: true,
        //contentType: "application/json; charset=utf-8",
        dataType: 'json',
        url: uri,
        //headers: {
        //    "Authorization": 'Bearer ' + localStorage.getItem('token')
        //},
        data: data,
        type: verb,
        success: function(data) {

            $('#btnRewrite').prop('disabled', false);
            if (callback !== undefined)
                callback(data);
        },
        error: function(r, t, e) {

            //if (r.status === 401) {
            //    if (r.statusText !== undefined && r.statusText.startsWith("No roles assigned to this user"))
            //        window.location.href = "/Account/NotAuthorized.aspx";
            //    else
            //        window.location.href = "/Account/Login";

            //    return;
            //}
            $('#btnRewrite').prop('disabled', false);
            if (errorCallback != null)
                errorCallback();
            else
                $('#txt_Result').val(e);
            alert("error");
        }
    });
}