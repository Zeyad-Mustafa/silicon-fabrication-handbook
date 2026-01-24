import React, { useEffect, useRef, useState } from 'react';
import * as THREE from 'three';
import { Thermometer, Zap, Play, Pause, RotateCcw, Settings } from 'lucide-react';

const ThermalActuatorSim3D = () => {
  const containerRef = useRef(null);
  const sceneRef = useRef(null);
  const rendererRef = useRef(null);
  const cameraRef = useRef(null);
  const actuatorRef = useRef(null);
  const frameRef = useRef(null);
  
  const [isRunning, setIsRunning] = useState(false);
  const [temperature, setTemperature] = useState(25);
  const [power, setPower] = useState(0);
  const [displacement, setDisplacement] = useState(0);
  const [showHeatMap, setShowHeatMap] = useState(true);
  
  const timeRef = useRef(0);
  const targetTempRef = useRef(25);

  useEffect(() => {
    if (!containerRef.current) return;

    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x0a0a14);
    sceneRef.current = scene;

    const camera = new THREE.PerspectiveCamera(
      50,
      containerRef.current.clientWidth / containerRef.current.clientHeight,
      0.1,
      1000
    );
    camera.position.set(120, 80, 120);
    camera.lookAt(0, 0, 0);
    cameraRef.current = camera;

    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(containerRef.current.clientWidth, containerRef.current.clientHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.shadowMap.enabled = true;
    containerRef.current.appendChild(renderer.domElement);
    rendererRef.current = renderer;

    // Lighting
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.4);
    scene.add(ambientLight);

    const mainLight = new THREE.DirectionalLight(0xffffff, 0.8);
    mainLight.position.set(100, 150, 100);
    mainLight.castShadow = true;
    scene.add(mainLight);

    const fillLight = new THREE.PointLight(0x4a9eff, 0.5);
    fillLight.position.set(-80, 50, -80);
    scene.add(fillLight);

    // Create thermal actuator structure
    const actuatorGroup = new THREE.Group();

    // Base/Anchor
    const baseGeom = new THREE.BoxGeometry(60, 8, 60);
    const baseMat = new THREE.MeshPhysicalMaterial({
      color: 0x2c3e50,
      metalness: 0.7,
      roughness: 0.3
    });
    const base = new THREE.Mesh(baseGeom, baseMat);
    base.position.y = -4;
    base.castShadow = true;
    actuatorGroup.add(base);

    // Heating element (bimorph beam)
    const beamGeom = new THREE.BoxGeometry(80, 4, 20);
    const beamMat = new THREE.MeshPhysicalMaterial({
      color: 0xff6b35,
      metalness: 0.5,
      roughness: 0.4,
      emissive: 0xff3300,
      emissiveIntensity: 0
    });
    const beam = new THREE.Mesh(beamGeom, beamMat);
    beam.position.set(0, 6, 0);
    beam.castShadow = true;
    actuatorGroup.add(beam);

    // Top layer (different thermal expansion)
    const topLayerGeom = new THREE.BoxGeometry(80, 1, 20);
    const topLayerMat = new THREE.MeshPhysicalMaterial({
      color: 0x3498db,
      metalness: 0.6,
      roughness: 0.3,
      transparent: true,
      opacity: 0.9
    });
    const topLayer = new THREE.Mesh(topLayerGeom, topLayerMat);
    topLayer.position.set(0, 8.5, 0);
    actuatorGroup.add(topLayer);

    // Electrodes
    for (let i = 0; i < 2; i++) {
      const electrodeGeom = new THREE.BoxGeometry(8, 3, 8);
      const electrodeMat = new THREE.MeshStandardMaterial({
        color: 0xffd700,
        metalness: 0.9,
        roughness: 0.1
      });
      const electrode = new THREE.Mesh(electrodeGeom, electrodeMat);
      electrode.position.set(i === 0 ? -36 : 36, 2, -15);
      actuatorGroup.add(electrode);
    }

    // Temperature indicator particles
    const particlesGeom = new THREE.BufferGeometry();
    const particleCount = 100;
    const positions = new Float32Array(particleCount * 3);
    
    for (let i = 0; i < particleCount; i++) {
      positions[i * 3] = (Math.random() - 0.5) * 80;
      positions[i * 3 + 1] = 6 + (Math.random() - 0.5) * 6;
      positions[i * 3 + 2] = (Math.random() - 0.5) * 20;
    }
    
    particlesGeom.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    const particlesMat = new THREE.PointsMaterial({
      color: 0xff6600,
      size: 0.8,
      transparent: true,
      opacity: 0
    });
    const particles = new THREE.Points(particlesGeom, particlesMat);
    actuatorGroup.add(particles);

    scene.add(actuatorGroup);
    actuatorRef.current = { group: actuatorGroup, beam, topLayer, particles, beamMat, particlesMat };

    // Grid
    const gridHelper = new THREE.GridHelper(200, 20, 0x444466, 0x222233);
    gridHelper.position.y = -10;
    scene.add(gridHelper);

    // Mouse controls
    let isDragging = false;
    let prevMouse = { x: 0, y: 0 };
    let rotation = { x: 0.2, y: 0.3 };

    const onMouseDown = (e) => {
      isDragging = true;
      prevMouse = { x: e.clientX, y: e.clientY };
    };

    const onMouseMove = (e) => {
      if (!isDragging) return;
      const dx = e.clientX - prevMouse.x;
      const dy = e.clientY - prevMouse.y;
      rotation.y += dx * 0.005;
      rotation.x += dy * 0.005;
      rotation.x = Math.max(-Math.PI / 2, Math.min(Math.PI / 2, rotation.x));
      prevMouse = { x: e.clientX, y: e.clientY };
    };

    const onMouseUp = () => {
      isDragging = false;
    };

    const onWheel = (e) => {
      e.preventDefault();
      const factor = e.deltaY > 0 ? 1.1 : 0.9;
      camera.position.multiplyScalar(factor);
    };

    renderer.domElement.addEventListener('mousedown', onMouseDown);
    renderer.domElement.addEventListener('mousemove', onMouseMove);
    renderer.domElement.addEventListener('mouseup', onMouseUp);
    renderer.domElement.addEventListener('wheel', onWheel);

    // Animation
    const animate = () => {
      frameRef.current = requestAnimationFrame(animate);

      if (isRunning) {
        timeRef.current += 0.016;
        
        // Temperature dynamics
        const heatRate = power * 50;
        const coolingRate = (temperature - 25) * 0.5;
        const newTemp = temperature + (heatRate - coolingRate) * 0.016;
        setTemperature(Math.max(25, Math.min(300, newTemp)));
        
        // Thermal expansion (bimorph bending)
        const tempDiff = temperature - 25;
        const bendAngle = tempDiff * 0.001; // radians
        const tipDisp = 40 * Math.sin(bendAngle); // approximate
        setDisplacement(tipDisp);
        
        if (actuatorRef.current) {
          const { beam, topLayer, particles, beamMat, particlesMat } = actuatorRef.current;
          
          // Bend the beam
          beam.rotation.z = bendAngle;
          beam.position.y = 6 + tipDisp * 0.1;
          topLayer.rotation.z = bendAngle * 0.95;
          topLayer.position.y = 8.5 + tipDisp * 0.1;
          
          // Heat glow
          const intensity = Math.min((temperature - 25) / 275, 1);
          beamMat.emissiveIntensity = intensity * 0.6;
          beamMat.color.setHex(intensity > 0.5 ? 0xff3300 : 0xff6b35);
          
          // Heat particles
          if (showHeatMap) {
            particlesMat.opacity = intensity * 0.7;
            const positions = particles.geometry.attributes.position.array;
            for (let i = 0; i < positions.length; i += 3) {
              positions[i + 1] += Math.sin(timeRef.current * 2 + i) * 0.1;
            }
            particles.geometry.attributes.position.needsUpdate = true;
          } else {
            particlesMat.opacity = 0;
          }
        }
      }

      if (actuatorRef.current && !isDragging) {
        actuatorRef.current.group.rotation.x = rotation.x;
        actuatorRef.current.group.rotation.y = rotation.y;
      }

      renderer.render(scene, camera);
    };
    animate();

    const handleResize = () => {
      if (!containerRef.current) return;
      camera.aspect = containerRef.current.clientWidth / containerRef.current.clientHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(containerRef.current.clientWidth, containerRef.current.clientHeight);
    };
    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
      renderer.domElement.removeEventListener('mousedown', onMouseDown);
      renderer.domElement.removeEventListener('mousemove', onMouseMove);
      renderer.domElement.removeEventListener('mouseup', onMouseUp);
      renderer.domElement.removeEventListener('wheel', onWheel);
      if (frameRef.current) cancelAnimationFrame(frameRef.current);
      renderer.dispose();
      if (containerRef.current && renderer.domElement) {
        containerRef.current.removeChild(renderer.domElement);
      }
    };
  }, [isRunning, temperature, power, showHeatMap]);

  const toggleSimulation = () => {
    setIsRunning(!isRunning);
  };

  const resetSimulation = () => {
    setIsRunning(false);
    setTemperature(25);
    setPower(0);
    setDisplacement(0);
    timeRef.current = 0;
  };

  return (
    <div className="w-full h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 flex flex-col">
      <div className="bg-slate-800/70 backdrop-blur-sm border-b border-slate-700 px-6 py-4">
        <h1 className="text-2xl font-bold text-white mb-1 flex items-center gap-2">
          <Thermometer className="text-orange-400" size={28} />
          3D Thermal Actuator Simulator
        </h1>
        <p className="text-sm text-slate-300">Bimorph beam with differential thermal expansion</p>
      </div>

      <div className="flex-1 relative" ref={containerRef} />

      <div className="absolute top-24 right-6 bg-slate-800/95 backdrop-blur-md rounded-lg shadow-2xl p-5 space-y-4 border border-slate-700 w-80">
        <div className="flex items-center justify-between mb-3">
          <h3 className="text-lg font-semibold text-white flex items-center gap-2">
            <Settings size={20} className="text-blue-400" />
            Controls
          </h3>
          <button
            onClick={resetSimulation}
            className="p-2 bg-slate-700 hover:bg-slate-600 rounded-lg transition-colors"
            title="Reset"
          >
            <RotateCcw size={18} className="text-white" />
          </button>
        </div>

        <div className="space-y-3">
          <button
            onClick={toggleSimulation}
            className={`w-full flex items-center justify-center gap-2 px-4 py-3 rounded-lg font-medium transition-all ${
              isRunning
                ? 'bg-red-500 hover:bg-red-600 text-white'
                : 'bg-green-500 hover:bg-green-600 text-white'
            }`}
          >
            {isRunning ? <Pause size={20} /> : <Play size={20} />}
            {isRunning ? 'Pause' : 'Start'} Simulation
          </button>

          <div>
            <label className="text-sm font-medium text-slate-300 flex items-center gap-2 mb-2">
              <Zap size={16} className="text-yellow-400" />
              Heating Power: {power.toFixed(1)} W
            </label>
            <input
              type="range"
              min="0"
              max="10"
              step="0.1"
              value={power}
              onChange={(e) => setPower(parseFloat(e.target.value))}
              className="w-full h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-orange-500"
            />
          </div>

          <div className="flex items-center justify-between">
            <span className="text-sm font-medium text-slate-300">Heat Particles</span>
            <button
              onClick={() => setShowHeatMap(!showHeatMap)}
              className={`w-12 h-6 rounded-full transition-colors ${
                showHeatMap ? 'bg-orange-500' : 'bg-slate-600'
              }`}
            >
              <div className={`w-5 h-5 bg-white rounded-full shadow-md transform transition-transform ${
                showHeatMap ? 'translate-x-6' : 'translate-x-1'
              }`} />
            </button>
          </div>
        </div>
      </div>

      <div className="absolute bottom-6 left-6 bg-slate-800/95 backdrop-blur-md rounded-lg shadow-2xl p-5 border border-slate-700">
        <h3 className="text-sm font-semibold text-white mb-3 flex items-center gap-2">
          <Thermometer size={18} className="text-orange-400" />
          Live Measurements
        </h3>
        <div className="space-y-2 text-sm">
          <div className="flex justify-between gap-8">
            <span className="text-slate-400">Temperature:</span>
            <span className="font-mono text-orange-400 font-semibold">{temperature.toFixed(1)} °C</span>
          </div>
          <div className="flex justify-between gap-8">
            <span className="text-slate-400">Displacement:</span>
            <span className="font-mono text-blue-400 font-semibold">{displacement.toFixed(2)} µm</span>
          </div>
          <div className="flex justify-between gap-8">
            <span className="text-slate-400">Bend Angle:</span>
            <span className="font-mono text-purple-400 font-semibold">
              {((temperature - 25) * 0.001 * 180 / Math.PI).toFixed(2)}°
            </span>
          </div>
          <div className="flex justify-between gap-8">
            <span className="text-slate-400">Power:</span>
            <span className="font-mono text-yellow-400 font-semibold">{power.toFixed(1)} W</span>
          </div>
        </div>
      </div>

      <div className="absolute bottom-6 right-6 bg-slate-800/95 backdrop-blur-md rounded-lg shadow-2xl p-4 border border-slate-700 text-xs text-slate-400 max-w-xs">
        <p className="font-semibold text-white mb-1">💡 How it works:</p>
        <p>Two materials with different thermal expansion coefficients are bonded together. When heated, differential expansion causes the beam to bend, creating linear motion from thermal energy.</p>
      </div>
    </div>
  );
};

export default ThermalActuatorSim3D;