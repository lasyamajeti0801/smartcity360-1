import React, { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { Badge } from '../../components/ui/Badge';
import { Button } from '../../components/ui/Button';
import { Table, Column } from '../../components/ui/Table';
import { useToast } from '../../context/ToastContext';
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
  const { addToast } = useToast();
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
      render: (c) => <span className="font-mono font-bold text-city-forest text-xs">{c.national_id}</span>,
    },
    {
      key: 'full_name',
      header: 'Resident Profile',
      render: (c) => (
        <div>
          <div className="font-bold text-city-charcoal">{c.full_name}</div>
          <div className="text-[11px] text-city-charcoal/70 flex items-center space-x-2 mt-0.5">
            <span className="flex items-center"><Mail className="h-3 w-3 mr-1 text-city-charcoal/50" />{c.email}</span>
            <span className="flex items-center"><Phone className="h-3 w-3 mr-1 text-city-charcoal/50" />{c.phone}</span>
          </div>
        </div>
      ),
    },
    {
      key: 'ward',
      header: 'Ward Jurisdiction',
      render: (c) => (
        <div>
          <span className="inline-block bg-city-forest/10 text-city-forest px-2 py-0.5 rounded text-xs font-semibold border border-city-forest/20">
            Ward {c.ward}
          </span>
          <div className="text-[11px] text-city-charcoal/60 mt-0.5 truncate max-w-xs">{c.address}</div>
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
        <span className={`text-xs font-bold ${c.active_complaints > 0 ? 'text-city-terracotta' : 'text-city-charcoal/40'}`}>
          {c.active_complaints} active
        </span>
      ),
    },
    {
      key: 'registered_date',
      header: 'Registered',
      render: (c) => <span className="text-[11px] font-mono text-city-charcoal/60">{c.registered_date}</span>,
    },
  ];

  return (
    <div className="space-y-6">
      {/* Header Banner */}
      <div className="bg-gradient-to-r from-city-forest to-city-charcoal text-white rounded-xl p-5 border border-city-forest/40 shadow-md flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <Users className="h-5 w-5 text-city-amber" />
            <h1 className="text-lg font-bold tracking-tight text-white">
              Municipal Citizen Registry & Resident Services
            </h1>
          </div>
          <p className="text-xs text-city-ivory/80 mt-1">
            Centralized database of verified civic residents, ward allocations, linked complaints, and property tax accounts.
          </p>
        </div>
        <div className="flex items-center space-x-2">
          <Button
            variant="outline"
            size="sm"
            onClick={() => addToast('Exporting Citizen Registry CSV...', 'info')}
            className="bg-white/10 hover:bg-white/20 text-city-ivory border-white/20 text-xs"
          >
            <Download className="h-3.5 w-3.5 mr-1" />
            Export CSV
          </Button>
          <Button
            variant="primary"
            size="sm"
            onClick={() => addToast('Resident registration form opened', 'info')}
            className="bg-city-terracotta hover:bg-city-terracotta/90 text-white font-semibold text-xs border-0"
          >
            + Register New Citizen
          </Button>
        </div>
      </div>

      {/* Stats Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-4 gap-4">
        <Card className="border-l-4 border-l-city-terracotta">
          <div className="text-[11px] font-bold text-city-charcoal/60 uppercase">Verified Residents</div>
          <div className="text-2xl font-black text-city-charcoal mt-0.5">148,920</div>
          <div className="text-[10px] text-city-forest font-semibold mt-0.5">99.2% Aadhaar / ID verified</div>
        </Card>
        <Card className="border-l-4 border-l-city-forest">
          <div className="text-[11px] font-bold text-city-charcoal/60 uppercase">Active Municipal Wards</div>
          <div className="text-2xl font-black text-city-charcoal mt-0.5">16 Wards</div>
          <div className="text-[10px] text-city-charcoal/60 mt-0.5">Metropolitan Urban District</div>
        </Card>
        <Card className="border-l-4 border-l-city-amber">
          <div className="text-[11px] font-bold text-city-charcoal/60 uppercase">Pending KYC Verification</div>
          <div className="text-2xl font-black text-city-amber mt-0.5">342</div>
          <div className="text-[10px] text-city-charcoal/60 mt-0.5">Under ward supervisor review</div>
        </Card>
        <Card className="border-l-4 border-l-city-ochre">
          <div className="text-[11px] font-bold text-city-charcoal/60 uppercase">Avg Citizen Satisfaction</div>
          <div className="text-2xl font-black text-city-forest mt-0.5">4.8 / 5.0</div>
          <div className="text-[10px] text-city-charcoal/60 mt-0.5">Based on post-resolution feedback</div>
        </Card>
      </div>

      {/* Filter and Table Card */}
      <Card
        title="Citizen Registry"
        subtitle="Search and filter verified metropolitan citizens across all city wards."
        action={
          <div className="flex flex-wrap items-center gap-2">
            <div className="relative w-64">
              <Search className="absolute left-2.5 top-2.5 h-3.5 w-3.5 text-city-charcoal/40" />
              <input
                type="text"
                placeholder="Search by Name, ID, Email, Ward..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full bg-surface-card border border-surface-border rounded-md pl-8 pr-3 py-1.5 text-xs text-city-charcoal placeholder-city-charcoal/40 focus:outline-none focus:ring-2 focus:ring-city-terracotta"
              />
            </div>
            <select
              value={selectedWard}
              onChange={(e) => setSelectedWard(e.target.value)}
              className="bg-surface-card border border-surface-border rounded-md px-2.5 py-1.5 text-xs text-city-charcoal focus:outline-none focus:ring-2 focus:ring-city-terracotta"
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
