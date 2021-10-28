/* Codigo para el mapa */
let coord = [];
let animales = ["Otro","Perro", "Gato", "Pez", "Tortuga", "Hámster", "Loro", "Iguana", "Araña"];
let icon = ["","clipboard-check.svg","clipboard-x.svg","question.svg"];
let icon_v = ["","suit-heart-fill.svg","suit-heart.svg","question.svg"];

function num_mascota(num){
    if(num <= 8){
        return animales[num];}
    else{
        return animales[0];}
}
function icon_ester(num){
    return icon[num];
}

function icon_vac(num){
    return icon_v[num];
}

function init_mapa(){
    console.log('iniciando la app');
    loadMapa();
    setInterval(function(){loadMapa()},1200000);
}

function loadMapa(){
    console.log('Cargando datos para el mapeo')
    let xhr = new XMLHttpRequest();
    xhr.open('POST','read_mapa.py');
    xhr.timeout = 2000;
    xhr.onload = function (data) {
        let datatext = data.currentTarget.responseText;
        let info = JSON.parse(datatext);
        crearMapa(info);
    }
    xhr.timeout = function (){
        showMensaje('Ta malo');
    }
    xhr.onerror = function(){
        showMensaje('ta re malo');
    }
    xhr.send();
}

function crearMapa(dicc) {
    let keys = Object.keys(dicc);
    let map = L.map('contenedor_mapa').setView([-33, -70], 5);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    for(let i = 0; i < keys.length; i++){
        let coord = [];
        let contenedor_html = `
        <table class="tabla_mapa">
        `;
        comuna = dicc[keys[i]];
        total_comuma = comuna.length.toString();
        for(j = 0; j < comuna.length; j++){
            contenedor_html = contenedor_html + `
            <tr class="info" onclick=redirrection_tab("info_mascota.py?id=${comuna[j][1][7]}")>
                <td><img src=${comuna[j][0]} width="120" height="120"></td>
                <td>Tipo: ${num_mascota(comuna[j][1][1])},<br>Edad: ${comuna[j][1][2]} año(s),<br>Color: ${comuna[j][1][3]},<br>Raza: ${comuna[j][1][4]},<br>Ester: <img src="icons/${icon_ester(comuna[j][1][5])}">,<br>Vacunas: <img src="icons/${icon_vac(comuna[j][1][6])}"></td>
            `;}
        obtener(function (datos){
            let dato = JSON.parse(datos);
            coord = [dato[keys[i]]["lng"],dato[keys[i]]["lat"]];
            let marcador = L.marker([coord[1], coord[0]],{
                title: total_comuma
            }).addTo(map);
            marcador.bindPopup(contenedor_html).openPopup();
        });
        contenedor_html = contenedor_html + `
        </table>
        `         
    }
}

let obtener = function(callback){
    let xhr = new XMLHttpRequest();
    xhr.overrideMimeType("application/json");
    xhr.open("POST","coordenadas.json",true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == "200"){
            callback(xhr.responseText);
        }
    }
    xhr.send();
}