import React from 'react';
import { Phone, Shield } from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer className="w-full bg-city-charcoal border-t border-city-forest text-city-concrete/80 text-xs py-5 px-4 sm:px-6 lg:px-8 mt-auto">
      <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
        {/* Left: Authority statement */}
        <div className="flex flex-col sm:flex-row items-center space-y-1 sm:space-y-0 sm:space-x-3 text-center sm:text-left">
          <div className="flex items-center space-x-2 text-city-ivory font-semibold">
            <Shield className="h-4 w-4 text-city-amber" />
            <span>SmartCity360 Municipal Corporation</span>
          </div>
          <span className="hidden sm:inline text-city-concrete/40">|</span>
          <p className="text-city-concrete/70">Integrated Urban Governance & Citizen Services Platform</p>
        </div>

        {/* Center: Emergency Help Hotline */}
        <div className="flex items-center space-x-2 text-city-danger bg-city-forest/40 px-3 py-1 rounded-full border border-city-forest">
          <Phone className="h-3.5 w-3.5 animate-pulse" />
          <span className="font-semibold tracking-wide">Emergency Services: 112 | Civic Toll-Free: 1800-360-CITY</span>
        </div>

        {/* Right: Policies & Accessibility */}
        <div className="flex items-center space-x-4 text-city-concrete/70">
          <span className="hover:text-city-ivory transition-colors cursor-pointer">Citizen Charter</span>
          <span className="hover:text-city-ivory transition-colors cursor-pointer">Accessibility (WCAG 2.1 AA)</span>
          <span className="hover:text-city-ivory transition-colors cursor-pointer">Open Data API</span>
        </div>
      </div>
    </footer>
  );
};

