import React, { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { Badge } from '../../components/ui/Badge';
import { Button } from '../../components/ui/Button';
import { Table, Column } from '../../components/ui/Table';
import {
  BarChart3,
  FileSpreadsheet,
  FileText
} from 'lucide-react';

interface WardStat {
  ward: number;
  name: string;
  total_lodged: number;
  resolved: number;
  resolution_rate_pct: number;
  avg_hours: number;
  satisfaction_score: number;
  grade: 'A+' | 'A' | 'B' | 'C';
}

export const ReportsAnalytics: React.FC = () => {
  const [selectedPeriod] = useState('CURRENT_MONTH');

  const wardStats: WardStat[] = [
    {
      ward: 4,
      name: 'Indiranagar Urban Zone',
      total_lodged: 412,
      resolved: 395,
      resolution_rate_pct: 95.8,
      avg_hours: 24.2,
      satisfaction_score: 4.8,
      grade: 'A+',
    },
    {
      ward: 7,
      name: 'Koramangala Commercial Hub',
      total_lodged: 580,
      resolved: 546,
      resolution_rate_pct: 94.1,
      avg_hours: 26.5,
      satisfaction_score: 4.7,
      grade: 'A',
    },
    {
      ward: 2,
      name: 'Central Business District',
      total_lodged: 340,
      resolved: 318,
      resolution_rate_pct: 93.5,
      avg_hours: 28.0,
      satisfaction_score: 4.6,
      grade: 'A',
    },
    {
      ward: 9,
      name: 'Lakeside Residential Sector',
      total_lodged: 290,
      resolved: 270,
      resolution_rate_pct: 93.1,
      avg_hours: 29.4,
      satisfaction_score: 4.5,
      grade: 'B',
    },
  ];

  const columns: Column<WardStat>[] = [
    {
      key: 'ward',
      header: 'Ward & Zone',
      render: (w) => (
        <div>
          <div className="font-bold text-slate-900">Ward {w.ward}: {w.name}</div>
        </div>
      ),
    },
    {
      key: 'total_lodged',
      header: 'Total Lodged',
      render: (w) => <span className="font-mono text-xs font-semibold text-slate-700">{w.total_lodged}</span>,
    },
    {
      key: 'resolved',
      header: 'Remediated',
      render: (w) => <span className="font-mono text-xs font-bold text-emerald-700">{w.resolved}</span>,
    },
    {
      key: 'resolution_rate_pct',
      header: 'Resolution Rate',
      render: (w) => (
        <div className="w-24">
          <div className="text-xs font-bold text-slate-900 font-mono">{w.resolution_rate_pct}%</div>
          <div className="w-full bg-slate-200 rounded-full h-1.5 mt-0.5">
            <div className="bg-teal-600 h-1.5 rounded-full" style={{ width: `${w.resolution_rate_pct}%` }} />
          </div>
        </div>
      ),
    },
    {
      key: 'avg_hours',
      header: 'Avg Remediation Time',
      render: (w) => <span className="font-mono text-xs text-slate-600">{w.avg_hours} hrs</span>,
    },
    {
      key: 'satisfaction_score',
      header: 'Citizen Rating',
      render: (w) => <span className="font-bold text-xs text-amber-600">★ {w.satisfaction_score} / 5</span>,
    },
    {
      key: 'grade',
      header: 'SLA Grade',
      render: (w) => <Badge status={w.grade === 'A+' || w.grade === 'A' ? 'RESOLVED' : 'GOOD'}>{w.grade}</Badge>,
    },
  ];

  const handleExport = (format: string) => {
    alert(`Generating official municipal ${format} audit report for ${selectedPeriod}... Download starting.`);
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="bg-slate-900 text-white rounded-xl p-5 border border-slate-800 shadow-md flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <BarChart3 className="h-5 w-5 text-teal-400" />
            <h1 className="text-lg font-bold tracking-tight text-white">
              Municipal Performance Reports & SLA Analytics
            </h1>
          </div>
          <p className="text-xs text-slate-300 mt-1">
            Statutory civic compliance audits, ward remediation velocity, and citizen satisfaction ratings.
          </p>
        </div>

        <div className="flex items-center space-x-2">
          <Button
            size="sm"
            variant="outline"
            onClick={() => handleExport('CSV')}
            className="bg-slate-800 hover:bg-slate-700 text-slate-200 border-slate-700 text-xs"
          >
            <FileSpreadsheet className="h-3.5 w-3.5 mr-1 text-emerald-400" />
            Export CSV
          </Button>
          <Button
            size="sm"
            variant="primary"
            onClick={() => handleExport('PDF')}
            className="bg-teal-600 hover:bg-teal-500 text-xs"
          >
            <FileText className="h-3.5 w-3.5 mr-1" />
            Executive PDF Report
          </Button>
        </div>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-4 gap-4">
        <Card className="border-l-4 border-l-teal-600">
          <div className="text-[11px] font-bold text-slate-500 uppercase">City-Wide SLA Compliance</div>
          <div className="text-2xl font-black text-slate-900 mt-0.5">94.8%</div>
          <div className="text-[10px] text-emerald-600 font-semibold mt-0.5">+1.8% above 93% statutory mark</div>
        </Card>
        <Card className="border-l-4 border-l-emerald-600">
          <div className="text-[11px] font-bold text-slate-500 uppercase">Remediated Grievances (YTD)</div>
          <div className="text-2xl font-black text-slate-900 mt-0.5">18,420</div>
          <div className="text-[10px] text-slate-500 mt-0.5">Across all 16 municipal wards</div>
        </Card>
        <Card className="border-l-4 border-l-sky-600">
          <div className="text-[11px] font-bold text-slate-500 uppercase">Avg Resolution Speed</div>
          <div className="text-2xl font-black text-slate-900 mt-0.5">26.8 hrs</div>
          <div className="text-[10px] text-slate-500 mt-0.5">Statutory max limit: 48.0 hrs</div>
        </Card>
        <Card className="border-l-4 border-l-amber-500">
          <div className="text-[11px] font-bold text-slate-500 uppercase">Citizen Audit Feedback</div>
          <div className="text-2xl font-black text-amber-600 mt-0.5">4.7 / 5.0</div>
          <div className="text-[10px] text-slate-500 mt-0.5">Based on 14,210 verified reviews</div>
        </Card>
      </div>

      {/* Ward Breakdown Table */}
      <Card
        title="Municipal Ward SLA Performance Audit"
        subtitle="Ranked by compliance percentage, average resolution velocity, and citizen audit score."
      >
        <Table
          columns={columns}
          data={wardStats}
          keyExtractor={(w) => w.ward.toString()}
        />
      </Card>
    </div>
  );
};
