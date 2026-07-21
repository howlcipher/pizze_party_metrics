import React, { useState, useEffect, useMemo } from 'react';
import Header from './Header';
import PizzaBoxFilter from '../Filters/PizzaBoxFilter';
import PizzaGauge from '../Charts/PizzaGauge';
import WorkSlicesChart from '../Charts/WorkSlicesChart';
import DemographicsChart from '../Charts/DemographicsChart';

const Dashboard = () => {
  const [rawData, setRawData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filters, setFilters] = useState({
    industry: '',
    age_group: '',
    work_setup: '' // this will filter by work_setup_category
  });

  const filteredData = useMemo(() => {
    return rawData.filter(item => {
      return (
        (!filters.industry || item.industry === filters.industry) &&
        (!filters.age_group || item.age_group === filters.age_group) &&
        (!filters.work_setup || item.work_setup_category === filters.work_setup)
      );
    });
  }, [filters, rawData]);

  useEffect(() => {
    fetch('/api/metrics')
      .then(res => res.json())
      .then(data => {
        setRawData(data.metrics || []);
        setLoading(false);
      })
      .catch(err => {
        console.error("Failed to fetch metrics", err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-950 flex flex-col items-center justify-center text-gray-100 font-sans">
        <div className="animate-spin rounded-full h-16 w-16 border-t-4 border-b-4 border-red-500 mb-4"></div>
        <p className="text-xl font-bold text-gray-300">Fetching Live Telemetry...</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-950 text-gray-100 font-sans">
      <Header rawData={rawData} />
      
      <main className="max-w-7xl mx-auto p-6 space-y-6">
        {/* Filters Section */}
        <section>
          <PizzaBoxFilter filters={filters} setFilters={setFilters} data={rawData} />
        </section>

        {/* Charts Section */}
        <section className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Gauge takes 1 column on large screens */}
          <div className="lg:col-span-1">
            <PizzaGauge data={filteredData} />
          </div>
          
          {/* Bar Chart takes 2 columns on large screens */}
          <div className="lg:col-span-2">
            <WorkSlicesChart data={filteredData} />
          </div>

          {/* Demographics Chart takes full width (3 cols) */}
          <div className="lg:col-span-3">
            <DemographicsChart data={filteredData} />
          </div>
        </section>

        {filteredData.length === 0 && (
          <div className="bg-red-900/30 border-2 border-red-500/50 p-6 rounded-xl text-center shadow-sm">
            <p className="text-red-400 font-bold text-lg mb-4">No slices left! Try adjusting your filters.</p>
            <button 
              onClick={() => setFilters({ industry: '', age_group: '', work_setup: '' })}
              className="px-6 py-2 bg-red-600 hover:bg-red-500 text-white rounded-lg font-bold transition-colors cursor-pointer"
            >
              Reset Filters
            </button>
          </div>
        )}
      </main>
      
      <footer className="text-center py-6 text-gray-500 text-sm font-semibold mt-auto space-y-2">
        <p>Telemetry generated with 🧀 & 🍅</p>
        <p className="text-xs font-normal">
          <strong>Live Data Sources:</strong> <a href="https://wfhresearch.com/" target="_blank" rel="noopener noreferrer" className="underline hover:text-red-400">WFH Research (SWAA)</a> &amp; <a href="https://docs.github.com/en/rest" target="_blank" rel="noopener noreferrer" className="underline hover:text-red-400">GitHub REST API</a>
        </p>
      </footer>
    </div>
  );
};

export default Dashboard;

