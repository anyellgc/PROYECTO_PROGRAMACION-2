const modal = document.getElementById("modalFormulario");
    const modalEntrega = document.getElementById("modalEntrega");
    const form = document.getElementById("formAsignacion");
    const formEntrega = document.getElementById("formEntrega");

    let tipoGlobal = null;
    let editando = false;

    function abrirModal(tipo, id = null, titulo = "", descripcion = "", fecha = "", curso = "") {
        tipoGlobal = tipo;
        editando = !!id;

        document.getElementById("modalTitulo").textContent = (editando ? "Editar " : "Nueva ") + (tipo === "tarea" ? "Tarea" : "Proyecto");
        document.getElementById("asignacionId").value = id || "";
        document.getElementById("titulo").value = titulo;
        document.getElementById("descripcion").value = descripcion;
        document.getElementById("fecha_entrega").value = fecha;
        document.getElementById("curso").value = curso;
        modal.style.display = "flex";
    }

    function abrirModalEntrega(id, tipo) {
        tipoGlobal = tipo;
        document.getElementById("entregaId").value = id;
        document.getElementById("enlaceEntrega").value = "";
        document.getElementById("observacionesEntrega").value = "";
        modalEntrega.style.display = "flex";
    }

    form.addEventListener("submit", function(e) {
        e.preventDefault();
        const data = {
            id: document.getElementById("asignacionId").value,
            tipo: tipoGlobal,
            titulo: document.getElementById("titulo").value,
            descripcion: document.getElementById("descripcion").value,
            fecha_entrega: document.getElementById("fecha_entrega").value,
            curso: document.getElementById("curso").value,
            editando: editando
        };

        fetch("{% url 'guardar_asignacion' %}", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": "{{ csrf_token }}"
            },
            body: JSON.stringify(data)
        })
        .then(r => r.json())
        .then(result => {
            alert(result.success ? "Guardado correctamente." : "Error: " + result.message);
            if (result.success) window.location.reload();
        });
    });

    formEntrega.addEventListener("submit", function(e) {
        e.preventDefault();
        const data = {
            id: document.getElementById("entregaId").value,
            tipo: tipoGlobal,
            enlace: document.getElementById("enlaceEntrega").value,
            observaciones: document.getElementById("observacionesEntrega").value
        };

        fetch("{% url 'guardar_entrega' %}", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": "{{ csrf_token }}"
            },
            body: JSON.stringify(data)
        })
        .then(r => r.json())
        .then(result => {
            alert(result.success ? "Entrega guardada correctamente." : "Error: " + result.message);
            if (result.success) window.location.reload();
        });
    });

    function eliminarAsignacion(id, tipo) {
        if (confirm("¿Estás seguro de eliminar esta " + tipo + "?")) {
            fetch("/eliminar-asignacion/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": "{{ csrf_token }}"
                },
                body: JSON.stringify({ id: id, tipo: tipo })
            })
            .then(r => r.json())
            .then(result => {
                alert(result.success ? "Eliminado correctamente." : "Error: " + result.message);
                if (result.success) window.location.reload();
            });
        }
    }

    window.onclick = function(event) {
        if (event.target === modal) modal.style.display = "none";
        if (event.target === modalEntrega) modalEntrega.style.display = "none";
    };