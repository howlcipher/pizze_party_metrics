import { PizzaData } from "../../types";
import React, { useMemo } from 'react';
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

const CollaborationChart = ({ data }: { data: PizzaData[] }) => {
  // Aggregate data by work_setup_category using memoized single-pass accumulator
  const chartData = useMemo(() => {
    if (!data || data.length === 0) return [];

    const setupMap = {};
    for (let i = 0; i < data.length; i++) {
      const curr = data[i];
      const cat = curr.work_setup_category;
      if (!setupMap[cat]) {
        setupMap[cat] = { collaboration_score: 0, turnaround_hours: 0, count: 0 };
      }
      setupMap[cat].collaboration_score += (curr.collaboration_score || 0);
      setupMap[cat].turnaround_hours += (curr.review_turnaround_hours || 0);
      setupMap[cat].count += 1;
    }

    return Object.entries(setupMap).map(([cat, item]) => ({
      name: cat,
      "Collaboration Score": Number((item.collaboration_score / item.count).toFixed(1)),
      "Review Turnaround (Hrs)": Number((item.turnaround_hours / item.count).toFixed(1))
    }));
  }, [data]);

  return (
    <div className="bg-[var(--card-bg)] border-[var(--card-border)] rounded p-5 shadow-sm h-full flex flex-col">
      <h3 className="text-xl font-bold text-[var(--card-text)] mb-2 border-b border-gray-200 pb-2">
        Async Collaboration Velocity
      </h3>
      <p className="text-sm text-[var(--card-subtext)] font-bold mb-4">
        Collaboration efficiency vs. time blocked waiting.
      </p>
      
      <div className="flex-grow min-h-[300px]" role="figure" aria-label="Bar chart comparing Collaboration Scores across work setups.">
        <div style={srOnlyStyle}>
          This bar chart displays the breakdown of collaboration scores versus review turnaround hours across different work setup categories.
        </div>
        <ResponsiveContainer width="100%" height="100%">
          <BarChart
            data={chartData}
            margin={{ top: 20, right: 30, left: 0, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" stroke="var(--grid-line)" vertical={false} />
            <XAxis 
              dataKey="name" 
              tick={{ fill: 'var(--axis-text)', fontWeight: 700 }} 
              axisLine={{ stroke: 'var(--axis-line)' }}
              tickLine={false}
            />
            <YAxis 
              yAxisId="left"
              tick={{ fill: 'var(--chart-primary)', fontWeight: 600 }}
              axisLine={{ stroke: 'var(--axis-line)' }}
              tickLine={false}
              label={{ value: 'Collab Score', angle: -90, position: 'insideLeft', fill: 'var(--chart-primary)', fontWeight: 'bold' }}
            />
            <YAxis 
              yAxisId="right"
              orientation="right"
              tick={{ fill: 'var(--chart-danger)', fontWeight: 600 }}
              axisLine={{ stroke: 'var(--axis-line)' }}
              tickLine={false}
              label={{ value: 'Wait Hours', angle: 90, position: 'insideRight', fill: 'var(--chart-danger)', fontWeight: 'bold' }}
            />
            <Tooltip 
              cursor={{ fill: '#e5e7eb', opacity: 0.3 }}
              contentStyle={{ 
                backgroundColor: 'var(--tooltip-bg)', 
                border: '2px solid #16a34a',
                borderRadius: '8px',
                color: '#333',
                fontWeight: 'bold'
              }}
            />
            <Legend wrapperStyle={{ paddingTop: '10px', fontWeight: 'bold', color: '#333' }} />
            <Bar yAxisId="left" dataKey="Collaboration Score" fill="var(--chart-primary)" radius={[4, 4, 0, 0]} maxBarSize={60} />
            <Bar yAxisId="right" dataKey="Review Turnaround (Hrs)" fill="var(--chart-danger)" radius={[4, 4, 0, 0]} maxBarSize={60} />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default CollaborationChart;
