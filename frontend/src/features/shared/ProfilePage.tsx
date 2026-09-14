import React from 'react';
import {
  ShieldCheck,
  Mail,
  Phone,
  MapPin,
  CheckCircle2
} from 'lucide-react';
import { useAuth } from '../../context/AuthContext';

export const ProfilePage: React.FC = () => {
  const { user } = useAuth();

  if (!user) return null;

  return (
    <div className="space-y-6 select-none font-sans max-w-4xl mx-auto">
      {/* Header */}
      <div className="bg-white p-5 rounded-xl border border-surface-border shadow-civic flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-city-forest">
            Municipal Identity & Service Profile
          </h1>
          <p className="text-xs text-city-charcoal/70 mt-0.5">
            Verified identity records maintained under SmartCity360 Public Directory Protocol.
          </p>
        </div>

        <div className="flex items-center space-x-1.5 px-3 py-1 rounded-full bg-city-sand/30 text-city-forest text-xs font-bold border border-city-sand">
          <CheckCircle2 className="w-4 h-4 text-city-amber" />
          <span>VERIFIED & AUDITED</span>
        </div>
      </div>

      {/* Main Identity Card */}
      <div className="bg-white rounded-2xl border border-surface-border shadow-civic overflow-hidden">
        <div className="p-6 bg-gradient-to-r from-[#1F0A38] via-[#38125E] to-[#18082B] text-white flex flex-col sm:flex-row items-center sm:items-start space-y-4 sm:space-y-0 sm:space-x-5">
          <div className="w-20 h-20 rounded-2xl bg-purple-700 text-white flex items-center justify-center font-extrabold text-2xl border-2 border-purple-300 shadow-civic">
            {user.avatarInitials}
          </div>

          <div className="text-center sm:text-left space-y-1">
            <div className="flex flex-col sm:flex-row sm:items-center gap-2">
              <h2 className="text-2xl font-bold">{user.fullName}</h2>
              <span className="text-xs font-mono font-bold px-2.5 py-0.5 rounded-full bg-city-sand text-city-charcoal">
                {user.role}
              </span>
            </div>
            <p className="text-xs text-city-sand font-mono">{user.badgeOrWard} • {user.zone}</p>
            <p className="text-xs text-city-concrete/90">{user.subRole}</p>
          </div>
        </div>

        <div className="p-6 grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
          <div className="p-3.5 rounded-xl bg-surface-card border border-surface-border space-y-1">
            <span className="text-city-charcoal/60 block flex items-center space-x-1.5">
              <Mail className="w-3.5 h-3.5 text-city-terracotta" />
              <span>Registered Email</span>
            </span>
            <p className="font-semibold text-city-forest font-mono">{user.email}</p>
          </div>

          <div className="p-3.5 rounded-xl bg-surface-card border border-surface-border space-y-1">
            <span className="text-city-charcoal/60 block flex items-center space-x-1.5">
              <Phone className="w-3.5 h-3.5 text-city-terracotta" />
              <span>Contact Phone</span>
            </span>
            <p className="font-semibold text-city-forest font-mono">{user.phone || '+91 98765 00000'}</p>
          </div>

          <div className="p-3.5 rounded-xl bg-surface-card border border-surface-border space-y-1">
            <span className="text-city-charcoal/60 block flex items-center space-x-1.5">
              <MapPin className="w-3.5 h-3.5 text-city-terracotta" />
              <span>Municipal Jurisdiction</span>
            </span>
            <p className="font-semibold text-city-forest">{user.zone || 'Central Municipal Zone'}</p>
          </div>

          <div className="p-3.5 rounded-xl bg-surface-card border border-surface-border space-y-1">
            <span className="text-city-charcoal/60 block flex items-center space-x-1.5">
              <ShieldCheck className="w-3.5 h-3.5 text-city-amber" />
              <span>Security Clearance</span>
            </span>
            <p className="font-semibold text-city-forest">
              {user.role === 'Admin' ? 'Level 4 (City Administrator)' : user.role === 'Staff' ? 'Level 2 (Field Operations)' : 'Level 1 (Verified Resident)'}
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};
