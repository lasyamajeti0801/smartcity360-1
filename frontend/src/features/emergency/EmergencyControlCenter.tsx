import React, { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { Badge } from '../../components/ui/Badge';
import { Button } from '../../components/ui/Button';
import { Table, Column } from '../../components/ui/Table';
import { CityMap } from '../../components/maps/CityMap';
import { EmergencyIncident } from '../../types';
import { Radio } from 'lucide-react';

export const EmergencyControlCenter: React.FC = () => {
  const [incidents] = useState<EmergencyIncident[]>([
    {
      id: 'emg-1',
      incident_number: 'EMG-20260912-004',
      incident_type: 'FIRE_RESCUE',
      severity: 'CRITICAL',
      status: 'RESPONDING',
      title: 'Structural Fire in Multi-Story Commercial Complex',
      description: 'Active smoke and flame reported on 3rd floor. 2 squads on scene conducting evacuation.',
      latitude: 12.9735,
      longitude: 77.5955,
      location_address: '42 Commercial Boulevard, Ward 4',
      caller_name: 'Building Security Dispatch',
      caller_phone: '+1-555-019-9110',
      created_at: '2026-09-12T10:15:00Z',
    },
    {
      id: 'emg-2',
      incident_number: 'EMG-20260912-003',
      incident_type: 'TRAFFIC_COLLISION',
      severity: 'HIGH',
      status: 'CONTAINED',
      title: 'Multi-Vehicle Traffic Accident with Lane Blockage',
      description: 'Two vehicles collided at intersection. Paramedics treating minor injuries. Left 2 lanes blocked.',
      latitude: 12.9698,
      longitude: 77.5912,
      location_address: 'Ring Road Exit 8B',
      caller_name: 'Highway Patrol',
      caller_phone: '+1-555-019-9112',
      created_at: '2026-09-12T09:40:00Z',
    },
  ]);

  const [responseUnits] = useState([
    { id: 'u1', name: 'Rescue Squad #4', type: 'FIRE', station: 'Central Fire House', status: 'ON_SCENE' },
    { id: 'u2', name: 'Medic Ambulance #12', type: 'EMS', station: 'General Hospital Base', status: 'DISPATCHED' },
    { id: 'u3', name: 'Patrol Cruiser #88', type: 'POLICE', station: 'Precinct 1', status: 'AVAILABLE' },
    { id: 'u4', name: 'Heavy Rescue Engine #2', type: 'FIRE', station: 'West Station', status: 'AVAILABLE' },
  ]);

  const columns: Column<EmergencyIncident>[] = [
    {
      key: 'incident_number',
      header: 'Incident ID',
      render: (i) => <span className="font-mono font-bold text-red-700">{i.incident_number}</span>,
    },
    {
      key: 'title',
      header: 'Incident Details',
      render: (i) => (
        <div>
          <div className="font-bold text-slate-900">{i.title}</div>
          <div className="text-xs text-slate-500">{i.location_address}</div>
        </div>
      ),
    },
    {
      key: 'severity',
      header: 'Severity',
      render: (i) => <Badge status={i.severity}>{i.severity}</Badge>,
    },
    {
      key: 'status',
      header: 'Stage',
      render: (i) => <Badge status={i.status}>{i.status}</Badge>,
    },
    {
      key: 'created_at',
      header: 'Elapsed',
      render: (i) => (
        <span className="text-xs font-mono font-medium text-slate-600">
          {new Date(i.created_at).toLocaleTimeString()}
        </span>
      ),
    },
  ];

  return (
    <div className="space-y-6">
      {/* Top Banner with Red Flashing Alert */}
      <div className="bg-red-950 text-white rounded-lg p-5 border border-red-900 shadow-md flex items-center justify-between">
        <div className="flex items-center space-x-3">
          <div className="h-10 w-10 rounded-full bg-red-700 flex items-center justify-center animate-pulse">
            <Radio className="h-5 w-5 text-white" />
          </div>
          <div>
            <h1 className="text-lg font-bold tracking-tight text-white flex items-center space-x-2">
              <span>Municipal 911 / Emergency Operations Command</span>
              <span className="text-[10px] bg-red-600 px-2 py-0.5 rounded font-mono uppercase">Live Dispatch</span>
            </h1>
            <p className="text-xs text-red-200 mt-0.5">
              Real-time incident priority triage, emergency services radio dispatch, and responder squad deployment.
            </p>
          </div>
        </div>

        <Button variant="danger" size="sm" className="bg-red-700 hover:bg-red-600 border-0">
          + New Emergency Dispatch
        </Button>
      </div>

      {/* Grid: Incidents Queue + Responder Units */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left 8 cols: Incident Queue */}
        <div className="lg:col-span-8 space-y-4">
          <Card
            title="Active Emergency Incidents"
            subtitle="Prioritized triage queue sorted by severity and response time SLA."
          >
            <Table
              columns={columns}
              data={incidents}
              keyExtractor={(i) => i.id}
            />
          </Card>

          <Card title="Emergency Spatial Incident Radar" subtitle="Real-time geo-coordinates of active emergencies.">
            <div className="h-[320px] w-full">
              <CityMap emergencies={incidents} />
            </div>
          </Card>
        </div>

        {/* Right 4 cols: Available Units */}
        <div className="lg:col-span-4 space-y-4">
          <Card
            title="Emergency Squad Status"
            subtitle="Live status of municipal fire, ambulance, and police units."
          >
            <div className="space-y-3">
              {responseUnits.map((u) => (
                <div
                  key={u.id}
                  className="p-3 bg-slate-50 border border-slate-200 rounded-md flex items-center justify-between"
                >
                  <div className="space-y-0.5">
                    <div className="text-xs font-bold text-slate-900">{u.name}</div>
                    <div className="text-[11px] text-slate-500">{u.station}</div>
                  </div>
                  <Badge status={u.status === 'AVAILABLE' ? 'GOOD' : 'HIGH'}>
                    {u.status}
                  </Badge>
                </div>
              ))}
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
};
