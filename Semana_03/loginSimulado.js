const usuariosLDAP = [
    {usuario: 'doctor', clave: 'abcd'},
];

function autenticarLDAP(usuario, clave) {

    return usuariosLDAP.find(
        u => u.usuario === usuario && u.clave === clave
    );
}

const usuario = 'doctor';
const clave = '1234';

if (autenticarLDAP(usuario, clave)) {
    console.log('Login exitoso');
} else {
    console.log('Login fallido');
}