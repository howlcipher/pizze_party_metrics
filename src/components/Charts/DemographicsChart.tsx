import { PizzaData } from "../../types";
import React, { useMemo } from 'react';
import { 
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, 
  PieChart, Pie, Cell, Legend
} from 'recharts';
import TooltipInfo from '../TooltipInfo';

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

const DemographicsChart = ({ data }: { data: PizzaData[] }) => {
  const { ageData, genderData } = useMemo(() => {
    if (!data || data.length === 0) return { ageData: [], genderData: [] };

    const ageMap = {};
    const genderMap = {};

    for (let i = 0; i < data.length; i++) {
      const curr = data[i];
      if (curr.age_group) {
        ageMap[curr.age_group] = (ageMap[curr.age_group] || 0) + 1;
      }
      if (curr.gender) {
        genderMap[curr.gender] = (genderMap[curr.gender] || 0) + 1;
      }
    }

    const ages = Object.entries(ageMap)
      .map(([age, count]) => ({ age, count }))
      .sort((a, b) => a.age.localeCompare(b.age));

    const genders = Object.entries(genderMap)
      .map(([name, value]) => ({ name, value }));

    return { ageData: ages, genderData: genders };
  }, [data]);

  const PIE_COLORS = ['var(--chart-primary)', 'var(--chart-danger)', 'var(--chart-warning)', 'var(--chart-info)']; // Italian green, red, cheese yellow, blue

  return (
    <div className="bg-[var(--card-bg)] border-[var(--card-border)] rounded p-5 shadow-sm h-full flex flex-col gap-6">
      <h3 className="text-xl font-bold text-[var(--card-text)] mb-2 border-b border-gray-200 pb-2 flex items-center">
        Demographic Distribution (Who's Eating The Pizza?)
        <TooltipInfo content={
          <div>
            <p className="font-bold mb-1">Chart Explanation:</p>
            <p>Displays the age and gender distribution of respondents included in the current filters.</p>
          </div>
        } />
      </h3>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 flex-grow">
        {/* Age Bar Chart */}
        <div className="flex flex-col min-h-[250px]" role="figure" aria-label="Bar chart showing age distribution of respondents.">
          <p className="text-sm text-[var(--card-subtext)] mb-2 text-center font-bold">Age Ranges</p>
          <div style={srOnlyStyle}>
            This bar chart displays the number of respondents for each age range.
          </div>
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={ageData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="var(--grid-line)" vertical={false} />
              <XAxis dataKey="age" tick={{ fill: 'var(--axis-text)', fontSize: 12, fontWeight: 'bold' }} axisLine={{ stroke: 'var(--axis-line)' }} tickLine={false} />
              <YAxis tick={{ fill: 'var(--axis-text)', fontSize: 12, fontWeight: 'bold' }} axisLine={{ stroke: 'var(--axis-line)' }} tickLine={false} />
              <Tooltip 
                cursor={{ fill: '#fcd34d', opacity: 0.3 }}
                contentStyle={{ backgroundColor: 'var(--tooltip-bg)', border: '2px solid #e3342f', borderRadius: '8px', color: '#333', fontWeight: 'bold' }}
              />
              <Bar dataKey="count" fill="var(--chart-danger)" radius={[4, 4, 0, 0]} name="Respondents" />
            </BarChart>
          </ResponsiveContainer>
        </div>

        {/* Gender Pie Chart */}
        <div className="flex flex-col min-h-[250px]" role="figure" aria-label="Pie chart showing gender breakdown of respondents.">
          <p className="text-sm text-[var(--card-subtext)] mb-2 text-center font-bold">Gender Breakdown</p>
          <div style={srOnlyStyle}>
            This pie chart displays the gender breakdown of the survey respondents.
          </div>
          <ResponsiveContainer width="100%" height="100%">
            <PieChart>
              <Pie
                data={genderData}
                cx="50%"
                cy="50%"
                innerRadius="40%"
                outerRadius="80%"
                paddingAngle={5}
                dataKey="value"
                stroke="none"
              >
                {genderData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={PIE_COLORS[index % PIE_COLORS.length]} />
                ))}
              </Pie>
              <Tooltip 
                formatter={(value, name) => [value, name]}
                contentStyle={{ backgroundColor: 'var(--tooltip-bg)', border: '2px solid #16a34a', borderRadius: '8px', color: '#333', fontWeight: 'bold' }}
              />
              <Legend wrapperStyle={{ fontSize: '12px', color: '#333', fontWeight: 'bold' }} />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
};

export default DemographicsChart;
