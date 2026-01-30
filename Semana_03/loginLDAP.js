const ladp = requeri('ldapjs')
const client = new ladp.Client({
    url: 'ldap://localhost:389'
});

const dn = 'cn=admin,dc=example,dc=com';
const password = '1234';

client.bind(dn, password, (err) => {
    if (err) {
        console.error(' X  usuario o contraseña incorrectos');
    } else {
        console.log('Connected to LDAP');
    }
});