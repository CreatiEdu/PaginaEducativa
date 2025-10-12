// Usuarios y contraseñas válidos
const usuarios = {
  'admin': '1234',
  'docente': 'ciem2025',
  'alumno': 'estudiante'
};

// Obtener el formulario
const formLogin = document.getElementById('formLogin');

// Cuando se envía el formulario
formLogin.addEventListener('submit', function(e) {
  e.preventDefault();
  
  // Obtener los valores ingresados
  const usuario = document.getElementById('usuario').value;
  const password = document.getElementById('password').value;
  
  // Verificar si el usuario existe
  if (usuarios[usuario]) {
    // Verificar si la contraseña es correcta
    if (usuarios[usuario] === password) {
      // Login correcto - guardar sesión y redirigir
      sessionStorage.setItem('logueado', 'true');
      alert('Login exitoso! Redirigiendo...');
      window.location.href = 'index.html';
    } else {
      // Contraseña incorrecta
      alert('Contraseña incorrecta');
      document.getElementById('password').value = '';
    }
  } else {
    // Usuario no existe
    alert('Usuario no encontrado');
    document.getElementById('password').value = '';
  }
});