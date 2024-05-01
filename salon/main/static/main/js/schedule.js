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
        $.ajax({
            url: "/get_appointments/",
            type: "GET",
            data: {
                day: selectedDay,
                month: selectedMonth,
                year: selectedYear
            },
            dataType: "json",
            success: function(response) {
            $('#appointments-list').empty();
            if (response.length > 0) {
                response.forEach(function(appointment) {
                    // Создаем строку таблицы для каждой заявки
                    var row = '<tr>';
                    row += '<td class="text-white">' + appointment.service + '</td>'; // Добавляем ячейку для услуги
                    row += '<td class="text-white">' + appointment.user + '</td>'; // Добавляем ячейку для заказчика
                    row += '<td class="text-white">' + appointment.date + '</td>'; // Добавляем ячейку для даты
                    row += '<td class="text-white">' + appointment.time + '</td>'; // Добавляем ячейку для времени
                    row += '</tr>';
                    $('#appointments-list').append(row); // Добавляем строку в таблицу
                });
            } else {
                // Если нет заявок, добавляем сообщение об этом
                $('#appointments-list').append('<tr><td colspan="4" class="text-white">Нет заявок</td></tr>');
            }
        },
            error: function(xhr, errmsg, err) {
                console.log(errmsg);
            }
         });
    });
});