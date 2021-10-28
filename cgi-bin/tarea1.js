let comunasDeRegiones =  [
      ["Iquique", "Alto Hospicio", "Pozo Almonte", "Camiña", "Colchane", "Huara", "Pica"],
      ["Antofagasta", "Mejillones", "Sierra Gorda", "Taltal", "Calama", "Ollague", "San Pedro de Atacama", "Tocopilla", "María Elena"],
      ["Copiapó", "Caldera", "Tierra Amarilla", "Chañaral", "Diego de Almagro", "Vallenar", "Alto del Carmen", "Freirina", "Huasco"],
      ["La Serena", "Coquimbo", "Andacollo", "La Higuera", "Paiguano", "Vicuña", "Illapel", "Canela", "Los Vilos", "Salamanca", "Ovalle", "Combarbalá", "Monte Patria", "Punitaqui", "Río Hurtado"],
      ["Valparaíso", "Casablanca", "Concón", "Juan Fernández", "Puchuncaví", "Quintero", "Viña del Mar", "Isla de Pascua", "Los Andes", "Calle Larga", "Rinconada", "San Esteban", "La Ligua", "Cabildo", "Papudo", "Petorca", "Zapallar", "Quillota", "La Calera", "Hijuelas", "La Cruz", "Nogales", "San Antonio", "Algarrobo", "Cartagena", "El Quisco", "El Tabo", "Santo Domingo", "San Felipe", "Catemu", "Llay llay", "Panquehue", "Putaendo", "Santa María", "Quilpué", "Limache", "Olmué", "Villa Alemana","Pencahue"],
      ["Rancagua", "Codegua", "Coinco", "Coltauco", "Doñihue", "Graneros", "Las Cabras", "Machalí", "Malloa", "Mostazal", "Olivar", "Peumo", "Pichidegua", "Quinta de Tilcoco", "Rengo", "Requínoa", "San Vicente", "Pichilemu", "La Estrella", "Litueche", "Marchigue", "Navidad", "Paredones", "San Fernando", "Chépica", "Chimbarongo", "Lolol", "Nancagua", "Palmilla", "Peralillo", "Placilla", "Pumanque", "Santa Cruz","Chepica"],
      ["Talca", "Constitución", "Curepto", "Empedrado", "Maule", "Pelarco", "Río Claro", "San Clemente", "San Rafael", "Cauquenes", "Chanco", "Pelluhue", "Curicó", "Hualañé", "Licantén", "Molina", "Rauco", "Romeral", "Sagrada Familia", "Teno", "Vichuquén", "Linares", "Colbún", "Longaví", "Parral", "Retiro", "San Javier", "Villa Alegre", "Yerbas Buenas"],
      ["Alto Bio Bío","Antuco","Arauco","Cabrero","Cañete","Chiguayante","Concepción","Contulmo","Coronel","Curanilahue","Florida","Hualpén","Hualqui","Laja","Lebu","Los Álamos","Los Ángeles","Lota","Mulchén","Nacimiento","Negrete","Penco","Quilaco","Quilleco","San Pedro de la Paz","San Rosendo","Santa Bárbara","Santa Juana","Talcahuano","Tirúa","Tomé","Tucapel", "Yumbel"],
      ["Temuco", "Carahue", "Cunco", "Curarrehue", "Freire", "Galvarino", "Gorbea", "Lautaro", "Loncoche", "Melipeuco", "Nueva Imperial", "Padre Las Casas", "Perquenco", "Pitrufquén", "Pucón", "Saavedra", "Teodoro Schmidt", "Toltén", "Vilcún", "Villarrica", "Cholchol", "Angol", "Collipulli", "Curacautín", "Ercilla", "Lonquimay", "Los Sauces", "Lumaco", "Purén", "Renaico", "Traiguén", "Victoria"],
      ["Puerto Montt", "Calbuco", "Cochamó", "Fresia", "Frutillar", "Los Muermos", "Llanquihue", "Maullín", "Puerto Varas", "Castro", "Ancud", "Chonchi", "Curaco de Vélez", "Dalcahue", "Puqueldón", "Queilén", "Quellón", "Quemchi", "Quinchao", "Osorno", "Puerto Octay", "Purranque", "Puyehue", "Río Negro", "San Juan de la Costa", "San Pablo", "Chaitén", "Futaleufú", "Hualaihué", "Palena"],
      ["Coihaique", "Lago Verde", "Aysén", "Cisnes", "Guaitecas", "Cochrane", "O'Higins", "Tortel", "Chile Chico"],
      ["Punta Arenas", "Laguna Blanca", "Río Verde", "San Gregorio", "Antártica", "Porvenir", "Primavera", "Timaukel", "Puerto Natales", "Torres del Paine"],
      ["Cerrillos", "Cerro Navia", "Conchalí", "El Bosque", "Estación Central", "Huechuraba", "Independencia", "La Cisterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "Ñuñoa", "Pedro Aguirre Cerda", "Peñalolén", "Providencia", "Pudahuel", "Quilicura", "Quinta Normal", "Recoleta", "Renca", "San Joaquín", "San Miguel", "San Ramón", "Vitacura", "Puente Alto", "Pirque", "San José de Maipo", "Colina", "Lampa", "Tiltil", "San Bernardo", "Buin", "Calera de Tango", "Paine", "Melipilla", "Alhué", "Curacaví", "María Pinto", "San Pedro", "Talagante", "El Monte", "Isla de Maipo", "Padre Hurtado", "Peñaflor","Santiago"],
      ["Valdivia", "Corral", "Lanco", "Los Lagos", "Máfil", "Mariquina", "Paillaco", "Panguipulli", "La Unión", "Futrono", "Lago Ranco", "Río Bueno"],
      ["Arica", "Camarones", "Putre", "Gral. Lagos"],
      ["Cobquecura", "Coelemu", "Ninhue", "Portezuelo", "Quirihue", "Ránquil", "Treguaco", "Bulnes", "Chillán Viejo", "Chillán", "El Carmen", "Pemuco", "Pinto", "Quillón", "San Ignacio", "Yungay", "Coihueco", "Ñiquén", "San Carlos", "San Fabián", "San Nicolás"],
]
let contMascotas = 0;
let showCampo = false;
let fotos = [0];
let imag = ['formularios.png','mascotas.png','perrorygatos.png'];

function mostrarComunas() {
      let contenedor = document.getElementById('region');
      let opciones = document.getElementById('comuna');
      let comunas = comunasDeRegiones[contenedor.value-1];
      opciones.innerText='';
      for(let i=0;i<comunas.length;i++){
            let opcion = comunas[i];
            let elemento = document.createElement("option");
            elemento.textContent = opcion;
            elemento.value = opcion;
            opciones.appendChild(elemento);
      }
}

function newAnimal(){
      let mascota = 'tipo-mascota'+contMascotas
      let texto = 'texto9'+contMascotas
      let contenedor = document.getElementById(mascota);
      let contenedor_u = document.getElementById(texto);
      if (contenedor.value === "9") {
           contenedor_u.innerHTML = `
                <input type='text' id='tipo-mascota9${contMascotas}' name='tipo-mascota9${contMascotas}' placeholder='Ingrese el tipo de mascota'>
                `;
           showCampo = true;
      }
      else{
            contenedor_u.innerHTML = '';
      }
}

function validacionFormulario(){
      let region = document.getElementById('region').value;
      let comuna = document.getElementById('comuna').value;
      let calle = document.getElementById('calle').value;
      let numero = document.getElementById('numero').value;
      let sector = document.getElementById('sector').value;
      let nombre = document.getElementById('nombre').value;
      let correo = document.getElementById('correo').value;
      let celular = document.getElementById('celular').value;
      let regexCelular = /^(\+?56)?(\s?)(0?9)(\s?)[9876543]\d{7}$/
      let regexCorreo = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/
      if(region === ""){
            mensajeError()
            return false
      }
      if(comuna === ""){
            mensajeError()
            return false
      }
      if(calle === "" || calle.length > 250){
            mensajeError()
            return false

      }
      if(numero === "" || numero.length > 20){
            mensajeError()
            return false
      }
      if(sector.length > 100){
            mensajeError()
            return false
      }
      if(nombre === "" || nombre.length > 200){
            mensajeError()
            return false
      }
      if(correo === "" || !regexCorreo.test(correo)){
            mensajeError()
            return false
      }
      if(!regexCelular.test(celular) && celular !== ""){
            mensajeError()
            return false
      }
      for(let i=0;i<=contMascotas;i++){
            let tipo = document.getElementById('tipo-mascota'+i).value;
            let edad = document.getElementById('edad-mascota'+i).value;
            let color = document.getElementById('color-mascota'+i).value;
            let raza = document.getElementById('raza-mascota'+i).value;
            let ester = document.getElementById('esterilizado-mascota'+i).value;
            let vacunas = document.getElementById('vacunas-mascota'+i).value;
            if(tipo === ""){
                  mensajeError()
                  return false
            }
            if(tipo === "9"){
                  let tipo1 = document.getElementById('tipo-mascota9'+i).value;
                  if(tipo1==="" || tipo1.length>40){
                        mensajeError()
                        return false
                  }
            }
            if(edad==="" || edad<0){
                  mensajeError()
                  return false
            }
            if(color==="" || color.length>30){
                  mensajeError()
                  return false
            }
            if(raza==="" || raza.length>30){
                  mensajeError()
                  return false
            }
            if(ester==="" || vacunas===""){
                  mensajeError()
                  return false
            }
            for(let j=0;j<=fotos[i];j++){
                  let foto = document.getElementById('foto-mascota-'+i+j).value;
                  if(foto===""){
                        mensajeError()
                        return false
                  }
            }
      }
      return true
}

function addMascota(){
      fotos = fotos.concat(0);
      contMascotas += 1;
      let conetendor_n = document.getElementById('masMascotas')
      conetendor_n.innerHTML += `           
      <div class="leyenda_principal">Información de la mascota ${contMascotas+1}</div>
            <div class="entrada">
                <div class="leyenda">Tipo *</div>
                <select id="tipo-mascota${contMascotas}" required="required" name="tipo-mascota${contMascotas}" onclick="newAnimal()">
                    <option value="" selected="selected">Tipo de mascota</option>
                    <option value="1">Perro</option>
                    <option value="2">Gato</option>
                    <option value="3">Pez</option>
                    <option value="4">Tortuga</option>
                    <option value="5">Hámster</option>
                    <option value="6">Loro</option>
                    <option value="7">Iguana</option>
                    <option value="8">Araña</option>
                    <option value="9">Otro</option>
                </select>
                <div id="texto9${contMascotas}"></div>
            </div>

            <div class="entrada">
                <div class="leyenda">Edad en años *</div>
                    <input type="number" id="edad-mascota${contMascotas}" required="required" name="edad-mascota${contMascotas}" size="5">
            </div>

            <div class="entrada">
                <div class="leyenda">Color *</div>
                    <input type="text" id="color-mascota${contMascotas}" required="required" name="color-mascota${contMascotas}" size="30">
            </div>

            <div class="entrada">
                <div class="leyenda">Raza *</div>
                    <input type="text" id="raza-mascota${contMascotas}" required="required" name="raza-mascota${contMascotas}" size="30">
            </div>

            <div class="entrada">
                <div class="leyenda">Esterilizado *</div>
                    <select id="esterilizado-mascota${contMascotas}" required="required" name="esterilizado-mascota${contMascotas}">
                        <option value="" selected="selected">Ingrese alguna preferencia</option>
                        <option value="1">Si</option>
                        <option value="2">No</option>
                        <option value="3">No aplica</option>
                    </select>
            </div>

            <div class="entrada">
                <div class="leyenda">Vacunas al día *</div>
                    <select id="vacunas-mascota${contMascotas}" required="required" name="vacunas-mascota${contMascotas}">
                        <option value="" selected="selected">Ingrese alguna preferencia</option>
                        <option value="1">Si</option>
                        <option value="2">No</option>
                        <option value="3">No aplica</option>
                </select>
            </div>

            <div class="entrada">
                <div class="leyenda">Foto *</div>
                    <input type="file" id="foto-mascota-${contMascotas}0" required="required" name="foto-mascota-${contMascotas}0">
                    <div id="mas-foto-mascota${contMascotas}"></div>
                    <div class="entrada botones">
                    <button id="agregarArchivo" onclick="addFoto(${contMascotas})">Agregar imagen</button>
                    </div>
            </div>
      </div>`;
}

function addFoto(i){
      fotos[i] += 1;
      let contenedor = document.getElementById('mas-foto-mascota'+ i);
      if(fotos[i] < 5){
            contenedor.innerHTML += `
            <input type="file" required="required" id="foto-mascota-${i}${fotos[i]}" name="foto-mascota-${i}${fotos[i]}">
            <br>
            `;
      }

}

function showMensaje(){
      let alerta = document.getElementById('mensajeAlerta');
      alerta.innerHTML = `
      <div class="cuadroAlerta">
            <div class="leyenda centrar">¿Estás seguro de enviar el formulario, aceptando las condiciones de uso?</div>
            <button class="centrar" id='confirmar' type="submit" value="confirmar" >Si, estoy total y absolutamente seguro</button>
            <button class="centrar" id="denegar" type="button" onclick="retornarMensaje()">No estoy seguro, quiero volver a ver el formulario</button>
      </div>
      `;
}
function retornarMensaje(){
      let alerta = document.getElementById('mensajeAlerta');
      alerta.innerHTML = `
            <div class="entrada botones">
                <button id="enviar" type="button" onclick="showMensaje()">Enviar formulario</button>            
      `;
}

function redirrection(url){
      window.location = url;
}
function redirrection_tab(url){
      window.open(url,'_blank');
}
function mostrarImagenes(i){
      let imagen = document.getElementById('imagen');
      imagen.innerHTML = `
      <img alt="${imag[i]}" src="graficios/${imag[i]}">
      `;
}

function mensajeError(){
      let alerta = document.getElementById('mensajeAlerta');
      alerta.innerHTML = `
      <div class="cuadroAlerta">
            <div class="leyenda centrar">¿Estás seguro de enviar el formulario?</div>
            <div class="leyenda">Por favor, llenar todas las entradas con * y no ingresar datos erroneo</div>
            <button class="centrar" id='confirmar' type="submit" value="confirmar">Si, estoy total y absolutamente seguro</button>
            <button class="centrar" id="denegar" type="button" onclick="retornarMensaje()">No estoy seguro, quiero volver a ver el formulario</button>
      </div>
      `;
}
function showMessages(msg) {
      let contenedor = document.getElementById('contenedor_error');
      if (msg === '') {
          contenedor.style.display = 'none';
          return true;
      }
      contenedor.innerHTML = msg;
      contenedor.style.display = 'block';
      contenedor.style.fontWeight = '800';
      setTimeout(function () {
          contenedor.style.display = 'none';
      }, 3000); // Después de 5 segundos se oculta el error
  }