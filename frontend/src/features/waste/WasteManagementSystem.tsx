import React, { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { Badge } from '../../components/ui/Badge';
import { Button } from '../../components/ui/Button';
import { Table, Column } from '../../components/ui/Table';
import {
  Trash2
} from 'lucide-react';

interface SmartBin {
  id: string;
  bin_code: string;
  ward: number;
  location: string;
  type: 'ORGANIC' | 'RECYCLABLE' | 'GENERAL' | 'HAZARDOUS';
  fill_percentage: number;
  battery_pct: number;
  last_cleared: string;
}

interface WasteTruck {
  id: string;
  truck_code: string;
  ward_assigned: number;
  driver_name: string;
  bins_collected: number;
  capacity_used_pct: number;
  status: 'COLLECTING' | 'EN_ROUTE_DISPOSAL' | 'AVAILABLE';
}

export const WasteManagementSystem: React.FC = () => {
  const [bins, setBins] = useState<SmartBin[]>([
    {
      id: 'b1',
      bin_code: 'BIN-W4-012',
      ward: 4,
      location: '100ft Road Market Square',
      type: 'ORGANIC',
      fill_percentage: 92,
      battery_pct: 88,
      last_cleared: '4 hours ago',
    },
    {
      id: 'b2',
      bin_code: 'BIN-W4-018',
      ward: 4,
      location: 'Indiranagar Metro Station Exit A',
      type: 'RECYCLABLE',
      fill_percentage: 84,
      battery_pct: 95,
      last_cleared: '2 hours ago',
    },
    {
      id: 'b3',
      bin_code: 'BIN-W7-044',
      ward: 7,
      location: 'Koramangala 5th Block Park',
      type: 'GENERAL',
      fill_percentage: 45,
      battery_pct: 79,
      last_cleared: '1 hour ago',
    },
    {
      id: 'b4',
      bin_code: 'BIN-W2-099',
      ward: 2,
      location: 'Commercial Street West Plaza',
      type: 'ORGANIC',
      fill_percentage: 78,
      battery_pct: 64,
      last_cleared: '5 hours ago',
    },
    {
      id: 'b5',
      bin_code: 'BIN-W9-003',
      ward: 9,
      location: 'Lakeside Promenade Entrance',
      type: 'RECYCLABLE',
      fill_percentage: 30,
      battery_pct: 91,
      last_cleared: '30 mins ago',
    },
  ]);

  const [trucks] = useState<WasteTruck[]>([
    {
      id: 't1',
      truck_code: 'TRK-SAN-01',
      ward_assigned: 4,
      driver_name: 'B. Ramesh',
      bins_collected: 38,
      capacity_used_pct: 82,
      status: 'COLLECTING',
    },
    {
      id: 't2',
      truck_code: 'TRK-SAN-04',
      ward_assigned: 7,
      driver_name: 'D. Prakash',
      bins_collected: 44,
      capacity_used_pct: 95,
      status: 'EN_ROUTE_DISPOSAL',
    },
    {
      id: 't3',
      truck_code: 'TRK-SAN-09',
      ward_assigned: 2,
      driver_name: 'S. Kumar',
      bins_collected: 12,
      capacity_used_pct: 25,
      status: 'AVAILABLE',
    },
  ]);

  const handleEmptyBin = (binId: string) => {
    setBins((prev) =>
      prev.map((b) =>
        b.id === binId
          ? { ...b, fill_percentage: 5, last_cleared: 'Just now' }
          : b
      )
    );
  };

  const binCols: Column<SmartBin>[] = [
    {
      key: 'bin_code',
      header: 'Bin Sensor Code',
      render: (b) => <span className="font-mono font-bold text-teal-800 text-xs">{b.bin_code}</span>,
    },
    {
      key: 'location',
      header: 'Location & Ward',
      render: (b) => (
        <div>
          <div className="font-bold text-slate-900">{b.location}</div>
          <div className="text-[11px] text-slate-500">Ward {b.ward}</div>
        </div>
      ),
    },
    {
      key: 'type',
      header: 'Stream Category',
      render: (b) => (
        <span
          className={`text-[10px] font-bold px-2 py-0.5 rounded border ${
            b.type === 'ORGANIC'
              ? 'bg-emerald-50 text-emerald-800 border-emerald-300'
              : b.type === 'RECYCLABLE'
              ? 'bg-sky-50 text-sky-800 border-sky-300'
              : 'bg-slate-100 text-slate-800 border-slate-300'
          }`}
        >
          {b.type}
        </span>
      ),
    },
    {
      key: 'fill_percentage',
      header: 'Fill Level',
      render: (b) => (
        <div className="w-28">
          <div className="flex justify-between text-[10px] font-mono mb-0.5 font-bold">
            <span className={b.fill_percentage >= 85 ? 'text-red-600' : 'text-slate-700'}>
              {b.fill_percentage}%
            </span>
            <span className="text-slate-400">{b.fill_percentage >= 85 ? 'OVERFILL' : 'NORMAL'}</span>
          </div>
          <div className="w-full bg-slate-200 rounded-full h-2 overflow-hidden">
            <div
              className={`h-2 rounded-full ${
                b.fill_percentage >= 85
                  ? 'bg-red-600'
                  : b.fill_percentage >= 60
                  ? 'bg-amber-500'
                  : 'bg-teal-600'
              }`}
              style={{ width: `${b.fill_percentage}%` }}
            />
          </div>
        </div>
      ),
    },
    {
      key: 'last_cleared',
      header: 'Last Emptied',
      render: (b) => <span className="text-[11px] text-slate-500">{b.last_cleared}</span>,
    },
    {
      key: 'id',
      header: 'Dispatch Action',
      render: (b) => (
        <Button
          size="sm"
          variant="outline"
          onClick={() => handleEmptyBin(b.id)}
          className="text-[10px] px-2 py-0.5 h-6 border-slate-300 hover:bg-teal-50 hover:text-teal-800 hover:border-teal-400"
        >
          Dispatch Clear
        </Button>
      ),
    },
  ];

  const truckCols: Column<WasteTruck>[] = [
    {
      key: 'truck_code',
      header: 'Truck Unit',
      render: (t) => <span className="font-mono font-bold text-slate-900 text-xs">{t.truck_code}</span>,
    },
    {
      key: 'driver_name',
      header: 'Assigned Driver',
      render: (t) => (
        <div>
          <div className="font-semibold text-slate-900">{t.driver_name}</div>
          <div className="text-[11px] text-slate-500">Assigned Ward {t.ward_assigned}</div>
        </div>
      ),
    },
    {
      key: 'capacity_used_pct',
      header: 'Payload',
      render: (t) => (
        <div className="font-mono text-xs font-bold text-slate-900">
          {t.capacity_used_pct}% capacity ({t.bins_collected} bins)
        </div>
      ),
    },
    {
      key: 'status',
      header: 'Duty Status',
      render: (t) => (
        <Badge
          status={
            t.status === 'AVAILABLE'
              ? 'RESOLVED'
              : t.status === 'COLLECTING'
              ? 'INVESTIGATING'
              : 'CRITICAL'
          }
        >
          {t.status}
        </Badge>
      ),
    },
  ];

  return (
    <div className="space-y-6">
      {/* Top Banner */}
      <div className="bg-slate-900 text-white rounded-xl p-5 border border-slate-800 shadow-md flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <Trash2 className="h-5 w-5 text-teal-400" />
            <h1 className="text-lg font-bold tracking-tight text-white">
              Municipal Waste & Smart Sanitation Command
            </h1>
          </div>
          <p className="text-xs text-slate-300 mt-1">
            IoT optical waste bin fill telemetry, automated collection truck routing, and circular economy recycling metrics.
          </p>
        </div>
        <div className="flex items-center space-x-2">
          <Button
            size="sm"
            variant="primary"
            onClick={() => {
              setBins((prev) => prev.map((b) => (b.fill_percentage >= 80 ? { ...b, fill_percentage: 5, last_cleared: 'Just now' } : b)));
              alert('Automated collection route optimized and all full bins dispatched!');
            }}
            className="bg-teal-600 hover:bg-teal-500 text-xs"
          >
            ⚡ Optimize Collection Routes
          </Button>
        </div>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-4 gap-4">
        <Card className="border-l-4 border-l-teal-600">
          <div className="text-[11px] font-bold text-slate-500 uppercase">Daily Waste Collected</div>
          <div className="text-2xl font-black text-slate-900 mt-0.5">842 Metric Tons</div>
          <div className="text-[10px] text-emerald-600 font-semibold mt-0.5">100% Ward coverage completed</div>
        </Card>
        <Card className="border-l-4 border-l-emerald-600">
          <div className="text-[11px] font-bold text-slate-500 uppercase">Recycling Diversion</div>
          <div className="text-2xl font-black text-emerald-600 mt-0.5">48.6% Diverted</div>
          <div className="text-[10px] text-slate-500 mt-0.5">Compost & plastic recycling</div>
        </Card>
        <Card className="border-l-4 border-l-amber-500">
          <div className="text-[11px] font-bold text-slate-500 uppercase">Bins Requiring Clearance</div>
          <div className="text-2xl font-black text-amber-600 mt-0.5">
            {bins.filter((b) => b.fill_percentage >= 80).length} Bins
          </div>
          <div className="text-[10px] text-slate-500 mt-0.5">Exceeding 80% fill threshold</div>
        </Card>
        <Card className="border-l-4 border-l-sky-600">
          <div className="text-[11px] font-bold text-slate-500 uppercase">Sanitation Fleet Readiness</div>
          <div className="text-2xl font-black text-slate-900 mt-0.5">42 / 45 Active</div>
          <div className="text-[10px] text-slate-500 mt-0.5">GPS tracked in real-time</div>
        </Card>
      </div>

      {/* Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <div className="lg:col-span-8 space-y-4">
          <Card
            title="IoT Smart Bin Sensors"
            subtitle="Ultrasonic volume sensors transmitting live bin fullness and battery telemetry."
          >
            <Table
              columns={binCols}
              data={bins}
              keyExtractor={(b) => b.id}
            />
          </Card>
        </div>

        <div className="lg:col-span-4 space-y-4">
          <Card
            title="Collection Truck Fleet"
            subtitle="Real-time compaction and payload capacity telemetry."
          >
            <Table
              columns={truckCols}
              data={trucks}
              keyExtractor={(t) => t.id}
            />
          </Card>
        </div>
      </div>
    </div>
  );
};
