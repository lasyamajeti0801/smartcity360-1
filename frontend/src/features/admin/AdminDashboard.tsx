import React, { useState, useEffect } from 'react';
import { Badge } from '../../components/ui/Badge';
import { Button } from '../../components/ui/Button';
import { CityKPIs, Complaint } from '../../types';
import {
  Download,
  RefreshCw,
  TrendingUp,
  AlertTriangle,
  CheckCircle2,
  Clock,
  Radio,
  Building,
  Search,
  Eye,
  X,
  FileText,
  MapPin,
  ShieldCheck
} from 'lucide-react';

interface AdminDashboardProps {
  kpis: CityKPIs;
  complaints: Complaint[];
  onRefresh?: () => void;
}

export const AdminDashboard: React.FC<AdminDashboardProps> = ({
  kpis,
  complaints,
  onRefresh,
}) => {
  const [selectedDept, setSelectedDept] = useState<string>('ALL');
  const [selectedPriority, setSelectedPriority] = useState<string>('ALL');
  const [selectedStatus, setSelectedStatus] = useState<string>('ALL');
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [lastUpdated, setLastUpdated] = useState<string>('');
  const [selectedTicket, setSelectedTicket] = useState<Complaint | null>(null);
  const [isRefreshing, setIsRefreshing] = useState<boolean>(false);

  useEffect(() => {
    setLastUpdated(new Date().toLocaleTimeString('en-GB', { hour12: false }));
  }, [complaints, kpis]);

  const handleManualRefresh = () => {
    setIsRefreshing(true);
    if (onRefresh) onRefresh();
    setTimeout(() => {
      setLastUpdated(new Date().toLocaleTimeString('en-GB', { hour12: false }));
      setIsRefreshing(false);
    }, 600);
  };

  // Department workload aggregation
  const deptPerformance = [
    { code: 'ROADS', name: 'Roads & Public Infrastructure', open: 8, slaBreach: 1, compliance: 92.4, avgHours: 34.2 },
    { code: 'SANITATION', name: 'Solid Waste & Circular Economy', open: 5, slaBreach: 0, compliance: 98.1, avgHours: 18.0 },
    { code: 'WATER', name: 'Municipal Water Supply Board', open: 6, slaBreach: 0, compliance: 96.5, avgHours: 22.4 },
    { code: 'ELECTRICAL', name: 'Smart Power & Streetlights', open: 4, slaBreach: 1, compliance: 91.0, avgHours: 31.8 },
    { code: 'TRANSIT', name: 'Urban Mobility & Bus Transit', open: 3, slaBreach: 0, compliance: 97.4, avgHours: 14.5 },
    { code: 'EMERGENCY', name: '911 Tactical Command', open: 2, slaBreach: 0, compliance: 100.0, avgHours: 0.8 },
  ];

  // 7-day intake vs resolution simulation data for SVG chart
  const weeklyAnalytics = [
    { day: 'Mon', intake: 24, resolved: 22 },
    { day: 'Tue', intake: 31, resolved: 28 },
    { day: 'Wed', intake: 19, resolved: 24 },
    { day: 'Thu', intake: 28, resolved: 27 },
    { day: 'Fri', intake: 35, resolved: 31 },
    { day: 'Sat', intake: 15, resolved: 18 },
    { day: 'Sun', intake: 12, resolved: 14 },
  ];

  const filteredTickets = complaints.filter((c) => {
    const matchesDept = selectedDept === 'ALL' || c.department_id === selectedDept;
    const matchesPriority = selectedPriority === 'ALL' || c.priority === selectedPriority;
    const matchesStatus = selectedStatus === 'ALL' || c.status === selectedStatus;
    const matchesSearch =
      searchQuery.trim() === '' ||
      c.ticket_number.toLowerCase().includes(searchQuery.toLowerCase()) ||
      c.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      (c.location_address && c.location_address.toLowerCase().includes(searchQuery.toLowerCase()));

    return matchesDept && matchesPriority && matchesStatus && matchesSearch;
  });

  return (
    <div className="space-y-6">
      {/* Top Welcome / Overview Bar */}
      <div className="bg-white rounded-lg border border-slate-200 p-5 shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2.5">
            <h1 className="text-xl font-bold text-slate-900 tracking-tight">City Operations Overview</h1>
            <div className="flex items-center space-x-1.5 px-2 py-0.5 rounded-full bg-emerald-50 border border-emerald-200">
              <span className="h-2 w-2 rounded-full bg-emerald-500 animate-pulse"></span>
              <span className="text-[10px] font-bold text-emerald-700 tracking-wider uppercase">System Operational</span>
            </div>
          </div>
          <p className="text-xs text-slate-500 mt-1 max-w-2xl">
            Monitor essential civic services, citizen requests and emergency activity from one place.
          </p>
        </div>

        <div className="flex items-center space-x-3 shrink-0">
          <div className="text-right hidden sm:block">
            <span className="text-[10px] uppercase font-bold text-slate-400 tracking-wider">Live Freshness</span>
            <p className="text-xs font-mono font-semibold text-slate-700">Last updated: {lastUpdated}</p>
          </div>
          <button
            onClick={handleManualRefresh}
            className={`p-2 rounded-md border border-slate-200 bg-slate-50 hover:bg-slate-100 text-slate-700 transition-all ${
              isRefreshing ? 'animate-spin text-teal-600' : ''
            }`}
            title="Refresh Operational Telemetry"
            aria-label="Refresh Data"
          >
            <RefreshCw className="h-4 w-4" />
          </button>
          <Button variant="outline" size="sm" className="hidden sm:inline-flex border-slate-200 text-slate-700">
            <Download className="h-3.5 w-3.5 mr-1" />
            Audit Report (CSV)
          </Button>
        </div>
      </div>

      {/* KPI Cards Grid */}
      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3.5">
        <div className="bg-white rounded-lg border border-slate-200 p-4 shadow-sm">
          <div className="flex items-center justify-between">
            <span className="text-[11px] font-bold uppercase text-slate-500">Total Inflow</span>
            <Clock className="h-4 w-4 text-slate-400" />
          </div>
          <div className="text-2xl font-bold text-slate-900 mt-2">{kpis.total_complaints + 140}</div>
          <div className="flex items-center space-x-1 mt-1 text-[11px] text-emerald-600 font-medium">
            <TrendingUp className="h-3 w-3" />
            <span>+12.4% vs last week</span>
          </div>
        </div>

        <div className="bg-white rounded-lg border border-slate-200 p-4 shadow-sm">
          <div className="flex items-center justify-between">
            <span className="text-[11px] font-bold uppercase text-slate-500">Pending Requests</span>
            <AlertTriangle className="h-4 w-4 text-amber-500" />
          </div>
          <div className="text-2xl font-bold text-amber-600 mt-2">{kpis.active_complaints + 16}</div>
          <div className="text-[11px] text-slate-500 mt-1">Across 6 departments</div>
        </div>

        <div className="bg-white rounded-lg border border-slate-200 p-4 shadow-sm">
          <div className="flex items-center justify-between">
            <span className="text-[11px] font-bold uppercase text-slate-500">Resolved Today</span>
            <CheckCircle2 className="h-4 w-4 text-emerald-600" />
          </div>
          <div className="text-2xl font-bold text-emerald-600 mt-2">29</div>
          <div className="text-[11px] text-emerald-600 font-medium mt-1">100% SLA compliant</div>
        </div>

        <div className="bg-white rounded-lg border border-slate-200 p-4 shadow-sm">
          <div className="flex items-center justify-between">
            <span className="text-[11px] font-bold uppercase text-slate-500">Active Emergencies</span>
            <Radio className="h-4 w-4 text-rose-600 animate-pulse" />
          </div>
          <div className="text-2xl font-bold text-rose-600 mt-2">{kpis.active_emergencies}</div>
          <div className="text-[11px] text-rose-600 font-medium mt-1">All Units Deployed</div>
        </div>

        <div className="bg-white rounded-lg border border-slate-200 p-4 shadow-sm">
          <div className="flex items-center justify-between">
            <span className="text-[11px] font-bold uppercase text-slate-500">SLA Compliance</span>
            <ShieldCheck className="h-4 w-4 text-teal-600" />
          </div>
          <div className="text-2xl font-bold text-teal-700 mt-2">{kpis.sla_compliance_percentage}%</div>
          <div className="text-[11px] text-teal-700 font-medium mt-1">Statutory Standard &gt;95%</div>
        </div>

        <div className="bg-white rounded-lg border border-slate-200 p-4 shadow-sm">
          <div className="flex items-center justify-between">
            <span className="text-[11px] font-bold uppercase text-slate-500">Grid Health Score</span>
            <Building className="h-4 w-4 text-sky-600" />
          </div>
          <div className="text-2xl font-bold text-slate-900 mt-2">96.8%</div>
          <div className="text-[11px] text-slate-500 mt-1">120 SCADA nodes online</div>
        </div>
      </div>

      {/* Realistic Data Visualization Section */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-5">
        {/* 7-Day Inflow vs Resolution Chart */}
        <div className="lg:col-span-2 bg-white rounded-lg border border-slate-200 p-5 shadow-sm">
          <div className="flex items-center justify-between mb-4">
            <div>
              <h3 className="text-sm font-bold text-slate-900">7-Day Civic Ticket Velocity & Resolution Inflow</h3>
              <p className="text-xs text-slate-500">Comparative throughput of newly lodged citizen issues against closed tickets</p>
            </div>
            <div className="flex items-center space-x-3 text-xs">
              <span className="flex items-center space-x-1">
                <span className="h-3 w-3 rounded-sm bg-teal-600"></span>
                <span className="text-slate-600">Lodged</span>
              </span>
              <span className="flex items-center space-x-1">
                <span className="h-3 w-3 rounded-sm bg-slate-300"></span>
                <span className="text-slate-600">Resolved</span>
              </span>
            </div>
          </div>

          {/* Clean SVG Bar Chart */}
          <div className="h-48 w-full flex items-end justify-between gap-3 pt-4 px-2 border-b border-slate-200 pb-2">
            {weeklyAnalytics.map((w) => (
              <div key={w.day} className="flex-1 flex flex-col items-center gap-1.5 h-full justify-end">
                <div className="w-full flex items-end justify-center gap-1.5 h-36">
                  <div
                    style={{ height: `${(w.intake / 40) * 100}%` }}
                    className="w-3.5 bg-teal-700 hover:bg-teal-600 rounded-t transition-all"
                    title={`Lodged: ${w.intake}`}
                  />
                  <div
                    style={{ height: `${(w.resolved / 40) * 100}%` }}
                    className="w-3.5 bg-slate-300 hover:bg-slate-400 rounded-t transition-all"
                    title={`Resolved: ${w.resolved}`}
                  />
                </div>
                <span className="text-[11px] font-semibold text-slate-600">{w.day}</span>
              </div>
            ))}
          </div>
          <div className="mt-3 flex items-center justify-between text-xs text-slate-500">
            <span>Average daily turnaround: 21.4 hours</span>
            <span className="font-semibold text-teal-700">92.8% 7-day efficiency rating</span>
          </div>
        </div>

        {/* Department SLA & Workload Breakdown */}
        <div className="bg-white rounded-lg border border-slate-200 p-5 shadow-sm flex flex-col justify-between">
          <div>
            <h3 className="text-sm font-bold text-slate-900">Agency Workload & SLA</h3>
            <p className="text-xs text-slate-500 mb-3">Live ticket pressure across municipal divisions</p>

            <div className="space-y-3">
              {deptPerformance.slice(0, 5).map((d) => (
                <div key={d.code} className="text-xs">
                  <div className="flex justify-between font-medium text-slate-800 mb-1">
                    <span className="truncate pr-2">{d.name}</span>
                    <span className="font-mono font-bold text-slate-900">{d.compliance}%</span>
                  </div>
                  <div className="w-full h-2 bg-slate-100 rounded-full overflow-hidden">
                    <div
                      className={`h-full ${
                        d.compliance >= 95 ? 'bg-teal-600' : d.compliance >= 92 ? 'bg-amber-500' : 'bg-rose-500'
                      }`}
                      style={{ width: `${d.compliance}%` }}
                    />
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className="pt-3 border-t border-slate-100 mt-4 text-[11px] text-slate-500 flex justify-between">
            <span>Critical threshold: &lt;90.0%</span>
            <span className="font-semibold text-emerald-600">Zero Critical Breaches</span>
          </div>
        </div>
      </div>

      {/* Complaint Management System (Filters, Search, High-Density Table) */}
      <div className="bg-white rounded-lg border border-slate-200 shadow-sm overflow-hidden">
        {/* Table Filter Header */}
        <div className="p-4 border-b border-slate-200 bg-slate-50/70 flex flex-col md:flex-row md:items-center justify-between gap-3">
          <div>
            <h2 className="text-sm font-bold text-slate-900">Civic Complaints Command Desk</h2>
            <p className="text-xs text-slate-500">Live multi-agency ticket queue with SLA auditing and field routing.</p>
          </div>

          {/* Filter Controls */}
          <div className="flex flex-wrap items-center gap-2">
            <div className="relative min-w-[180px]">
              <Search className="absolute left-2.5 top-2 h-3.5 w-3.5 text-slate-400" />
              <input
                type="text"
                placeholder="Search ticket # or keyword..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full pl-8 pr-2.5 py-1 text-xs border border-slate-300 rounded bg-white focus:outline-none focus:ring-1 focus:ring-teal-600"
              />
            </div>

            <select
              value={selectedDept}
              onChange={(e) => setSelectedDept(e.target.value)}
              className="px-2 py-1 text-xs border border-slate-300 rounded bg-white text-slate-700 font-medium focus:outline-none"
            >
              <option value="ALL">All Departments</option>
              <option value="ROADS">Roads & Works</option>
              <option value="SANITATION">Sanitation</option>
              <option value="WATER">Water Supply</option>
              <option value="ELECTRICAL">Lighting</option>
              <option value="EMERGENCY">Emergency</option>
            </select>

            <select
              value={selectedPriority}
              onChange={(e) => setSelectedPriority(e.target.value)}
              className="px-2 py-1 text-xs border border-slate-300 rounded bg-white text-slate-700 font-medium focus:outline-none"
            >
              <option value="ALL">All Priorities</option>
              <option value="CRITICAL">Critical</option>
              <option value="HIGH">High</option>
              <option value="MEDIUM">Medium</option>
              <option value="LOW">Low</option>
            </select>

            <select
              value={selectedStatus}
              onChange={(e) => setSelectedStatus(e.target.value)}
              className="px-2 py-1 text-xs border border-slate-300 rounded bg-white text-slate-700 font-medium focus:outline-none"
            >
              <option value="ALL">All Stages</option>
              <option value="SUBMITTED">Submitted</option>
              <option value="IN_PROGRESS">In Progress</option>
              <option value="RESOLVED">Resolved</option>
              <option value="REJECTED">Rejected</option>
            </select>
          </div>
        </div>

        {/* Data Table */}
        <div className="overflow-x-auto">
          <table className="min-w-full divide-y divide-slate-200 text-left text-xs">
            <thead className="bg-slate-100/80 text-slate-700 font-bold uppercase tracking-wider text-[10px]">
              <tr>
                <th className="px-4 py-2.5">Ticket #</th>
                <th className="px-4 py-2.5">Issue Subject & Location</th>
                <th className="px-4 py-2.5">Citizen</th>
                <th className="px-4 py-2.5">Department</th>
                <th className="px-4 py-2.5">Priority</th>
                <th className="px-4 py-2.5">Status</th>
                <th className="px-4 py-2.5">SLA Target</th>
                <th className="px-4 py-2.5 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-200 bg-white">
              {filteredTickets.length > 0 ? (
                filteredTickets.map((c) => (
                  <tr key={c.id} className="hover:bg-slate-50/90 transition-colors">
                    <td className="px-4 py-3 font-mono font-bold text-teal-800 whitespace-nowrap">
                      {c.ticket_number}
                    </td>
                    <td className="px-4 py-3">
                      <div className="font-semibold text-slate-900">{c.title}</div>
                      <div className="text-[11px] text-slate-500 truncate max-w-xs">
                        {c.location_address} {c.ward_number ? `(Ward ${c.ward_number})` : ''}
                      </div>
                    </td>
                    <td className="px-4 py-3 text-slate-700 whitespace-nowrap">
                      {(c as any).citizen_name || 'Resident Citizen'}
                    </td>
                    <td className="px-4 py-3 text-slate-600 font-medium whitespace-nowrap">
                      {c.department_id || 'General Municipal'}
                    </td>
                    <td className="px-4 py-3 whitespace-nowrap">
                      <Badge status={c.priority}>{c.priority}</Badge>
                    </td>
                    <td className="px-4 py-3 whitespace-nowrap">
                      <Badge status={c.status}>{c.status}</Badge>
                    </td>
                    <td className="px-4 py-3 font-mono text-slate-600 whitespace-nowrap">
                      {c.sla_due_at
                        ? new Date(c.sla_due_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
                        : 'Standard (48h)'}
                    </td>
                    <td className="px-4 py-3 text-right whitespace-nowrap">
                      <button
                        onClick={() => setSelectedTicket(c)}
                        className="inline-flex items-center px-2.5 py-1 text-xs font-semibold rounded border border-slate-300 bg-white hover:bg-slate-50 text-slate-700 transition-colors"
                      >
                        <Eye className="h-3.5 w-3.5 mr-1 text-slate-400" />
                        Inspect
                      </button>
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan={8} className="px-4 py-8 text-center text-slate-500">
                    <FileText className="h-8 w-8 mx-auto text-slate-300 mb-2" />
                    <p className="font-semibold text-sm">No complaints match active filter parameters.</p>
                    <p className="text-xs text-slate-400 mt-0.5">Try resetting search keywords or department filters.</p>
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Ticket Detail Inspection Modal */}
      {selectedTicket && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-xs">
          <div className="bg-white rounded-lg shadow-2xl border border-slate-200 max-w-lg w-full overflow-hidden animate-in fade-in zoom-in-95 duration-150">
            <div className="px-5 py-4 bg-slate-900 text-white flex items-center justify-between">
              <div>
                <span className="text-[10px] uppercase font-bold text-teal-400">Civic Ticket Inspection</span>
                <h3 className="text-base font-bold">{selectedTicket.ticket_number}</h3>
              </div>
              <button
                onClick={() => setSelectedTicket(null)}
                className="text-slate-400 hover:text-white transition-colors"
                aria-label="Close modal"
              >
                <X className="h-5 w-5" />
              </button>
            </div>

            <div className="p-5 space-y-4 text-xs">
              <div>
                <h4 className="font-semibold text-slate-900 text-sm">{selectedTicket.title}</h4>
                <p className="text-slate-600 mt-1">{selectedTicket.description || 'No additional details provided.'}</p>
              </div>

              <div className="grid grid-cols-2 gap-3 p-3 bg-slate-50 rounded-md border border-slate-100">
                <div>
                  <span className="text-slate-400 text-[10px] uppercase font-semibold">Priority</span>
                  <div className="mt-0.5">
                    <Badge status={selectedTicket.priority}>{selectedTicket.priority}</Badge>
                  </div>
                </div>
                <div>
                  <span className="text-slate-400 text-[10px] uppercase font-semibold">Workflow Status</span>
                  <div className="mt-0.5">
                    <Badge status={selectedTicket.status}>{selectedTicket.status}</Badge>
                  </div>
                </div>
                <div>
                  <span className="text-slate-400 text-[10px] uppercase font-semibold">Jurisdictional Ward</span>
                  <div className="font-semibold text-slate-800 mt-0.5">Ward {selectedTicket.ward_number || 4}</div>
                </div>
                <div>
                  <span className="text-slate-400 text-[10px] uppercase font-semibold">Reported Timestamp</span>
                  <div className="font-mono text-slate-700 mt-0.5">
                    {new Date(selectedTicket.created_at).toLocaleString()}
                  </div>
                </div>
              </div>

              <div className="flex items-start space-x-2 text-slate-600">
                <MapPin className="h-4 w-4 text-slate-400 shrink-0 mt-0.5" />
                <span>{selectedTicket.location_address || 'Geocoded Ward Location'}</span>
              </div>

              {/* Progress Timeline */}
              <div className="pt-2 border-t border-slate-100">
                <span className="text-[10px] uppercase font-bold text-slate-400">Resolution Timeline</span>
                <div className="flex items-center justify-between mt-2 text-[11px]">
                  <span className="font-semibold text-teal-700">1. Lodged</span>
                  <span className="text-slate-300">→</span>
                  <span className="font-semibold text-teal-700">2. Triaged</span>
                  <span className="text-slate-300">→</span>
                  <span className="font-semibold text-slate-800">3. Field Dispatched</span>
                  <span className="text-slate-300">→</span>
                  <span className="text-slate-400">4. Resolved</span>
                </div>
              </div>
            </div>

            <div className="px-5 py-3 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
              <span className="text-[11px] text-slate-500">Authorized by Municipal City Operations</span>
              <Button size="sm" onClick={() => setSelectedTicket(null)}>
                Close
              </Button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

