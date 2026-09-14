import React, { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { Badge } from '../../components/ui/Badge';
import { Button } from '../../components/ui/Button';
import { Table, Column } from '../../components/ui/Table';
import { useToast } from '../../context/ToastContext';
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
  const { addToast } = useToast();
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
      resolved: 541,
      resolution_rate_pct: 93.2,
      avg_hours: 28.5,
      satisfaction_score: 4.6,
      grade: 'A',
    },
    {
      ward: 12,
      name: 'Whitefield IT Corridor',
      total_lodged: 690,
      resolved: 630,
      resolution_rate_pct: 91.3,
      avg_hours: 31.0,
      satisfaction_score: 4.5,
      grade: 'B',
    },
    {
      ward: 2,
      name: 'Malleshwaram Heritage Sector',
      total_lodged: 310,
      resolved: 302,
      resolution_rate_pct: 97.4,
      avg_hours: 19.4,
      satisfaction_score: 4.9,
      grade: 'A+',
    },
    {
      ward: 9,
      name: 'Jayanagar Residential Block',
      total_lodged: 440,
      resolved: 418,
      resolution_rate_pct: 95.0,
      avg_hours: 22.1,
      satisfaction_score: 4.7,
      grade: 'A+',
    },
    {
      ward: 15,
      name: 'Electronic City Industrial Belt',
      total_lodged: 520,
      resolved: 472,
      resolution_rate_pct: 90.7,
      avg_hours: 34.6,
      satisfaction_score: 4.4,
      grade: 'B',
    },
  ];

  const columns: Column<WardStat>[] = [
    {
      key: 'ward',
      header: 'Ward & Zone',
      render: (w) => (
        <div>
          <div className="font-bold text-city-charcoal">Ward {w.ward}: {w.name}</div>
        </div>
      ),
    },
    {
      key: 'total_lodged',
      header: 'Total Lodged',
      render: (w) => <span className="font-mono text-xs font-semibold text-city-charcoal/80">{w.total_lodged}</span>,
    },
    {
      key: 'resolved',
      header: 'Remediated',
      render: (w) => <span className="font-mono text-xs font-bold text-city-forest">{w.resolved}</span>,
    },
    {
      key: 'resolution_rate_pct',
      header: 'Resolution Rate',
      render: (w) => (
        <div className="w-24">
          <div className="text-xs font-bold text-city-charcoal font-mono">{w.resolution_rate_pct}%</div>
          <div className="w-full bg-city-sand/40 rounded-full h-1.5 mt-0.5">
            <div className="bg-city-terracotta h-1.5 rounded-full" style={{ width: `${w.resolution_rate_pct}%` }} />
          </div>
        </div>
      ),
    },
    {
      key: 'avg_hours',
      header: 'Avg Remediation Time',
      render: (w) => <span className="font-mono text-xs text-city-charcoal/70">{w.avg_hours} hrs</span>,
    },
    {
      key: 'satisfaction_score',
      header: 'Citizen Rating',
      render: (w) => <span className="font-bold text-xs text-city-amber">★ {w.satisfaction_score} / 5</span>,
    },
    {
      key: 'grade',
      header: 'SLA Grade',
      render: (w) => <Badge status={w.grade === 'A+' || w.grade === 'A' ? 'RESOLVED' : 'GOOD'}>{w.grade}</Badge>,
    },
  ];

  const handleExport = (format: string) => {
    addToast(`Generating official municipal ${format} audit report for ${selectedPeriod}...`, 'info');
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="bg-gradient-to-r from-city-forest to-city-charcoal text-white rounded-xl p-5 border border-city-forest/40 shadow-md flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <BarChart3 className="h-5 w-5 text-city-amber" />
            <h1 className="text-lg font-bold tracking-tight text-white">
              Municipal Performance Reports & SLA Analytics
            </h1>
          </div>
          <p className="text-xs text-city-ivory/80 mt-1">
            Statutory civic compliance audits, ward remediation velocity, and citizen satisfaction ratings.
          </p>
        </div>

        <div className="flex items-center space-x-2">
          <Button
            size="sm"
            variant="outline"
            onClick={() => handleExport('CSV')}
            className="bg-white/10 hover:bg-white/20 text-city-ivory border-white/20 text-xs"
          >
            <FileSpreadsheet className="h-3.5 w-3.5 mr-1 text-city-amber" />
            Export CSV
          </Button>
          <Button
            size="sm"
            variant="primary"
            onClick={() => handleExport('PDF')}
            className="bg-city-terracotta hover:bg-city-terracotta/90 text-white font-semibold text-xs border-0"
          >
            <FileText className="h-3.5 w-3.5 mr-1" />
            Executive PDF Report
          </Button>
        </div>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-4 gap-4">
        <Card className="border-l-4 border-l-city-terracotta">
          <div className="text-[11px] font-bold text-city-charcoal/60 uppercase">City-Wide SLA Compliance</div>
          <div className="text-2xl font-black text-city-charcoal mt-0.5">94.8%</div>
          <div className="text-[10px] text-city-forest font-semibold mt-0.5">+1.8% above 93% statutory mark</div>
        </Card>
        <Card className="border-l-4 border-l-city-forest">
          <div className="text-[11px] font-bold text-city-charcoal/60 uppercase">Remediated Grievances (YTD)</div>
          <div className="text-2xl font-black text-city-charcoal mt-0.5">18,420</div>
          <div className="text-[10px] text-city-charcoal/60 mt-0.5">Across all 16 municipal wards</div>
        </Card>
        <Card className="border-l-4 border-l-city-ochre">
          <div className="text-[11px] font-bold text-city-charcoal/60 uppercase">Avg Resolution Speed</div>
          <div className="text-2xl font-black text-city-charcoal mt-0.5">26.8 hrs</div>
          <div className="text-[10px] text-city-charcoal/60 mt-0.5">Statutory max limit: 48.0 hrs</div>
        </Card>
        <Card className="border-l-4 border-l-city-amber">
          <div className="text-[11px] font-bold text-city-charcoal/60 uppercase">Citizen Audit Feedback</div>
          <div className="text-2xl font-black text-city-amber mt-0.5">4.7 / 5.0</div>
          <div className="text-[10px] text-city-charcoal/60 mt-0.5">Based on 14,210 verified reviews</div>
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
          emptyMessage="No ward metrics currently recorded."
        />
      </Card>
    </div>
  );
};
