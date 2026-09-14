import React from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import {
  LayoutDashboard,
  AlertCircle,
  FileText,
  Building,
  Radio,
  Car,
  Trash2,
  Droplets,
  BarChart3,
  Bell,
  Settings,
  ShieldAlert,
  CreditCard,
  MapPin,
  ClipboardList,
  Users,
  HardHat,
  ChevronRight,
  ShieldCheck,
  Building2,
  Activity,
  PlusCircle,
  UserCheck
} from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { PrimaryRole } from '../../types';

interface SidebarItem {
  to: string;
  label: string;
  icon: React.ComponentType<{ className?: string }>;
  badge?: string | number;
}

export const MunicipalSidebar: React.FC = () => {
  const { user } = useAuth();
  const location = useLocation();

  if (!user) return null;

  const role: PrimaryRole = user.role;

  // Citizen Navigation Catalog
  const citizenItems: SidebarItem[] = [
    { to: '/citizen/dashboard', label: 'Civic Overview', icon: LayoutDashboard },
    { to: '/citizen/my-requests', label: 'My Requests', icon: AlertCircle },
    { to: '/citizen/report', label: 'Report Issue', icon: PlusCircle },
    { to: '/citizen/services', label: 'Municipal Services', icon: FileText },
    { to: '/citizen/map', label: 'Nearby Facilities & GIS', icon: MapPin },
    { to: '/citizen/payments', label: 'Payments & Receipts', icon: CreditCard },
    { to: '/citizen/notifications', label: 'Civic Alerts', icon: Bell },
    { to: '/citizen/emergency', label: 'Emergency 112', icon: ShieldAlert },
    { to: '/citizen/profile', label: 'Citizen Profile', icon: UserCheck },
  ];

  // Field Staff Navigation Catalog
  const staffItems: SidebarItem[] = [
    { to: '/staff/dashboard', label: 'Operations Desk', icon: LayoutDashboard },
    { to: '/staff/work-orders', label: 'My Work Orders', icon: ClipboardList },
    { to: '/staff/map', label: 'Field Route & GIS', icon: MapPin },
    { to: '/staff/department', label: 'Department Metrics', icon: Building },
    { to: '/staff/emergency-alerts', label: 'Emergency Alerts', icon: ShieldAlert },
    { to: '/staff/reports', label: 'Field Progress Logs', icon: BarChart3 },
    { to: '/staff/notifications', label: 'Dispatch Alerts', icon: Bell },
    { to: '/staff/profile', label: 'Staff Identity', icon: UserCheck },
  ];

  // Admin Command Centre Navigation Catalog
  const adminItems: SidebarItem[] = [
    { to: '/admin/dashboard', label: 'Command Centre', icon: Activity },
    { to: '/admin/requests', label: 'Civic Grievances', icon: AlertCircle },
    { to: '/admin/work-orders', label: 'Work Orders Oversight', icon: ClipboardList },
    { to: '/admin/departments', label: 'Municipal Departments', icon: Building2 },
    { to: '/admin/staff', label: 'Workforce & Teams', icon: HardHat },
    { to: '/admin/citizens', label: 'Citizens Registry', icon: Users },
    { to: '/admin/map', label: 'Full City GIS Radar', icon: MapPin },
    { to: '/admin/emergency', label: 'Tactical Emergency (112)', icon: Radio },
    { to: '/admin/traffic', label: 'Traffic & Urban Transit', icon: Car },
    { to: '/admin/water', label: 'Water Utilities Grid', icon: Droplets },
    { to: '/admin/waste', label: 'Solid Waste Systems', icon: Trash2 },
    { to: '/admin/analytics', label: 'Executive Analytics', icon: BarChart3 },
    { to: '/admin/settings', label: 'System Configuration', icon: Settings },
    { to: '/admin/audit-logs', label: 'Audit Trail & Logs', icon: ShieldCheck },
  ];

  let items: SidebarItem[] = citizenItems;
  if (role === 'Staff') items = staffItems;
  if (role === 'Admin') items = adminItems;

  return (
    <aside
      className="w-64 bg-[#120524] text-purple-200 border-r border-purple-900/60 min-h-[calc(100vh-4rem)] p-3 flex flex-col justify-between shrink-0 select-none shadow-xl"
      aria-label="Municipal Sidebar Navigation"
    >
      <div className="space-y-4">
        {/* Role Workspace Identifier */}
        <div className="px-3 pt-2 pb-2 border-b border-purple-900/60 flex items-center justify-between">
          <div className="flex flex-col">
            <span className="text-[10px] font-bold uppercase tracking-wider text-purple-400">
              {role === 'Admin' ? 'Governance Desk' : role === 'Staff' ? 'Operations Desk' : 'Citizen Portal'}
            </span>
            <span className="text-xs font-semibold text-purple-100 mt-0.5">
              {user.zone || user.badgeOrWard}
            </span>
          </div>
          <span className="text-[10px] bg-purple-900/80 text-purple-200 border border-purple-500/30 px-2 py-0.5 rounded font-mono font-bold">
            {role.toUpperCase()}
          </span>
        </div>

        {/* Navigation Items */}
        <nav className="space-y-1">
          {items.map((item) => {
            const Icon = item.icon;
            const isActive = location.pathname === item.to || location.pathname.startsWith(`${item.to}/`);

            return (
              <NavLink
                key={item.to}
                to={item.to}
                className={`w-full flex items-center justify-between px-3 py-2.5 rounded-lg text-xs font-medium transition-all group ${
                  isActive
                    ? 'bg-gradient-to-r from-purple-600 to-purple-700 text-white font-bold shadow-md border border-purple-400/40'
                    : 'text-purple-200/80 hover:bg-purple-900/50 hover:text-white'
                }`}
              >
                <div className="flex items-center space-x-2.5 min-w-0">
                  <Icon
                    className={`h-4 w-4 shrink-0 transition-colors ${
                      isActive ? 'text-white' : 'text-purple-400 group-hover:text-purple-200'
                    }`}
                  />
                  <span className="truncate">{item.label}</span>
                </div>

                {item.badge ? (
                  <span className="text-[10px] font-mono px-1.5 py-0.2 rounded bg-purple-500 text-white font-bold">
                    {item.badge}
                  </span>
                ) : isActive ? (
                  <ChevronRight className="h-3.5 w-3.5 text-purple-200" />
                ) : null}
              </NavLink>
            );
          })}
        </nav>
      </div>

      {/* Municipal Security & SLA Transparency Pill */}
      <div className="p-3 mt-4 bg-purple-950/60 border border-purple-900/80 rounded-lg text-[11px] text-purple-300">
        <div className="flex items-center space-x-1.5 text-purple-200 font-semibold">
          <ShieldCheck className="w-3.5 h-3.5 text-purple-400" />
          <span>Municipal Service Guarantee</span>
        </div>
        <p className="mt-1 text-[10px] leading-tight text-purple-300/80">
          Complaints governed under the Public Services Guarantee Act (Karnataka SAKALA standard).
        </p>
      </div>
    </aside>
  );
};
