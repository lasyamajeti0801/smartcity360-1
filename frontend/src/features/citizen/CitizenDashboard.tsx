import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import {
  AlertCircle,
  CreditCard,
  FileText,
  Clock,
  CheckCircle2,
  Search,
  MapPin,
  Building2,
  ChevronRight,
  ShieldAlert,
  Star,
  PlusCircle,
  PhoneCall,
  Calendar,
  MessageSquare
} from 'lucide-react';
import { Badge } from '../../components/ui/Badge';
import { CityMap } from '../../components/maps/CityMap';
import { useAuth } from '../../context/AuthContext';
import { useCityData } from '../../context/CityDataContext';
import { useToast } from '../../context/ToastContext';
import { Complaint } from '../../types';

interface CitizenDashboardProps {
  onOpenReportModal?: () => void;
}

export const CitizenDashboard: React.FC<CitizenDashboardProps> = ({ onOpenReportModal }) => {
  const { user } = useAuth();
  const { complaints, facilities, addCitizenFeedback } = useCityData();
  const { success, error: toastError } = useToast();

  const [ticketSearch, setTicketSearch] = useState('');
  const [selectedTicket, setSelectedTicket] = useState<Complaint | null>(complaints[0] || null);
  const [feedbackRating, setFeedbackRating] = useState<number>(5);
  const [feedbackText, setFeedbackText] = useState<string>('');
  const [isRatingSubmitted, setIsRatingSubmitted] = useState<boolean>(false);

  // Filter complaints for current citizen or ward
  const citizenComplaints = complaints.filter(
    (c) => c.citizen_id === user?.id || c.ward_number === 4 || !c.citizen_id
  );

  const activeCount = citizenComplaints.filter(
    (c) => c.status !== 'RESOLVED' && c.status !== 'CLOSED'
  ).length;
  const resolvedCount = citizenComplaints.filter(
    (c) => c.status === 'RESOLVED' || c.status === 'CLOSED'
  ).length;

  const currentTracker = selectedTicket || citizenComplaints[0] || complaints[0];

  const handleTrackSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!ticketSearch.trim()) return;
    const found = complaints.find(
      (c) =>
        c.ticket_number.toLowerCase().includes(ticketSearch.trim().toLowerCase()) ||
        c.title.toLowerCase().includes(ticketSearch.trim().toLowerCase())
    );
    if (found) {
      setSelectedTicket(found);
      success('Complaint Located', `Displaying tracking details for ${found.ticket_number}.`);
    } else {
      toastError('Complaint Not Found', `No grievance matches "${ticketSearch}". Please verify the ticket number.`);
    }
  };

  const handleFeedbackSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!currentTracker) return;
    addCitizenFeedback(currentTracker.id, feedbackRating, feedbackText);
    setIsRatingSubmitted(true);
    success('Feedback Submitted', 'Thank you for rating your municipal service experience.');
  };

  // Stage timeline helper
  const getStageIndex = (status: string) => {
    switch (status) {
      case 'NEW':
        return 0;
      case 'UNDER_REVIEW':
        return 1;
      case 'ASSIGNED':
        return 2;
      case 'IN_PROGRESS':
        return 3;
      case 'RESOLVED':
      case 'CLOSED':
        return 4;
      default:
        return 1;
    }
  };

  const stages = [
    { label: 'Reported', desc: 'Registered with GPS pin' },
    { label: 'Under Review', desc: 'Ward triage & SLA set' },
    { label: 'Assigned', desc: 'Dispatched to field crew' },
    { label: 'In Progress', desc: 'Work order underway' },
    { label: 'Resolved', desc: 'Verified & closed' },
  ];

  const currentStageIdx = currentTracker ? getStageIndex(currentTracker.status) : 0;

  return (
    <div className="space-y-6 select-none font-sans">
      {/* 1. Personalized Municipal Welcome Header */}
      <div className="bg-white rounded-xl border border-surface-border p-5 shadow-civic flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2.5">
            <h1 className="text-2xl font-extrabold text-city-forest tracking-tight">
              Good morning, {user?.fullName || 'Priya'}
            </h1>
            <span className="text-[11px] font-mono px-2.5 py-0.5 rounded-full bg-city-sage/60 text-city-forest font-semibold border border-city-leaf/30">
              CITIZEN PORTAL
            </span>
          </div>
          <p className="text-xs text-city-charcoal/80 mt-1">
            Here is what is happening in <strong className="text-city-forest">{user?.badgeOrWard || 'Ward 04'} ({user?.zone || 'Greenfield Extension'})</strong> today.
          </p>
        </div>

        <div className="flex items-center gap-3 shrink-0">
          {onOpenReportModal && (
            <button
              onClick={onOpenReportModal}
              className="flex items-center space-x-2 px-4 py-2.5 rounded-lg bg-city-terracotta hover:bg-city-terracotta-dark text-white text-xs font-bold shadow-civic border border-city-amber/30 transition-all transform hover:-translate-y-0.5"
            >
              <PlusCircle className="w-4 h-4" />
              <span>Report Civic Issue</span>
            </button>
          )}

          <Link
            to="/citizen/services"
            className="flex items-center space-x-2 px-4 py-2.5 rounded-lg bg-city-sand/40 hover:bg-city-sand text-city-charcoal text-xs font-bold shadow-civic border border-surface-border transition-colors"
          >
            <span>Municipal Services</span>
          </Link>
        </div>
      </div>

      {/* 2. Citizen KPI Hero Strip */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <div className="bg-white p-4 rounded-xl border border-surface-border shadow-civic space-y-2">
          <div className="flex items-center justify-between text-city-charcoal/70">
            <span className="text-xs font-medium">Your Active Requests</span>
            <AlertCircle className="w-4 h-4 text-city-amber" />
          </div>
          <p className="text-2xl font-extrabold font-mono text-city-forest">{activeCount}</p>
          <p className="text-[11px] text-city-charcoal/60">Monitored under SAKALA SLA</p>
        </div>

        <div className="bg-white p-4 rounded-xl border border-surface-border shadow-civic space-y-2">
          <div className="flex items-center justify-between text-city-charcoal/70">
            <span className="text-xs font-medium">Resolved This Month</span>
            <CheckCircle2 className="w-4 h-4 text-city-success" />
          </div>
          <p className="text-2xl font-extrabold font-mono text-city-success">{resolvedCount}</p>
          <p className="text-[11px] text-city-charcoal/60">Verified field remediations</p>
        </div>

        <div className="bg-white p-4 rounded-xl border border-surface-border shadow-civic space-y-2">
          <div className="flex items-center justify-between text-city-charcoal/70">
            <span className="text-xs font-medium">Average Resolution SLA</span>
            <Clock className="w-4 h-4 text-city-green" />
          </div>
          <p className="text-2xl font-extrabold font-mono text-city-forest">18.4 Hours</p>
          <p className="text-[11px] text-city-charcoal/60">Ward 4 Field Response Team</p>
        </div>

        <div className="bg-white p-4 rounded-xl border border-surface-border shadow-civic space-y-2">
          <div className="flex items-center justify-between text-city-charcoal/70">
            <span className="text-xs font-medium">Citizen Identity</span>
            <Building2 className="w-4 h-4 text-city-terracotta" />
          </div>
          <p className="text-lg font-bold font-mono text-city-forest">{user?.id || 'CIT-10482'}</p>
          <p className="text-[11px] text-city-charcoal/60 truncate">Ward 04 • Taxpayer Verified</p>
        </div>
      </div>

      {/* 3. Quick Action Buttons Grid */}
      <div className="bg-surface-card p-4 rounded-xl border border-surface-border shadow-civic">
        <p className="text-xs font-bold uppercase tracking-wider text-city-charcoal/70 mb-3 font-mono">
          Civic Quick Actions
        </p>
        <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-2.5">
          <button
            onClick={onOpenReportModal}
            className="p-3 rounded-lg bg-white border border-surface-border hover:border-city-terracotta hover:bg-city-sage/20 text-center transition-all flex flex-col items-center justify-center space-y-1.5 group"
          >
            <PlusCircle className="w-5 h-5 text-city-terracotta group-hover:scale-110 transition-transform" />
            <span className="text-xs font-semibold text-city-forest">Report Issue</span>
          </button>

          <Link
            to="/citizen/my-requests"
            className="p-3 rounded-lg bg-white border border-surface-border hover:border-city-green hover:bg-city-sage/20 text-center transition-all flex flex-col items-center justify-center space-y-1.5 group"
          >
            <AlertCircle className="w-5 h-5 text-city-green group-hover:scale-110 transition-transform" />
            <span className="text-xs font-semibold text-city-forest">Track Status</span>
          </Link>

          <Link
            to="/citizen/services"
            className="p-3 rounded-lg bg-white border border-surface-border hover:border-city-green hover:bg-city-sage/20 text-center transition-all flex flex-col items-center justify-center space-y-1.5 group"
          >
            <FileText className="w-5 h-5 text-city-leaf group-hover:scale-110 transition-transform" />
            <span className="text-xs font-semibold text-city-forest">Services</span>
          </Link>

          <Link
            to="/citizen/payments"
            className="p-3 rounded-lg bg-white border border-surface-border hover:border-city-green hover:bg-city-sage/20 text-center transition-all flex flex-col items-center justify-center space-y-1.5 group"
          >
            <CreditCard className="w-5 h-5 text-city-amber group-hover:scale-110 transition-transform" />
            <span className="text-xs font-semibold text-city-forest">Pay / Bills</span>
          </Link>

          <Link
            to="/citizen/map"
            className="p-3 rounded-lg bg-white border border-surface-border hover:border-city-green hover:bg-city-sage/20 text-center transition-all flex flex-col items-center justify-center space-y-1.5 group"
          >
            <MapPin className="w-5 h-5 text-city-forest group-hover:scale-110 transition-transform" />
            <span className="text-xs font-semibold text-city-forest">City Map</span>
          </Link>

          <Link
            to="/citizen/emergency"
            className="p-3 rounded-lg bg-white border border-surface-border hover:border-city-danger hover:bg-red-50 text-center transition-all flex flex-col items-center justify-center space-y-1.5 group"
          >
            <ShieldAlert className="w-5 h-5 text-city-danger group-hover:scale-110 transition-transform" />
            <span className="text-xs font-semibold text-city-danger">112 SOS</span>
          </Link>

          <Link
            to="/citizen/notifications"
            className="p-3 rounded-lg bg-white border border-surface-border hover:border-city-green hover:bg-city-sage/20 text-center transition-all flex flex-col items-center justify-center space-y-1.5 group"
          >
            <MessageSquare className="w-5 h-5 text-city-leaf group-hover:scale-110 transition-transform" />
            <span className="text-xs font-semibold text-city-forest">Alerts</span>
          </Link>

          <Link
            to="/citizen/profile"
            className="p-3 rounded-lg bg-white border border-surface-border hover:border-city-green hover:bg-city-sage/20 text-center transition-all flex flex-col items-center justify-center space-y-1.5 group"
          >
            <Building2 className="w-5 h-5 text-city-sand group-hover:scale-110 transition-transform" />
            <span className="text-xs font-semibold text-city-forest">My Ward</span>
          </Link>
        </div>
      </div>

      {/* 4. Active Request Live Tracker (Card with Multi-Stage Timeline) */}
      <div className="bg-white rounded-xl border border-surface-border shadow-civic overflow-hidden">
        <div className="p-5 border-b border-surface-border bg-surface-card flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <div className="flex items-center space-x-2">
              <h2 className="text-base font-bold text-city-forest">
                Civic Request Progress Tracker
              </h2>
              {currentTracker && <Badge status={currentTracker.status}>{currentTracker.status}</Badge>}
            </div>
            <p className="text-xs text-city-charcoal/70 mt-0.5">
              Real-time audit stages for ticket <span className="font-mono font-bold text-city-forest">{currentTracker?.ticket_number}</span>
            </p>
          </div>

          {/* Ticket search input */}
          <form onSubmit={handleTrackSubmit} className="flex items-center space-x-2">
            <div className="relative">
              <Search className="w-3.5 h-3.5 text-city-charcoal/40 absolute left-2.5 top-2.5" />
              <input
                type="text"
                value={ticketSearch}
                onChange={(e) => setTicketSearch(e.target.value)}
                placeholder="Search ticket #..."
                className="pl-8 pr-3 py-1.5 rounded-lg border border-surface-border text-xs text-city-charcoal focus:outline-none focus:ring-1 focus:ring-city-terracotta"
              />
            </div>
            <button
              type="submit"
              className="px-3 py-1.5 rounded-lg bg-city-terracotta text-white text-xs font-bold hover:bg-city-terracotta-dark transition-colors shadow-sm"
            >
              Track
            </button>
          </form>
        </div>

        {currentTracker ? (
          <div className="p-6 space-y-6">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div>
                <h3 className="text-base font-bold text-city-forest">{currentTracker.title}</h3>
                <p className="text-xs text-city-charcoal/70 mt-0.5 flex items-center space-x-1.5">
                  <MapPin className="w-3.5 h-3.5 text-city-terracotta" />
                  <span>{currentTracker.location_address}</span>
                  <span className="text-surface-border">•</span>
                  <span>Ward {currentTracker.ward_number || 4}</span>
                </p>
              </div>

              <div className="text-right">
                <span className="text-[11px] text-city-charcoal/60">Expected SLA Deadline</span>
                <p className="text-xs font-mono font-bold text-city-forest">
                  {currentTracker.sla_due_at ? new Date(currentTracker.sla_due_at).toLocaleDateString('en-IN', { day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' }) : 'Standard 48h'}
                </p>
              </div>
            </div>

            {/* 5-Stage Visual Progression Timeline */}
            <div className="py-4">
              <div className="grid grid-cols-5 gap-2 relative">
                {stages.map((st, idx) => {
                  const isPassed = currentStageIdx >= idx;
                  const isCurrent = currentStageIdx === idx;

                  return (
                    <div key={idx} className="flex flex-col items-center text-center relative">
                      <div
                        className={`w-9 h-9 rounded-full flex items-center justify-center font-bold text-xs transition-colors z-10 ${
                          isPassed
                            ? 'bg-city-terracotta text-white shadow-civic'
                            : 'bg-surface-muted text-city-charcoal/40 border border-surface-border'
                        } ${isCurrent ? 'ring-4 ring-city-amber/30' : ''}`}
                      >
                        {isPassed ? <CheckCircle2 className="w-4 h-4" /> : idx + 1}
                      </div>
                      <p className={`text-xs font-bold mt-2 ${isPassed ? 'text-city-forest' : 'text-city-charcoal/40'}`}>
                        {st.label}
                      </p>
                      <p className="text-[10px] text-city-charcoal/60 mt-0.5 hidden sm:block">
                        {st.desc}
                      </p>
                    </div>
                  );
                })}
              </div>

              {/* Progress Line */}
              <div className="w-full bg-surface-muted h-2 rounded-full mt-4 overflow-hidden">
                <div
                  className="bg-city-terracotta h-full transition-all duration-500 rounded-full"
                  style={{ width: `${Math.min(100, (currentStageIdx / (stages.length - 1)) * 100)}%` }}
                />
              </div>
            </div>

            {/* If Resolved: Citizen Feedback & Rating Module */}
            {(currentTracker.status === 'RESOLVED' || currentTracker.status === 'CLOSED') && (
              <div className="p-4 rounded-xl bg-city-sage/30 border border-city-leaf/30 space-y-3">
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-2">
                    <CheckCircle2 className="w-4 h-4 text-city-success" />
                    <span className="text-xs font-bold text-city-forest">
                      This grievance has been resolved by Municipal Field Teams.
                    </span>
                  </div>
                  <span className="text-[11px] text-city-charcoal/70">Public Verification Audit</span>
                </div>

                {!isRatingSubmitted && !currentTracker.citizen_rating ? (
                  <form onSubmit={handleFeedbackSubmit} className="space-y-3 pt-2">
                    <div>
                      <label className="block text-xs font-semibold text-city-forest mb-1">
                        Rate the resolution quality:
                      </label>
                      <div className="flex items-center space-x-1.5">
                        {[1, 2, 3, 4, 5].map((star) => (
                          <button
                            type="button"
                            key={star}
                            onClick={() => setFeedbackRating(star)}
                            className="p-1 text-city-amber hover:scale-125 transition-transform"
                          >
                            <Star
                              className={`w-5 h-5 ${feedbackRating >= star ? 'fill-city-amber text-city-amber' : 'text-surface-border'}`}
                            />
                          </button>
                        ))}
                        <span className="text-xs font-mono font-bold text-city-forest ml-2">
                          {feedbackRating} / 5 Stars
                        </span>
                      </div>
                    </div>

                    <div>
                      <input
                        type="text"
                        value={feedbackText}
                        onChange={(e) => setFeedbackText(e.target.value)}
                        placeholder="Leave a short comment regarding the repair quality..."
                        className="w-full px-3 py-2 rounded-lg border border-surface-border text-xs text-city-charcoal focus:outline-none focus:ring-1 focus:ring-city-terracotta"
                      />
                    </div>

                    <button
                      type="submit"
                      className="px-4 py-2 rounded-lg bg-city-terracotta hover:bg-city-terracotta-dark text-white text-xs font-bold shadow-civic transition-colors"
                    >
                      Submit Citizen Feedback
                    </button>
                  </form>
                ) : (
                  <div className="p-3 bg-white rounded-lg border border-surface-border flex items-center justify-between text-xs">
                    <div className="flex items-center space-x-2">
                      <div className="flex text-city-amber">
                        {[...Array(currentTracker.citizen_rating || feedbackRating)].map((_, i) => (
                          <Star key={i} className="w-3.5 h-3.5 fill-city-amber text-city-amber" />
                        ))}
                      </div>
                      <span className="text-city-charcoal/80 font-medium">
                        "{currentTracker.citizen_feedback || feedbackText || 'Resolution verified by resident.'}"
                      </span>
                    </div>
                    <span className="text-[10px] font-mono text-city-success font-semibold">FEEDBACK LOGGED</span>
                  </div>
                )}
              </div>
            )}
          </div>
        ) : (
          <div className="p-8 text-center text-xs text-city-charcoal/60">
            No complaints currently logged. Click "+ Report Issue" above to register a civic problem.
          </div>
        )}
      </div>

      {/* 5. Bottom Split: Neighborhood GIS Map & Ward Announcements */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left: Interactive Neighborhood GIS Map */}
        <div className="lg:col-span-8 bg-white p-5 rounded-xl border border-surface-border shadow-civic space-y-3">
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-sm font-bold text-city-forest">Ward 04 Public Infrastructure & Issue Map</h3>
              <p className="text-xs text-city-charcoal/70">
                Interactive OpenStreetMap showing nearby clinics, fire stations, and verified citizen reports.
              </p>
            </div>
            <Link
              to="/citizen/map"
              className="text-xs font-semibold text-city-terracotta hover:text-city-terracotta-dark hover:underline inline-flex items-center space-x-1"
            >
              <span>Expand Map</span>
              <ChevronRight className="w-3.5 h-3.5" />
            </Link>
          </div>

          <div className="h-[360px] w-full rounded-lg overflow-hidden border border-surface-border">
            <CityMap complaints={citizenComplaints} facilities={facilities} />
          </div>
        </div>

        {/* Right: Ward Alerts & Neighborhood Bulletin */}
        <div className="lg:col-span-4 bg-white p-5 rounded-xl border border-surface-border shadow-civic space-y-4">
          <div className="flex items-center justify-between pb-2 border-b border-surface-border">
            <div className="flex items-center space-x-2">
              <Calendar className="w-4 h-4 text-city-green" />
              <h3 className="text-sm font-bold text-city-forest">Ward 04 Bulletin</h3>
            </div>
            <span className="text-[10px] font-mono text-city-charcoal/60">UPDATED TODAY</span>
          </div>

          <div className="space-y-3">
            <div className="p-3 rounded-lg bg-city-sage/20 border border-city-leaf/20 space-y-1">
              <div className="flex items-center justify-between text-[11px]">
                <span className="font-bold text-city-forest">Water Main Calibration</span>
                <span className="text-city-amber font-semibold">Tonight</span>
              </div>
              <p className="text-xs text-city-charcoal/80 leading-snug">
                Pressure optimization in Greenfield Sector 4 & 5 between 01:00 and 04:00.
              </p>
            </div>

            <div className="p-3 rounded-lg bg-surface-card border border-surface-border space-y-1">
              <div className="flex items-center justify-between text-[11px]">
                <span className="font-bold text-city-forest">Door-to-Door E-Waste Drive</span>
                <span className="text-city-green font-semibold">14 Sep</span>
              </div>
              <p className="text-xs text-city-charcoal/80 leading-snug">
                Special collection van at Greenfield Community Center Gate 1.
              </p>
            </div>

            <div className="p-3 rounded-lg bg-surface-card border border-surface-border space-y-1">
              <div className="flex items-center justify-between text-[11px]">
                <span className="font-bold text-city-forest">Ward Committee Meeting</span>
                <span className="text-city-charcoal/60 font-semibold">16 Sep</span>
              </div>
              <p className="text-xs text-city-charcoal/80 leading-snug">
                Public grievance hearing with Ward Commissioner Arthur Vance.
              </p>
            </div>
          </div>

          <div className="pt-2 border-t border-surface-border text-center">
            <a
              href="tel:112"
              className="w-full flex items-center justify-center space-x-2 py-2 rounded-lg bg-city-danger/10 text-city-danger hover:bg-city-danger/20 text-xs font-bold transition-colors"
            >
              <PhoneCall className="w-3.5 h-3.5" />
              <span>Direct Hotline: Dial 112</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};
