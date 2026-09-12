import React, { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { Badge } from '../../components/ui/Badge';
import { Button } from '../../components/ui/Button';
import { Table, Column } from '../../components/ui/Table';
import { Users, Search, Mail, Phone, Download } from 'lucide-react';

interface CitizenRecord {
  id: string;
  national_id: string;
  full_name: string;
  email: string;
  phone: string;
  ward: number;
  address: string;
  status: 'VERIFIED' | 'PENDING' | 'FLAGGED';
  active_complaints: number;
  registered_date: string;
}

export const CitizensDirectory: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedWard, setSelectedWard] = useState<string>('ALL');

  const [citizens] = useState<CitizenRecord[]>([
    {
      id: 'cit-1',
      national_id: 'ID-8839201',
      full_name: 'Priya Sharma',
      email: 'priya.sharma@example.gov.in',
      phone: '+91 98450 12345',
      ward: 4,
      address: 'Plot 18, 4th Cross, Indiranagar',
      status: 'VERIFIED',
      active_complaints: 1,
      registered_date: '2025-03-14',
    },
    {
      id: 'cit-2',
      national_id: 'ID-4491023',
      full_name: 'Rahul Verma',
      email: 'rahul.v@domain.org',
      phone: '+91 97120 99881',
      ward: 7,
      address: '22 Metro View Enclave, Koramangala',
      status: 'VERIFIED',
      active_complaints: 0,
      registered_date: '2025-06-22',
    },
    {
      id: 'cit-3',
      national_id: 'ID-1928374',
      full_name: 'Ananya Rao',
      email: 'ananya.rao@civicmail.in',
      phone: '+91 94480 34112',
      ward: 4,
      address: '105 Green Acres, Ward 4',
      status: 'VERIFIED',
      active_complaints: 2,
      registered_date: '2025-09-01',
    },
    {
      id: 'cit-4',
      national_id: 'ID-9928172',
      full_name: 'David Christopher',
      email: 'david.c@cityworks.net',
      phone: '+91 98110 54321',
      ward: 2,
      address: '77 Residency Road, Central Sector',
      status: 'PENDING',
      active_complaints: 0,
      registered_date: '2026-01-10',
    },
    {
      id: 'cit-5',
      national_id: 'ID-7728190',
      full_name: 'Fatima Sheikh',
      email: 'f.sheikh@urbanconnect.in',
      phone: '+91 98800 76543',
      ward: 9,
      address: '12 Lake View Road, Ward 9',
      status: 'VERIFIED',
      active_complaints: 1,
      registered_date: '2025-11-19',
    },
  ]);

  const filtered = citizens.filter((c) => {
    const matchesSearch =
      c.full_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      c.national_id.toLowerCase().includes(searchTerm.toLowerCase()) ||
      c.email.toLowerCase().includes(searchTerm.toLowerCase()) ||
      c.address.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesWard = selectedWard === 'ALL' || c.ward.toString() === selectedWard;
    return matchesSearch && matchesWard;
  });

  const columns: Column<CitizenRecord>[] = [
    {
      key: 'national_id',
      header: 'Citizen ID',
      render: (c) => <span className="font-mono font-bold text-teal-800 text-xs">{c.national_id}</span>,
    },
    {
      key: 'full_name',
      header: 'Resident Profile',
      render: (c) => (
        <div>
          <div className="font-bold text-slate-900">{c.full_name}</div>
          <div className="text-[11px] text-slate-500 flex items-center space-x-2 mt-0.5">
            <span className="flex items-center"><Mail className="h-3 w-3 mr-1 text-slate-400" />{c.email}</span>
            <span className="flex items-center"><Phone className="h-3 w-3 mr-1 text-slate-400" />{c.phone}</span>
          </div>
        </div>
      ),
    },
    {
      key: 'ward',
      header: 'Ward Jurisdiction',
      render: (c) => (
        <div>
          <span className="inline-block bg-slate-100 text-slate-800 px-2 py-0.5 rounded text-xs font-semibold border border-slate-200">
            Ward {c.ward}
          </span>
          <div className="text-[11px] text-slate-500 mt-0.5 truncate max-w-xs">{c.address}</div>
        </div>
      ),
    },
    {
      key: 'status',
      header: 'Verification Status',
      render: (c) => (
        <Badge status={c.status === 'VERIFIED' ? 'RESOLVED' : 'PENDING'}>
          {c.status}
        </Badge>
      ),
    },
    {
      key: 'active_complaints',
      header: 'Active Grievances',
      render: (c) => (
        <span className={`text-xs font-bold ${c.active_complaints > 0 ? 'text-amber-600' : 'text-slate-400'}`}>
          {c.active_complaints} active
        </span>
      ),
    },
    {
      key: 'registered_date',
      header: 'Registered',
      render: (c) => <span className="text-[11px] font-mono text-slate-500">{c.registered_date}</span>,
    },
  ];

  return (
    <div className="space-y-6">
      {/* Header Banner */}
      <div className="bg-slate-900 text-white rounded-xl p-5 border border-slate-800 shadow-md flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <Users className="h-5 w-5 text-teal-400" />
            <h1 className="text-lg font-bold tracking-tight text-white">
              Municipal Citizen Registry & Resident Services
            </h1>
          </div>
          <p className="text-xs text-slate-300 mt-1">
            Centralized database of verified civic residents, ward allocations, linked complaints, and property tax accounts.
          </p>
        </div>
        <div className="flex items-center space-x-2">
          <Button
            variant="outline"
            size="sm"
            onClick={() => alert('Exporting Citizen Registry CSV...')}
            className="bg-slate-800 hover:bg-slate-700 text-slate-200 border-slate-700 text-xs"
          >
            <Download className="h-3.5 w-3.5 mr-1" />
            Export CSV
          </Button>
          <Button
            variant="primary"
            size="sm"
            onClick={() => alert('Resident registration modal opened')}
            className="bg-teal-600 hover:bg-teal-500 text-xs"
          >
            + Register New Citizen
          </Button>
        </div>
      </div>

      {/* Stats Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-4 gap-4">
        <Card className="border-l-4 border-l-teal-600">
          <div className="text-[11px] font-bold text-slate-500 uppercase">Verified Residents</div>
          <div className="text-2xl font-black text-slate-900 mt-0.5">148,920</div>
          <div className="text-[10px] text-emerald-600 font-semibold mt-0.5">99.2% Aadhaar / ID verified</div>
        </Card>
        <Card className="border-l-4 border-l-sky-600">
          <div className="text-[11px] font-bold text-slate-500 uppercase">Active Municipal Wards</div>
          <div className="text-2xl font-black text-slate-900 mt-0.5">16 Wards</div>
          <div className="text-[10px] text-slate-500 mt-0.5">Metropolitan Urban District</div>
        </Card>
        <Card className="border-l-4 border-l-amber-500">
          <div className="text-[11px] font-bold text-slate-500 uppercase">Pending KYC Verification</div>
          <div className="text-2xl font-black text-amber-600 mt-0.5">342</div>
          <div className="text-[10px] text-slate-500 mt-0.5">Under ward supervisor review</div>
        </Card>
        <Card className="border-l-4 border-l-emerald-600">
          <div className="text-[11px] font-bold text-slate-500 uppercase">Avg Citizen Satisfaction</div>
          <div className="text-2xl font-black text-emerald-600 mt-0.5">4.8 / 5.0</div>
          <div className="text-[10px] text-slate-500 mt-0.5">Based on post-resolution feedback</div>
        </Card>
      </div>

      {/* Filter and Table Card */}
      <Card
        title="Citizen Registry"
        subtitle="Search and filter verified metropolitan citizens across all city wards."
        action={
          <div className="flex flex-wrap items-center gap-2">
            <div className="relative w-64">
              <Search className="absolute left-2.5 top-2.5 h-3.5 w-3.5 text-slate-400" />
              <input
                type="text"
                placeholder="Search by Name, ID, Email, Ward..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full bg-slate-50 border border-slate-300 rounded-md pl-8 pr-3 py-1.5 text-xs text-slate-900 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-teal-500"
              />
            </div>
            <select
              value={selectedWard}
              onChange={(e) => setSelectedWard(e.target.value)}
              className="bg-slate-50 border border-slate-300 rounded-md px-2.5 py-1.5 text-xs text-slate-700 focus:outline-none focus:ring-2 focus:ring-teal-500"
            >
              <option value="ALL">All Wards</option>
              <option value="2">Ward 2 (Commercial)</option>
              <option value="4">Ward 4 (Indiranagar)</option>
              <option value="7">Ward 7 (Koramangala)</option>
              <option value="9">Ward 9 (Lakeside)</option>
            </select>
          </div>
        }
      >
        <Table
          columns={columns}
          data={filtered}
          keyExtractor={(c) => c.id}
          emptyMessage="No citizens match the given search criteria."
        />
      </Card>
    </div>
  );
};
