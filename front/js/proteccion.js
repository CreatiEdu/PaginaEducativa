// Verificar si el usuario ha iniciado sesión
if (!sessionStorage.getItem('logueado')) {
  // Si no está logueado, redirigir al login
  window.location.href = 'iniciarsesion.html';
}