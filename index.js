const { exec } = require('child_process');

process.chdir('./flask-server');
exec('pip install -r requirements.txt', (error, stdout, stderr) => {
    if (error) {
        console.error(`Error al instalar dependencias de Python: ${error}`);
        return;
    }
    console.log(`Instalación de dependencias de Python: ${stdout}`);
});


// Instalar dependencias de Node.js
process.chdir('../frontend');
exec('npm install', (error, stdout, stderr) => {
    if (error) {
        console.error(`Error al ejecutar servidor de Node.js: ${error}`);
        return;
    }
    console.log(`Instalación de dependencias de Node.js: ${stdout}`);
});


