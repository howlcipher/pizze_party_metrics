import React from 'react';
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip } from 'recharts';

const srOnlyStyle = {
  position: 'absolute',
  width: '1px',
  height: '1px',
  padding: 0,
  margin: '-1px',
  overflow: 'hidden',
  clip: 'rect(0, 0, 0, 0)',
  whiteSpace: 'nowrap',
  border: 0,
};

const PizzaGauge = ({ data }) => {
  // Calculate average index
  const avgIndex = data.length > 0 
    ? data.reduce((acc, curr) => acc + curr.pizza_party_index, 0) / data.length 
    : 0;
  
  // Assume max index is 40 for the gauge (based on typical 20-30 averages)
  const maxIndex = 40;
  const normalizedValue = Math.min(avgIndex, maxIndex);
  const remainingValue = maxIndex - normalizedValue;

  const gaugeData = [
    { name: 'Pizza Party Index', value: normalizedValue },
    { name: 'Remaining', value: remainingValue }
  ];

  const COLORS = ['#16a34a', '#f0e6d2']; // Green (good performance) and dough color

  // Determine environment optimization based on score
  let optimizationLabel = "⚖️ Hybrid-Balanced";
  let optimizationColor = "text-yellow-600";
  if (avgIndex >= 22) {
    optimizationLabel = "🏠 Remote-Optimized (High Focus)";
    optimizationColor = "text-green-600";
  } else if (avgIndex < 18 && avgIndex > 0) {
    optimizationLabel = "🏢 Office-Optimized (High Sync/Meetings)";
    optimizationColor = "text-red-600";
  }

  const renderCustomNeedle = () => {
    return (
      <div className="absolute inset-0 flex flex-col items-center justify-center pointer-events-none mt-20">
        <span className="text-5xl font-extrabold text-gray-800 drop-shadow-md">{avgIndex.toFixed(1)}</span>
        <span className="text-sm font-extrabold text-gray-500 uppercase mt-1">Avg Index</span>
        <span className={`text-xs font-bold mt-2 px-3 py-1 bg-white border border-gray-200 rounded-full shadow-sm ${optimizationColor}`}>
          {optimizationLabel}
        </span>
      </div>
    );
  };

  return (
    <div className="bg-white/95 border border-gray-200 rounded p-5 shadow-sm h-full flex flex-col relative">
      <h3 className="text-xl font-bold text-[#3E2723] mb-2 border-b border-gray-200 pb-2">
        The Pizza Party Index Gauge
      </h3>
      <p className="text-sm text-gray-600 mb-4 font-bold">
        Collaboration Speed + Focus Hours. Higher scores = Better suited for Remote work. Lower scores = Better suited for Onsite/Meetings.
      </p>
      
      <div className="flex-grow relative min-h-[200px]" role="img" aria-label={`Pizza Party Index Gauge. Current average index is ${avgIndex.toFixed(1)} out of 40.`}>
        <div style={srOnlyStyle}>
          This gauge displays the Pizza Party Index, reflecting collaboration speed and actual productivity. The current average index is {avgIndex.toFixed(1)} out of 40.
        </div>
        <ResponsiveContainer width="100%" height="100%">
          <PieChart>
            <Pie
              data={gaugeData}
              cx="50%"
              cy="80%" // Push down since it's a half circle
              startAngle={180}
              endAngle={0}
              innerRadius="60%"
              outerRadius="90%"
              dataKey="value"
              stroke="none"
              cornerRadius={5}
            >
              {gaugeData.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            <Tooltip 
              formatter={(value, name) => [value.toFixed(2), name]}
              contentStyle={{ backgroundColor: '#fff', borderRadius: '8px', border: '2px solid #e3342f', color: '#333', fontWeight: 'bold' }}
            />
          </PieChart>
        </ResponsiveContainer>
        {renderCustomNeedle()}
      </div>
    </div>
  );
};

export default PizzaGauge;

