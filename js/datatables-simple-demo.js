window.addEventListener('DOMContentLoaded', event => {
    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple, {
            labels: {
                placeholder: "Buscar...",
                perPage: " resultados por página",
                noRows: "Nenhum resultado encontrado",
                info: "Mostrando {start} a {end} de {rows} resultados"
            }
        });
    }
});

window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple2 = document.getElementById('datatablesSimple2');
    if (datatablesSimple2) {
        new datatablesSimple2.DataTable(datatablesSimple2);
    }
});
