import React, { useState } from 'react';
import { Pizza, Download, Info } from 'lucide-react';
import rawData from '../../data/pizza_metrics.json';
import MethodologyModal from './MethodologyModal';

const Header = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const exportData = () => {
    const payload = {
      metadata: {
        random_seed: 42,
        source: "Pizza Party Metrics Dashboard",
        exported_at: new Date().toISOString()
      },
      dataset: rawData
    };
    
    const blob = new Blob([JSON.stringify(payload, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'pizza_metrics_export.json';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  };

  return (
    <header className="bg-gray-900 border-b border-gray-800 p-6 flex items-center justify-between shadow-md">
      <div className="flex items-center gap-4">
        <div className="bg-gradient-to-br from-red-500 to-orange-600 p-3 rounded-full text-white shadow-[0_0_15px_rgba(239,68,68,0.5)]">
          <Pizza size={32} />
        </div>
        <div>
          <h1 className="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-red-400 to-orange-500 tracking-tight">
            Pizza Party Metrics
          </h1>
          <p className="text-gray-400 font-medium mt-1">
            Replacing Performative Perks with Real Productivity Telemetry
          </p>
        </div>
      </div>
      <div className="flex items-center gap-3">
        <button
          onClick={() => setIsModalOpen(true)}
          className="flex items-center gap-2 bg-gray-800 hover:bg-gray-700 text-blue-400 hover:text-blue-300 px-4 py-2 rounded-lg border border-gray-700 transition-colors text-sm font-medium"
        >
          <Info size={16} />
          <span>Methodology</span>
        </button>
        <button
          onClick={exportData}
          className="flex items-center gap-2 bg-gray-800 hover:bg-gray-700 text-gray-200 hover:text-white px-4 py-2 rounded-lg border border-gray-700 transition-colors text-sm font-medium"
        >
          <Download size={16} />
          <span>Download Raw Data</span>
        </button>
        <div className="hidden md:flex items-center gap-2 bg-gray-800 px-4 py-2 rounded-full border border-gray-700">
          <span className="flex h-3 w-3 relative">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
            <span className="relative inline-flex rounded-full h-3 w-3 bg-green-500"></span>
          </span>
          <span className="text-sm font-bold text-green-400">Live Telemetry</span>
        </div>
      </div>
      <MethodologyModal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} />
    </header>
  );
};

export default Header;

