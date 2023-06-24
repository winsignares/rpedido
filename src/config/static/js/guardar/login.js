function Guar_Clientes() {
  const tipoPersona = document.getElementById('tipoPersona');
  const nombre = document.getElementById('nombre');
  const correo = document.getElementById('correo');
  const contraseña = document.getElementById('contraseña');
  const nomusario = document.getElementById('nomusario');
  const direc = document.getElementById('direc');
  const telefono = document.getElementById('telefono');


  axios.post('/fronted/Guardar_Clientes', {
    tipoPersona: tipoPersona.value,
    NombreC: nombre.value,
    Email: correo.value,
    password: contraseña.value,
    usuario: nomusario.value,
    telefono: telefono.value,
    direccion: tipoPersona.value === 'PersonaNormal' ? direc.value : ''
  }, {
    headers: {
      'Content-Type': 'multipart/form-data'

    }
  }
  ).then((res) => {
    console.log(res.data)
    alert("si")
    document.getElementById('tipoPersona').value = "Selecciona"
    document.getElementById('nombre').value = ""
    document.getElementById('correo').value = ""
    document.getElementById('contraseña').value = ""
    document.getElementById('nomusario').value = ""
    document.getElementById('direc').value = ""
    document.getElementById('telefono').value = ""
  })
    .catch((error) => {
      console.error(error)
      alert(error)
    })
}

function ingreso() {
  const tipoPersona = document.getElementById('tipoPersonalogin');
  const email = document.getElementById('email').value;
  const password = document.getElementById('pass').value;

  axios.post('/fronted/validar_login', {
    tipoPersona: tipoPersona.value,
    email: email,
    password: password
  })
    .then((response) => {
      const resultado = response.data;
      if (resultado.message === 'Correcto cliente') {
        window.location.href = '/fronted/cliente';
      } else if (resultado.message === 'Correcto repartidor') {
        window.location.href = '/fronted/repartidor';
      } else {
        alert('Inicio de sesión incorrecto');
      }
    })
    .catch((error) => {
      console.error(error);
      alert('Ocurrió un error en la solicitud');
    });
}





function tipo() {
  // Obtenemos el valor del tipo de persona
  const tipoPersona = document.getElementById("tipoPersona").value;

  // Seleccionamos el elemento que queremos mostrar/ocultar
  const direccion = document.getElementById("direc");

  // Mostramos u ocultamos el elemento según el tipo de persona
  if (tipoPersona === 'Selecciona') {
    direccion.style.display = 'none';
  } else if (tipoPersona === 'PersonaNormal') {
    direccion.style.display = 'block';
  }else if (tipoPersona === 'Repartidor') {
    direccion.style.display = 'none';
  } 
}

function mostrar() {
  const divcate = document.getElementById('tablaM');
  axios.get('/fronted/mostrar_pedido', {
    responseType: 'json'
  })

    .then(function (response) {
      let datos = response.data
      var length = (Object.keys(datos).length) + 1;
      let mostrar = '';
      i = 0
      for (let index = 1; index < length; index++) {
        mostrar += ` <tr>   
                  <td >${datos[index].Id}</td>  
                  <td >${datos[index].N_de_pedido}</td>  
                  <td >${datos[index].Nombre_del_Cliente}</td>  
                  <td>${datos[index].Productos}</td>
                  <td>${datos[index].Cantidad}</td>
                  <td>${datos[index].Local}</td>  
                  <td><a onclick="eliminarP(${datos[index].Id}) "class="btn btn-primary btn-edit">Entregado</a></td>
                </tr> `;
      }
      divcate.innerHTML = mostrar
    })
    .catch(function (error) {
      // Maneja los errores aquí
      console.log(error);
    });
}
window.addEventListener('load', function () {
  mostrar();
})

function eliminarP(Id) {
  axios.post('/fronted/eliminarss', {
    id: Id
  })
    .then(function (response) {
      mostrar();
      console.log(response);
      if (response.data.message === 'Eliminado correctamente') {
        console.log('Eliminado(a) con éxito!');
      } else if (response.data.message === 'No se puede eliminar') {
        console.log('No se puede eliminar');
      } else {
        console.log('Error al eliminar');
      }
    })
    .catch(function (error) {
      console.log(error);
    });
}
function cerrarV() {
  // Obtén una referencia a la ventana emergente actual
  const contener_todo = document.getElementById('contener__todo');

  // Cierra la ventana emergente
  if (contener_todo == contener_todo) {
    window.location.href = '/fronted/index';
  }
}

