import React from 'react';
import { Building2, ShieldAlert, Bell, Search, UserCheck } from 'lucide-react';
import { UserRole } from '../../types';

interface NavbarProps {
  currentRole: UserRole;
  onRoleChange: (role: UserRole) => void;
  onReportClick?: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  currentRole,
  onRoleChange,
  onReportClick,
}) => {
  const roles: UserRole[] = [
    'Citizen',
    'Department Staff',
    'Field Staff',
    'Supervisor',
    'Emergency Operator',
    'City Administrator',
  ];

  return (
    <header className="sticky top-0 z-40 w-full bg-slate-900 text-white border-b border-slate-800 shadow-sm">
      {/* Emergency broadcast ticker */}
      <div className="bg-red-800/90 text-white px-4 py-1 text-xs flex items-center justify-between font-medium">
        <div className="flex items-center space-x-2">
          <ShieldAlert className="h-3.5 w-3.5 text-amber-300 animate-pulse" />
          <span>MUNICIPAL ADVISORY: Scheduled water line calibration in Wards 4 & 5 between 01:00 - 05:00 UTC.</span>
        </div>
        <span className="text-[10px] bg-red-950/60 px-2 py-0.5 rounded text-red-200">OFFICIAL CITY BULLETIN</span>
      </div>

      {/* Main navigation toolbar */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-14 flex items-center justify-between">
        {/* City Identity / Logo */}
        <div className="flex items-center space-x-3">
          <div className="h-9 w-9 rounded-md bg-sky-600 flex items-center justify-center text-white shadow-sm">
            <Building2 className="h-5 w-5" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <span className="font-bold text-sm tracking-wide">SMARTCITY360</span>
              <span className="text-[10px] bg-slate-800 border border-slate-700 px-1.5 py-0.2 rounded font-mono text-slate-300">
                v1.0-PROD
              </span>
            </div>
            <p className="text-[11px] text-slate-400">Metropolitan Civic Services & Urban Operations</p>
          </div>
        </div>

        {/* Search & Actions */}
        <div className="hidden md:flex items-center flex-1 max-w-xs mx-6">
          <div className="relative w-full">
            <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-slate-400" />
            <input
              type="text"
              placeholder="Search services, permits, tickets..."
              className="w-full bg-slate-800/80 border border-slate-700 rounded-md pl-9 pr-3 py-1.5 text-xs text-white placeholder-slate-400 focus:outline-none focus:ring-1 focus:ring-sky-500 focus:border-sky-500"
            />
          </div>
        </div>

        {/* Role Switcher & User Profile Info */}
        <div className="flex items-center space-x-4">
          <div className="flex items-center space-x-1.5 bg-slate-800 border border-slate-700 px-2.5 py-1 rounded-md">
            <UserCheck className="h-3.5 w-3.5 text-sky-400" />
            <span className="text-xs text-slate-300 font-medium mr-1">Workspace:</span>
            <select
              value={currentRole}
              onChange={(e) => onRoleChange(e.target.value as UserRole)}
              className="bg-transparent text-xs font-semibold text-white focus:outline-none cursor-pointer"
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
              className="hidden sm:inline-flex items-center px-3 py-1.5 rounded text-xs font-semibold bg-sky-600 hover:bg-sky-500 text-white shadow-sm transition-colors"
            >
              Report Issue
            </button>
          )}

          <div className="relative">
            <button className="p-1.5 rounded-md text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
              <Bell className="h-4 w-4" />
            </button>
            <span className="absolute top-1 right-1 h-2 w-2 rounded-full bg-sky-500" />
          </div>
        </div>
      </div>
    </header>
  );
};
