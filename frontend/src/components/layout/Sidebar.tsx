import React from 'react';
import {
  LayoutDashboard,
  Users,
  AlertCircle,
  FileText,
  Radio,
  Car,
  Trash2,
  Droplets,
  Building,
  BarChart3,
  Bell,
  Settings,
  ChevronRight
} from 'lucide-react';
import { UserRole } from '../../types';

interface SidebarProps {
  currentRole: UserRole;
  activeTab: string;
  onTabChange: (tabId: string) => void;
}

export const Sidebar: React.FC<SidebarProps> = ({
  currentRole,
  activeTab,
  onTabChange,
}) => {
  // Master municipal navigation catalog
  const navItems = [
    { id: 'dashboard', label: 'Overview', icon: LayoutDashboard },
    { id: 'citizens', label: 'Citizens', icon: Users },
    { id: 'complaints', label: 'Complaints', icon: AlertCircle },
    { id: 'services', label: 'Service Requests', icon: FileText },
    { id: 'emergency', label: 'Emergency 911', icon: Radio },
    { id: 'traffic', label: 'Traffic & Transit', icon: Car },
    { id: 'waste', label: 'Waste Management', icon: Trash2 },
    { id: 'water', label: 'Water Supply', icon: Droplets },
    { id: 'map', label: 'Public Facilities', icon: Building },
    { id: 'reports', label: 'Reports & Analytics', icon: BarChart3 },
    { id: 'notifications', label: 'Notifications', icon: Bell },
    { id: 'settings', label: 'Settings', icon: Settings },
  ];

  const getUserDetails = () => {
    switch (currentRole) {
      case 'City Administrator':
        return { name: 'Dr. Anita Desai', title: 'City Commissioner', initials: 'AD' };
      case 'Emergency Operator':
        return { name: 'Vikram Mehta', title: '911 Incident Lead', initials: 'VM' };
      case 'Field Staff':
      case 'Department Staff':
        return { name: 'Rajesh Kumar', title: 'Senior Public Works Tech', initials: 'RK' };
      case 'Supervisor':
        return { name: 'Sunita Rao', title: 'Zonal Superintendent', initials: 'SR' };
      default:
        return { name: 'Priya Sharma', title: 'Verified Citizen (Ward 4)', initials: 'PS' };
    }
  };

  const user = getUserDetails();

  return (
    <aside className="w-64 bg-slate-900 text-slate-300 border-r border-slate-800 min-h-[calc(100vh-5.5rem)] p-3 flex flex-col justify-between shrink-0 shadow-lg select-none">
      <div className="space-y-4">
        {/* Navigation Group Header */}
        <div className="px-3 pt-1 flex items-center justify-between">
          <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400">
            Municipal Modules
          </span>
          <span className="text-[10px] bg-slate-800 text-teal-400 border border-slate-700/80 px-1.5 py-0.5 rounded font-mono">
            {currentRole}
          </span>
        </div>

        {/* Navigation Items List */}
        <nav className="space-y-0.5" aria-label="Sidebar Navigation">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => onTabChange(item.id)}
                className={`w-full flex items-center justify-between px-3 py-2 rounded-md text-xs font-medium transition-all group ${
                  isActive
                    ? 'bg-teal-700 text-white font-semibold shadow-sm border border-teal-600/50'
                    : 'text-slate-300 hover:bg-slate-800 hover:text-white'
                }`}
              >
                <div className="flex items-center space-x-2.5">
                  <Icon
                    className={`h-4 w-4 transition-colors ${
                      isActive ? 'text-white' : 'text-slate-400 group-hover:text-teal-400'
                    }`}
                  />
                  <span>{item.label}</span>
                </div>
                {isActive && <ChevronRight className="h-3 w-3 text-teal-200" />}
              </button>
            );
          })}
        </nav>
      </div>

      {/* Bottom User Profile Card & Status */}
      <div className="pt-4 border-t border-slate-800 space-y-3">
        {/* Real-time System Status Pill */}
        <div className="p-2.5 bg-slate-800/80 rounded-md border border-slate-700/60 text-[11px] text-slate-400">
          <div className="flex items-center justify-between text-emerald-400 font-semibold mb-1">
            <span className="flex items-center space-x-1.5">
              <span className="h-2 w-2 rounded-full bg-emerald-400 animate-pulse"></span>
              <span>City Telemetry Grid</span>
            </span>
            <span className="text-[10px] bg-emerald-950 border border-emerald-800 px-1 rounded text-emerald-300">
              OPERATIONAL
            </span>
          </div>
          <div className="flex items-center justify-between text-[10px] text-slate-400 pt-0.5">
            <span>SLA Standard: 95.0%</span>
            <span className="text-slate-300 font-mono font-bold">94.8% (Target)</span>
          </div>
        </div>

        {/* User Card */}
        <div className="p-2.5 bg-slate-800/40 rounded-md border border-slate-800 flex items-center justify-between">
          <div className="flex items-center space-x-2.5 overflow-hidden">
            <div className="h-8 w-8 rounded-full bg-teal-800 text-teal-100 flex items-center justify-center font-bold text-xs border border-teal-600 shrink-0">
              {user.initials}
            </div>
            <div className="overflow-hidden">
              <h4 className="text-xs font-semibold text-white truncate leading-tight">{user.name}</h4>
              <p className="text-[10px] text-slate-400 truncate leading-tight mt-0.5">{user.title}</p>
            </div>
          </div>
          <button
            onClick={() => onTabChange('settings')}
            className="p-1 text-slate-400 hover:text-white rounded hover:bg-slate-700 transition-colors"
            title="Account Settings"
            aria-label="Settings"
          >
            <Settings className="h-3.5 w-3.5" />
          </button>
        </div>
      </div>
    </aside>
  );
};

