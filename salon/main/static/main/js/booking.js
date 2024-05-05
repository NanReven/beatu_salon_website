document.addEventListener('DOMContentLoaded', function () {
    let dateInput = document.querySelector('#id_date'); // Замените 'id_date' на реальный id поля даты
    let today = new Date();
    let mm = String(today.getMonth() + 1).padStart(2, '0'); // текущий месяц
    let yyyy = today.getFullYear();

    // Вычисляем последний день следующего месяца
    let nextMonthDate = new Date();
    nextMonthDate.setMonth(nextMonthDate.getMonth() + 1);
    let nextMonthLastDate = new Date(nextMonthDate.getFullYear(), nextMonthDate.getMonth() + 1, 0);

    let maxDate = nextMonthLastDate.getFullYear() + '-' + String(nextMonthLastDate.getMonth() + 1).padStart(2, '0') + '-' + String(nextMonthLastDate.getDate()).padStart(2, '0');

    let todayFormatted = yyyy + '-' + mm + '-' + String(today.getDate()).padStart(2, '0');

    dateInput.setAttribute('min', todayFormatted);
    dateInput.setAttribute('max', maxDate);

    dateInput.addEventListener('change', function () {
        let selectedDate = new Date(this.value);
        let currentDate = new Date(todayFormatted);
        if (selectedDate < currentDate) {
            this.value = todayFormatted;
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    let timeInput = document.querySelector('#id_time'); // Замените 'id_time' на реальный id поля времени

    timeInput.addEventListener('change', function () {
        let selectedTime = this.value.split(':'); // Разбиваем строку времени на часы и минуты
        let selectedHour = parseInt(selectedTime[0]); // Получаем выбранный час
        let selectedMinute = parseInt(selectedTime[1]); // Получаем выбранные минуты
        let minHour = 10; // Минимальный час
        let maxHour = 20; // Максимальный час

        // Если выбранный час находится в пределах допустимого диапазона
        if (selectedHour >= minHour && selectedHour <= maxHour) {
            // Округляем выбранные минуты до ближайшего значению: 0, 15, 30 или 45
            let roundedMinute = Math.round(selectedMinute / 15) * 15;
            // Если округленное значение минут больше 45, устанавливаем 0 минут и добавляем 1 час
            if (roundedMinute > 45) {
                selectedHour += 1;
                selectedMinute = 0;
            } else {
                selectedMinute = roundedMinute;
            }
            // Форматируем время обратно в строку
            let formattedTime = ('0' + selectedHour).slice(-2) + ':' + ('0' + selectedMinute).slice(-2);
            // Устанавливаем новое значение времени в поле
            this.value = formattedTime;
        } else {
            // Если выбранное время находится за пределами допустимого диапазона, устанавливаем минимальное значение
            this.value = ('0' + minHour).slice(-2) + ':00';
        }
    });
});


document.addEventListener('DOMContentLoaded', function () {
    let selectedMaster = document.getElementById("id_master");
    let serviceSelect = document.querySelector('#id_service');
    console.log(selectedMaster);
    function getServices() {
        console.log("im here");
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
    };

    // Добавляем обработчики событий на изменение значений полей
    selectedMaster.addEventListener('change', getServices);
});