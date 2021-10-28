/*Codigo para los gráficos*/
function loadGraphics(){
    console.log('Cargando datos desde el servidor');
    let xhr = new XMLHttpRequest();
    xhr.open('POST','cgi-bin/read_graficos.py');
    xhr.timeout = 3000;
    xhr.onload = function (data) {
        let datatext = data.currentTarget.responseText;
        let info = JSON.parse(datatext);
        let llaves = Object.keys(info);
        generarTablas(info[llaves[0]],info[llaves[1]],info[llaves[2]]);
    }
    xhr.timeout = function(){
        showMessages('Se ha excedido del tiempo máximo de conexión');
    }
    xhr.onerror = function(){
        showMessages('Error al cargar los datos de la base de datos');
    }
    xhr.send();
}

function init_graficos(){
    console.log('comenzando a ejecutar la aplicación');
    loadGraphics();
    setInterval(function(){loadGraphics()},300000);
}

function generarTablas(datos1,datos2,datos3){
    let eje_x = [];
    let info_dia = [];
    for (let i = 0; i < datos1.length ; i++) {
        eje_x.push(datos1[i][0]);
        info_dia.push(
            {name: datos1[i][0],
            y: datos1[i][1]
        })
    }
        Highcharts.chart('contenedor_grafico1', {
            title: {
                text: 'Cantidad de domicilios censados'
            },
            subtitle: {
                text: 'Por día'
            },
            yAxis: {
                title: {
                    text: 'Número de domicilios censados'
                }
            },
            xAxis: {
                title: {
                    text: 'Fecha'
                },
                categories : eje_x,
                accessibility: {

                }
            },
            accessibility: {
                point: {
                    valueSuffix: 'Domicilios'
                }
            },
            series : [{
                name: "Domicilio(s) censado(s)",
                data: info_dia
            }]
        });
        Highcharts.chart('contenedor_grafico2',{
            chart: {
                type: 'pie'
            },
            title: {
                text: 'Cantidad de mascotas censadas'
            },
            subtitle: {
                text: 'Según su tipo'
            },
            series: [{
                name: 'Cantidad',
                data: [{
                    name: 'Perros',
                    y: datos2[0],
                }, {
                    name: 'Gatos',
                    y: datos2[1]
                }, {
                    name: 'Pez',
                    y: datos2[2]
                }, {
                    name: 'Tortuga',
                    y: datos2[3]
                }, {
                    name: 'Hámster',
                    y: datos2[4]
                }, {
                    name: 'Loro',
                    y: datos2[5]
                }, {
                    name: 'Iguana',
                    y: datos2[6]
                }, {
                    name: 'Araña',
                    y: datos2[7]
                }, {
                    name: 'Otros',
                    y: datos2[8]
                }]
            }]
        });
        let n_perros = [];
        let n_gatos = [];
        for(let i=0;i<datos3[0].length;i++){
            n_perros.push(datos3[1][i][0]);
            n_gatos.push(datos3[1][i][1]);
        }
        Highcharts.chart('contenedor_grafico3',{
            chart: {
                type:'column'
            },
            title: {
                text: 'Cantidad de perros y gatos censados'
            },
            subtitle: {
                text: 'Por mes'
            },
            xAxis: {
                text: 'Mes',
                categories: datos3[0],
                crosshair: true
            },
            yAxis: {
                min: 0,
                title :{
                    text: 'N° de mascotas de censados'
                }
            },
            series: [{
                name: 'Perros',
                data: n_perros
            }, {
                name: 'Gatos',
                data: n_gatos
            }]
        })
}