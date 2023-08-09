const daysTag = document.querySelector(".days"),
    currentDate = document.querySelector(".current-date"),
    prevNextIcon = document.querySelectorAll(".icons span"),
    eventDescription = document.querySelector(".event-description");

let date = new Date(2023,7 )// 7 corresponds to August
    currYear = date.getFullYear(),
    currMonth = date.getMonth();

const events = {
    18: ["Responder examen de inglés y cuestionario de datos estadísticos", "Descargar e imprimir documentación"],
    19: ["Ceremonia de bienvenida (apellidos A-I)"],
    20: ["Ceremonia de bienvenida (apellidos M-Z)"],
    21: ["Proceso de inscripción en línea", "Curso Igualdad de Género en la UNAM"],
    22: ["Proceso de inscripción en línea", "Curso Igualdad de Género en la UNAM"],
    23: ["Proceso de inscripción presencial", "Curso Igualdad de Género en la UNAM"],
    24: ["Proceso de inscripción presencial", "Curso Igualdad de Género en la UNAM", "Responde el Examen Diagnóstico de Ingreso (EDI)"],
    25: ["Proceso de inscripción presencial", "Curso Igualdad de Género en la UNAM"],
    26: ["Responde el Examen Diagnóstico de Ingreso (EDI)"],
    28: ["Inicio de clases", "Activa tu correo institucional", "Minicurso Herramientas TIC", "Ticómetro"],
    29: ["Activa tu correo institucional", "Minicurso Herramientas TIC", "Ticómetro"],
    30: ["Activa tu correo institucional", "Minicurso Herramientas TIC", "Ticómetro"],
    31: ["Activa tu correo institucional", "Minicurso Herramientas TIC", "Ticómetro"],
};

const renderCalendar = () => {
    let firstDayofMonth = (new Date(currYear, currMonth, 1).getDay() - 1 + 7) % 7, 
        lastDateofMonth = new Date(currYear, currMonth + 1, 0).getDate(),
        lastDayofMonth = new Date(currYear, currMonth, lastDateofMonth).getDay(),
        lastDateofLastMonth = new Date(currYear, currMonth, 0).getDate();
    let liTag = "";

    for (let i = firstDayofMonth; i > 0; i--) {
        liTag += `<li class="inactive">${lastDateofLastMonth - i + 1}</li>`;
    }

    for (let i = 1; i <= lastDateofMonth; i++) {
        let today = new Date();
        let isToday = i === today.getDate() ? "active" : "";
        let isEvent = events[i] ? "event" : "";
        liTag += `<li class="${isToday} ${isEvent}" data-day="${i}">${i}</li>`;
    }

    for (let i = lastDayofMonth; i < 6; i++) {
        liTag += `<li class="inactive">${i - lastDayofMonth + 1}</li>`
    }
    currentDate.innerText = `Agosto ${currYear}`;
    daysTag.innerHTML = liTag;
    addEventListeners();
}

const addEventListeners = () => {
    const eventDays = document.querySelectorAll('.days .event');
    eventDays.forEach(day => {
        day.addEventListener('click', (e) => {
            const day = e.target.dataset.day;
            const eventList = events[day].join('<br>');
            eventDescription.innerHTML = `<strong>Eventos para el ${day} de Agosto:</strong><br>${eventList}`;
            eventDescription.style.display = 'block';

        });
    });
}

renderCalendar();