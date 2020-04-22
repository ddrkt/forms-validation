let validForm = document.getElementById("main-form");
let submitButton = document.getElementById("submit-button");


submitButton.onclick = function(e) {
    e.preventDefault();
    let inputs = validForm.getElementsByClassName("form-for-valid");
    let values = {};
    for (let input of inputs) {
        var name = input.getAttribute("name");
        values[name] = input.value;
    }
    jQuery.ajax({
        url: 'forms/values/',
        method: 'POST',
        data: values,
        success: (response) => {
            debugger;
        },
        error: (response) => {
            debugger;
        }
    });
}
