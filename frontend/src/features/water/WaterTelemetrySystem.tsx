import React, { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { Badge } from '../../components/ui/Badge';
import { Button } from '../../components/ui/Button';
import { Table, Column } from '../../components/ui/Table';
import {
  Droplets,
  RefreshCw
} from 'lucide-react';

interface ReservoirData {
  id: string;
  name: string;
  capacity_ml: number;
  current_level_pct: number;
  wqi_score: number;
  wqi_grade: 'EXCELLENT' | 'GOOD' | 'FAIR' | 'POOR';
  supply_hours_daily: number;
}

interface PipelineNode {
  id: string;
  node_code: string;
  zone: string;
  pressure_psi: number;
  flow_rate_lps: number;
  leak_detected: boolean;
  status: 'STABLE' | 'ELEVATED' | 'LEAK_WARNING';
}

export const WaterTelemetrySystem: React.FC = () => {
  const [reservoirs] = useState<ReservoirData[]>([
    {
      id: 'r1',
      name: 'Central Metropolitan Reservoir (Cauvery Main)',
      capacity_ml: 1250,
      current_level_pct: 88,
      wqi_score: 94,
      wqi_grade: 'EXCELLENT',
      supply_hours_daily: 24,
    },
    {
      id: 'r2',
      name: 'North Sector Elevated Storage Reservoir',
      capacity_ml: 450,
      current_level_pct: 76,
      wqi_score: 91,
      wqi_grade: 'EXCELLENT',
      supply_hours_daily: 20,
    },
    {
      id: 'r3',
      name: 'East Tech Park Balancing Tank',
      capacity_ml: 320,
      current_level_pct: 69,
      wqi_score: 87,
      wqi_grade: 'GOOD',
      supply_hours_daily: 24,
    },
    {
      id: 'r4',
      name: 'South Industrial Supply Lake',
      capacity_ml: 600,
      current_level_pct: 82,
      wqi_score: 83,
      wqi_grade: 'GOOD',
      supply_hours_daily: 18,
    },
  ]);

  const [nodes, setNodes] = useState<PipelineNode[]>([
    {
      id: 'p1',
      node_code: 'NODE-PRS-W4A',
      zone: 'Indiranagar Main Line',
      pressure_psi: 58,
      flow_rate_lps: 420,
      leak_detected: false,
      status: 'STABLE',
    },
    {
      id: 'p2',
      node_code: 'NODE-PRS-W7B',
      zone: 'Koramangala 80ft Road',
      pressure_psi: 32,
      flow_rate_lps: 680,
      leak_detected: true,
      status: 'LEAK_WARNING',
    },
    {
      id: 'p3',
      node_code: 'NODE-PRS-W2C',
      zone: 'Commercial Sector Feeder',
      pressure_psi: 62,
      flow_rate_lps: 310,
      leak_detected: false,
      status: 'STABLE',
    },
    {
      id: 'p4',
      node_code: 'NODE-PRS-W9A',
      zone: 'Lakeside Trunk Line',
      flow_rate_lps: 510,
      pressure_psi: 55,
      leak_detected: false,
      status: 'STABLE',
    },
  ]);

  const handleBalancePressure = () => {
    setNodes((prev) =>
      prev.map((n) => ({
        ...n,
        pressure_psi: 56,
        leak_detected: false,
        status: 'STABLE',
      }))
    );
    alert('SCADA hydraulic pressure auto-balancing executed across municipal trunk lines.');
  };

  const reservoirCols: Column<ReservoirData>[] = [
    {
      key: 'name',
      header: 'Reservoir / Balancing Tank',
      render: (r) => (
        <div>
          <div className="font-bold text-slate-900">{r.name}</div>
          <div className="text-[11px] text-slate-500 font-mono">
            {r.capacity_ml} Million Liters (ML) capacity
          </div>
        </div>
      ),
    },
    {
      key: 'current_level_pct',
      header: 'Water Storage Level',
      render: (r) => (
        <div className="w-28">
          <div className="flex justify-between text-[10px] font-mono mb-0.5 font-bold text-slate-700">
            <span>{r.current_level_pct}%</span>
            <span>{((r.capacity_ml * r.current_level_pct) / 100).toFixed(0)} ML</span>
          </div>
          <div className="w-full bg-slate-200 rounded-full h-2 overflow-hidden">
            <div
              className={`h-2 rounded-full ${
                r.current_level_pct > 75 ? 'bg-teal-600' : r.current_level_pct > 40 ? 'bg-amber-500' : 'bg-red-500'
              }`}
              style={{ width: `${r.current_level_pct}%` }}
            />
          </div>
        </div>
      ),
    },
    {
      key: 'wqi_score',
      header: 'Water Quality (WQI)',
      render: (r) => (
        <div>
          <div className="font-bold text-xs text-slate-900">{r.wqi_score} / 100</div>
          <Badge status="GOOD">{r.wqi_grade}</Badge>
        </div>
      ),
    },
    {
      key: 'supply_hours_daily',
      header: 'Supply Schedule',
      render: (r) => (
        <span className="font-mono text-xs text-slate-700 font-semibold">
          {r.supply_hours_daily} hrs/day
        </span>
      ),
    },
  ];

  const nodeCols: Column<PipelineNode>[] = [
    {
      key: 'node_code',
      header: 'Sensor Code',
      render: (n) => <span className="font-mono font-bold text-teal-800 text-xs">{n.node_code}</span>,
    },
    {
      key: 'zone',
      header: 'Pipeline Zone',
      render: (n) => <span className="font-semibold text-slate-900 text-xs">{n.zone}</span>,
    },
    {
      key: 'pressure_psi',
      header: 'Hydraulic Pressure',
      render: (n) => (
        <span className={`font-mono font-bold text-xs ${n.pressure_psi < 40 ? 'text-red-600' : 'text-slate-800'}`}>
          {n.pressure_psi} PSI
        </span>
      ),
    },
    {
      key: 'flow_rate_lps',
      header: 'Flow Rate',
      render: (n) => <span className="font-mono text-xs text-slate-600">{n.flow_rate_lps} L/s</span>,
    },
    {
      key: 'status',
      header: 'Telemetry State',
      render: (n) => (
        <Badge status={n.status === 'STABLE' ? 'RESOLVED' : 'CRITICAL'}>
          {n.status}
        </Badge>
      ),
    },
  ];

  return (
    <div className="space-y-6">
      {/* Header Banner */}
      <div className="bg-slate-900 text-white rounded-xl p-5 border border-slate-800 shadow-md flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <Droplets className="h-5 w-5 text-teal-400" />
            <h1 className="text-lg font-bold tracking-tight text-white">
              Smart Water Supply & SCADA Telemetry Network
            </h1>
          </div>
          <p className="text-xs text-slate-300 mt-1">
            Real-time reservoir capacities, water quality index (WQI) testing, hydraulic pipe pressures, and automated leak detection.
          </p>
        </div>
        <div className="flex items-center space-x-2">
          <Button
            size="sm"
            variant="primary"
            onClick={handleBalancePressure}
            className="bg-teal-600 hover:bg-teal-500 text-xs"
          >
            <RefreshCw className="h-3.5 w-3.5 mr-1" />
            Auto-Balance Pressure
          </Button>
        </div>
      </div>

      {/* KPI Stats */}
      <div className="grid grid-cols-1 sm:grid-cols-4 gap-4">
        <Card className="border-l-4 border-l-teal-600">
          <div className="text-[11px] font-bold text-slate-500 uppercase">Total City Water Storage</div>
          <div className="text-2xl font-black text-slate-900 mt-0.5">2,620 ML</div>
          <div className="text-[10px] text-emerald-600 font-semibold mt-0.5">82.4% aggregate capacity</div>
        </Card>
        <Card className="border-l-4 border-l-sky-600">
          <div className="text-[11px] font-bold text-slate-500 uppercase">Daily Drinking Supply</div>
          <div className="text-2xl font-black text-slate-900 mt-0.5">490 MLD</div>
          <div className="text-[10px] text-slate-500 mt-0.5">135 Liters per capita per day</div>
        </Card>
        <Card className="border-l-4 border-l-emerald-600">
          <div className="text-[11px] font-bold text-slate-500 uppercase">Potable Water Quality Index</div>
          <div className="text-2xl font-black text-emerald-600 mt-0.5">91.5 / 100</div>
          <div className="text-[10px] text-emerald-600 font-semibold mt-0.5">Grade A (Statutory Potable)</div>
        </Card>
        <Card className="border-l-4 border-l-amber-500">
          <div className="text-[11px] font-bold text-slate-500 uppercase">Non-Revenue Water / Leaks</div>
          <div className="text-2xl font-black text-amber-600 mt-0.5">9.8%</div>
          <div className="text-[10px] text-slate-500 mt-0.5">Well under 15% national target</div>
        </Card>
      </div>

      {/* Tables Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <div className="lg:col-span-7 space-y-4">
          <Card
            title="City Water Reservoirs & Storage Assets"
            subtitle="Live SCADA level gauges and automated laboratory quality verification."
          >
            <Table
              columns={reservoirCols}
              data={reservoirs}
              keyExtractor={(r) => r.id}
            />
          </Card>
        </div>

        <div className="lg:col-span-5 space-y-4">
          <Card
            title="Trunk Pipeline Pressure Telemetry"
            subtitle="Pressure and flow velocity transducers detecting underground burst anomalies."
          >
            <Table
              columns={nodeCols}
              data={nodes}
              keyExtractor={(n) => n.id}
            />
          </Card>
        </div>
      </div>
    </div>
  );
};
