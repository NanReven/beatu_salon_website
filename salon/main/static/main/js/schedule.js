$(document).ready(function() {
    $('.input-group.date').datepicker({
        format: "dd/mm/yyyy",
        todayBtn: "linked",
        language: "ru"
    });

    $('.input-group.date').datepicker().on('changeDate', function (e) {
        let value = $('.input-group.date').datepicker("getDate");
        let selectedDay = value.getDate();
        let selectedMonth = value.getMonth() + 1;
        let selectedYear = value.getFullYear();
        let selectedMaster = document.getElementById('id_master');
        if (selectedMaster != null) {
            selectedMaster = selectedMaster.value;
        }
        $.ajax({
            url: "/get_appointments/",
            type: "GET",
            data: {
                day: selectedDay,
                month: selectedMonth,
                year: selectedYear,
                master: selectedMaster
            },
            dataType: "json",
            success: function(response) {
            $('#appointments-list').empty();
            if (response.length > 0) {
                response.forEach(function(appointment) {
                    let row = '<tr>';
                    row += '<td class="text-white">' + appointment.service + '</td>';
                    row += '<td class="text-white">' + appointment.user + '</td>';
                    row += '<td class="text-white">' + appointment.date + '</td>';
                    row += '<td class="text-white">' + appointment.time + '</td>';
                    row += '</tr>';
                    $('#appointments-list').append(row);
                });
            } else {
                $('#appointments-list').append('<tr><td colspan="4" class="text-white">Нет заявок</td></tr>');
            }
        },
            error: function(xhr, errmsg, err) {
                console.log(errmsg);
            }
         });
    });
});