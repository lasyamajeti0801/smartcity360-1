import React, { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';
import { Badge } from '../../components/ui/Badge';
import { Table, Column } from '../../components/ui/Table';
import { CityMap } from '../../components/maps/CityMap';
import { Complaint, Facility } from '../../types';
import {
  AlertCircle,
  CreditCard,
  FileCheck2,
  Clock,
  CheckCircle2,
  Search,
  PhoneCall,
  MapPin,
  Building2,
  ChevronRight,
  ShieldAlert,
  Sparkles
} from 'lucide-react';

interface CitizenDashboardProps {
  complaints: Complaint[];
  facilities: Facility[];
  onOpenReportModal: () => void;
  onNavigateToServices: () => void;
  onNavigateToTab?: (tabId: string) => void;
}

export const CitizenDashboard: React.FC<CitizenDashboardProps> = ({
  complaints,
  facilities,
  onOpenReportModal,
  onNavigateToServices,
  onNavigateToTab,
}) => {
  const [ticketSearchInput, setTicketSearchInput] = useState('');
  const [selectedTicket, setSelectedTicket] = useState<Complaint | null>(complaints[0] || null);
  const [statusFilter, setStatusFilter] = useState<'ALL' | 'PENDING' | 'IN_PROGRESS' | 'RESOLVED'>('ALL');
  const [detailModalComplaint, setDetailModalComplaint] = useState<Complaint | null>(null);

  const activeCount = complaints.filter((c) => c.status !== 'RESOLVED' && c.status !== 'CLOSED').length;
  const resolvedCount = complaints.filter((c) => c.status === 'RESOLVED' || c.status === 'CLOSED').length;

  // Filter complaints list
  const filteredComplaints = complaints.filter((c) => {
    if (statusFilter === 'ALL') return true;
    if (statusFilter === 'RESOLVED') return c.status === 'RESOLVED' || c.status === 'CLOSED';
    if (statusFilter === 'IN_PROGRESS') return c.status === 'IN_PROGRESS' || c.status === 'ASSIGNED';
    if (statusFilter === 'PENDING') return c.status === 'NEW' || c.status === 'UNDER_REVIEW';
    return true;
  });

  // Ticket lookup handler
  const handleTrackSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (!ticketSearchInput.trim()) return;
    const found = complaints.find(
      (c) =>
        c.ticket_number.toLowerCase() === ticketSearchInput.trim().toLowerCase() ||
        c.id.toLowerCase() === ticketSearchInput.trim().toLowerCase()
    );
    if (found) {
      setSelectedTicket(found);
    } else {
      alert(`No complaint found matching ticket number "${ticketSearchInput}". Please check the ID and try again.`);
    }
  };

  // Determine stage progress for the selected ticket
  const getStageStatus = (stageIndex: number, status: string) => {
    const statusMap: Record<string, number> = {
      NEW: 0,
      UNDER_REVIEW: 1,
      ASSIGNED: 2,
      IN_PROGRESS: 2,
      ON_HOLD: 2,
      RESOLVED: 3,
      CLOSED: 4,
    };
    const currentStep = statusMap[status] ?? 1;
    if (currentStep > stageIndex) return 'complete';
    if (currentStep === stageIndex) return 'current';
    return 'upcoming';
  };

  const activeTrackerTicket = selectedTicket || complaints[0];

  const columns: Column<Complaint>[] = [
    {
      key: 'ticket_number',
      header: 'Ticket #',
      render: (c) => (
        <button
          onClick={() => {
            setSelectedTicket(c);
            setDetailModalComplaint(c);
          }}
          className="font-mono font-bold text-teal-700 hover:text-teal-900 hover:underline text-xs text-left"
        >
          {c.ticket_number}
        </button>
      ),
    },
    {
      key: 'title',
      header: 'Subject & Location',
      render: (c) => (
        <div className="max-w-xs">
          <div className="font-semibold text-slate-900 truncate">{c.title}</div>
          <div className="text-[11px] text-slate-500 flex items-center mt-0.5">
            <MapPin className="h-3 w-3 mr-1 text-slate-400 shrink-0" />
            <span className="truncate">{c.location_address || `Ward ${c.ward_number || 4}`}</span>
          </div>
        </div>
      ),
    },
    {
      key: 'priority',
      header: 'Priority',
      render: (c) => <Badge status={c.priority}>{c.priority}</Badge>,
    },
    {
      key: 'status',
      header: 'Status',
      render: (c) => <Badge status={c.status}>{c.status}</Badge>,
    },
    {
      key: 'created_at',
      header: 'Reported',
      render: (c) => (
        <span className="text-[11px] text-slate-500 font-mono">
          {new Date(c.created_at).toLocaleDateString(undefined, {
            day: '2-digit',
            month: 'short',
            year: 'numeric',
          })}
        </span>
      ),
    },
    {
      key: 'id',
      header: 'Action',
      render: (c) => (
        <button
          onClick={() => {
            setSelectedTicket(c);
            setDetailModalComplaint(c);
          }}
          className="text-[11px] font-semibold text-teal-700 hover:text-teal-800 inline-flex items-center"
        >
          View Details <ChevronRight className="h-3 w-3 ml-0.5" />
        </button>
      ),
    },
  ];

  return (
    <div className="space-y-6">
      {/* Top Banner with Civic Branding & Actions */}
      <div className="bg-gradient-to-r from-slate-900 via-slate-800 to-teal-950 text-white rounded-xl p-6 border border-slate-700/80 shadow-md flex flex-col lg:flex-row items-start lg:items-center justify-between gap-5">
        <div className="space-y-1.5 max-w-2xl">
          <div className="inline-flex items-center space-x-2 px-2.5 py-0.5 rounded-full bg-teal-500/20 text-teal-300 border border-teal-500/30 text-xs font-semibold tracking-wide">
            <Sparkles className="h-3.5 w-3.5" />
            <span>MUNICIPAL CITIZEN ASSISTANCE SYSTEM</span>
          </div>
          <h1 className="text-2xl font-bold tracking-tight text-white">
            Welcome to Smart City 360 Citizen Portal
          </h1>
          <p className="text-xs text-slate-300 leading-relaxed">
            Report civic infrastructure issues, track live municipal remediation with SLA accountability, access public
            amenities, and manage civic utility payments from one integrated, transparent dashboard.
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-2.5 shrink-0">
          <Button
            variant="primary"
            onClick={onOpenReportModal}
            className="bg-teal-600 hover:bg-teal-500 text-white font-semibold shadow-sm px-4 py-2 text-xs"
          >
            <AlertCircle className="h-4 w-4 mr-1.5" />
            Report Civic Issue
          </Button>
          <Button
            variant="outline"
            onClick={onNavigateToServices}
            className="bg-slate-800/80 hover:bg-slate-700 text-slate-100 border-slate-600 text-xs px-4 py-2"
          >
            <FileCheck2 className="h-4 w-4 mr-1.5 text-teal-400" />
            Service Catalog
          </Button>
        </div>
      </div>

      {/* Quick Action Grid (6 Cards) */}
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3">
        <button
          onClick={onOpenReportModal}
          className="bg-white p-4 rounded-lg border border-slate-200 shadow-sm hover:border-teal-500 hover:shadow transition-all text-left flex flex-col justify-between group"
        >
          <div className="h-9 w-9 rounded-lg bg-teal-50 text-teal-700 flex items-center justify-center mb-2 group-hover:bg-teal-600 group-hover:text-white transition-colors">
            <AlertCircle className="h-5 w-5" />
          </div>
          <div>
            <div className="text-xs font-bold text-slate-900 group-hover:text-teal-700">Lodge Issue</div>
            <div className="text-[10px] text-slate-500 mt-0.5">Potholes, waste, power</div>
          </div>
        </button>

        <button
          onClick={() => {
            const el = document.getElementById('ticket-tracker-section');
            el?.scrollIntoView({ behavior: 'smooth' });
          }}
          className="bg-white p-4 rounded-lg border border-slate-200 shadow-sm hover:border-teal-500 hover:shadow transition-all text-left flex flex-col justify-between group"
        >
          <div className="h-9 w-9 rounded-lg bg-sky-50 text-sky-700 flex items-center justify-center mb-2 group-hover:bg-sky-600 group-hover:text-white transition-colors">
            <Search className="h-5 w-5" />
          </div>
          <div>
            <div className="text-xs font-bold text-slate-900 group-hover:text-teal-700">Track Ticket</div>
            <div className="text-[10px] text-slate-500 mt-0.5">Live status & SLA</div>
          </div>
        </button>

        <button
          onClick={onNavigateToServices}
          className="bg-white p-4 rounded-lg border border-slate-200 shadow-sm hover:border-teal-500 hover:shadow transition-all text-left flex flex-col justify-between group"
        >
          <div className="h-9 w-9 rounded-lg bg-indigo-50 text-indigo-700 flex items-center justify-center mb-2 group-hover:bg-indigo-600 group-hover:text-white transition-colors">
            <FileCheck2 className="h-5 w-5" />
          </div>
          <div>
            <div className="text-xs font-bold text-slate-900 group-hover:text-teal-700">Apply Permit</div>
            <div className="text-[10px] text-slate-500 mt-0.5">Building, road cuts</div>
          </div>
        </button>

        <button
          onClick={() => onNavigateToTab && onNavigateToTab('emergency')}
          className="bg-white p-4 rounded-lg border border-slate-200 shadow-sm hover:border-red-500 hover:shadow transition-all text-left flex flex-col justify-between group"
        >
          <div className="h-9 w-9 rounded-lg bg-red-50 text-red-700 flex items-center justify-center mb-2 group-hover:bg-red-600 group-hover:text-white transition-colors">
            <PhoneCall className="h-5 w-5" />
          </div>
          <div>
            <div className="text-xs font-bold text-slate-900 group-hover:text-red-700">911 SOS</div>
            <div className="text-[10px] text-slate-500 mt-0.5">Fire, police, ambulance</div>
          </div>
        </button>

        <button
          onClick={() => onNavigateToTab && onNavigateToTab('map')}
          className="bg-white p-4 rounded-lg border border-slate-200 shadow-sm hover:border-teal-500 hover:shadow transition-all text-left flex flex-col justify-between group"
        >
          <div className="h-9 w-9 rounded-lg bg-emerald-50 text-emerald-700 flex items-center justify-center mb-2 group-hover:bg-emerald-600 group-hover:text-white transition-colors">
            <Building2 className="h-5 w-5" />
          </div>
          <div>
            <div className="text-xs font-bold text-slate-900 group-hover:text-teal-700">Facilities</div>
            <div className="text-[10px] text-slate-500 mt-0.5">Hospitals, fire hubs</div>
          </div>
        </button>

        <button
          onClick={() => alert('Civic Tax & Water Billing Gateway: All municipal dues for Ward 4 are currently cleared.')}
          className="bg-white p-4 rounded-lg border border-slate-200 shadow-sm hover:border-teal-500 hover:shadow transition-all text-left flex flex-col justify-between group"
        >
          <div className="h-9 w-9 rounded-lg bg-purple-50 text-purple-700 flex items-center justify-center mb-2 group-hover:bg-purple-600 group-hover:text-white transition-colors">
            <CreditCard className="h-5 w-5" />
          </div>
          <div>
            <div className="text-xs font-bold text-slate-900 group-hover:text-teal-700">Pay Dues</div>
            <div className="text-[10px] text-slate-500 mt-0.5">Water & tax clearance</div>
          </div>
        </button>
      </div>

      {/* Metric Cards (3 Cards) */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <Card className="border-l-4 border-l-amber-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-[11px] font-bold text-slate-500 uppercase tracking-wide">Active Grievances</p>
              <h2 className="text-2xl font-black text-slate-900 mt-1">{activeCount}</h2>
              <p className="text-xs text-slate-500 mt-0.5">Assigned to municipal engineers</p>
            </div>
            <div className="p-3 bg-amber-50 rounded-lg text-amber-700">
              <Clock className="h-6 w-6" />
            </div>
          </div>
        </Card>

        <Card className="border-l-4 border-l-emerald-600">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-[11px] font-bold text-slate-500 uppercase tracking-wide">Resolved Complaints</p>
              <h2 className="text-2xl font-black text-slate-900 mt-1">{resolvedCount}</h2>
              <p className="text-xs text-slate-500 mt-0.5">Field remediations verified</p>
            </div>
            <div className="p-3 bg-emerald-50 rounded-lg text-emerald-700">
              <CheckCircle2 className="h-6 w-6" />
            </div>
          </div>
        </Card>

        <Card className="border-l-4 border-l-teal-600">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-[11px] font-bold text-slate-500 uppercase tracking-wide">SLA Compliance Rate</p>
              <h2 className="text-2xl font-black text-slate-900 mt-1">94.8%</h2>
              <p className="text-xs text-emerald-700 font-semibold mt-0.5">+1.2% over statutory benchmark</p>
            </div>
            <div className="p-3 bg-teal-50 rounded-lg text-teal-700">
              <ShieldAlert className="h-6 w-6" />
            </div>
          </div>
        </Card>
      </div>

      {/* Ticket Progress Tracker Section */}
      <div id="ticket-tracker-section" className="bg-white rounded-xl border border-slate-200 shadow-sm p-5 space-y-4">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-100 pb-4">
          <div>
            <div className="flex items-center space-x-2">
              <span className="text-xs font-bold text-teal-800 bg-teal-50 px-2 py-0.5 rounded border border-teal-200 uppercase">
                Citizen SLA Tracker
              </span>
              <h3 className="text-base font-bold text-slate-900">Live Complaint Resolution Workflow</h3>
            </div>
            <p className="text-xs text-slate-500 mt-1">
              Lookup any municipal ticket to inspect stage-by-stage department dispatch, investigation, and physical resolution.
            </p>
          </div>

          <form onSubmit={handleTrackSearch} className="flex items-center space-x-2 max-w-sm w-full">
            <div className="relative flex-1">
              <Search className="absolute left-3 top-2.5 h-4 w-4 text-slate-400" />
              <input
                type="text"
                placeholder="Enter Ticket # (e.g. CMP-20260912-001)"
                value={ticketSearchInput}
                onChange={(e) => setTicketSearchInput(e.target.value)}
                className="w-full bg-slate-50 border border-slate-300 rounded-md pl-9 pr-3 py-1.5 text-xs text-slate-900 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-teal-500"
              />
            </div>
            <Button type="submit" size="sm" variant="primary" className="bg-teal-700 hover:bg-teal-600 text-xs px-3">
              Track
            </Button>
          </form>
        </div>

        {activeTrackerTicket ? (
          <div className="space-y-4 pt-1">
            {/* Active Ticket Banner */}
            <div className="flex flex-col sm:flex-row sm:items-center justify-between bg-slate-50 rounded-lg p-3 border border-slate-200 gap-2">
              <div className="flex items-center space-x-3">
                <div className="font-mono text-sm font-bold text-teal-800 bg-white px-2.5 py-1 rounded border border-slate-200">
                  {activeTrackerTicket.ticket_number}
                </div>
                <div>
                  <h4 className="text-xs font-bold text-slate-900">{activeTrackerTicket.title}</h4>
                  <p className="text-[11px] text-slate-500">
                    Location: {activeTrackerTicket.location_address} | Priority: <strong>{activeTrackerTicket.priority}</strong>
                  </p>
                </div>
              </div>
              <div className="flex items-center space-x-2">
                <Badge status={activeTrackerTicket.status}>{activeTrackerTicket.status}</Badge>
                <button
                  onClick={() => setDetailModalComplaint(activeTrackerTicket)}
                  className="text-xs font-semibold text-teal-700 hover:text-teal-900 underline ml-1"
                >
                  Full Dossier
                </button>
              </div>
            </div>

            {/* 5-Step Horizontal Progress Bar */}
            <div className="py-3 px-2">
              <div className="grid grid-cols-5 gap-2 relative">
                {[
                  { title: '1. Ticket Lodged', desc: 'Acknowledged via portal', stepIdx: 0 },
                  { title: '2. Triage & Verified', desc: 'Ward supervisor inspection', stepIdx: 1 },
                  { title: '3. Field Dispatched', desc: 'Work crew on scene', stepIdx: 2 },
                  { title: '4. Remediated', desc: 'Repairs & photos taken', stepIdx: 3 },
                  { title: '5. Verified & Closed', desc: 'Citizen sign-off completed', stepIdx: 4 },
                ].map((step) => {
                  const state = getStageStatus(step.stepIdx, activeTrackerTicket.status);
                  const isDone = state === 'complete';
                  const isCurrent = state === 'current';

                  return (
                    <div key={step.stepIdx} className="flex flex-col items-center text-center relative z-10">
                      <div
                        className={`h-9 w-9 rounded-full flex items-center justify-center font-bold text-xs transition-all ${
                          isDone
                            ? 'bg-teal-600 text-white shadow-sm ring-4 ring-teal-50'
                            : isCurrent
                            ? 'bg-amber-500 text-white shadow-md ring-4 ring-amber-100 animate-pulse'
                            : 'bg-slate-200 text-slate-500'
                        }`}
                      >
                        {isDone ? <CheckCircle2 className="h-5 w-5" /> : step.stepIdx + 1}
                      </div>
                      <div className="mt-2 text-xs font-bold text-slate-900">{step.title}</div>
                      <div className="text-[10px] text-slate-500 mt-0.5 max-w-[120px]">{step.desc}</div>
                    </div>
                  );
                })}
              </div>
            </div>
          </div>
        ) : (
          <div className="text-center py-6 text-xs text-slate-500">
            Select a complaint from below to view its live resolution step progress.
          </div>
        )}
      </div>

      {/* Main Grid: My Complaints Table & Leaflet Spatial Map */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left 7 cols: Grievance Queue */}
        <div className="lg:col-span-7 space-y-4">
          <Card
            title="My Lodged Complaints & Requests"
            subtitle="Real-time municipal intake queue, field engineer work orders, and resolution proof."
            action={
              <div className="flex items-center space-x-2">
                <div className="flex items-center space-x-1 bg-slate-100 p-0.5 rounded text-[11px]">
                  {(['ALL', 'PENDING', 'IN_PROGRESS', 'RESOLVED'] as const).map((filter) => (
                    <button
                      key={filter}
                      onClick={() => setStatusFilter(filter)}
                      className={`px-2 py-0.5 rounded font-medium transition-colors ${
                        statusFilter === filter
                          ? 'bg-white text-slate-900 font-semibold shadow-xs'
                          : 'text-slate-600 hover:text-slate-900'
                      }`}
                    >
                      {filter}
                    </button>
                  ))}
                </div>
                <Button
                  size="sm"
                  variant="primary"
                  onClick={onOpenReportModal}
                  className="bg-teal-700 hover:bg-teal-600 text-xs px-2.5 py-1"
                >
                  + New
                </Button>
              </div>
            }
          >
            <Table
              columns={columns}
              data={filteredComplaints}
              keyExtractor={(c) => c.id}
              emptyMessage="No complaints match the selected filter."
            />
          </Card>
        </div>

        {/* Right 5 cols: Interactive Neighborhood Map */}
        <div className="lg:col-span-5 space-y-4">
          <Card
            title="Neighborhood Civic Map"
            subtitle="Interactive OpenStreetMap layer displaying active civic tickets and public facilities."
          >
            <div className="h-[380px] w-full">
              <CityMap complaints={complaints} facilities={facilities} />
            </div>

            <div className="mt-3 grid grid-cols-2 gap-2 text-[11px] text-slate-600 bg-slate-50 p-2.5 rounded-lg border border-slate-200">
              <div className="flex items-center space-x-2">
                <span className="h-2.5 w-2.5 rounded-full bg-red-600 shrink-0"></span>
                <span>Critical / High Severity</span>
              </div>
              <div className="flex items-center space-x-2">
                <span className="h-2.5 w-2.5 rounded-full bg-amber-500 shrink-0"></span>
                <span>Active Remediation</span>
              </div>
              <div className="flex items-center space-x-2">
                <span className="h-2.5 w-2.5 rounded-full bg-emerald-600 shrink-0"></span>
                <span>Verified Resolved</span>
              </div>
              <div className="flex items-center space-x-2">
                <span className="h-2.5 w-2.5 rounded-sm bg-sky-600 shrink-0"></span>
                <span>Hospital / Civic Clinic</span>
              </div>
            </div>
          </Card>

          {/* Emergency 911 Callout Banner */}
          <div className="bg-red-50 border border-red-200 rounded-xl p-4 flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="h-9 w-9 rounded-full bg-red-600 text-white flex items-center justify-center shrink-0">
                <PhoneCall className="h-4 w-4" />
              </div>
              <div>
                <h4 className="text-xs font-bold text-red-950">Immediate Public Safety Emergency?</h4>
                <p className="text-[11px] text-red-700">Call Central Police & Fire Dispatch Hotline: <strong>911</strong></p>
              </div>
            </div>
            <Button
              size="sm"
              variant="danger"
              onClick={() => onNavigateToTab && onNavigateToTab('emergency')}
              className="bg-red-600 hover:bg-red-700 text-xs px-3"
            >
              SOS Portal
            </Button>
          </div>
        </div>
      </div>

      {/* Ticket Details Inspection Modal */}
      {detailModalComplaint && (
        <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white rounded-xl shadow-2xl border border-slate-200 max-w-xl w-full overflow-hidden">
            {/* Modal Header */}
            <div className="bg-slate-900 text-white p-4 flex items-center justify-between">
              <div>
                <span className="text-[10px] font-mono uppercase bg-teal-800 text-teal-200 px-2 py-0.5 rounded font-bold">
                  {detailModalComplaint.ticket_number}
                </span>
                <h3 className="text-sm font-bold text-white mt-1">{detailModalComplaint.title}</h3>
              </div>
              <button
                onClick={() => setDetailModalComplaint(null)}
                className="text-slate-400 hover:text-white text-lg font-bold p-1"
              >
                ✕
              </button>
            </div>

            {/* Modal Body */}
            <div className="p-5 space-y-4 max-h-[75vh] overflow-y-auto text-xs text-slate-700">
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 bg-slate-50 p-3 rounded-lg border border-slate-200">
                <div>
                  <span className="text-[10px] font-bold text-slate-500 uppercase">Status</span>
                  <div className="mt-0.5"><Badge status={detailModalComplaint.status}>{detailModalComplaint.status}</Badge></div>
                </div>
                <div>
                  <span className="text-[10px] font-bold text-slate-500 uppercase">Priority</span>
                  <div className="mt-0.5"><Badge status={detailModalComplaint.priority}>{detailModalComplaint.priority}</Badge></div>
                </div>
                <div>
                  <span className="text-[10px] font-bold text-slate-500 uppercase">Ward #</span>
                  <div className="font-bold text-slate-900 mt-1">Ward {detailModalComplaint.ward_number || 4}</div>
                </div>
                <div>
                  <span className="text-[10px] font-bold text-slate-500 uppercase">Report Date</span>
                  <div className="font-medium text-slate-600 mt-1 font-mono">
                    {new Date(detailModalComplaint.created_at).toLocaleDateString()}
                  </div>
                </div>
              </div>

              <div>
                <h4 className="font-bold text-slate-900 mb-1">Issue Description & Citizen Notes</h4>
                <div className="p-3 bg-slate-50 rounded border border-slate-200 text-slate-800 leading-relaxed">
                  {detailModalComplaint.description || 'No additional notes entered by the citizen.'}
                </div>
              </div>

              <div>
                <h4 className="font-bold text-slate-900 mb-1">Physical Location Coordinates</h4>
                <div className="flex items-center justify-between p-2.5 bg-slate-50 rounded border border-slate-200">
                  <span className="text-slate-600">{detailModalComplaint.location_address || 'City Center, Main Boulevard'}</span>
                  <span className="font-mono text-slate-500 text-[11px]">
                    {detailModalComplaint.latitude.toFixed(4)}, {detailModalComplaint.longitude.toFixed(4)}
                  </span>
                </div>
              </div>

              {(detailModalComplaint as any).resolution_notes && (
                <div className="p-3 bg-emerald-50 rounded border border-emerald-200">
                  <h4 className="font-bold text-emerald-900 mb-0.5">Municipal Field Remediation Report</h4>
                  <p className="text-emerald-800">{(detailModalComplaint as any).resolution_notes}</p>
                </div>
              )}
            </div>

            {/* Modal Footer */}
            <div className="bg-slate-50 border-t border-slate-200 p-3 flex items-center justify-between">
              <span className="text-[11px] text-slate-500">
                Department SLA: Under statutory municipal review
              </span>
              <Button
                variant="outline"
                size="sm"
                onClick={() => setDetailModalComplaint(null)}
                className="text-xs"
              >
                Close Dossier
              </Button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
