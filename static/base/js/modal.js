window.onload = () => {

    var default_currency_localStorage = localStorage.getItem('def_cur')

    if (!default_currency_localStorage) {
        $(`#currency_selector_modal`).modal("show");
        $('#currency_selector_modal').on('hidden.bs.modal', function (e) {
            if (!localStorage.getItem('def_cur')){
                $(`#currency_selector_modal`).modal("show");
            }
          })
        $('#currency_selector_modal_submit_btn').on('click', () => {
            localStorage.setItem('def_cur', $('#currency_selector_modal_select_input').val())
            $(`#currency_selector_modal`).modal("hide");
        })
    }
    
}