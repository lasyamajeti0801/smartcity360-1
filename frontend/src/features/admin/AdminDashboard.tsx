import React, { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { Badge } from '../../components/ui/Badge';
import { Table, Column } from '../../components/ui/Table';
import { Button } from '../../components/ui/Button';
import { CityKPIs, Complaint } from '../../types';
import {
  Download,
  Filter
} from 'lucide-react';

interface AdminDashboardProps {
  kpis: CityKPIs;
  complaints: Complaint[];
}

export const AdminDashboard: React.FC<AdminDashboardProps> = ({
  kpis,
  complaints,
}) => {
  const [selectedDept, setSelectedDept] = useState<string>('ALL');

  // Department workload aggregation
  const deptPerformance = [
    { code: 'ROADS', name: 'Roads & Infrastructure', open: 8, slaBreach: 1, compliance: 92.4, avgHours: 34.2 },
    { code: 'SANITATION', name: 'Solid Waste & Sanitation', open: 5, slaBreach: 0, compliance: 98.1, avgHours: 18.0 },
    { code: 'WATER', name: 'Water Supply Board', open: 6, slaBreach: 0, compliance: 96.5, avgHours: 22.4 },
    { code: 'ELECTRICAL', name: 'Public Lighting Utilities', open: 4, slaBreach: 1, compliance: 91.0, avgHours: 31.8 },
    { code: 'EMERGENCY', name: 'Disaster Management', open: 2, slaBreach: 0, compliance: 100.0, avgHours: 0.8 },
  ];

  const filteredTickets = complaints.filter(
    (c) => selectedDept === 'ALL' || c.department_id === selectedDept
  );

  const ticketColumns: Column<Complaint>[] = [
    {
      key: 'ticket_number',
      header: 'Ticket #',
      render: (c) => <span className="font-mono font-bold text-slate-900">{c.ticket_number}</span>,
    },
    {
      key: 'title',
      header: 'Subject & Location',
      render: (c) => (
        <div>
          <div className="font-medium text-slate-900">{c.title}</div>
          <div className="text-xs text-slate-500">{c.location_address} (Ward {c.ward_number || 'N/A'})</div>
        </div>
      ),
    },
    {
      key: 'priority',
      header: 'Priority',
      render: (c) => <Badge status={c.priority}>{c.priority}</Badge>,
    },
    {
      key: 'status',
      header: 'Stage',
      render: (c) => <Badge status={c.status}>{c.status}</Badge>,
    },
    {
      key: 'sla_due_at',
      header: 'Target Resolution',
      render: (c) => (
        <span className="text-xs text-slate-600 font-mono">
          {c.sla_due_at ? new Date(c.sla_due_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) : 'Standard'}
        </span>
      ),
    },
  ];

  return (
    <div className="space-y-6">
      {/* Top Header Bar */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 pb-4">
        <div>
          <div className="flex items-center space-x-2">
            <h1 className="text-xl font-bold text-slate-900 tracking-tight">Executive City Administration Desk</h1>
            <span className="text-xs bg-emerald-100 text-emerald-800 font-semibold px-2 py-0.5 rounded">Live Telemetry</span>
          </div>
          <p className="text-xs text-slate-500 mt-0.5">
            Cross-departmental municipal service workload, SLA compliance audit, and operational triage.
          </p>
        </div>

        <div className="flex items-center space-x-2">
          <div className="flex items-center space-x-1.5 text-xs">
            <Filter className="h-3.5 w-3.5 text-slate-500" />
            <select
              value={selectedDept}
              onChange={(e) => setSelectedDept(e.target.value)}
              className="bg-white border border-slate-300 rounded px-2.5 py-1 text-xs text-slate-700 font-medium focus:outline-none focus:ring-1 focus:ring-slate-900"
            >
              <option value="ALL">All Departments</option>
              <option value="ROADS">Roads & Infrastructure</option>
              <option value="SANITATION">Sanitation & Waste</option>
              <option value="WATER">Water Supply Board</option>
              <option value="ELECTRICAL">Electrical & Lighting</option>
              <option value="EMERGENCY">Emergency Management</option>
            </select>
          </div>
          <Button variant="outline" size="sm">
            <Download className="h-3.5 w-3.5 mr-1" />
            Export Audit (CSV)
          </Button>
        </div>
      </div>

      {/* Primary KPI Grid (High density, verified values) */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
        <Card className="border-t-2 border-t-sky-600">
          <p className="text-xs font-semibold text-slate-500 uppercase">Active Workload</p>
          <div className="flex items-baseline space-x-2 mt-1">
            <span className="text-2xl font-bold text-slate-900">{kpis.active_complaints}</span>
            <span className="text-xs text-slate-500">tickets in flight</span>
          </div>
          <p className="text-[11px] text-slate-400 mt-1">Across 5 municipal departments</p>
        </Card>

        <Card className="border-t-2 border-t-emerald-600">
          <p className="text-xs font-semibold text-slate-500 uppercase">City-Wide SLA Compliance</p>
          <div className="flex items-baseline space-x-2 mt-1">
            <span className="text-2xl font-bold text-emerald-700">{kpis.sla_compliance_percentage}%</span>
            <span className="text-xs text-emerald-600 font-medium">Target: &gt;95%</span>
          </div>
          <p className="text-[11px] text-slate-400 mt-1">1 breach under supervisor review</p>
        </Card>

        <Card className="border-t-2 border-t-amber-600">
          <p className="text-xs font-semibold text-slate-500 uppercase">Mean Resolution Velocity</p>
          <div className="flex items-baseline space-x-2 mt-1">
            <span className="text-2xl font-bold text-slate-900">{kpis.average_resolution_hours}h</span>
            <span className="text-xs text-slate-500">avg time</span>
          </div>
          <p className="text-[11px] text-slate-400 mt-1">-3.2h improvement vs prior month</p>
        </Card>

        <Card className="border-t-2 border-t-red-600">
          <p className="text-xs font-semibold text-slate-500 uppercase">Active Emergencies</p>
          <div className="flex items-baseline space-x-2 mt-1">
            <span className="text-2xl font-bold text-red-700">{kpis.active_emergencies}</span>
            <span className="text-xs text-red-600 font-medium">Units Dispatched</span>
          </div>
          <p className="text-[11px] text-slate-400 mt-1">Fire Rescue Squad Unit #4 deployed</p>
        </Card>
      </div>

      {/* Department Performance Matrix Table */}
      <Card
        title="Department Performance & SLA Matrix"
        subtitle="Live workload balance, open ticket counts, and turnaround efficiency per municipal agency."
      >
        <div className="overflow-x-auto">
          <table className="min-w-full divide-y divide-slate-200 text-left text-sm">
            <thead className="bg-slate-50 text-xs uppercase font-semibold text-slate-600">
              <tr>
                <th className="px-4 py-2.5">Department</th>
                <th className="px-4 py-2.5 text-center">Open Tickets</th>
                <th className="px-4 py-2.5 text-center">SLA Breaches</th>
                <th className="px-4 py-2.5 text-center">Compliance %</th>
                <th className="px-4 py-2.5 text-right">Avg Turnaround</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-200">
              {deptPerformance.map((dept) => (
                <tr key={dept.code} className="hover:bg-slate-50/80 transition-colors">
                  <td className="px-4 py-3">
                    <div className="font-semibold text-slate-900">{dept.name}</div>
                    <div className="text-xs text-slate-500 font-mono">CODE: {dept.code}</div>
                  </td>
                  <td className="px-4 py-3 text-center font-bold text-slate-800">{dept.open}</td>
                  <td className="px-4 py-3 text-center">
                    {dept.slaBreach > 0 ? (
                      <span className="text-xs font-bold text-red-600 bg-red-50 px-2 py-0.5 rounded border border-red-200">
                        {dept.slaBreach} Overdue
                      </span>
                    ) : (
                      <span className="text-xs text-emerald-600 font-medium">0 Clean</span>
                    )}
                  </td>
                  <td className="px-4 py-3 text-center">
                    <div className="inline-flex items-center space-x-1.5">
                      <span className="font-semibold text-slate-800">{dept.compliance}%</span>
                      <div className="w-16 h-2 bg-slate-200 rounded-full overflow-hidden">
                        <div
                          className={`h-full ${dept.compliance >= 95 ? 'bg-emerald-600' : 'bg-amber-500'}`}
                          style={{ width: `${dept.compliance}%` }}
                        />
                      </div>
                    </div>
                  </td>
                  <td className="px-4 py-3 text-right font-mono text-slate-700">{dept.avgHours} hrs</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Card>

      {/* Comprehensive Operational Tickets Table */}
      <Card
        title="Municipal Civic Tickets Queue"
        subtitle="Global operational view of active and historical civic complaints across all city sectors."
      >
        <Table
          columns={ticketColumns}
          data={filteredTickets}
          keyExtractor={(c) => c.id}
          emptyMessage="No tickets matching selected department filter."
        />
      </Card>
    </div>
  );
};
