import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import {
  Activity,
  Radio,
  RefreshCw,
  MapPin,
  ShieldAlert,
  Droplets,
  Zap,
  Trash2,
  Bus,
  Shield
} from 'lucide-react';
import { Badge } from '../../components/ui/Badge';
import { CityMap } from '../../components/maps/CityMap';
import { useCityData } from '../../context/CityDataContext';
import { useToast } from '../../context/ToastContext';

export const AdminDashboard: React.FC = () => {
  const { kpis, complaints, facilities, refreshData } = useCityData();
  const { success } = useToast();

  const [lastRefreshed, setLastRefreshed] = useState<string>('');
  const [isRefreshing, setIsRefreshing] = useState<boolean>(false);

  useEffect(() => {
    setLastRefreshed(new Date().toLocaleTimeString('en-IN', { hour12: true }));
  }, [complaints, kpis]);

  const handleManualRefresh = async () => {
    setIsRefreshing(true);
    await refreshData();
    setTimeout(() => {
      setLastRefreshed(new Date().toLocaleTimeString('en-IN', { hour12: true }));
      setIsRefreshing(false);
      success('Command Center Refreshed', 'Telemetry and municipal KPIs synchronized.');
    }, 500);
  };

  // City Pulse Grid Data
  const cityPulseItems = [
    { name: 'Urban Mobility & Traffic', status: 'Optimal', trend: '+2.4%', alertLevel: 'LOW', icon: Bus, color: 'text-city-green', desc: '142 bus routes on schedule; intersection signals synced.' },
    { name: 'Drinking Water Utilities', status: 'Calibrating', trend: '-0.8%', alertLevel: 'MEDIUM', icon: Droplets, color: 'text-city-amber', desc: 'Nocturnal pressure testing scheduled for Ward 4 & 5 mains.' },
    { name: 'Public Power & Lighting', status: 'Stable', trend: '+1.2%', alertLevel: 'LOW', icon: Zap, color: 'text-city-leaf', desc: '99.4% streetlight grid reliability; 4 luminaire drivers fixed.' },
    { name: 'Solid Waste Operations', status: 'Active', trend: '+4.0%', alertLevel: 'LOW', icon: Trash2, color: 'text-city-terracotta', desc: '94% community secondary dumpsters cleared by morning shift.' },
    { name: 'Emergency 112 Triage', status: 'Standby', trend: '0.0%', alertLevel: 'LOW', icon: Radio, color: 'text-city-danger', desc: '2 squads on station; average response time 4.2 mins.' },
    { name: 'Public Safety & Surveillance', status: 'Normal', trend: '+0.5%', alertLevel: 'LOW', icon: Shield, color: 'text-city-forest', desc: 'Precinct 1 active patrols deployed across commercial zones.' },
    { name: 'Environmental Air Quality', status: 'Moderate (AQI 84)', trend: '-1.5%', alertLevel: 'LOW', icon: Activity, color: 'text-city-green', desc: 'Particulate sensors within prescribed CPCB ambient standards.' },
  ];

  // Department Performance Breakdown
  const deptPerformance = [
    { code: 'ROADS', name: 'Roads & Public Works', open: complaints.filter(c => c.department_id === 'ROADS' && c.status !== 'RESOLVED').length, resolved: complaints.filter(c => c.department_id === 'ROADS' && c.status === 'RESOLVED').length, compliance: 93.8, avgHours: 32.4 },
    { code: 'SANITATION', name: 'Solid Waste & Sanitation', open: complaints.filter(c => c.department_id === 'SANITATION' && c.status !== 'RESOLVED').length, resolved: complaints.filter(c => c.department_id === 'SANITATION' && c.status === 'RESOLVED').length, compliance: 98.1, avgHours: 18.0 },
    { code: 'WATER', name: 'Water Supply & Sewerage', open: complaints.filter(c => c.department_id === 'WATER' && c.status !== 'RESOLVED').length, resolved: complaints.filter(c => c.department_id === 'WATER' && c.status === 'RESOLVED').length, compliance: 96.5, avgHours: 22.4 },
    { code: 'ELECTRICAL', name: 'Public Lighting Utilities', open: complaints.filter(c => c.department_id === 'ELECTRICAL' && c.status !== 'RESOLVED').length, resolved: complaints.filter(c => c.department_id === 'ELECTRICAL' && c.status === 'RESOLVED').length, compliance: 91.0, avgHours: 31.8 },
    { code: 'TRANSIT', name: 'Urban Mobility & Bus Transit', open: 0, resolved: 3, compliance: 97.4, avgHours: 14.5 },
    { code: 'EMERGENCY', name: '112 Disaster Management', open: 1, resolved: 4, compliance: 100.0, avgHours: 0.8 },
  ];

  return (
    <div className="space-y-6 select-none font-sans">
      {/* 1. Command Centre Header Bar */}
      <div className="bg-city-charcoal text-city-ivory p-5 rounded-xl border border-city-forest shadow-civic flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-3">
            <h1 className="text-xl font-bold tracking-tight text-city-ivory">
              City Operations Command Centre
            </h1>
            <div className="flex items-center space-x-1.5 px-2.5 py-0.5 rounded-full bg-city-forest text-city-leaf border border-city-leaf/30 text-[10px] font-mono font-bold tracking-wide">
              <span className="w-2 h-2 rounded-full bg-city-leaf animate-pulse" />
              <span>LIVE GOVERNANCE</span>
            </div>
          </div>
          <p className="text-xs text-city-concrete/80 mt-1">
            Executive oversight, multi-department SLA monitoring, and real-time municipal telemetry.
          </p>
        </div>

        <div className="flex items-center space-x-3">
          <div className="text-right hidden sm:block text-xs font-mono">
            <span className="text-[10px] text-city-concrete/60 block uppercase">LAST TELEMETRY SYNC</span>
            <span className="text-city-sand font-bold">{lastRefreshed || 'Just now'}</span>
          </div>

          <button
            onClick={handleManualRefresh}
            disabled={isRefreshing}
            className="flex items-center space-x-2 px-3.5 py-2 rounded-lg bg-city-terracotta hover:bg-city-terracotta-dark border border-city-amber/30 text-white text-xs font-bold shadow-civic transition-all"
          >
            <RefreshCw className={`w-3.5 h-3.5 ${isRefreshing ? 'animate-spin text-city-sand' : ''}`} />
            <span>Sync Data</span>
          </button>
        </div>
      </div>

      {/* 2. Top-Level Executive KPI Cards (8 metrics) */}
      <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-3">
        <div className="bg-white p-3.5 rounded-xl border border-surface-border shadow-civic">
          <span className="text-[10px] uppercase font-bold text-city-charcoal/60 font-mono">Total Requests</span>
          <p className="text-xl font-extrabold font-mono text-city-forest mt-1">{kpis.total_complaints}</p>
          <span className="text-[10px] text-city-charcoal/50">Fiscal Year</span>
        </div>

        <div className="bg-white p-3.5 rounded-xl border border-surface-border shadow-civic">
          <span className="text-[10px] uppercase font-bold text-city-charcoal/60 font-mono">Open Grievances</span>
          <p className="text-xl font-extrabold font-mono text-city-amber mt-1">{kpis.active_complaints}</p>
          <span className="text-[10px] text-city-amber font-medium">In Department Queue</span>
        </div>

        <div className="bg-white p-3.5 rounded-xl border border-surface-border shadow-civic">
          <span className="text-[10px] uppercase font-bold text-city-charcoal/60 font-mono">Resolved Today</span>
          <p className="text-xl font-extrabold font-mono text-city-success mt-1">{kpis.resolved_complaints}</p>
          <span className="text-[10px] text-city-success font-medium">Audited & Verified</span>
        </div>

        <div className="bg-white p-3.5 rounded-xl border border-surface-border shadow-civic">
          <span className="text-[10px] uppercase font-bold text-city-charcoal/60 font-mono">SLA Compliance</span>
          <p className="text-xl font-extrabold font-mono text-city-forest mt-1">{kpis.sla_compliance_percentage}%</p>
          <span className="text-[10px] text-city-charcoal/50">SAKALA Standard</span>
        </div>

        <div className="bg-white p-3.5 rounded-xl border border-surface-border shadow-civic">
          <span className="text-[10px] uppercase font-bold text-city-charcoal/60 font-mono">Emergencies (112)</span>
          <p className="text-xl font-extrabold font-mono text-city-danger mt-1">{kpis.active_emergencies}</p>
          <span className="text-[10px] text-city-danger font-medium">Active Incidents</span>
        </div>

        <div className="bg-white p-3.5 rounded-xl border border-surface-border shadow-civic">
          <span className="text-[10px] uppercase font-bold text-city-charcoal/60 font-mono">Field Work Orders</span>
          <p className="text-xl font-extrabold font-mono text-city-forest mt-1">{kpis.active_work_orders}</p>
          <span className="text-[10px] text-city-charcoal/50">Dispatched Crews</span>
        </div>

        <div className="bg-white p-3.5 rounded-xl border border-surface-border shadow-civic">
          <span className="text-[10px] uppercase font-bold text-city-charcoal/60 font-mono">Infra Health</span>
          <p className="text-xl font-extrabold font-mono text-city-leaf mt-1">96.8%</p>
          <span className="text-[10px] text-city-charcoal/50">Asset Uptime</span>
        </div>

        <div className="bg-white p-3.5 rounded-xl border border-surface-border shadow-civic">
          <span className="text-[10px] uppercase font-bold text-city-charcoal/60 font-mono">Citizen Rating</span>
          <p className="text-xl font-extrabold font-mono text-city-amber mt-1">4.8 / 5.0</p>
          <span className="text-[10px] text-city-charcoal/50">Public Satisfaction</span>
        </div>
      </div>

      {/* 3. CITY PULSE (7 Key Urban Infrastructure Domains) */}
      <div className="bg-white p-5 rounded-xl border border-surface-border shadow-civic space-y-3">
        <div className="flex items-center justify-between pb-2 border-b border-surface-border">
          <div className="flex items-center space-x-2">
            <Activity className="w-4 h-4 text-city-green" />
            <h2 className="text-sm font-bold text-city-forest uppercase tracking-wide font-mono">
              CITY PULSE • Real-Time Grid Telemetry
            </h2>
          </div>
          <span className="text-[11px] text-city-charcoal/60">Automated sensor polling every 30s</span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
          {cityPulseItems.map((item, idx) => {
            const Icon = item.icon;
            return (
              <div
                key={idx}
                className="p-3.5 rounded-lg bg-surface-card border border-surface-border space-y-2 hover:border-city-forest/40 transition-colors"
              >
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-2">
                    <Icon className={`w-4 h-4 ${item.color}`} />
                    <span className="text-xs font-bold text-city-forest truncate max-w-[150px]">
                      {item.name}
                    </span>
                  </div>
                  <span className="text-[10px] font-mono font-bold px-1.5 py-0.5 rounded bg-city-sage/50 text-city-forest border border-city-leaf/30">
                    {item.status}
                  </span>
                </div>

                <p className="text-[11px] text-city-charcoal/70 leading-snug">{item.desc}</p>

                <div className="flex items-center justify-between text-[10px] text-city-charcoal/50 pt-1 border-t border-surface-border/50 font-mono">
                  <span>Alert: {item.alertLevel}</span>
                  <span className="text-city-green font-semibold">{item.trend} vs yesterday</span>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* 4. Centerpiece: Full City GIS Operational Map */}
      <div className="bg-white p-5 rounded-xl border border-surface-border shadow-civic space-y-3">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-sm font-bold text-city-forest uppercase tracking-wide font-mono flex items-center space-x-2">
              <MapPin className="w-4 h-4 text-city-terracotta" />
              <span>Live City-Wide GIS Spatial Operations Radar</span>
            </h2>
            <p className="text-xs text-city-charcoal/70 mt-0.5">
              Integrated OpenStreetMap layer visualizing reported complaints, work order crews, and public emergency facilities.
            </p>
          </div>

          <div className="flex items-center space-x-2">
            <span className="text-xs text-city-charcoal/60 hidden sm:inline">
              Active Map Pins: {complaints.length + facilities.length}
            </span>
          </div>
        </div>

        <div className="h-[420px] w-full rounded-xl overflow-hidden border border-surface-border shadow-inner">
          <CityMap complaints={complaints} facilities={facilities} />
        </div>
      </div>

      {/* 5. Department Performance & Alert Centre Split */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left: Department Performance Table */}
        <div className="lg:col-span-8 bg-white p-5 rounded-xl border border-surface-border shadow-civic space-y-4">
          <div className="flex items-center justify-between pb-2 border-b border-surface-border">
            <h3 className="text-sm font-bold text-city-forest">Department Workload & SLA Performance</h3>
            <span className="text-[11px] text-city-charcoal/60">Cross-Department Audited Metrics</span>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead>
                <tr className="border-b border-surface-border text-city-charcoal/60 uppercase font-mono text-[10px]">
                  <th className="py-2.5 px-3">Department</th>
                  <th className="py-2.5 px-3">Open</th>
                  <th className="py-2.5 px-3">Resolved</th>
                  <th className="py-2.5 px-3">SLA Compliance</th>
                  <th className="py-2.5 px-3">Avg Resolution</th>
                  <th className="py-2.5 px-3">Status</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-surface-border">
                {deptPerformance.map((d) => (
                  <tr key={d.code} className="hover:bg-surface-card transition-colors">
                    <td className="py-3 px-3 font-semibold text-city-forest">{d.name}</td>
                    <td className="py-3 px-3 font-mono font-bold text-city-amber">{d.open}</td>
                    <td className="py-3 px-3 font-mono font-bold text-city-success">{d.resolved}</td>
                    <td className="py-3 px-3">
                      <div className="flex items-center space-x-2">
                        <div className="w-16 bg-surface-muted h-1.5 rounded-full overflow-hidden">
                          <div className="bg-city-terracotta h-full rounded-full" style={{ width: `${d.compliance}%` }} />
                        </div>
                        <span className="font-mono font-bold text-city-forest">{d.compliance}%</span>
                      </div>
                    </td>
                    <td className="py-3 px-3 font-mono text-city-charcoal/80">{d.avgHours}h</td>
                    <td className="py-3 px-3">
                      <Badge status={d.compliance > 92 ? 'RESOLVED' : 'HIGH'}>
                        {d.compliance > 92 ? 'ON TARGET' : 'ATTENTION'}
                      </Badge>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        {/* Right: Alert Centre */}
        <div className="lg:col-span-4 bg-white p-5 rounded-xl border border-surface-border shadow-civic space-y-4">
          <div className="flex items-center justify-between pb-2 border-b border-surface-border">
            <div className="flex items-center space-x-2">
              <ShieldAlert className="w-4 h-4 text-city-amber" />
              <h3 className="text-sm font-bold text-city-forest">Active Municipal Alerts</h3>
            </div>
            <span className="text-[10px] font-mono text-city-amber font-bold">3 ACTIVE</span>
          </div>

          <div className="space-y-3">
            <div className="p-3 rounded-lg bg-purple-50 border border-purple-200 space-y-1">
              <div className="flex items-center justify-between text-[11px]">
                <span className="font-bold text-purple-700 uppercase font-mono">PRIORITY ATTENTION</span>
                <span className="text-purple-950/50 text-[10px]">10m ago</span>
              </div>
              <p className="text-xs font-bold text-city-forest">Pothole cluster reported in Ward 4</p>
              <p className="text-[11px] text-city-charcoal/80">
                Multiple reports near MG Road Metro Station. Dispatched to Roads crew (WO-20260912-001).
              </p>
            </div>

            <div className="p-3 rounded-lg bg-city-sand/20 border border-city-sand space-y-1">
              <div className="flex items-center justify-between text-[11px]">
                <span className="font-bold text-city-forest uppercase font-mono">SCHEDULED OPERATION</span>
                <span className="text-city-charcoal/50 text-[10px]">1h ago</span>
              </div>
              <p className="text-xs font-bold text-city-forest">Nocturnal Water Line Pressure Test</p>
              <p className="text-[11px] text-city-charcoal/80">
                Water Board testing 600mm feeder pipeline in Central Zone between 01:00 and 04:00.
              </p>
            </div>

            <div className="p-3 rounded-lg bg-surface-card border border-surface-border space-y-1">
              <div className="flex items-center justify-between text-[11px]">
                <span className="font-bold text-city-forest uppercase font-mono">SLA MILESTONE</span>
                <span className="text-city-charcoal/50 text-[10px]">2h ago</span>
              </div>
              <p className="text-xs font-bold text-city-forest">98% Streetlight Uptime Achieved</p>
              <p className="text-[11px] text-city-charcoal/80">
                Electrical utility cleared 8 non-functional street poles in Sector 7 ahead of deadline.
              </p>
            </div>
          </div>

          <div className="pt-2 border-t border-surface-border text-center">
            <Link
              to="/admin/emergency"
              className="w-full flex items-center justify-center space-x-1.5 py-2.5 rounded-lg bg-city-terracotta hover:bg-city-terracotta-dark text-white text-xs font-bold shadow-civic border border-city-amber/30 transition-colors"
            >
              <Radio className="w-3.5 h-3.5 text-city-sand" />
              <span>Launch 112 Emergency Triage Desk</span>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};
