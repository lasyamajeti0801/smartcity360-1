import React from 'react';
import { Card } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';
import { Badge } from '../../components/ui/Badge';
import { Table, Column } from '../../components/ui/Table';
import { CityMap } from '../../components/maps/CityMap';
import { Complaint, Facility } from '../../types';
import { AlertCircle, CreditCard, FileCheck2, Clock, CheckCircle2 } from 'lucide-react';

interface CitizenDashboardProps {
  complaints: Complaint[];
  facilities: Facility[];
  onOpenReportModal: () => void;
  onNavigateToServices: () => void;
}

export const CitizenDashboard: React.FC<CitizenDashboardProps> = ({
  complaints,
  facilities,
  onOpenReportModal,
  onNavigateToServices,
}) => {
  const activeCount = complaints.filter(c => c.status !== 'RESOLVED' && c.status !== 'CLOSED').length;
  const resolvedCount = complaints.filter(c => c.status === 'RESOLVED' || c.status === 'CLOSED').length;

  const columns: Column<Complaint>[] = [
    {
      key: 'ticket_number',
      header: 'Ticket #',
      render: (c) => <span className="font-mono font-semibold text-sky-700">{c.ticket_number}</span>,
    },
    {
      key: 'title',
      header: 'Issue Subject',
      render: (c) => (
        <div>
          <div className="font-medium text-slate-900">{c.title}</div>
          <div className="text-xs text-slate-500">{c.location_address}</div>
        </div>
      ),
    },
    {
      key: 'status',
      header: 'Status',
      render: (c) => <Badge status={c.status}>{c.status}</Badge>,
    },
    {
      key: 'priority',
      header: 'Priority',
      render: (c) => <Badge status={c.priority}>{c.priority}</Badge>,
    },
    {
      key: 'created_at',
      header: 'Reported',
      render: (c) => <span className="text-xs text-slate-500">{new Date(c.created_at).toLocaleDateString()}</span>,
    },
  ];

  return (
    <div className="space-y-6">
      {/* Top Banner with Quick Actions */}
      <div className="bg-slate-900 text-white rounded-lg p-6 border border-slate-800 shadow-sm flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold tracking-tight">Citizen Self-Service Portal</h1>
          <p className="text-xs text-slate-400 mt-1 max-w-xl">
            Lodge civic complaints, track municipal service applications, access city maps, and pay property fees in a verified, SLA-backed public system.
          </p>
        </div>
        <div className="flex flex-wrap gap-2.5 shrink-0">
          <Button variant="primary" onClick={onOpenReportModal} className="bg-sky-600 hover:bg-sky-500 text-white border-0">
            <AlertCircle className="h-4 w-4 mr-1.5" />
            Report Civic Issue
          </Button>
          <Button variant="outline" onClick={onNavigateToServices} className="bg-slate-800 text-slate-200 border-slate-700 hover:bg-slate-700">
            <FileCheck2 className="h-4 w-4 mr-1.5" />
            Service Catalog
          </Button>
        </div>
      </div>

      {/* Overview Stat Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <Card className="border-l-4 border-l-sky-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-xs font-semibold text-slate-500 uppercase">My Active Issues</p>
              <h2 className="text-2xl font-bold text-slate-900 mt-1">{activeCount}</h2>
              <p className="text-xs text-slate-500 mt-0.5">Currently with municipal departments</p>
            </div>
            <div className="p-3 bg-sky-50 rounded-md text-sky-700">
              <Clock className="h-6 w-6" />
            </div>
          </div>
        </Card>

        <Card className="border-l-4 border-l-emerald-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-xs font-semibold text-slate-500 uppercase">Resolved Issues</p>
              <h2 className="text-2xl font-bold text-slate-900 mt-1">{resolvedCount}</h2>
              <p className="text-xs text-slate-500 mt-0.5">Remediated & citizen-verified</p>
            </div>
            <div className="p-3 bg-emerald-50 rounded-md text-emerald-700">
              <CheckCircle2 className="h-6 w-6" />
            </div>
          </div>
        </Card>

        <Card className="border-l-4 border-l-purple-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-xs font-semibold text-slate-500 uppercase">Municipal Fees Due</p>
              <h2 className="text-2xl font-bold text-slate-900 mt-1">$0.00</h2>
              <p className="text-xs text-emerald-600 font-medium mt-0.5">All civic property taxes clear</p>
            </div>
            <div className="p-3 bg-purple-50 rounded-md text-purple-700">
              <CreditCard className="h-6 w-6" />
            </div>
          </div>
        </Card>
      </div>

      {/* Main Grid: Recent Tickets & Interactive City Map */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left 7 cols: Table */}
        <div className="lg:col-span-7 space-y-4">
          <Card
            title="My Reported Complaints & Civic Requests"
            subtitle="Track live department investigation, field staff dispatch, and resolution evidence."
            action={
              <button
                onClick={onOpenReportModal}
                className="text-xs font-semibold text-sky-700 hover:text-sky-800 inline-flex items-center"
              >
                + New Report
              </button>
            }
          >
            <Table
              columns={columns}
              data={complaints}
              keyExtractor={(c) => c.id}
              emptyMessage="You have not lodged any civic complaints."
            />
          </Card>
        </div>

        {/* Right 5 cols: Interactive Map */}
        <div className="lg:col-span-5 space-y-4">
          <Card
            title="Neighborhood Civic Map"
            subtitle="Live OpenStreetMap spatial visualization of active civic tickets and public facilities."
          >
            <div className="h-[360px] w-full">
              <CityMap complaints={complaints} facilities={facilities} />
            </div>
            <div className="mt-3 flex items-center justify-between text-xs text-slate-500">
              <span className="flex items-center space-x-1.5">
                <span className="h-2.5 w-2.5 rounded-full bg-red-600 inline-block"></span>
                <span>Critical/High</span>
              </span>
              <span className="flex items-center space-x-1.5">
                <span className="h-2.5 w-2.5 rounded-full bg-amber-500 inline-block"></span>
                <span>In Progress</span>
              </span>
              <span className="flex items-center space-x-1.5">
                <span className="h-2.5 w-2.5 rounded-full bg-emerald-600 inline-block"></span>
                <span>Resolved</span>
              </span>
              <span className="flex items-center space-x-1.5">
                <span className="h-2.5 w-2.5 rounded-sm bg-sky-600 inline-block"></span>
                <span>Hospital/Clinic</span>
              </span>
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
};
