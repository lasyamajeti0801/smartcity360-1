import React from 'react';
import { Phone, Shield } from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer className="w-full bg-slate-900 border-t border-slate-800 text-slate-400 text-xs py-6 px-4 sm:px-6 lg:px-8 mt-auto">
      <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
        {/* Left: Authority statement */}
        <div className="flex flex-col sm:flex-row items-center space-y-1 sm:space-y-0 sm:space-x-3 text-center sm:text-left">
          <div className="flex items-center space-x-1.5 text-slate-300 font-semibold">
            <Shield className="h-4 w-4 text-sky-400" />
            <span>SmartCity360 Unified Municipal Operations</span>
          </div>
          <span className="hidden sm:inline text-slate-600">|</span>
          <p>Official Public Digital Services System</p>
        </div>

        {/* Center: Emergency Help Hotline */}
        <div className="flex items-center space-x-2 text-red-400 font-medium">
          <Phone className="h-4 w-4" />
          <span>Emergency Hotline: 911 / 112 | Civic Control Desk: 311</span>
        </div>

        {/* Right: Policies & Accessibility */}
        <div className="flex items-center space-x-4 text-slate-400">
          <span className="hover:text-slate-200 cursor-pointer">Privacy Notice</span>
          <span className="hover:text-slate-200 cursor-pointer">Accessibility (WCAG 2.1)</span>
          <span className="hover:text-slate-200 cursor-pointer">Open Data</span>
        </div>
      </div>
    </footer>
  );
};
