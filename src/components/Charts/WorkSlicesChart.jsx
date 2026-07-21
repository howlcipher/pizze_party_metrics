import React from 'react';
import { 
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer 
} from 'recharts';

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

const WorkSlicesChart = ({ data }) => {
  // Aggregate data by work_setup to compare
  const aggregatedData = data.reduce((acc, curr) => {
    // using work_setup_category now instead of work_setup object
    const existing = acc.find(item => item.work_setup === curr.work_setup_category);
    if (existing) {
      existing.focus_hours += curr.focus_hours;
      existing.meeting_overhead += curr.meeting_overhead;
      existing.count += 1;
    } else {
      acc.push({
        work_setup: curr.work_setup_category,
        focus_hours: curr.focus_hours,
        meeting_overhead: curr.meeting_overhead,
        count: 1
      });
    }
    return acc;
  }, []);

  const chartData = aggregatedData.map(item => ({
    name: item.work_setup,
    "Focus Hours": Number((item.focus_hours / item.count).toFixed(1)),
    "Meeting Overhead": Number((item.meeting_overhead / item.count).toFixed(1))
  }));

  return (
    <div className="bg-white/95 border border-gray-200 rounded p-5 shadow-sm h-full flex flex-col">
      <h3 className="text-xl font-bold text-[#3E2723] mb-2 border-b border-gray-200 pb-2">
        Slices of Work: Focus vs Meetings
      </h3>
      <p className="text-sm text-gray-600 font-bold mb-4">
        Weekly Focus Hours vs. Meeting Overhead across different mandates.
      </p>
      
      <div className="flex-grow min-h-[300px]" role="img" aria-label="Bar chart comparing Focus Hours versus Meeting Overhead by work setup category.">
        <div style={srOnlyStyle}>
          This bar chart displays the breakdown of weekly focus hours versus meeting overhead in hours across different work setup categories, such as In-Office, Hybrid, and Remote.
        </div>
        <ResponsiveContainer width="100%" height="100%">
          <BarChart
            data={chartData}
            margin={{ top: 20, right: 30, left: 0, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" stroke="#e5e7eb" vertical={false} />
            <XAxis 
              dataKey="name" 
              tick={{ fill: '#4b5563', fontWeight: 700 }} 
              axisLine={{ stroke: '#d1d5db' }}
              tickLine={false}
            />
            <YAxis 
              tick={{ fill: '#4b5563', fontWeight: 600 }}
              axisLine={{ stroke: '#d1d5db' }}
              tickLine={false}
              label={{ value: 'Hours', angle: -90, position: 'insideLeft', fill: '#4b5563', fontWeight: 'bold' }}
            />
            <Tooltip 
              cursor={{ fill: '#fcd34d', opacity: 0.3 }}
              contentStyle={{ 
                backgroundColor: '#fff', 
                border: '2px solid #22c55e',
                borderRadius: '8px',
                color: '#333',
                fontWeight: 'bold'
              }}
            />
            <Legend wrapperStyle={{ paddingTop: '10px', fontWeight: 'bold', color: '#333' }} />
            <Bar dataKey="Focus Hours" fill="#22c55e" radius={[4, 4, 0, 0]} maxBarSize={60} />
            <Bar dataKey="Meeting Overhead" fill="#ef4444" radius={[4, 4, 0, 0]} maxBarSize={60} />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default WorkSlicesChart;

