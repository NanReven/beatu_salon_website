let master_days = [];

//  master_days and datepicker
document.addEventListener('DOMContentLoaded', function () {
    let master = document.getElementById("id_master");

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

                 $('.input-group.date').datepicker('destroy');
                let new_options = {
                    format: "dd/mm/yyyy",
                    todayBtn: "linked",
                    language: "ru",
                    daysOfWeekDisabled: master_days,
                };
                $('.input-group.date').datepicker(new_options);
            },
            error: function (xhr, errmsg, err) {
                console.log(errmsg);
            }
        });
    }
    master.addEventListener('change', getDaysOff);
});

// main calendar
document.addEventListener('DOMContentLoaded', function () {
    let dateInput = document.querySelector('#id_datetime');
    let today = new Date();
    let mm = String(today.getMonth() + 1).padStart(2, '0');
    let yyyy = today.getFullYear();

    let nextMonthDate = new Date();
    nextMonthDate.setMonth(nextMonthDate.getMonth() + 1);
    let nextMonthLastDate = new Date(nextMonthDate.getFullYear(), nextMonthDate.getMonth() + 1, 0);

    let maxDate = nextMonthLastDate.getFullYear() + '-' + String(nextMonthLastDate.getMonth() + 1).padStart(2, '0') + '-' + String(today.getDate()).padStart(2, '0');
    let todayFormatted = yyyy + '-' + mm + '-' + String(today.getDate()).padStart(2, '0');

    dateInput.setAttribute('min', todayFormatted);
    dateInput.setAttribute('max', maxDate);
    dateInput.addEventListener('change', function () {
        let day = dateInput.valueAsDate.getDay();
        master_days.forEach(function (master_day_off) {
            if (day === master_day_off) {
                dateInput.value = '';
            }
        });

        let selectedDate = new Date(this.value);
        let currentDate = new Date(todayFormatted);
        if (selectedDate < currentDate) {
            this.value = todayFormatted;
        }
    });
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
        document.querySelector('#id_datetime').value = '';
        getServices();
    }

    selectedMaster.addEventListener('change', Handle);
});

document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('appointmentForm');
    const masterField = form.elements['master'];
    const serviceField = form.elements['service'];
    const datetimeField = form.elements['datetime'];
    const commentField = form.elements['comment'];
    const submitButton = form.elements['submit'];

    // Initially disable all fields except the first one
    serviceField.disabled = true;
    datetimeField.disabled = true;
    commentField.disabled = true;
    submitButton.disabled = true;

    // Enable the next field when the current one is filled
    masterField.addEventListener('change', function() {
        if (masterField.value !== '') {
            serviceField.disabled = false;
        } else {
            serviceField.disabled = true;
            serviceField.value = '';
            datetimeField.disabled = true;
            datetimeField.value = '';
            commentField.disabled = true;
            commentField.value = '';
            submitButton.disabled = true;
        }
    });

    serviceField.addEventListener('change', function() {
        if (serviceField.value !== '') {
            datetimeField.disabled = false;
        } else {
            datetimeField.disabled = true;
            datetimeField.value = '';
            commentField.disabled = true;
            commentField.value = '';
            submitButton.disabled = true;
        }
    });

    datetimeField.addEventListener('input', function() {
        if (datetimeField.value !== '') {
            commentField.disabled = false;
            submitButton.disabled = false; // Enable submit button as datetime is filled
        } else {
            commentField.disabled = true;
            commentField.value = '';
            submitButton.disabled = true;
        }
    });

    commentField.addEventListener('input', function() {
        // Comment field is optional, no need to check its value to enable submit button
    });
});

