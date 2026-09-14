import React, { useState } from 'react';
import {
  AlertCircle,
  Search,
  MapPin,
  ChevronRight,
  PlusCircle,
  Star,
  X
} from 'lucide-react';
import { Badge } from '../../components/ui/Badge';
import { useCityData } from '../../context/CityDataContext';
import { useToast } from '../../context/ToastContext';
import { Complaint } from '../../types';

interface CitizenRequestsPageProps {
  onOpenReportModal?: () => void;
}

export const CitizenRequestsPage: React.FC<CitizenRequestsPageProps> = ({ onOpenReportModal }) => {
  const { complaints, addCitizenFeedback } = useCityData();
  const { success } = useToast();

  const [search, setSearch] = useState('');
  const [filter, setFilter] = useState<'ALL' | 'NEW' | 'IN_PROGRESS' | 'RESOLVED'>('ALL');
  const [selectedTicket, setSelectedTicket] = useState<Complaint | null>(null);
  const [feedbackRating, setFeedbackRating] = useState(5);
  const [feedbackNotes, setFeedbackNotes] = useState('');

  const filtered = complaints.filter((c) => {
    const matchesSearch =
      search.trim() === '' ||
      c.ticket_number.toLowerCase().includes(search.toLowerCase()) ||
      c.title.toLowerCase().includes(search.toLowerCase()) ||
      c.location_address.toLowerCase().includes(search.toLowerCase());

    if (!matchesSearch) return false;
    if (filter === 'ALL') return true;
    if (filter === 'RESOLVED') return c.status === 'RESOLVED' || c.status === 'CLOSED';
    if (filter === 'IN_PROGRESS') return c.status === 'IN_PROGRESS' || c.status === 'ASSIGNED';
    if (filter === 'NEW') return c.status === 'NEW' || c.status === 'UNDER_REVIEW';
    return true;
  });

  const handleFeedbackSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedTicket) return;
    addCitizenFeedback(selectedTicket.id, feedbackRating, feedbackNotes);
    success('Feedback Logged', 'Thank you for verifying your civic complaint resolution.');
    setSelectedTicket(null);
  };

  return (
    <div className="space-y-6 select-none font-sans">
      {/* Page Header */}
      <div className="bg-white p-5 rounded-xl border border-surface-border shadow-civic flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-city-forest">My Civic Grievances & Service Requests</h1>
          <p className="text-xs text-city-charcoal/70 mt-0.5">
            Track all submitted municipal complaints, department assignments, and resolution progress.
          </p>
        </div>

        {onOpenReportModal && (
          <button
            onClick={onOpenReportModal}
            className="flex items-center space-x-2 px-4 py-2 rounded-lg bg-city-terracotta hover:bg-city-terracotta-dark text-white text-xs font-bold shadow-civic border border-city-amber/30 transition-colors"
          >
            <PlusCircle className="w-4 h-4" />
            <span>Lodge New Grievance</span>
          </button>
        )}
      </div>

      {/* Filter & Search Bar */}
      <div className="bg-white p-4 rounded-xl border border-surface-border shadow-civic flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        {/* Status Filters */}
        <div className="flex items-center space-x-2 overflow-x-auto pb-1 sm:pb-0">
          {(['ALL', 'NEW', 'IN_PROGRESS', 'RESOLVED'] as const).map((tab) => (
            <button
              key={tab}
              onClick={() => setFilter(tab)}
              className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-colors shrink-0 ${
                filter === tab
                  ? 'bg-city-terracotta text-white shadow-civic'
                  : 'bg-surface-muted text-city-charcoal/70 hover:bg-city-sand/30'
              }`}
            >
              {tab === 'ALL' ? 'All Requests' : tab === 'NEW' ? 'New / Pending' : tab === 'IN_PROGRESS' ? 'In Progress' : 'Resolved'}
            </button>
          ))}
        </div>

        {/* Search */}
        <div className="relative min-w-[240px]">
          <Search className="w-4 h-4 text-city-charcoal/40 absolute left-3 top-2.5" />
          <input
            type="text"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search by ticket # or keyword..."
            className="w-full pl-9 pr-3 py-1.5 rounded-lg border border-surface-border text-xs text-city-charcoal focus:outline-none focus:ring-1 focus:ring-city-terracotta"
          />
        </div>
      </div>

      {/* Complaints List */}
      <div className="space-y-3">
        {filtered.length === 0 ? (
          <div className="bg-white p-12 rounded-xl border border-surface-border shadow-civic text-center space-y-2">
            <AlertCircle className="w-8 h-8 text-city-charcoal/30 mx-auto" />
            <p className="text-sm font-bold text-city-forest">No complaints match your filter</p>
            <p className="text-xs text-city-charcoal/60">
              Try adjusting your search terms or status filter above.
            </p>
          </div>
        ) : (
          filtered.map((ticket) => (
            <div
              key={ticket.id}
              onClick={() => setSelectedTicket(ticket)}
              className="bg-white p-4 sm:p-5 rounded-xl border border-surface-border shadow-civic hover:border-city-terracotta transition-all cursor-pointer flex flex-col sm:flex-row sm:items-center justify-between gap-4 group"
            >
              <div className="space-y-2 min-w-0">
                <div className="flex items-center space-x-2.5 flex-wrap gap-y-1">
                  <span className="font-mono text-xs font-bold text-city-terracotta">
                    {ticket.ticket_number}
                  </span>
                  <Badge status={ticket.status}>{ticket.status}</Badge>
                  <span className="text-[11px] font-mono px-2 py-0.5 rounded bg-surface-muted text-city-charcoal border border-surface-border">
                    {ticket.department_id}
                  </span>
                  <span className="text-[11px] text-city-charcoal/60">
                    Logged {new Date(ticket.created_at).toLocaleDateString('en-IN', { day: '2-digit', month: 'short' })}
                  </span>
                </div>

                <h3 className="text-sm font-bold text-city-forest group-hover:text-city-terracotta transition-colors">
                  {ticket.title}
                </h3>

                <p className="text-xs text-city-charcoal/70 flex items-center space-x-1.5">
                  <MapPin className="w-3.5 h-3.5 text-city-terracotta shrink-0" />
                  <span className="truncate">{ticket.location_address}</span>
                  <span className="text-surface-border">•</span>
                  <span>Ward {ticket.ward_number || 4}</span>
                </p>
              </div>

              <div className="flex sm:flex-col items-center sm:items-end justify-between shrink-0 pt-2 sm:pt-0 border-t sm:border-t-0 border-surface-border">
                <span className="text-[11px] text-city-charcoal/60">Priority Level</span>
                <Badge status={ticket.priority}>{ticket.priority}</Badge>
                <div className="hidden sm:flex items-center text-xs text-city-terracotta font-medium mt-2 group-hover:translate-x-1 transition-transform">
                  <span>View Details</span>
                  <ChevronRight className="w-3.5 h-3.5" />
                </div>
              </div>
            </div>
          ))
        )}
      </div>

      {/* Ticket Detail & Feedback Drawer/Modal */}
      {selectedTicket && (
        <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl border border-surface-border shadow-civic-lg max-w-lg w-full p-6 space-y-5 overflow-hidden">
            <div className="flex items-center justify-between pb-3 border-b border-surface-border">
              <div>
                <span className="font-mono text-xs font-bold text-city-terracotta">
                  {selectedTicket.ticket_number}
                </span>
                <h3 className="text-base font-bold text-city-forest mt-0.5">{selectedTicket.title}</h3>
              </div>
              <button
                onClick={() => setSelectedTicket(null)}
                className="p-1.5 rounded-lg hover:bg-surface-muted text-city-charcoal/60 hover:text-city-charcoal"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            <div className="space-y-3 text-xs">
              <div>
                <span className="font-semibold text-city-forest">Description:</span>
                <p className="text-city-charcoal/80 mt-1 leading-relaxed bg-surface-card p-3 rounded-lg border border-surface-border">
                  {selectedTicket.description}
                </p>
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div className="p-2.5 rounded-lg bg-surface-card border border-surface-border">
                  <span className="text-city-charcoal/60">Department</span>
                  <p className="font-bold text-city-forest mt-0.5">{selectedTicket.department_id}</p>
                </div>
                <div className="p-2.5 rounded-lg bg-surface-card border border-surface-border">
                  <span className="text-city-charcoal/60">Current Status</span>
                  <div className="mt-0.5">
                    <Badge status={selectedTicket.status}>{selectedTicket.status}</Badge>
                  </div>
                </div>
              </div>

              <div className="p-2.5 rounded-lg bg-surface-card border border-surface-border">
                <span className="text-city-charcoal/60">Location & Ward</span>
                <p className="font-medium text-city-charcoal mt-0.5 flex items-center space-x-1">
                  <MapPin className="w-3.5 h-3.5 text-city-terracotta" />
                  <span>{selectedTicket.location_address} (Ward {selectedTicket.ward_number || 4})</span>
                </p>
              </div>

              {/* Feedback section if resolved */}
              {(selectedTicket.status === 'RESOLVED' || selectedTicket.status === 'CLOSED') && (
                <div className="pt-2 border-t border-surface-border">
                  <form onSubmit={handleFeedbackSubmit} className="space-y-3">
                    <label className="block font-bold text-city-forest">
                      Citizen Resolution Verification
                    </label>
                    <div className="flex items-center space-x-1">
                      {[1, 2, 3, 4, 5].map((star) => (
                        <button
                          key={star}
                          type="button"
                          onClick={() => setFeedbackRating(star)}
                          className="p-1 text-city-amber"
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
                    <input
                      type="text"
                      value={feedbackNotes}
                      onChange={(e) => setFeedbackNotes(e.target.value)}
                      placeholder="Comment on repair speed or quality..."
                      className="w-full px-3 py-2 rounded-lg border border-surface-border text-xs text-city-charcoal"
                    />
                    <button
                      type="submit"
                      className="w-full py-2.5 rounded-lg bg-city-terracotta hover:bg-city-terracotta-dark text-white text-xs font-bold shadow-civic transition-colors"
                    >
                      Submit Rating & Verification
                    </button>
                  </form>
                </div>
              )}
            </div>

            <div className="pt-2 border-t border-surface-border flex justify-end">
              <button
                onClick={() => setSelectedTicket(null)}
                className="px-4 py-2 rounded-lg border border-surface-border text-xs font-semibold text-city-charcoal hover:bg-surface-muted"
              >
                Close Drawer
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
