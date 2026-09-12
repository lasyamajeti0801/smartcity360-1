import React from 'react';
import {
  LayoutDashboard,
  FileText,
  AlertCircle,
  MapPin,
  ClipboardList,
  ShieldAlert,
  Building,
  BarChart3,
  Users,
  Radio
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
  const getNavItems = () => {
    switch (currentRole) {
      case 'Citizen':
        return [
          { id: 'dashboard', label: 'Citizen Home', icon: LayoutDashboard },
          { id: 'services', label: 'Civic Services', icon: FileText },
          { id: 'complaints', label: 'My Complaints', icon: AlertCircle },
          { id: 'map', label: 'City Map & GIS', icon: MapPin },
          { id: 'emergency', label: 'Emergency Info', icon: ShieldAlert },
        ];
      case 'City Administrator':
      case 'System Administrator':
        return [
          { id: 'dashboard', label: 'City Pulse & KPIs', icon: BarChart3 },
          { id: 'departments', label: 'Departments & SLA', icon: Building },
          { id: 'complaints', label: 'All Civic Tickets', icon: AlertCircle },
          { id: 'map', label: 'City GIS Assets', icon: MapPin },
          { id: 'emergency', label: 'Emergency Center', icon: Radio },
          { id: 'users', label: 'Staff & Roles', icon: Users },
        ];
      case 'Field Staff':
      case 'Department Staff':
      case 'Supervisor':
        return [
          { id: 'workorders', label: 'Assigned Work Orders', icon: ClipboardList },
          { id: 'complaints', label: 'Department Queue', icon: AlertCircle },
          { id: 'map', label: 'Field Map', icon: MapPin },
        ];
      case 'Emergency Operator':
        return [
          { id: 'emergency', label: 'Active Incidents', icon: Radio },
          { id: 'teams', label: 'Response Units', icon: ShieldAlert },
          { id: 'map', label: 'Incident Radar', icon: MapPin },
        ];
      default:
        return [{ id: 'dashboard', label: 'Dashboard', icon: LayoutDashboard }];
    }
  };

  const navItems = getNavItems();

  return (
    <aside className="w-56 bg-slate-900 text-slate-300 border-r border-slate-800 min-h-[calc(100vh-5.5rem)] p-3 flex flex-col justify-between shrink-0">
      <div className="space-y-1">
        <div className="px-3 py-2 text-[11px] font-bold uppercase tracking-wider text-slate-400">
          {currentRole} Workspace
        </div>
        {navItems.map((item) => {
          const Icon = item.icon;
          const isActive = activeTab === item.id;
          return (
            <button
              key={item.id}
              onClick={() => onTabChange(item.id)}
              className={`w-full flex items-center space-x-2.5 px-3 py-2 rounded-md text-xs font-medium transition-colors ${
                isActive
                  ? 'bg-sky-600 text-white font-semibold shadow-sm'
                  : 'text-slate-300 hover:bg-slate-800 hover:text-white'
              }`}
            >
              <Icon className={`h-4 w-4 ${isActive ? 'text-white' : 'text-slate-400'}`} />
              <span>{item.label}</span>
            </button>
          );
        })}
      </div>

      {/* Municipal Status Footer in Sidebar */}
      <div className="p-3 bg-slate-800/60 rounded-md border border-slate-700/60 text-[11px] text-slate-400">
        <div className="flex items-center space-x-1.5 text-emerald-400 font-medium mb-1">
          <span className="h-2 w-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span>City Grid: Operational</span>
        </div>
        <p>SLA Target: 95.0%</p>
        <p>Current SLA: 94.2%</p>
      </div>
    </aside>
  );
};
