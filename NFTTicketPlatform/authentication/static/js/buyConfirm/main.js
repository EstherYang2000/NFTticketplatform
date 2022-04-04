$(function(){
    $("#form-total").steps({
        headerTag: "h2",
        bodyTag: "section",
        transitionEffect: "fade",
        enableAllSteps: true,
        autoFocus: true,
        transitionEffectSpeed: 500,
        titleTemplate : '<div class="title">#title#</div>',
        labels: {
            previous : 'Back',
            next : 'Next',
            finish : 'Confirm',

            current : 'exhibitionOrder'
        },

        onStepChanging: function (event, currentIndex, newIndex) {
            var fullname = $('#first_name').val() + ' ' + $('#last_name').val();
            var room = $('#room').val();
            var day = $('#day').val();
            var time = $('#time').val();

            $('#fullname-val').text(fullname);
            $('#room-val').text(room);
            $('#day-val').text(day);
            $('#time-val').text(time);
            return true;
        },
        onFinished: function (event, currentIndex) {
            $("#form-register").submit();
        }

    });
    $("#day").datepicker({
        dateFormat: "MM - DD - yy",
        showOn: "both",
        buttonText : '<i class="zmdi zmdi-chevron-down"></i>',
    });
    $('#fee').val(parseFloat(($('#ticket_cost').val()*0.03)));

    $('#total_cost').val(parseFloat($('#ticket_cost').val())+parseFloat($('#fee').val()));

});
