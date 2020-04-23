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
            let validBlock = $(".form-is-valid");
            validBlock[0].innerHTML = response.result;
            validBlock.show();
            validBlock.fadeOut(10000);
        },
        error: (response) => {
            for (let key in response.responseJSON) {
                let errorMessage = response.responseJSON[key];
                let errorBlock = $(`input[name="${key}"]`).siblings('.valid-message');
                let temp = '';
                errorMessage.forEach((item) => {
                    temp += `<li>${item}</li>`;
                });
                errorBlock[0].innerHTML = temp;
                errorBlock.show();
                errorBlock.fadeOut(10000);
            };
        }
    });
}
