import React from 'react';
import { Link } from 'react-router-dom';
import {
  Building2,
  PhoneCall,
  ArrowRight,
  Droplets,
  Zap,
  Bus,
  Trash2,
  Radio,
  Hammer,
  Lightbulb,
  FileText,
  ChevronRight,
  TreePine,
  HeartPulse
} from 'lucide-react';
import { Footer } from '../../components/layout/Footer';

export const LandingPage: React.FC = () => {
  const citySystems = [
    { name: 'Drinking Water Supply', metric: '48.2 MLD Flow Rate', status: 'Optimal', icon: Droplets, color: 'text-city-green' },
    { name: 'Public Power & Lighting', metric: '99.4% Grid Reliability', status: 'Stable', icon: Zap, color: 'text-city-amber' },
    { name: 'Urban Bus Transit', metric: '142 Active Corridors', status: 'On Schedule', icon: Bus, color: 'text-city-leaf' },
    { name: 'Solid Waste Collection', metric: '94% Wards Cleared Today', status: 'Active', icon: Trash2, color: 'text-city-terracotta' },
    { name: 'Emergency 112 Command', metric: '4.2 Min Avg Dispatch', status: 'Standby', icon: Radio, color: 'text-city-danger' },
  ];

  const civicServices = [
    { title: 'Pothole & Asphalt Repair', dept: 'Roads & Infrastructure', sla: '48h SLA', icon: Hammer, desc: 'GPS-pinned crater remediation, road leveling, and asphalt resurfacing.' },
    { title: 'Community Waste Disposal', dept: 'Solid Waste & Sanitation', sla: '24h SLA', icon: Trash2, desc: 'Door-to-door bin clearance, e-waste pickup, and neighborhood cleaning.' },
    { title: 'Drinking Water Pipeline', dept: 'Water Supply Board', sla: '24h SLA', icon: Droplets, desc: 'Pipeline rupture repair, valve inspection, and new domestic connections.' },
    { title: 'Streetlight & Dark Corridors', dept: 'Public Lighting Utility', sla: '36h SLA', icon: Lightbulb, desc: 'LED module replacement, luminaire fixes, and smart pole automation.' },
    { title: 'Traffic Signals & Mobility', dept: 'Urban Transit Authority', sla: '12h SLA', icon: Bus, desc: 'Intersectional signal calibration, congestion alerts, and lane safety.' },
    { title: 'Civic Permits & Licenses', dept: 'Municipal Corporation', sla: '7-10 Days', icon: FileText, desc: 'Building completion certificates, road-cutting permits, and trade registrations.' },
    { title: 'Public Health & Trauma', dept: 'Municipal Health Services', sla: '24/7 Live', icon: HeartPulse, desc: 'Ward clinics, vector control spraying, and hospital facility directory.' },
    { title: 'Parks & Green Spaces', dept: 'Horticulture & Ecology', sla: '48h SLA', icon: TreePine, desc: 'Urban canopy maintenance, fallen tree clearance, and public gardens.' },
  ];

  return (
    <div className="min-h-screen bg-city-ivory text-city-charcoal flex flex-col font-sans selection:bg-city-sage selection:text-city-forest">
      {/* Top Municipal Navigation Bar */}
      <header className="sticky top-0 z-50 bg-[#120524]/95 backdrop-blur-md text-purple-100 border-b border-purple-900/60 shadow-md">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-18 flex items-center justify-between">
          {/* Logo & Emblem */}
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-purple-600 to-purple-800 border border-purple-400/40 flex items-center justify-center shadow-md">
              <Building2 className="w-5 h-5 text-purple-100" />
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <span className="text-lg font-extrabold tracking-tight text-white">
                  SmartCity<span className="text-purple-400">360</span>
                </span>
                <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-purple-900/80 text-purple-200 border border-purple-500/30 uppercase tracking-widest font-semibold">
                  MUNICIPAL
                </span>
              </div>
              <p className="text-[11px] text-purple-300/80 leading-none mt-0.5">
                Integrated Urban Management & Citizen Services Platform
              </p>
            </div>
          </div>

          {/* Quick Jump Links */}
          <nav className="hidden md:flex items-center space-x-6 text-xs text-purple-200 font-medium">
            <a href="#services" className="hover:text-white transition-colors">Civic Services</a>
            <a href="#pulse" className="hover:text-white transition-colors">City Status</a>
            <a href="#workflow" className="hover:text-white transition-colors">How It Connects</a>
            <a href="#governance" className="hover:text-white transition-colors">Citizen Charter</a>
          </nav>

          {/* Action CTAs */}
          <div className="flex items-center space-x-3">
            <a
              href="tel:112"
              className="hidden sm:flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-rose-500/20 text-rose-200 border border-rose-500/40 text-xs font-semibold hover:bg-rose-500/30 transition-colors"
            >
              <PhoneCall className="w-3.5 h-3.5 text-rose-400" />
              <span>112 Emergency</span>
            </a>

            <Link
              to="/login"
              className="flex items-center space-x-2 px-4 py-2 rounded-lg bg-gradient-to-r from-purple-600 to-purple-700 hover:from-purple-500 hover:to-purple-600 text-white text-xs font-semibold shadow-md border border-purple-400/30 transition-all transform hover:-translate-y-0.5"
            >
              <span>Access Portal</span>
              <ArrowRight className="w-3.5 h-3.5 text-purple-200" />
            </Link>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="relative pt-16 pb-20 overflow-hidden bg-gradient-to-b from-[#1F0A38] via-[#160728] to-[#0D0418] text-white border-b border-[#3D146D]">
        {/* Subtle SVG Indian Urban Grid Blueprint Motif */}
        <div className="absolute inset-0 opacity-15 pointer-events-none">
          <svg className="w-full h-full" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <pattern id="grid" width="48" height="48" patternUnits="userSpaceOnUse">
                <path d="M 48 0 L 0 0 0 48" fill="none" stroke="#C084FC" strokeWidth="0.75" />
              </pattern>
            </defs>
            <rect width="100%" height="100%" fill="url(#grid)" />
          </svg>
        </div>

        <div className="relative max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="space-y-6">
            <div className="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-purple-950/70 border border-purple-500/40 text-xs font-medium text-purple-200 shadow-inner">
              <span className="w-2 h-2 rounded-full bg-purple-400 animate-pulse" />
              <span>One City. One Connected Platform.</span>
            </div>

            <h1 className="text-4xl sm:text-6xl font-extrabold tracking-tight text-white leading-[1.15]">
              One Connected City. <br />
              <span className="text-purple-300">Better Every Day.</span>
            </h1>

            <p className="text-base sm:text-lg text-purple-100/80 max-w-2xl mx-auto font-normal leading-relaxed">
              SmartCity360 connects citizens, municipal field crews, utility engineers, and urban administrators into a single unified digital nervous system. Real-time accountability, GPS dispatch, and transparent service-level guarantees.
            </p>

            {/* Action Buttons */}
            <div className="pt-2 flex flex-col sm:flex-row items-center justify-center gap-4">
              <Link
                to="/login"
                className="w-full sm:w-auto flex items-center justify-center space-x-2.5 px-7 py-3.5 rounded-lg bg-purple-600 hover:bg-purple-500 text-white text-sm font-semibold shadow-lg shadow-purple-950/50 border border-purple-400/40 transition-all transform hover:-translate-y-0.5"
              >
                <span>Enter Smart City Portal</span>
                <ArrowRight className="w-4 h-4 text-purple-200" />
              </Link>

              <a
                href="#services"
                className="w-full sm:w-auto flex items-center justify-center space-x-2 px-7 py-3.5 rounded-lg bg-purple-950/60 hover:bg-purple-900/70 text-purple-200 hover:text-white text-sm font-medium border border-purple-500/30 transition-colors"
              >
                <span>Explore 26 Civic Services</span>
              </a>
            </div>

            {/* Citizen Guarantee Badges */}
            <div className="pt-6 max-w-xl mx-auto grid grid-cols-3 gap-6 border-t border-purple-900/60 text-center">
              <div>
                <p className="text-2xl font-bold font-mono text-purple-300">100%</p>
                <p className="text-xs text-purple-200/70 mt-0.5">Verified Public Audits</p>
              </div>
              <div>
                <p className="text-2xl font-bold font-mono text-purple-300">&lt; 24h</p>
                <p className="text-xs text-purple-200/70 mt-0.5">Average Triage SLA</p>
              </div>
              <div>
                <p className="text-2xl font-bold font-mono text-purple-300">112</p>
                <p className="text-xs text-purple-200/70 mt-0.5">Unified Emergency Line</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* City Status Strip */}
      <section id="pulse" className="bg-city-charcoal text-city-ivory py-4 border-b border-city-forest shadow-inner">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col md:flex-row items-center justify-between gap-4">
            <div className="flex items-center space-x-2.5 shrink-0">
              <div className="flex items-center space-x-1.5 px-2.5 py-1 rounded-full bg-city-forest text-city-sand border border-city-leaf/30 text-xs font-bold">
                <span className="w-2 h-2 rounded-full bg-city-leaf animate-ping" />
                <span>CITY STATUS</span>
              </div>
              <span className="text-xs text-city-concrete">● All municipal core grids operational</span>
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-5 gap-3 w-full md:w-auto">
              {citySystems.map((s, idx) => {
                const Icon = s.icon;
                return (
                  <div key={idx} className="flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-city-forest/40 border border-city-forest text-xs">
                    <Icon className={`w-3.5 h-3.5 ${s.color}`} />
                    <div className="min-w-0">
                      <p className="text-[10px] text-city-concrete/70 truncate">{s.name}</p>
                      <p className="font-mono text-[11px] font-semibold text-city-ivory">{s.status}</p>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      </section>

      {/* How SmartCity360 Connects the City Workflow */}
      <section id="workflow" className="py-16 bg-[#FAF7FD] border-b border-purple-200/60">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-3xl mx-auto space-y-3">
            <p className="text-xs font-bold font-mono tracking-wider text-city-terracotta uppercase">
              Interconnected Municipal Governance
            </p>
            <h2 className="text-3xl font-extrabold text-city-forest">
              How SmartCity360 Connects Your City
            </h2>
            <p className="text-sm text-city-charcoal/80">
              From an everyday pothole reported on a smartphone to real-time administrative oversight and completed field repairs.
            </p>
          </div>

          {/* Workflow Chain */}
          <div className="mt-12 grid grid-cols-1 md:grid-cols-5 gap-4 relative">
            {/* Step 1 */}
            <div className="bg-white p-5 rounded-xl border border-surface-border shadow-civic space-y-3 text-center hover:border-city-terracotta transition-colors">
              <div className="w-12 h-12 mx-auto rounded-full bg-city-terracotta/15 text-city-terracotta border border-city-terracotta/30 flex items-center justify-center font-bold text-sm">
                1
              </div>
              <p className="text-xs font-mono font-bold text-city-terracotta uppercase">Citizen Report</p>
              <h3 className="text-sm font-bold text-city-forest">Lodge with Map Pin</h3>
              <p className="text-xs text-city-charcoal/70 leading-relaxed">
                Citizen pins GPS location, uploads evidence photos, and receives SAKALA tracked ticket #.
              </p>
            </div>

            {/* Step 2 */}
            <div className="bg-white p-5 rounded-xl border border-surface-border shadow-civic space-y-3 text-center hover:border-city-amber transition-colors">
              <div className="w-12 h-12 mx-auto rounded-full bg-city-amber/20 text-city-amber border border-city-amber/40 flex items-center justify-center font-bold text-sm">
                2
              </div>
              <p className="text-xs font-mono font-bold text-city-amber uppercase">SmartCity360</p>
              <h3 className="text-sm font-bold text-city-forest">Auto Triage & SLA</h3>
              <p className="text-xs text-city-charcoal/70 leading-relaxed">
                System routes ticket to the appropriate department (Roads, Water, Waste) and sets SLA timer.
              </p>
            </div>

            {/* Step 3 */}
            <div className="bg-white p-5 rounded-xl border border-surface-border shadow-civic space-y-3 text-center hover:border-city-forest transition-colors">
              <div className="w-12 h-12 mx-auto rounded-full bg-city-forest/20 text-city-forest border border-city-forest/30 flex items-center justify-center font-bold text-sm">
                3
              </div>
              <p className="text-xs font-mono font-bold text-city-forest uppercase">Field Operations</p>
              <h3 className="text-sm font-bold text-city-forest">Staff Work Order</h3>
              <p className="text-xs text-city-charcoal/70 leading-relaxed">
                Technician accepts job on field tablet, reviews safety checklist, and updates status en-route.
              </p>
            </div>

            {/* Step 4 */}
            <div className="bg-white p-5 rounded-xl border border-surface-border shadow-civic space-y-3 text-center hover:border-city-terracotta transition-colors">
              <div className="w-12 h-12 mx-auto rounded-full bg-city-terracotta/15 text-city-terracotta border border-city-terracotta/30 flex items-center justify-center font-bold text-sm">
                4
              </div>
              <p className="text-xs font-mono font-bold text-city-terracotta uppercase">Remediation</p>
              <h3 className="text-sm font-bold text-city-forest">Checklist & Evidence</h3>
              <p className="text-xs text-city-charcoal/70 leading-relaxed">
                Crews execute repair, complete procedural verification, and capture photographic completion proof.
              </p>
            </div>

            {/* Step 5 */}
            <div className="bg-white p-5 rounded-xl border border-surface-border shadow-civic space-y-3 text-center hover:border-city-amber transition-colors">
              <div className="w-12 h-12 mx-auto rounded-full bg-city-amber/20 text-city-amber border border-city-amber/40 flex items-center justify-center font-bold text-sm">
                5
              </div>
              <p className="text-xs font-mono font-bold text-city-amber uppercase">Citizen Feedback</p>
              <h3 className="text-sm font-bold text-city-forest">Audit & Star Rating</h3>
              <p className="text-xs text-city-charcoal/70 leading-relaxed">
                Citizen receives resolution alert, rates satisfaction, and data feeds into City Admin scorecards.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Civic Services Directory Showcase */}
      <section id="services" className="py-16 bg-city-ivory">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-4 mb-12">
            <div>
              <p className="text-xs font-bold font-mono tracking-wider text-city-terracotta uppercase">
                Public Service Directory
              </p>
              <h2 className="text-3xl font-extrabold text-city-forest mt-1">
                Essential Municipal Services
              </h2>
              <p className="text-sm text-city-charcoal/80 mt-1 max-w-xl">
                Submit grievances, apply for official certificates, and track government department performance with zero bureaucracy.
              </p>
            </div>

            <Link
              to="/login"
              className="inline-flex items-center space-x-2 text-xs font-bold text-city-terracotta hover:text-city-terracotta-dark transition-colors"
            >
              <span>Explore Complete Civic Catalog</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </Link>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
            {civicServices.map((svc, idx) => {
              const Icon = svc.icon;
              return (
                <div
                  key={idx}
                  className="p-5 rounded-xl bg-surface-card border border-surface-border shadow-civic hover:border-city-terracotta transition-all hover:shadow-civic-md group flex flex-col justify-between"
                >
                  <div className="space-y-3">
                    <div className="flex items-center justify-between">
                      <div className="w-10 h-10 rounded-lg bg-city-terracotta/10 text-city-terracotta flex items-center justify-center group-hover:bg-city-terracotta group-hover:text-white transition-colors">
                        <Icon className="w-5 h-5" />
                      </div>
                      <span className="text-[11px] font-mono font-semibold px-2 py-0.5 rounded bg-city-ivory text-city-forest border border-surface-border">
                        {svc.sla}
                      </span>
                    </div>

                    <div>
                      <h3 className="text-sm font-bold text-city-forest group-hover:text-city-terracotta transition-colors">
                        {svc.title}
                      </h3>
                      <p className="text-[11px] text-city-charcoal/60 mt-0.5">{svc.dept}</p>
                    </div>

                    <p className="text-xs text-city-charcoal/80 leading-relaxed">
                      {svc.desc}
                    </p>
                  </div>

                  <div className="pt-4 mt-3 border-t border-surface-border/60">
                    <Link
                      to="/login"
                      className="text-xs font-semibold text-city-terracotta hover:underline inline-flex items-center space-x-1"
                    >
                      <span>Request Service</span>
                      <ChevronRight className="w-3 h-3" />
                    </Link>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* Bottom CTA & Indian Municipal Charter Notice */}
      <section id="governance" className="py-14 bg-gradient-to-r from-[#1F0A38] via-[#38125E] to-[#18082B] text-white border-t border-purple-800/40">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-5">
          <h2 className="text-2xl sm:text-3xl font-bold tracking-tight">
            Ready to connect with your municipal corporation?
          </h2>
          <p className="text-sm text-purple-200/90 max-w-2xl mx-auto">
            Experience the new standard of transparent urban administration. Access the Citizen Portal, Field Operations Workdesk, or Executive Command Centre.
          </p>
          <div className="pt-2">
            <Link
              to="/login"
              className="inline-flex items-center space-x-2 px-8 py-3.5 rounded-lg bg-gradient-to-r from-purple-500 to-indigo-600 hover:from-purple-400 hover:to-indigo-500 text-white text-sm font-extrabold shadow-lg shadow-purple-950/60 border border-purple-300/30 transition-transform hover:scale-105"
            >
              <span>Access Your Civic Workspace</span>
              <ArrowRight className="w-4 h-4 text-purple-200" />
            </Link>
          </div>
        </div>
      </section>

      {/* Official Municipal Footer */}
      <Footer />
    </div>
  );
};
