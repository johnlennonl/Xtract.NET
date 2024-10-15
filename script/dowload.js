 // Inicializa el contador de descargas
 let downloadCount = 213;

 // Actualiza el contador al cargar la página
 const downloadCounter = document.getElementById('downloadCounter');
 const downloadButton = document.getElementById('downloadButton');

 function updateDownloadCount() {
     downloadCount++;
     downloadCounter.textContent = `Descargas realizadas: ${downloadCount}`;
 }

 // Agrega el evento de click al botón para la descarga y actualización del contador
 downloadButton.addEventListener('click', function() {
     window.location.href = 'https://www.mediafire.com/file/wqta39o24tbbv9h/extractor_gui.zip/file';
     updateDownloadCount();
 });