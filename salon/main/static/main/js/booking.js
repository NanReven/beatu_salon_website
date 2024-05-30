//  master_days and datepicker
document.addEventListener('DOMContentLoaded', function () {
    let master = document.getElementById("id_master");
    let master_days = [];

    function getDaysOff() {
        $.ajax({
            url: "/get_master_weekends/",
            type: "GET",
            data: {
                master: master.value,
            },
            dataType: "json",
            success: function (response) {
                master_days = [];
                let weekdays = {'ПН': 1, 'ВТ': 2, 'СР': 3, 'ЧТ': 4, 'ПТ': 5, 'СБ': 6, 'ВС': 0};
                response.forEach(function (resp) {
                    master_days.push(weekdays[resp.day]);
                });

                $('.input-group.date').datepicker('setDaysOfWeekDisabled', master_days);
                $('#id_datetime').datetimepicker('setDaysOfWeekDisabled', master_days);
            },
            error: function (xhr, errmsg, err) {
                console.log(errmsg);
            }
        });
    }
    master.addEventListener('change', getDaysOff);
});

// master services
document.addEventListener('DOMContentLoaded', function () {
    let selectedMaster = document.getElementById("id_master");
    let serviceSelect = document.querySelector('#id_service');
    function getServices() {
        $.ajax({
            url: "/get_master_services/",
            type: "GET",
            data: {
                master: selectedMaster.value,
            },
            dataType: "json",
            success: function (response) {
                   $("#id_service").empty();
                   response.forEach(function(service) {
                      let option = document.createElement("option");
                      option.value = service.id;
                      option.textContent = service.title;
                      serviceSelect.appendChild(option);
                   });
            },
            error: function (xhr, errmsg, err) {
                console.log(errmsg);
            }
        });
    }

    function Handle() {
        $('.input-group.date').datepicker('update', '');
        $('#id_datetime').val("");
        $('#id_datetime').datetimepicker('update');
        $('#booking_info').text(`Стоимость: 0 руб. Длительность: 0 мин.`);
        getServices();
    }

    selectedMaster.addEventListener('change', Handle);
});

document.addEventListener('DOMContentLoaded', function () {
     $('.input-group.date').datepicker( {
         format: "dd/mm/yyyy",
         language: "ru",
     });
     let now = new Date();
     let oneMonthLater = new Date(now.getFullYear(), now.getMonth() + 1, now.getDate());
    $('#id_datetime').datetimepicker( {
        formatViewType: 'date',
        autoclose: true,
        minuteStep: 15,
        language: 'ru',
        weekStart: 1,
        startDate: now,
        endDate: oneMonthLater,
    });
    $('#id_datetime').datetimepicker('setHoursDisabled', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 21, 22, 23]);
});

$(document).ready(function() {
    $('#id_service').select2();
    $('#id_service').select2().on('change', function() {
        let services_id = $('#id_service').val();
        if (services_id.length === 0) {
             $('#booking_info').text(`Стоимость: 0 руб. Длительность: 0 мин.`);
        } else {
            $.ajax({
                url: "/get_service_details/",
                type: "GET",
                data: {
                    services: JSON.stringify(services_id),
                },
                dataType: "json",
                success: function (response) {
                   const minutes = response.minutes;
                   const cost = response.cost;
                   $('#booking_info').text(`Стоимость: ${cost} руб. Длительность: ${minutes} мин.`);
                },
                error: function (xhr, errmsg, err) {
                    console.log(errmsg);
                }
            });
        }
    });
});
