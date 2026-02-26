import React, { useState, useEffect, useRef } from 'react';
import { Shield, ShieldAlert, Zap, Activity, Server, Smartphone, Cpu, CheckCircle, Info } from 'lucide-react';

const App = () => {
  // Estado del sistema
  const [isAttacking, setIsAttacking] = useState(false);
  const [mitigationActive, setMitigationActive] = useState(false);
  const [load, setLoad] = useState(0);
  const [requestsPerSecond, setRequestsPerSecond] = useState(100);
  const [responseTime, setResponseTime] = useState(20);
  const [uptime, setUptime] = useState(100);
  const [logs, setLogs] = useState([]);

  const logEndRef = useRef(null);

  // Auto-scroll para logs
  useEffect(() => {
    logEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [logs]);

  // Lógica de simulación
  useEffect(() => {
    const interval = setInterval(() => {
      let targetLoad = 5;
      let targetRPS = 100;
      let targetResponse = 20;

      if (isAttacking) {
        if (mitigationActive) {
          targetLoad = 45; // El sistema aguanta bajo mitigación
          targetRPS = 12000;
          targetResponse = 85;
          if (Math.random() < 0.05) addLog("Alerta: Tráfico malicioso filtrado por WAF/Rate Limit", "warning");
        } else {
          targetLoad = 100; // Colapso total
          targetRPS = 50000;
          targetResponse = 5000;
          if (Math.random() < 0.1) addLog("Error: Servidor DNS no responde. Timeout excedido.", "error");
        }
      } else {
        if (Math.random() < 0.1) addLog("INFO: Procesando consulta DNS estándar.", "info");
      }

      // Suavizado de transiciones
      setLoad(prev => prev + (targetLoad - prev) * 0.2);
      setRequestsPerSecond(prev => prev + (targetRPS - prev) * 0.2);
      setResponseTime(prev => prev + (targetResponse - prev) * 0.2);
      
      // Cálculo de Uptime basado en carga
      if (load > 95 && !mitigationActive) {
        setUptime(prev => Math.max(0, prev - 0.5));
      } else {
        setUptime(prev => Math.min(100, prev + 0.2));
      }
    }, 500);

    return () => clearInterval(interval);
  }, [isAttacking, mitigationActive, load]);

  const addLog = (message, type) => {
    const timestamp = new Date().toLocaleTimeString();
    setLogs(prev => [...prev.slice(-15), { message, type, timestamp }]);
  };

  const toggleAttack = () => {
    const nextState = !isAttacking;
    setIsAttacking(nextState);
    addLog(nextState ? "¡ALERTA! Inicio de inundación masiva detectado" : "ATAQUE FINALIZADO", nextState ? "error" : "success");
  };

  const toggleMitigation = () => {
    const nextState = !mitigationActive;
    setMitigationActive(nextState);
    addLog(nextState ? "Activando Rate Limiting y Anycast..." : "Sistemas de protección desactivados", nextState ? "success" : "warning");
  };

  const getStatusColor = () => {
    if (load > 90) return "text-red-500";
    if (load > 60) return "text-amber-500";
    return "text-green-500";
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-200 p-4 md:p-8 font-mono">
      {/* Header */}
      <div className="max-w-6xl mx-auto flex flex-col md:flex-row justify-between items-center mb-8 border-b border-slate-800 pb-4">
        <div>
          <h1 className="text-2xl font-bold text-white flex items-center gap-2">
            <Activity className="text-blue-500" /> SIMULADOR DDoS: INFRAESTRUCTURA DNS
          </h1>
          <p className="text-slate-500 text-sm mt-1">Análisis de impacto y mitigación de botnets (Estilo Mirai)</p>
        </div>
        <div className="flex gap-4 mt-4 md:mt-0">
          <button 
            onClick={toggleAttack}
            className={`px-6 py-2 rounded-md font-bold transition-all flex items-center gap-2 ${
              isAttacking ? "bg-red-600 hover:bg-red-700 text-white" : "bg-slate-800 hover:bg-slate-700 text-red-500"
            }`}
          >
            <Zap size={18} />
            {isAttacking ? "DETENER ATAQUE" : "INICIAR ATAQUE"}
          </button>
          <button 
            onClick={toggleMitigation}
            className={`px-6 py-2 rounded-md font-bold transition-all flex items-center gap-2 ${
              mitigationActive ? "bg-green-600 hover:bg-green-700 text-white" : "bg-slate-800 hover:bg-slate-700 text-green-500"
            }`}
          >
            <Shield size={18} />
            {mitigationActive ? "MITIGACIÓN ACTIVA" : "ACTIVAR MITIGACIÓN"}
          </button>
        </div>
      </div>

      <div className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-3 gap-8">
        
        {/* Panel de Métricas */}
        <div className="lg:col-span-1 space-y-4">
          <div className="bg-slate-900 border border-slate-800 p-6 rounded-xl shadow-lg">
            <h2 className="text-xs uppercase tracking-widest text-slate-500 mb-4 font-bold">Estado del Servidor</h2>
            
            <div className="space-y-6">
              <div>
                <div className="flex justify-between mb-2">
                  <span className="text-sm">Carga de CPU/Red</span>
                  <span className={`text-sm font-bold ${getStatusColor()}`}>{Math.round(load)}%</span>
                </div>
                <div className="w-full bg-slate-800 h-3 rounded-full overflow-hidden">
                  <div 
                    className={`h-full transition-all duration-500 ${load > 80 ? 'bg-red-500' : load > 50 ? 'bg-amber-500' : 'bg-green-500'}`}
                    style={{ width: `${load}%` }}
                  ></div>
                </div>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div className="bg-slate-800/50 p-4 rounded-lg">
                  <span className="text-[10px] text-slate-500 block uppercase">Peticiones / seg</span>
                  <span className="text-xl font-bold">{Math.round(requestsPerSecond).toLocaleString()}</span>
                </div>
                <div className="bg-slate-800/50 p-4 rounded-lg">
                  <span className="text-[10px] text-slate-500 block uppercase">Latencia (ms)</span>
                  <span className={`text-xl font-bold ${responseTime > 500 ? 'text-red-400' : 'text-slate-200'}`}>
                    {Math.round(responseTime)}
                  </span>
                </div>
              </div>

              <div className="flex items-center justify-between pt-4 border-t border-slate-800">
                <span className="text-sm text-slate-400">Disponibilidad (Uptime)</span>
                <span className={`text-lg font-bold ${uptime < 90 ? 'text-red-500' : 'text-green-500'}`}>
                  {uptime.toFixed(2)}%
                </span>
              </div>
            </div>
          </div>

          <div className="bg-blue-900/10 border border-blue-900/30 p-4 rounded-xl">
            <h3 className="text-blue-400 text-sm font-bold flex items-center gap-2 mb-2">
              <Info size={16} /> Nota Técnica
            </h3>
            <p className="text-xs text-blue-200/70 leading-relaxed">
              En un ataque real, la botnet utiliza dispositivos IoT comprometidos para inundar la red. 
              La mitigación mediante <strong>Anycast</strong> distribuye la carga entre múltiples nodos, 
              mientras que el <strong>Rate Limiting</strong> descarta el exceso de paquetes maliciosos.
            </p>
          </div>
        </div>

        {/* Visualización de Red */}
        <div className="lg:col-span-2 space-y-4">
          <div className="bg-slate-900 border border-slate-800 p-6 rounded-xl shadow-lg h-[400px] relative overflow-hidden">
            <h2 className="text-xs uppercase tracking-widest text-slate-500 mb-8 font-bold">Topología del Ataque</h2>
            
            <div className="flex justify-between items-center h-48 mt-12 px-8 relative">
              {/* Botnet */}
              <div className="flex flex-col gap-6 z-10">
                {[1, 2, 3].map(i => (
                  <div key={i} className={`flex items-center gap-3 ${isAttacking ? 'text-red-500' : 'text-slate-600'}`}>
                    <div className="p-2 bg-slate-800 rounded-lg relative">
                      {i === 1 ? <Smartphone size={20} /> : i === 2 ? <Cpu size={20} /> : <Server size={20} />}
                      {isAttacking && (
                        <div className="absolute -top-1 -right-1 w-2 h-2 bg-red-500 rounded-full animate-ping"></div>
                      )}
                    </div>
                    <span className="text-[10px] hidden md:block">Dispositivo IoT #{i}</span>
                  </div>
                ))}
              </div>

              {/* Animación de Paquetes */}
              {isAttacking && (
                <div className="absolute inset-x-20 top-1/2 -translate-y-1/2 h-20 pointer-events-none w-full">
                  {[...Array(10)].map((_, i) => (
                    <div 
                      key={i}
                      className="absolute h-1 bg-red-500 rounded-full"
                      style={{
                        width: '8px',
                        left: '0px',
                        top: `${10 + Math.random() * 80}%`,
                        opacity: 0,
                        animation: `dash ${0.4 + Math.random() * 0.4}s linear infinite`,
                        animationDelay: `${Math.random()}s`
                      }}
                    ></div>
                  ))}
                </div>
              )}

              {/* Servidor DNS */}
              <div className="flex flex-col items-center gap-4 z-10">
                <div className={`p-6 rounded-2xl border-2 transition-all duration-500 ${
                  load > 90 ? 'bg-red-900/20 border-red-500 shadow-[0_0_20px_rgba(239,68,68,0.3)]' : 
                  mitigationActive ? 'bg-blue-900/20 border-blue-500 shadow-[0_0_20px_rgba(59,130,246,0.3)]' :
                  'bg-slate-800 border-slate-700'
                }`}>
                  <Server size={48} className={load > 90 ? 'text-red-500 animate-pulse' : 'text-slate-300'} />
                </div>
                <div className="text-center">
                  <span className="text-xs font-bold block">Servidor DNS de Dyn</span>
                  <span className={`text-[10px] px-2 py-0.5 rounded ${
                    load > 95 ? 'bg-red-500/20 text-red-400' : 'bg-green-500/20 text-green-400'
                  }`}>
                    {load > 95 ? "SOBRECARGADO" : "OPERATIVO"}
                  </span>
                </div>
              </div>
            </div>

            {/* Estilo para animación de paquetes */}
            <style>
              {`
                @keyframes dash {
                  0% { left: 0%; opacity: 0; }
                  20% { opacity: 1; }
                  80% { opacity: 1; }
                  100% { left: 75%; opacity: 0; }
                }
              `}
            </style>

            {/* Consola de Logs */}
            <div className="mt-8 bg-black rounded-lg border border-slate-800 p-4 font-mono text-[10px] h-32 overflow-y-auto">
              {logs.map((log, i) => (
                <div key={i} className="mb-1 flex gap-2">
                  <span className="text-slate-600">[{log.timestamp}]</span>
                  <span className={
                    log.type === 'error' ? 'text-red-500' : 
                    log.type === 'warning' ? 'text-amber-500' : 
                    log.type === 'success' ? 'text-green-500' : 
                    'text-blue-400'
                  }>
                    {log.message}
                  </span>
                </div>
              ))}
              <div ref={logEndRef} />
            </div>
          </div>
        </div>
      </div>
      
      {/* Footer Info */}
      <div className="max-w-6xl mx-auto mt-8 grid grid-cols-1 md:grid-cols-2 gap-8 text-slate-400 text-xs italic">
        <p>{"*"} El ataque de 2016 demostró que el volumen de tráfico puede saturar incluso a los proveedores más grandes.</p>
        <p className="text-right">Simulación diseñada para fines de examen final de Ciberseguridad.</p>
      </div>
    </div>
  );
};

export default App;