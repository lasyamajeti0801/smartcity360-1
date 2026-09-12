import React, { useState, useEffect } from 'react';
import {
  Building2,
  Bell,
  Search,
  UserCheck,
  Radio,
  X
} from 'lucide-react';
import { UserRole } from '../../types';

interface NavbarProps {
  currentRole: UserRole;
  onRoleChange: (role: UserRole) => void;
  onReportClick?: () => void;
  activeTab?: string;
}

export const Navbar: React.FC<NavbarProps> = ({
  currentRole,
  onRoleChange,
  onReportClick,
  activeTab = 'dashboard',
}) => {
  const [time, setTime] = useState<string>('');
  const [date, setDate] = useState<string>('');
  const [isNotificationOpen, setIsNotificationOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [unreadCount, setUnreadCount] = useState(3);

  const notifications = [
    {
      id: 1,
      title: 'Water Line Maintenance Alert',
      desc: 'Scheduled pressure calibration in Wards 4 & 5 starting 01:00 UTC.',
      time: '4 mins ago',
      type: 'warning',
      read: false,
    },
    {
      id: 2,
      title: 'Emergency Unit Dispatched',
      desc: 'Unit Medic-14 assigned to incident on Mahatma Gandhi Rd.',
      time: '18 mins ago',
      type: 'emergency',
      read: false,
    },
    {
      id: 3,
      title: 'SLA Milestone Achieved',
      desc: 'Roads & Works cleared 14 pending pothole complaints today.',
      time: '42 mins ago',
      type: 'success',
      read: false,
    },
    {
      id: 4,
      title: 'Civic Feedback Published',
      desc: '98% citizen satisfaction score recorded for North Zone waste clearance.',
      time: '2 hours ago',
      type: 'info',
      read: true,
    },
  ];

  useEffect(() => {
    const updateDateTime = () => {
      const now = new Date();
      setTime(now.toLocaleTimeString('en-GB', { hour12: false }));
      setDate(
        now.toLocaleDateString('en-GB', {
          day: '2-digit',
          month: 'short',
          year: 'numeric',
        })
      );
    };
    updateDateTime();
    const interval = setInterval(updateDateTime, 1000);
    return () => clearInterval(interval);
  }, []);

  const roles: UserRole[] = [
    'Citizen',
    'Department Staff',
    'Field Staff',
    'Supervisor',
    'Emergency Operator',
    'City Administrator',
  ];

  const getBreadcrumb = () => {
    switch (activeTab) {
      case 'dashboard':
        return 'City Operations / Overview';
      case 'citizens':
        return 'Citizen Registry / Demographics';
      case 'complaints':
        return 'Civic Affairs / Complaint Management';
      case 'services':
        return 'Civic Catalog / Service Applications';
      case 'emergency':
        return 'Emergency 911 / Tactical Command';
      case 'traffic':
        return 'Urban Mobility / Traffic & Transit';
      case 'waste':
        return 'Sanitation / Smart Waste Management';
      case 'water':
        return 'Utilities / Municipal Water SCADA';
      case 'map':
        return 'GIS Spatial Intelligence / City Assets';
      case 'reports':
        return 'Executive Analytics / SLA Performance';
      case 'notifications':
        return 'Communications / Municipal Bulletins';
      case 'settings':
        return 'Administration / System Settings';
      default:
        return 'City Operations / Overview';
    }
  };

  return (
    <header className="sticky top-0 z-40 w-full bg-slate-900 text-white border-b border-slate-800 shadow-md">
      {/* Official Municipal Advisory Bulletin */}
      <div className="bg-slate-950 text-slate-300 px-4 py-1 text-[11px] flex items-center justify-between border-b border-slate-800/80">
        <div className="flex items-center space-x-2 overflow-hidden text-ellipsis whitespace-nowrap">
          <span className="inline-flex items-center px-1.5 py-0.5 rounded text-[9px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">
            CITY ADVISORY
          </span>
          <span className="text-slate-300 font-medium">
            SmartCity360 Municipal Infrastructure Sensor Network: All 26 jurisdictional domains operating within standard statutory limits.
          </span>
        </div>
        <div className="hidden sm:flex items-center space-x-3 text-[10px] text-slate-400 shrink-0">
          <span className="flex items-center space-x-1">
            <Radio className="h-3 w-3 text-emerald-400" />
            <span>Telemetry: 120 Nodes Active</span>
          </span>
          <span className="text-slate-600">|</span>
          <span>Security Level: Alpha-1 (Normal)</span>
        </div>
      </div>

      {/* Primary Navigation Toolbar */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-14 flex items-center justify-between gap-4">
        {/* Branding & Logo */}
        <div className="flex items-center space-x-3 shrink-0">
          <div className="h-9 w-9 rounded-md bg-teal-700 flex items-center justify-center text-white shadow-sm border border-teal-600">
            <Building2 className="h-5 w-5" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <span className="font-bold text-sm tracking-wider text-white">SMART CITY 360</span>
              <span className="text-[9px] bg-teal-950 border border-teal-800/80 px-1.5 py-0.2 rounded font-mono text-teal-300 font-semibold">
                GOV-PROD
              </span>
            </div>
            <p className="text-[10px] text-slate-400 font-medium leading-none mt-0.5">
              One Platform. A Smarter City.
            </p>
          </div>
        </div>

        {/* Breadcrumb / Section Context */}
        <div className="hidden lg:flex items-center space-x-2 text-xs text-slate-400 pl-4 border-l border-slate-800">
          <span className="text-slate-300 font-medium">{getBreadcrumb()}</span>
        </div>

        {/* Global Search Bar */}
        <div className="hidden md:flex items-center flex-1 max-w-sm mx-4">
          <div className="relative w-full">
            <Search className="absolute left-3 top-2.5 h-3.5 w-3.5 text-slate-400" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search complaints, permits, ward records..."
              className="w-full bg-slate-800/90 border border-slate-700/80 rounded-md pl-9 pr-3 py-1.5 text-xs text-white placeholder-slate-400 focus:outline-none focus:ring-1 focus:ring-teal-500 focus:border-teal-500 transition-colors"
            />
          </div>
        </div>

        {/* Live System Indicator & Clock */}
        <div className="hidden xl:flex items-center space-x-3 text-right">
          <div className="flex items-center space-x-1.5 px-2 py-1 rounded bg-slate-800/60 border border-slate-700/60">
            <span className="relative flex h-2 w-2">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
            </span>
            <span className="text-[11px] font-semibold text-emerald-400 tracking-tight">LIVE</span>
          </div>
          <div className="text-[11px] leading-tight">
            <div className="font-mono font-bold text-slate-200">{time || '12:00:00'}</div>
            <div className="text-[10px] text-slate-400">{date || '12 Sep 2026'}</div>
          </div>
        </div>

        {/* Actions, Notifications & Workspace Selector */}
        <div className="flex items-center space-x-3 shrink-0">
          {/* Workspace Switcher */}
          <div className="flex items-center space-x-1.5 bg-slate-800 border border-slate-700 px-2.5 py-1 rounded-md">
            <UserCheck className="h-3.5 w-3.5 text-teal-400" />
            <span className="text-[11px] text-slate-400 font-medium hidden sm:inline">Role:</span>
            <select
              value={currentRole}
              onChange={(e) => onRoleChange(e.target.value as UserRole)}
              className="bg-transparent text-xs font-semibold text-white focus:outline-none cursor-pointer pr-1"
              aria-label="Select User Role"
            >
              {roles.map((r) => (
                <option key={r} value={r} className="bg-slate-900 text-white">
                  {r}
                </option>
              ))}
            </select>
          </div>

          {currentRole === 'Citizen' && onReportClick && (
            <button
              onClick={onReportClick}
              className="inline-flex items-center px-3 py-1.5 rounded text-xs font-semibold bg-teal-600 hover:bg-teal-500 text-white shadow-sm transition-colors"
            >
              Report Issue
            </button>
          )}

          {/* Notification Button & Drawer */}
          <div className="relative">
            <button
              onClick={() => setIsNotificationOpen(!isNotificationOpen)}
              className="relative p-2 rounded-md text-slate-400 hover:text-white hover:bg-slate-800 transition-colors focus:outline-none"
              aria-label="Toggle notifications"
            >
              <Bell className="h-4 w-4" />
              {unreadCount > 0 && (
                <span className="absolute top-1 right-1 h-2 w-2 rounded-full bg-teal-400 animate-pulse" />
              )}
            </button>

            {isNotificationOpen && (
              <div className="absolute right-0 mt-2 w-80 sm:w-96 bg-white rounded-lg shadow-xl border border-slate-200 text-slate-900 z-50 overflow-hidden">
                <div className="px-4 py-3 bg-slate-900 text-white flex items-center justify-between">
                  <div className="flex items-center space-x-2">
                    <Bell className="h-4 w-4 text-teal-400" />
                    <span className="text-xs font-bold uppercase tracking-wider">City Notifications</span>
                    <span className="text-[10px] bg-teal-500/20 text-teal-300 px-1.5 py-0.5 rounded font-bold">
                      {unreadCount} New
                    </span>
                  </div>
                  <button
                    onClick={() => setIsNotificationOpen(false)}
                    className="text-slate-400 hover:text-white"
                  >
                    <X className="h-4 w-4" />
                  </button>
                </div>

                <div className="max-h-80 overflow-y-auto divide-y divide-slate-100">
                  {notifications.map((n) => (
                    <div
                      key={n.id}
                      className={`p-3.5 hover:bg-slate-50 transition-colors ${
                        !n.read ? 'bg-teal-50/40' : ''
                      }`}
                    >
                      <div className="flex items-start justify-between gap-2">
                        <h4 className="text-xs font-semibold text-slate-900">{n.title}</h4>
                        <span className="text-[10px] text-slate-400 whitespace-nowrap">{n.time}</span>
                      </div>
                      <p className="text-xs text-slate-600 mt-1">{n.desc}</p>
                    </div>
                  ))}
                </div>

                <div className="p-2.5 bg-slate-50 border-t border-slate-100 flex items-center justify-between text-xs">
                  <button
                    onClick={() => setUnreadCount(0)}
                    className="text-teal-700 font-medium hover:underline"
                  >
                    Mark all as read
                  </button>
                  <span className="text-slate-400 text-[11px]">Auto-refreshes live</span>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </header>
  );
};

