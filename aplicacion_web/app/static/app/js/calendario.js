document.addEventListener('DOMContentLoaded', function () {
            const calendarEl = document.getElementById('calendar');
            const modal = document.getElementById('modalEvento');
            const form = document.getElementById('formEvento');

            const calendar = new FullCalendar.Calendar(calendarEl, {
                initialView: 'dayGridMonth',
                headerToolbar: {
                    left: 'prev,next today',
                    center: 'title',
                    right: 'dayGridMonth,timeGridWeek,listWeek'
                },
                events: [],
                eventClick: function (info) {
                    alert("Evento: " + info.event.title);
                }
            });

            calendar.render();

            form.addEventListener('submit', function (e) {
                e.preventDefault();
                const nuevoEvento = {
                    title: document.getElementById('titulo').value,
                    start: document.getElementById('inicio').value,
                    end: document.getElementById('fin').value,
                    color: document.getElementById('color').value
                };

                calendar.addEvent(nuevoEvento);
                form.reset();
                cerrarModal();
            });
        });

        function abrirModal() {
            document.getElementById('modalEvento').style.display = 'block';
        }

        function cerrarModal() {
            document.getElementById('modalEvento').style.display = 'none';
        }