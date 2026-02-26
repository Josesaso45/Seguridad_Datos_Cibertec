import React, { useState } from 'react';
import { ShieldAlert, Mail, Lock, Info, Eye, EyeOff } from 'lucide-react';

const App = () => {
  const [email, setEmail] = useState('john.podesta@gmail.com');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [view, setView] = useState('email'); // 'email' o 'password'
  const [capturedData, setCapturedData] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleNext = (e) => {
    e.preventDefault();
    if (email) setView('password');
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // En un ataque real, estos datos se enviarían a un servidor controlado por el atacante
    const data = {
      user: email,
      pass: password,
      timestamp: new Date().toLocaleString(),
      target_url: "https://accounts.google.com/signin/v2/challenge/pwd",
      phish_url: "http://my-secure-update-google.bitly.net/login"
    };
    setCapturedData(data);
    setIsModalOpen(true);
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center justify-center p-4 font-sans">
      {/* Aviso Educativo */}
      <div className="max-w-md w-full mb-6 bg-amber-50 border-l-4 border-amber-500 p-4 rounded shadow-sm">
        <div className="flex items-center">
          <ShieldAlert className="text-amber-500 mr-2" size={20} />
          <h3 className="font-bold text-amber-800">Simulación Educativa</h3>
        </div>
        <p className="text-xs text-amber-700 mt-1">
          Esta es una réplica controlada para analizar cómo un atacante suplanta la identidad de un servicio legítimo.
        </p>
      </div>

      {/* Contenedor principal de la página de Phishing */}
      <div className="bg-white p-10 rounded-lg shadow-xl border border-gray-200 w-full max-w-[450px]">
        <div className="flex flex-col items-center">
          {/* Logo falso de Google */}
          <div className="flex mb-4 text-2xl font-bold">
            <span className="text-blue-500">G</span>
            <span className="text-red-500">o</span>
            <span className="text-yellow-500">o</span>
            <span className="text-blue-500">g</span>
            <span className="text-green-500">l</span>
            <span className="text-red-500">e</span>
          </div>
          
          <h1 className="text-2xl font-normal text-gray-800 mb-2">
            {view === 'email' ? 'Iniciar sesión' : 'Te damos la bienvenida'}
          </h1>
          <div className="text-gray-600 mb-8">
            {view === 'email' ? 'Ir a Gmail' : (
              <div className="flex items-center bg-gray-100 px-3 py-1 rounded-full border border-gray-200">
                <span className="text-sm font-medium mr-1 text-gray-700">{email}</span>
                <button onClick={() => setView('email')} className="text-blue-600 text-xs">▼</button>
              </div>
            )}
          </div>

          <form className="w-full" onSubmit={view === 'email' ? handleNext : handleSubmit}>
            {view === 'email' ? (
              <div className="mb-6">
                <input
                  type="email"
                  placeholder="Correo electrónico o teléfono"
                  className="w-full p-3 border border-gray-300 rounded focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-all"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
                <button type="button" className="text-blue-600 text-sm font-semibold mt-2 hover:underline text-left">
                  ¿Has olvidado tu correo electrónico?
                </button>
              </div>
            ) : (
              <div className="mb-6">
                <div className="relative">
                  <input
                    type={showPassword ? "text" : "password"}
                    placeholder="Introduce tu contraseña"
                    className="w-full p-3 border border-gray-300 rounded focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-all"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                    autoFocus
                  />
                  <button 
                    type="button"
                    onClick={() => setShowPassword(!showPassword)}
                    className="absolute right-3 top-3 text-gray-500"
                  >
                    {showPassword ? <EyeOff size={20} /> : <Eye size={20} />}
                  </button>
                </div>
                <button type="button" className="text-blue-600 text-sm font-semibold mt-2 hover:underline text-left">
                  ¿Has olvidado tu contraseña?
                </button>
              </div>
            )}

            <div className="flex justify-between items-center mt-8">
              <button type="button" className="text-blue-600 font-semibold hover:bg-blue-50 px-2 py-1 rounded transition-colors">
                {view === 'email' ? 'Crear cuenta' : ''}
              </button>
              <button 
                type="submit" 
                className="bg-blue-600 text-white px-6 py-2 rounded font-medium hover:bg-blue-700 transition-shadow shadow-sm"
              >
                Siguiente
              </button>
            </div>
          </form>
        </div>
      </div>

      <div className="mt-8 text-xs text-gray-500 flex gap-4">
        <span>Español (España)</span>
        <div className="flex gap-4">
          <a href="#" className="hover:underline">Ayuda</a>
          <a href="#" className="hover:underline">Privacidad</a>
          <a href="#" className="hover:underline">Términos</a>
        </div>
      </div>

      {/* Modal de Análisis de Datos Capturados */}
      {isModalOpen && (
        <div className="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center p-4 z-50">
          <div className="bg-slate-900 text-green-400 p-6 rounded-lg max-w-lg w-full font-mono text-sm border border-green-900 shadow-2xl">
            <div className="flex items-center justify-between border-b border-green-900 pb-2 mb-4">
              <span className="flex items-center gap-2"><Lock size={16}/> LOGS DEL ATACANTE (CAPTURA)</span>
              <button onClick={() => setIsModalOpen(false)} className="text-red-400 hover:text-red-300">Cerrar [X]</button>
            </div>
            <p className="mb-2">{" >> "} Conexión establecida desde IP: 185.12.XXX.XXX</p>
            <p className="mb-2">{" >> "} POST /harvest_credentials.php HTTP/1.1</p>
            <div className="bg-black p-4 rounded border border-green-800 overflow-x-auto">
              <pre>{JSON.stringify(capturedData, null, 2)}</pre>
            </div>
            <div className="mt-4 p-3 bg-red-900 bg-opacity-20 border border-red-900 text-red-300 rounded">
              <p className="font-bold flex items-center gap-2"><Info size={16}/> ¿Cómo detectar esto?</p>
              <ul className="list-disc ml-5 mt-1 text-xs">
                <li>Verifica la URL en la barra de direcciones.</li>
                <li>Habilita el Segundo Factor de Autenticación (2FA).</li>
                <li>Los servicios oficiales nunca te enviarán a dominios extraños para "validar" tu cuenta.</li>
              </ul>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default App;