import React from 'react';
import { X, Info } from 'lucide-react';

const MethodologyModal = ({ isOpen, onClose }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm">
      <div className="bg-[#fdf5e6] border-4 border-red-600 rounded-xl shadow-2xl w-full max-w-2xl max-h-[90vh] overflow-y-auto">
        <div className="sticky top-0 bg-white border-b-4 border-red-200 p-4 flex justify-between items-center z-10 shadow-sm">
          <div className="flex items-center gap-3">
            <Info className="text-red-600" size={24} />
            <h2 className="text-2xl font-extrabold text-red-800 font-serif">The Secret Recipe (Methodology)</h2>
          </div>
          <button 
            onClick={onClose}
            className="text-red-700 hover:text-red-900 transition-colors p-1 bg-red-100 hover:bg-red-200 rounded-lg border-2 border-transparent hover:border-red-300 font-bold"
          >
            <X size={20} />
          </button>
        </div>
        
        <div className="p-6 space-y-6 text-gray-800 text-sm leading-relaxed font-medium">
          <section>
            <h3 className="text-xl font-extrabold text-red-800 mb-2 flex items-center gap-2 font-serif italic">
              <span className="text-xl">🍕</span> Pizza Party Index (PPI)
            </h3>
            <div className="bg-white p-4 rounded-lg border-2 border-green-600 shadow-sm">
              <p className="mb-2 text-gray-800">
                The <strong>Pizza Party Index</strong> quantifies the prevalence of "performative perks" versus actual productive time. It acts as an inverse indicator of productivity—a higher PPI suggests an environment bloated with performative activities.
              </p>
              <h4 className="font-extrabold text-green-800 mt-3 mb-1 uppercase tracking-wide text-xs">Calculation:</h4>
              <ul className="list-disc list-inside space-y-1 ml-2 text-gray-700 font-medium">
                <li>Derived from self-reported survey data (e.g., SWAA) regarding the number of mandatory, non-working meetings (like "pizza parties") an employee attends per week.</li>
                <li>Weighted by industry standards and company size.</li>
                <li>Normalized to a scale of 0 to 100, where 100 indicates peak performative culture.</li>
              </ul>
            </div>
          </section>

          <section>
            <h3 className="text-xl font-extrabold text-red-800 mb-2 flex items-center gap-2 font-serif italic">
              <span className="text-xl">⚡</span> Velocity Proxy
            </h3>
            <div className="bg-white p-4 rounded-lg border-2 border-green-600 shadow-sm">
              <p className="mb-2 text-gray-800">
                The <strong>Velocity Proxy</strong> is our primary measure of real-world development speed and efficiency across different work setups (remote, hybrid, in-office).
              </p>
              <h4 className="font-extrabold text-green-800 mt-3 mb-1 uppercase tracking-wide text-xs">Calculation:</h4>
              <ul className="list-disc list-inside space-y-1 ml-2 text-gray-700 font-medium">
                <li>Pulled directly from repository telemetry (e.g., GitHub REST API).</li>
                <li>Calculates the median time from PR creation to merge (PR Merge Time).</li>
                <li>Measures the average Issue Resolution Time.</li>
                <li>Aggregated and averaged to form a composite score that indicates how quickly value is delivered.</li>
              </ul>
            </div>
          </section>

          <section>
            <h3 className="text-xl font-extrabold text-red-800 mb-2 font-serif italic">Data Ingredients</h3>
            <p className="mb-2 text-gray-800">
              Our models fuse subjective survey data with objective repository telemetry to provide a balanced view of modern software development environments.
            </p>
            <ul className="list-disc list-inside space-y-1 ml-2 text-gray-700 font-medium bg-red-50 p-4 rounded-lg border-2 border-red-200">
              <li><strong>Survey of Working Arrangements and Attitudes (SWAA):</strong> Provides foundational data on work setups and meeting loads.</li>
              <li><strong>GitHub REST API:</strong> Supplies real-time, objective data on PR merge times and issue resolution rates.</li>
            </ul>
          </section>
        </div>
      </div>
    </div>
  );
};

export default MethodologyModal;
