import React, { useState, useEffect } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import {
  Building2,
  Bell,
  LogOut,
  PhoneCall,
  Clock,
  ChevronDown
} from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { useCityData } from '../../context/CityDataContext';
import { useToast } from '../../context/ToastContext';

interface MunicipalNavbarProps {
  onReportClick?: () => void;
}

export const MunicipalNavbar: React.FC<MunicipalNavbarProps> = ({ onReportClick }) => {
  const { user, logout } = useAuth();
  const { notifications, markNotificationAsRead } = useCityData();
  const { info } = useToast();
  const navigate = useNavigate();

  const [time, setTime] = useState<string>('');
  const [date, setDate] = useState<string>('');
  const [isNotifOpen, setIsNotifOpen] = useState<boolean>(false);
  const [isProfileOpen, setIsProfileOpen] = useState<boolean>(false);

  useEffect(() => {
    const updateTime = () => {
      const now = new Date();
      setTime(now.toLocaleTimeString('en-IN', { hour12: true }));
      setDate(
        now.toLocaleDateString('en-IN', {
          day: '2-digit',
          month: 'short',
          year: 'numeric',
        })
      );
    };
    updateTime();
    const interval = setInterval(updateTime, 1000);
    return () => clearInterval(interval);
  }, []);

  const handleLogout = () => {
    logout();
    info('Logged out successfully', 'You have been safely signed out of SmartCity360.');
    navigate('/login');
  };

  // Filter notifications for current role
  const roleNotifs = notifications.filter(
    (n) => n.targetRole === 'ALL' || (user && n.targetRole === user.role)
  );
  const unreadCount = roleNotifs.filter((n) => !n.isRead).length;

  const getRoleBadgeStyle = () => {
    if (!user) return 'bg-purple-100 text-purple-900';
    switch (user.role) {
      case 'Admin':
        return 'bg-purple-900 text-purple-100 border border-purple-700';
      case 'Staff':
        return 'bg-purple-700 text-white font-bold border border-purple-600';
      case 'Citizen':
      default:
        return 'bg-purple-600 text-white font-bold border border-purple-500';
    }
  };

  return (
    <header className="sticky top-0 z-40 bg-[#120524] text-purple-100 border-b border-purple-900/60 shadow-md select-none">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        {/* Left: Branding & City Emblem */}
        <div className="flex items-center space-x-3.5">
          <Link
            to={user ? `/${user.role.toLowerCase()}/dashboard` : '/'}
            className="flex items-center space-x-2.5 group"
          >
            <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-purple-600 to-purple-800 border border-purple-400/40 flex items-center justify-center shadow-md transition-transform group-hover:scale-105">
              <Building2 className="w-5 h-5 text-purple-100" />
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <span className="text-base font-bold tracking-tight text-white">
                  SmartCity<span className="text-purple-400">360</span>
                </span>
                <span className="text-[10px] font-mono uppercase px-1.5 py-0.5 rounded bg-purple-900/80 text-purple-200 border border-purple-500/30 tracking-wider">
                  2026
                </span>
              </div>
              <p className="text-[10px] text-purple-300/70 tracking-wide">
                Integrated Urban Command & Civic Platform
              </p>
            </div>
          </Link>
        </div>

        {/* Center: System Clock & Operational Status */}
        <div className="hidden md:flex items-center space-x-5 text-xs text-purple-300/80">
          <div className="flex items-center space-x-1.5 bg-purple-900/40 px-3 py-1.5 rounded-full border border-purple-800/60">
            <span className="w-2 h-2 rounded-full bg-purple-400 animate-pulse" />
            <span className="text-purple-100 font-medium tracking-wide">City Grid: Operational</span>
          </div>

          <div className="flex items-center space-x-2 text-purple-200 font-mono">
            <Clock className="w-3.5 h-3.5 text-purple-400" />
            <span>{time || '12:00:00 PM'}</span>
            <span className="text-purple-400/40">•</span>
            <span>{date}</span>
          </div>
        </div>

        {/* Right: Actions, Notifications, Profile */}
        <div className="flex items-center space-x-3">
          {/* Emergency 112 quick access */}
          <Link
            to={user?.role === 'Admin' ? '/admin/emergency' : `/${user?.role.toLowerCase() || 'citizen'}/emergency`}
            className="hidden sm:flex items-center space-x-1.5 px-2.5 py-1 rounded bg-rose-500/20 hover:bg-rose-500/30 text-rose-200 border border-rose-500/40 text-xs font-semibold transition-colors"
          >
            <PhoneCall className="w-3.5 h-3.5 text-rose-400" />
            <span>112 Emergency</span>
          </Link>

          {/* Citizen Report Action */}
          {user?.role === 'Citizen' && onReportClick && (
            <button
              onClick={onReportClick}
              className="hidden lg:flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-gradient-to-r from-purple-600 to-purple-700 hover:from-purple-500 hover:to-purple-600 text-white text-xs font-semibold shadow-md border border-purple-400/30 transition-all"
            >
              <span>+ Lodge Complaint</span>
            </button>
          )}

          {/* Notifications Drawer Toggle */}
          <div className="relative">
            <button
              onClick={() => {
                setIsNotifOpen(!isNotifOpen);
                setIsProfileOpen(false);
              }}
              className="relative p-2 rounded-lg bg-purple-950/60 hover:bg-purple-900 text-purple-300 hover:text-white transition-colors border border-purple-800/60"
              aria-label="Notifications"
            >
              <Bell className="w-4 h-4" />
              {unreadCount > 0 && (
                <span className="absolute -top-1 -right-1 w-4 h-4 bg-purple-500 text-white text-[10px] font-bold rounded-full flex items-center justify-center">
                  {unreadCount}
                </span>
              )}
            </button>

            {/* Notifications Dropdown Panel */}
            {isNotifOpen && (
              <div className="absolute right-0 mt-2 w-80 sm:w-96 bg-white text-slate-900 rounded-xl shadow-2xl border border-purple-200 overflow-hidden z-50">
                <div className="px-4 py-3 bg-[#15052A] text-purple-100 flex items-center justify-between border-b border-purple-900">
                  <div className="flex items-center space-x-2">
                    <Bell className="w-4 h-4 text-purple-400" />
                    <span className="text-xs font-bold tracking-wide uppercase">Civic Alerts</span>
                  </div>
                  <span className="text-[11px] font-mono text-purple-300">
                    {unreadCount} unread
                  </span>
                </div>

                <div className="max-h-72 overflow-y-auto divide-y divide-purple-100">
                  {roleNotifs.length === 0 ? (
                    <div className="p-6 text-center text-xs text-slate-500">
                      No notifications at this time.
                    </div>
                  ) : (
                    roleNotifs.map((n) => (
                      <div
                        key={n.id}
                        onClick={() => markNotificationAsRead(n.id)}
                        className={`p-3.5 text-left transition-colors cursor-pointer hover:bg-purple-50/70 ${
                          !n.isRead ? 'bg-purple-50/50 font-medium' : ''
                        }`}
                      >
                        <div className="flex items-center justify-between text-[10px] text-slate-500">
                          <span className="font-semibold text-purple-950">{n.title}</span>
                          <span>{n.timestamp}</span>
                        </div>
                        <p className="text-xs text-slate-700 mt-1 leading-snug">{n.message}</p>
                      </div>
                    ))
                  )}
                </div>

                <div className="p-2 bg-purple-50/50 border-t border-purple-100 text-center">
                  <Link
                    to={user ? `/${user.role.toLowerCase()}/notifications` : '/'}
                    onClick={() => setIsNotifOpen(false)}
                    className="text-xs text-purple-700 hover:text-purple-900 hover:underline font-semibold"
                  >
                    View All Notifications
                  </Link>
                </div>
              </div>
            )}
          </div>

          {/* User Profile Pill & Logout */}
          {user && (
            <div className="relative">
              <button
                onClick={() => {
                  setIsProfileOpen(!isProfileOpen);
                  setIsNotifOpen(false);
                }}
                className="flex items-center space-x-2.5 pl-2 pr-3 py-1.5 rounded-lg bg-purple-950/60 hover:bg-purple-900/80 border border-purple-800/60 transition-colors"
              >
                <div className="w-7 h-7 rounded-full bg-gradient-to-br from-purple-500 to-purple-700 text-white flex items-center justify-center font-bold text-xs border border-purple-300/40">
                  {user.avatarInitials}
                </div>
                <div className="text-left hidden sm:block">
                  <p className="text-xs font-semibold text-purple-100 leading-tight truncate max-w-[120px]">
                    {user.fullName}
                  </p>
                  <p className="text-[10px] text-purple-300 truncate max-w-[120px]">
                    {user.badgeOrWard || user.role}
                  </p>
                </div>
                <ChevronDown className="w-3.5 h-3.5 text-purple-300/60" />
              </button>

              {/* Profile Dropdown */}
              {isProfileOpen && (
                <div className="absolute right-0 mt-2 w-64 bg-white text-slate-900 rounded-xl shadow-2xl border border-purple-100 overflow-hidden z-50 p-2">
                  <div className="p-3 border-b border-purple-100">
                    <p className="text-xs font-bold text-purple-950">{user.fullName}</p>
                    <p className="text-[11px] text-slate-500 font-mono mt-0.5">{user.email}</p>
                    <div className="mt-2 flex items-center gap-1.5">
                      <span className={`text-[10px] font-semibold px-2 py-0.5 rounded-full ${getRoleBadgeStyle()}`}>
                        {user.role}
                      </span>
                      <span className="text-[10px] text-slate-500">
                        {user.zone || user.subRole}
                      </span>
                    </div>
                  </div>

                  <div className="p-1 space-y-0.5">
                    <Link
                      to={`/${user.role.toLowerCase()}/profile`}
                      onClick={() => setIsProfileOpen(false)}
                      className="block px-3 py-2 text-xs text-slate-700 hover:bg-purple-50 hover:text-purple-900 rounded-lg transition-colors"
                    >
                      My Municipal Profile
                    </Link>
                    <Link
                      to={`/${user.role.toLowerCase()}/dashboard`}
                      onClick={() => setIsProfileOpen(false)}
                      className="block px-3 py-2 text-xs text-slate-700 hover:bg-purple-50 hover:text-purple-900 rounded-lg transition-colors"
                    >
                      Workspace Dashboard
                    </Link>
                  </div>

                  <div className="pt-2 border-t border-purple-100">
                    <button
                      onClick={handleLogout}
                      className="w-full flex items-center space-x-2 px-3 py-2 text-xs text-rose-600 hover:bg-rose-50 rounded-lg transition-colors"
                    >
                      <LogOut className="w-3.5 h-3.5" />
                      <span>Sign Out</span>
                    </button>
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </header>
  );
};
