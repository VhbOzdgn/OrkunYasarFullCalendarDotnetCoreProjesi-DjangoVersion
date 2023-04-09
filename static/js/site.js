function errorMessages(err){
    $('#patient_name_error').text(err.patient_name);
    $('#patient_surname_error').text(err.patient_surname);
    $('#description_error').text(err.description);
    $('#start_date_error').text(err.start_date);
    $('#end_date_error').text(err.end_date);
    $('#user_error').text(err.user);
}


function clearMessages(){
    $('.clear-message').text('');
}


function inputsDisabledFromDetailModal(){
    $("#detailModal").find("input, select").prop("disabled", true);
}