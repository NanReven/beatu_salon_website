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
    let dateInput = document.querySelector('#id_date');
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

// time picker
document.addEventListener('DOMContentLoaded', function () {
    let timeInput = document.querySelector('#id_time');

    timeInput.addEventListener('change', function () {
        let selectedTime = this.value.split(':');
        let selectedHour = parseInt(selectedTime[0]);
        let selectedMinute = parseInt(selectedTime[1]);
        let minHour = 10;
        let maxHour = 20;

        if (selectedHour >= minHour && selectedHour <= maxHour) {
            let roundedMinute = Math.round(selectedMinute / 15) * 15;
            if (roundedMinute > 45) {
                selectedHour += 1;
                selectedMinute = 0;
            } else {
                selectedMinute = roundedMinute;
            }
            this.value = ('0' + selectedHour).slice(-2) + ':' + ('0' + selectedMinute).slice(-2);
        } else {
            this.value = ('0' + minHour).slice(-2) + ':00';
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
        document.querySelector('#id_date').value = '';
        getServices();
    }

    selectedMaster.addEventListener('change', Handle);
});