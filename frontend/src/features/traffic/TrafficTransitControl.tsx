import React, { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { Badge } from '../../components/ui/Badge';
import { Button } from '../../components/ui/Button';
import { Table, Column } from '../../components/ui/Table';
import {
  Car,
  Zap
} from 'lucide-react';

interface CorridorStatus {
  id: string;
  name: string;
  speed_kmh: number;
  congestion_level: 'NORMAL' | 'MODERATE' | 'HEAVY' | 'CRITICAL';
  signal_status: 'AI_OPTIMIZED' | 'MANUAL_OVERRIDE' | 'HOLD';
  active_vehicles_hourly: number;
}

interface TransitVehicle {
  id: string;
  vehicle_number: string;
  route: string;
  driver: string;
  speed: number;
  occupancy_pct: number;
  status: 'ON_TIME' | 'DELAYED' | 'MAINTENANCE';
  power_type: 'EV_ELECTRIC' | 'CNG';
}

export const TrafficTransitControl: React.FC = () => {
  const [corridors, setCorridors] = useState<CorridorStatus[]>([
    {
      id: 'c1',
      name: 'Outer Ring Road (Tech Corridor)',
      speed_kmh: 38,
      congestion_level: 'MODERATE',
      signal_status: 'AI_OPTIMIZED',
      active_vehicles_hourly: 4820,
    },
    {
      id: 'c2',
      name: 'Airport Super Expressway',
      speed_kmh: 74,
      congestion_level: 'NORMAL',
      signal_status: 'AI_OPTIMIZED',
      active_vehicles_hourly: 2950,
    },
    {
      id: 'c3',
      name: 'MG Road & Central Commercial Axis',
      speed_kmh: 18,
      congestion_level: 'HEAVY',
      signal_status: 'MANUAL_OVERRIDE',
      active_vehicles_hourly: 6100,
    },
    {
      id: 'c4',
      name: 'South Metro Flyover Junction',
      speed_kmh: 22,
      congestion_level: 'HEAVY',
      signal_status: 'AI_OPTIMIZED',
      active_vehicles_hourly: 5200,
    },
    {
      id: 'c5',
      name: 'North Industrial Freight Arterial',
      speed_kmh: 52,
      congestion_level: 'NORMAL',
      signal_status: 'AI_OPTIMIZED',
      active_vehicles_hourly: 1840,
    },
  ]);

  const [transitFleet] = useState<TransitVehicle[]>([
    {
      id: 'v1',
      vehicle_number: 'EV-BUS-104',
      route: 'Line 1: Central Station ⇄ Airport',
      driver: 'K. Somanna',
      speed: 42,
      occupancy_pct: 68,
      status: 'ON_TIME',
      power_type: 'EV_ELECTRIC',
    },
    {
      id: 'v2',
      vehicle_number: 'EV-BUS-209',
      route: 'Line 3: Indiranagar Circular',
      driver: 'M. Farhan',
      speed: 24,
      occupancy_pct: 92,
      status: 'DELAYED',
      power_type: 'EV_ELECTRIC',
    },
    {
      id: 'v3',
      vehicle_number: 'CNG-BUS-088',
      route: 'Line 7: Suburb Express',
      driver: 'P. Suresh',
      speed: 55,
      occupancy_pct: 45,
      status: 'ON_TIME',
      power_type: 'CNG',
    },
    {
      id: 'v4',
      vehicle_number: 'EV-BUS-312',
      route: 'Line 2: Tech Park Shuttle',
      driver: 'V. Anand',
      speed: 36,
      occupancy_pct: 84,
      status: 'ON_TIME',
      power_type: 'EV_ELECTRIC',
    },
  ]);

  const toggleSignalAI = (corridorId: string) => {
    setCorridors((prev) =>
      prev.map((c) =>
        c.id === corridorId
          ? {
              ...c,
              signal_status: c.signal_status === 'AI_OPTIMIZED' ? 'MANUAL_OVERRIDE' : 'AI_OPTIMIZED',
            }
          : c
      )
    );
  };

  const corridorCols: Column<CorridorStatus>[] = [
    {
      key: 'name',
      header: 'Arterial Corridor',
      render: (c) => (
        <div>
          <div className="font-bold text-slate-900">{c.name}</div>
          <div className="text-[11px] text-slate-500 font-mono">
            {c.active_vehicles_hourly.toLocaleString()} vehicles/hr
          </div>
        </div>
      ),
    },
    {
      key: 'speed_kmh',
      header: 'Avg Flow Speed',
      render: (c) => (
        <span className="font-mono font-bold text-slate-900 text-xs">{c.speed_kmh} km/h</span>
      ),
    },
    {
      key: 'congestion_level',
      header: 'Congestion Level',
      render: (c) => (
        <Badge
          status={
            c.congestion_level === 'NORMAL'
              ? 'RESOLVED'
              : c.congestion_level === 'MODERATE'
              ? 'INVESTIGATING'
              : 'CRITICAL'
          }
        >
          {c.congestion_level}
        </Badge>
      ),
    },
    {
      key: 'signal_status',
      header: 'Adaptive Signal Cycle',
      render: (c) => (
        <button
          onClick={() => toggleSignalAI(c.id)}
          className={`px-2 py-0.5 rounded text-[11px] font-semibold border transition-all ${
            c.signal_status === 'AI_OPTIMIZED'
              ? 'bg-teal-50 text-teal-800 border-teal-300 hover:bg-teal-100'
              : 'bg-amber-50 text-amber-800 border-amber-300 hover:bg-amber-100'
          }`}
        >
          {c.signal_status === 'AI_OPTIMIZED' ? '● AI Adaptive Wave' : '⚙ Manual Override'}
        </button>
      ),
    },
  ];

  const transitCols: Column<TransitVehicle>[] = [
    {
      key: 'vehicle_number',
      header: 'Vehicle ID',
      render: (v) => <span className="font-mono font-bold text-teal-800 text-xs">{v.vehicle_number}</span>,
    },
    {
      key: 'route',
      header: 'Transit Route',
      render: (v) => (
        <div>
          <div className="font-semibold text-slate-900">{v.route}</div>
          <div className="text-[11px] text-slate-500">Driver: {v.driver}</div>
        </div>
      ),
    },
    {
      key: 'power_type',
      header: 'Propulsion',
      render: (v) => (
        <span className="inline-flex items-center text-[10px] font-bold bg-emerald-50 text-emerald-800 border border-emerald-200 px-1.5 py-0.5 rounded">
          <Zap className="h-3 w-3 mr-0.5 text-emerald-600" />
          {v.power_type}
        </span>
      ),
    },
    {
      key: 'occupancy_pct',
      header: 'Passenger Load',
      render: (v) => (
        <div className="w-24">
          <div className="flex justify-between text-[10px] text-slate-600 font-mono mb-0.5">
            <span>Load</span>
            <span>{v.occupancy_pct}%</span>
          </div>
          <div className="w-full bg-slate-200 rounded-full h-1.5 overflow-hidden">
            <div
              className={`h-1.5 rounded-full ${
                v.occupancy_pct > 85 ? 'bg-red-500' : v.occupancy_pct > 60 ? 'bg-amber-500' : 'bg-teal-600'
              }`}
              style={{ width: `${v.occupancy_pct}%` }}
            />
          </div>
        </div>
      ),
    },
    {
      key: 'status',
      header: 'Schedule State',
      render: (v) => (
        <Badge status={v.status === 'ON_TIME' ? 'RESOLVED' : 'HIGH'}>
          {v.status}
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
            <Car className="h-5 w-5 text-teal-400" />
            <h1 className="text-lg font-bold tracking-tight text-white">
              Intelligent Traffic & Public Transit Command System
            </h1>
          </div>
          <p className="text-xs text-slate-300 mt-1">
            Real-time optical radar telemetry, adaptive signal phase timings, and zero-emission municipal bus fleet tracking.
          </p>
        </div>
        <div className="flex items-center space-x-2">
          <Button
            size="sm"
            variant="outline"
            onClick={() => alert('Green Wave synchronization applied to MG Road')}
            className="bg-slate-800 hover:bg-slate-700 text-teal-300 border-slate-700 text-xs"
          >
            ⚡ Trigger Green Wave
          </Button>
        </div>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-4 gap-4">
        <Card className="border-l-4 border-l-teal-600">
          <div className="text-[11px] font-bold text-slate-500 uppercase">City Congestion Index</div>
          <div className="text-2xl font-black text-slate-900 mt-0.5">32% (Fluid)</div>
          <div className="text-[10px] text-emerald-600 font-semibold mt-0.5">-4.5% vs yesterday peak</div>
        </Card>
        <Card className="border-l-4 border-l-sky-600">
          <div className="text-[11px] font-bold text-slate-500 uppercase">Adaptive Traffic Signals</div>
          <div className="text-2xl font-black text-slate-900 mt-0.5">248 / 250</div>
          <div className="text-[10px] text-slate-500 mt-0.5">99.2% AI sync efficiency</div>
        </Card>
        <Card className="border-l-4 border-l-indigo-600">
          <div className="text-[11px] font-bold text-slate-500 uppercase">Active Transit Fleet</div>
          <div className="text-2xl font-black text-indigo-700 mt-0.5">184 Buses</div>
          <div className="text-[10px] text-slate-500 mt-0.5">91% On-time schedule rate</div>
        </Card>
        <Card className="border-l-4 border-l-emerald-600">
          <div className="text-[11px] font-bold text-slate-500 uppercase">EV Transit Fleet Ratio</div>
          <div className="text-2xl font-black text-emerald-600 mt-0.5">74.2% EV</div>
          <div className="text-[10px] text-emerald-600 font-semibold mt-0.5">Target: 80% by 2027</div>
        </Card>
      </div>

      {/* Grid: Corridors & Bus Fleet */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <div className="lg:col-span-7 space-y-4">
          <Card
            title="Metropolitan Arterial Corridors"
            subtitle="Click signal button to toggle between AI-adaptive coordination and manual hold."
          >
            <Table
              columns={corridorCols}
              data={corridors}
              keyExtractor={(c) => c.id}
            />
          </Card>
        </div>

        <div className="lg:col-span-5 space-y-4">
          <Card
            title="Public Transit Fleet Radar"
            subtitle="Live passenger loading and timetable adherence for municipal bus lines."
          >
            <Table
              columns={transitCols}
              data={transitFleet}
              keyExtractor={(v) => v.id}
            />
          </Card>
        </div>
      </div>
    </div>
  );
};
