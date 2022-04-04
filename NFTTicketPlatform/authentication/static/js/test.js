$(document).ready(function () {

    // SmartWizard initialize
    $('#smartwizard').smartWizard();
    $('#done-btn').click(function () {
        $('#done-btn').css('pointerEvents', 'none');
        alert('You son of a bitch');
    })

});