$(document).ready(function() {
    $('.input-group.date').datepicker({
        format: "dd/mm/yyyy",
        todayBtn: "linked",
        language: "ru"
    });

    $('.input-group.date').datepicker().on('changeDate', function (e) {
        let value = $('.input-group.date').datepicker("getDate");
        let selectedMaster = document.getElementById('id_master');
        if (selectedMaster != null) {
            selectedMaster = selectedMaster.value;
        }
        $.ajax({
            url: "/get_appointments/",
            type: "GET",
            data: {
                day: value.getDate(),
                month: value.getMonth() + 1,
                year: value.getFullYear(),
                master: selectedMaster
            },
            dataType: "json",
            success: function(response) {
            $('#appointments-list').empty();
            if (response.length > 0) {
                response.forEach(function(appointment) {
                    let row = '<tr>';
                    row += '<td>' + appointment.start + '</td>';
                    row += '<td>' + appointment.end + '</td>';
                    row += '</tr>';
                    $('#appointments-list').append(row);
                });
            } else {
                $('#appointments-list').append('<tr><td colspan="2">Нет заявок</td></tr>');
            }
        },
            error: function(xhr, errmsg, err) {
                console.log(errmsg);
            }
         });
    });
});