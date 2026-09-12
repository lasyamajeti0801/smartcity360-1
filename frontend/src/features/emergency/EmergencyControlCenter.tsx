import React, { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { Badge } from '../../components/ui/Badge';
import { Button } from '../../components/ui/Button';
import { Table, Column } from '../../components/ui/Table';
import { CityMap } from '../../components/maps/CityMap';
import { EmergencyIncident } from '../../types';
import {
  Radio,
  Siren,
  Flame,
  ShieldCheck,
  AlertTriangle,
  MapPin,
  CheckCircle,
  PlusCircle
} from 'lucide-react';

export const EmergencyControlCenter: React.FC = () => {
  const [incidents, setIncidents] = useState<EmergencyIncident[]>([
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

  const [responseUnits, setResponseUnits] = useState([
    { id: 'u1', name: 'Rescue Squad #4', type: 'FIRE', station: 'Central Fire House', status: 'ON_SCENE' },
    { id: 'u2', name: 'Medic Ambulance #12', type: 'EMS', station: 'General Hospital Base', status: 'DISPATCHED' },
    { id: 'u3', name: 'Patrol Cruiser #88', type: 'POLICE', station: 'Precinct 1', status: 'AVAILABLE' },
    { id: 'u4', name: 'Heavy Rescue Engine #2', type: 'FIRE', station: 'West Station', status: 'AVAILABLE' },
    { id: 'u5', name: 'Hazmat Response Unit #1', type: 'HAZMAT', station: 'Industrial Precinct', status: 'AVAILABLE' },
  ]);

  const [isNewDispatchOpen, setIsNewDispatchOpen] = useState(false);
  const [selectedIncident, setSelectedIncident] = useState<EmergencyIncident | null>(null);

  // Form states for new dispatch
  const [newTitle, setNewTitle] = useState('');
  const [newType, setNewType] = useState('FIRE_RESCUE');
  const [newSeverity, setNewSeverity] = useState<'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW'>('CRITICAL');
  const [newLocation, setNewLocation] = useState('');
  const [newDesc, setNewDesc] = useState('');

  const handleCreateDispatch = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newTitle.trim()) return;

    const newInc: EmergencyIncident = {
      id: `emg-${Date.now()}`,
      incident_number: `EMG-20260912-00${incidents.length + 5}`,
      incident_type: newType,
      severity: newSeverity,
      status: 'RESPONDING',
      title: newTitle,
      description: newDesc || 'Urgent 911 dispatch generated from municipal control center.',
      latitude: 12.9716 + (Math.random() - 0.5) * 0.02,
      longitude: 77.5946 + (Math.random() - 0.5) * 0.02,
      location_address: newLocation || 'City Center Sector 3',
      caller_name: 'Municipal Telemetry Sensor',
      caller_phone: '+1-555-019-9119',
      created_at: new Date().toISOString(),
    };

    setIncidents([newInc, ...incidents]);
    setIsNewDispatchOpen(false);
    setNewTitle('');
    setNewDesc('');
    setNewLocation('');
  };

  const handleAdvanceStatus = (id: string, newStatus: string) => {
    setIncidents((prev) =>
      prev.map((inc) => (inc.id === id ? { ...inc, status: newStatus } : inc))
    );
    if (selectedIncident && selectedIncident.id === id) {
      setSelectedIncident((prev) => (prev ? { ...prev, status: newStatus } : null));
    }
  };

  const toggleUnitStatus = (unitId: string) => {
    setResponseUnits((prev) =>
      prev.map((u) => {
        if (u.id !== unitId) return u;
        const nextStatus = u.status === 'AVAILABLE' ? 'DISPATCHED' : u.status === 'DISPATCHED' ? 'ON_SCENE' : 'AVAILABLE';
        return { ...u, status: nextStatus };
      })
    );
  };

  const columns: Column<EmergencyIncident>[] = [
    {
      key: 'incident_number',
      header: 'Incident ID',
      render: (i) => (
        <button
          onClick={() => setSelectedIncident(i)}
          className="font-mono font-bold text-red-700 hover:underline text-xs text-left"
        >
          {i.incident_number}
        </button>
      ),
    },
    {
      key: 'title',
      header: 'Incident Details',
      render: (i) => (
        <div className="max-w-xs">
          <div className="font-bold text-slate-900 truncate">{i.title}</div>
          <div className="text-[11px] text-slate-500 flex items-center mt-0.5">
            <MapPin className="h-3 w-3 mr-1 text-slate-400 shrink-0" />
            <span className="truncate">{i.location_address}</span>
          </div>
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
        <span className="text-[11px] font-mono font-medium text-slate-600">
          {new Date(i.created_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
        </span>
      ),
    },
    {
      key: 'id',
      header: 'Control',
      render: (i) => (
        <div className="flex items-center space-x-1.5">
          {i.status === 'RESPONDING' && (
            <button
              onClick={() => handleAdvanceStatus(i.id, 'ON_SCENE')}
              className="text-[10px] font-semibold bg-amber-500 hover:bg-amber-600 text-white px-2 py-0.5 rounded"
            >
              Mark On-Scene
            </button>
          )}
          {i.status === 'ON_SCENE' && (
            <button
              onClick={() => handleAdvanceStatus(i.id, 'CONTAINED')}
              className="text-[10px] font-semibold bg-teal-600 hover:bg-teal-700 text-white px-2 py-0.5 rounded"
            >
              Mark Contained
            </button>
          )}
          {i.status === 'CONTAINED' && (
            <button
              onClick={() => handleAdvanceStatus(i.id, 'RESOLVED')}
              className="text-[10px] font-semibold bg-emerald-600 hover:bg-emerald-700 text-white px-2 py-0.5 rounded"
            >
              Close
            </button>
          )}
          {i.status === 'RESOLVED' && (
            <span className="text-[11px] text-emerald-700 font-semibold flex items-center">
              <CheckCircle className="h-3 w-3 mr-0.5" /> Cleared
            </span>
          )}
        </div>
      ),
    },
  ];

  return (
    <div className="space-y-6">
      {/* Top Banner with Red Flashing Alert */}
      <div className="bg-gradient-to-r from-red-950 via-slate-900 to-red-900 text-white rounded-xl p-5 border border-red-800 shadow-lg flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div className="flex items-center space-x-3.5">
          <div className="h-11 w-11 rounded-full bg-red-600 flex items-center justify-center animate-pulse shrink-0 ring-4 ring-red-900">
            <Radio className="h-5 w-5 text-white" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <h1 className="text-lg font-bold tracking-tight text-white">
                Municipal 911 & Emergency Operations Command (EOC)
              </h1>
              <span className="text-[10px] bg-red-600 text-white font-mono px-2 py-0.5 rounded font-bold uppercase tracking-wider animate-pulse">
                LIVE DISPATCH
              </span>
            </div>
            <p className="text-xs text-red-200 mt-1">
              Integrated municipal emergency dispatch, real-time vehicle GPS telemetry, and mutual-aid coordination.
            </p>
          </div>
        </div>

        <div className="flex items-center space-x-2.5 shrink-0">
          <Button
            variant="danger"
            size="sm"
            onClick={() => setIsNewDispatchOpen(true)}
            className="bg-red-600 hover:bg-red-500 font-bold text-xs px-3.5 py-2 shadow-md border-0"
          >
            <PlusCircle className="h-4 w-4 mr-1.5" />
            + New Emergency Dispatch
          </Button>
        </div>
      </div>

      {/* KPI Stats Bar */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
        <Card className="border-l-4 border-l-red-600">
          <div className="text-[11px] font-bold uppercase text-slate-500">Active Incidents</div>
          <div className="text-2xl font-black text-red-600 mt-0.5">
            {incidents.filter((i) => i.status !== 'RESOLVED').length}
          </div>
          <div className="text-[10px] text-slate-500 mt-0.5">1 Critical Structural Fire</div>
        </Card>

        <Card className="border-l-4 border-l-amber-500">
          <div className="text-[11px] font-bold uppercase text-slate-500">Average Response Time</div>
          <div className="text-2xl font-black text-slate-900 mt-0.5">4.2 min</div>
          <div className="text-[10px] text-emerald-600 font-semibold mt-0.5">Below 6.0 min statutory goal</div>
        </Card>

        <Card className="border-l-4 border-l-teal-600">
          <div className="text-[11px] font-bold uppercase text-slate-500">Field Squads On-Scene</div>
          <div className="text-2xl font-black text-teal-700 mt-0.5">
            {responseUnits.filter((u) => u.status === 'ON_SCENE' || u.status === 'DISPATCHED').length}
          </div>
          <div className="text-[10px] text-slate-500 mt-0.5">Across all zones</div>
        </Card>

        <Card className="border-l-4 border-l-emerald-600">
          <div className="text-[11px] font-bold uppercase text-slate-500">Available Reserve Units</div>
          <div className="text-2xl font-black text-emerald-700 mt-0.5">
            {responseUnits.filter((u) => u.status === 'AVAILABLE').length}
          </div>
          <div className="text-[10px] text-slate-500 mt-0.5">Ready at municipal bases</div>
        </Card>
      </div>

      {/* Grid: Incidents Queue + Responder Units */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left 8 cols: Incident Queue & Spatial Map */}
        <div className="lg:col-span-8 space-y-4">
          <Card
            title="Active Emergency Incidents"
            subtitle="Prioritized triage queue sorted by severity, location, and responder SLA."
          >
            <Table
              columns={columns}
              data={incidents}
              keyExtractor={(i) => i.id}
            />
          </Card>

          <Card
            title="Emergency Spatial Incident Radar"
            subtitle="Real-time geo-coordinates of active emergencies across municipal sectors."
          >
            <div className="h-[340px] w-full">
              <CityMap emergencies={incidents} />
            </div>
          </Card>
        </div>

        {/* Right 4 cols: Available Units */}
        <div className="lg:col-span-4 space-y-4">
          <Card
            title="Emergency Squad Readiness"
            subtitle="Click any unit to toggle dispatch or on-scene deployment state."
          >
            <div className="space-y-2.5">
              {responseUnits.map((u) => (
                <div
                  key={u.id}
                  onClick={() => toggleUnitStatus(u.id)}
                  className="p-3 bg-slate-50 hover:bg-slate-100 border border-slate-200 rounded-lg flex items-center justify-between cursor-pointer transition-colors"
                >
                  <div className="space-y-0.5">
                    <div className="text-xs font-bold text-slate-900 flex items-center space-x-1.5">
                      {u.type === 'FIRE' && <Flame className="h-3.5 w-3.5 text-red-600" />}
                      {u.type === 'EMS' && <Siren className="h-3.5 w-3.5 text-indigo-600" />}
                      {u.type === 'POLICE' && <ShieldCheck className="h-3.5 w-3.5 text-blue-600" />}
                      {u.type === 'HAZMAT' && <AlertTriangle className="h-3.5 w-3.5 text-amber-600" />}
                      <span>{u.name}</span>
                    </div>
                    <div className="text-[11px] text-slate-500">{u.station}</div>
                  </div>
                  <div className="text-right">
                    <Badge
                      status={
                        u.status === 'AVAILABLE'
                          ? 'GOOD'
                          : u.status === 'ON_SCENE'
                          ? 'HIGH'
                          : 'PENDING'
                      }
                    >
                      {u.status}
                    </Badge>
                    <div className="text-[9px] text-slate-400 mt-1">Tap to cycle</div>
                  </div>
                </div>
              ))}
            </div>
          </Card>

          {/* Quick Dispatch Protocols Card */}
          <Card title="Emergency Standard Operating Protocols" subtitle="Municipal safety directives">
            <div className="space-y-2 text-xs text-slate-600">
              <div className="p-2 bg-red-50 rounded border border-red-200 text-red-900">
                <span className="font-bold">Code Red (Structural Fire):</span> Minimum 2 fire engines + 1 ALS ambulance automatically dispatched within 90 seconds.
              </div>
              <div className="p-2 bg-amber-50 rounded border border-amber-200 text-amber-900">
                <span className="font-bold">Code Amber (Major Collision):</span> Traffic management unit to seal off lanes 200m upstream from accident site.
              </div>
            </div>
          </Card>
        </div>
      </div>

      {/* New Dispatch Modal */}
      {isNewDispatchOpen && (
        <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white rounded-xl shadow-2xl border border-slate-200 max-w-lg w-full overflow-hidden">
            <div className="bg-red-950 text-white p-4 flex items-center justify-between">
              <div className="flex items-center space-x-2">
                <Siren className="h-5 w-5 text-red-400 animate-pulse" />
                <h3 className="text-sm font-bold text-white">Create Immediate 911 Emergency Dispatch</h3>
              </div>
              <button
                onClick={() => setIsNewDispatchOpen(false)}
                className="text-slate-400 hover:text-white text-base font-bold"
              >
                ✕
              </button>
            </div>

            <form onSubmit={handleCreateDispatch} className="p-5 space-y-3.5 text-xs text-slate-700">
              <div>
                <label className="block font-bold text-slate-900 mb-1">Incident Title / Summary *</label>
                <input
                  type="text"
                  required
                  placeholder="e.g. Gas Leak Reported at Metro Station"
                  value={newTitle}
                  onChange={(e) => setNewTitle(e.target.value)}
                  className="w-full bg-slate-50 border border-slate-300 rounded-md p-2 text-xs focus:ring-2 focus:ring-red-500"
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block font-bold text-slate-900 mb-1">Incident Category</label>
                  <select
                    value={newType}
                    onChange={(e) => setNewType(e.target.value)}
                    className="w-full bg-slate-50 border border-slate-300 rounded-md p-2 text-xs"
                  >
                    <option value="FIRE_RESCUE">Fire & Rescue</option>
                    <option value="TRAFFIC_COLLISION">Major Traffic Collision</option>
                    <option value="MEDICAL_ALS">Medical Emergency (ALS)</option>
                    <option value="HAZMAT_LEAK">Hazardous Chemical Leak</option>
                    <option value="CIVIL_DEFENSE">Civil Defense / Structural Failure</option>
                  </select>
                </div>

                <div>
                  <label className="block font-bold text-slate-900 mb-1">Severity Level</label>
                  <select
                    value={newSeverity}
                    onChange={(e) => setNewSeverity(e.target.value as any)}
                    className="w-full bg-slate-50 border border-slate-300 rounded-md p-2 text-xs"
                  >
                    <option value="CRITICAL">CRITICAL (Immediate Threat)</option>
                    <option value="HIGH">HIGH (Urgent Dispatch)</option>
                    <option value="MEDIUM">MEDIUM (Standard Response)</option>
                    <option value="LOW">LOW (Advisory)</option>
                  </select>
                </div>
              </div>

              <div>
                <label className="block font-bold text-slate-900 mb-1">Incident Location Address</label>
                <input
                  type="text"
                  placeholder="e.g. 5th Avenue & Central Mall, Ward 2"
                  value={newLocation}
                  onChange={(e) => setNewLocation(e.target.value)}
                  className="w-full bg-slate-50 border border-slate-300 rounded-md p-2 text-xs"
                />
              </div>

              <div>
                <label className="block font-bold text-slate-900 mb-1">Caller Details & Tactical Notes</label>
                <textarea
                  rows={3}
                  placeholder="Caller remarks, victim count, hazards..."
                  value={newDesc}
                  onChange={(e) => setNewDesc(e.target.value)}
                  className="w-full bg-slate-50 border border-slate-300 rounded-md p-2 text-xs"
                />
              </div>

              <div className="pt-3 border-t border-slate-200 flex items-center justify-end space-x-2">
                <Button
                  type="button"
                  variant="outline"
                  size="sm"
                  onClick={() => setIsNewDispatchOpen(false)}
                >
                  Cancel
                </Button>
                <Button
                  type="submit"
                  variant="danger"
                  size="sm"
                  className="bg-red-700 hover:bg-red-600 font-bold"
                >
                  Deploy Emergency Squads Now
                </Button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Incident Detail Modal */}
      {selectedIncident && (
        <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white rounded-xl shadow-2xl border border-slate-200 max-w-md w-full overflow-hidden">
            <div className="bg-slate-900 text-white p-4 flex items-center justify-between">
              <div>
                <span className="text-[10px] font-mono uppercase bg-red-800 text-red-100 px-2 py-0.5 rounded font-bold">
                  {selectedIncident.incident_number}
                </span>
                <h3 className="text-sm font-bold text-white mt-1">{selectedIncident.title}</h3>
              </div>
              <button
                onClick={() => setSelectedIncident(null)}
                className="text-slate-400 hover:text-white text-base font-bold"
              >
                ✕
              </button>
            </div>

            <div className="p-5 space-y-3 text-xs text-slate-700">
              <div className="grid grid-cols-2 gap-2 bg-slate-50 p-2.5 rounded border border-slate-200">
                <div>
                  <span className="text-[10px] font-bold text-slate-500 uppercase">Severity</span>
                  <div className="mt-0.5"><Badge status={selectedIncident.severity}>{selectedIncident.severity}</Badge></div>
                </div>
                <div>
                  <span className="text-[10px] font-bold text-slate-500 uppercase">Status</span>
                  <div className="mt-0.5"><Badge status={selectedIncident.status}>{selectedIncident.status}</Badge></div>
                </div>
              </div>

              <div>
                <h4 className="font-bold text-slate-900 mb-0.5">Description</h4>
                <p className="p-2.5 bg-slate-50 rounded border border-slate-200">{selectedIncident.description}</p>
              </div>

              <div>
                <h4 className="font-bold text-slate-900 mb-0.5">Caller / Source</h4>
                <div className="flex items-center justify-between p-2 bg-slate-50 rounded border border-slate-200 text-slate-600">
                  <span>{selectedIncident.caller_name || 'Anonymous 911 Call'}</span>
                  <span className="font-mono">{selectedIncident.caller_phone || 'N/A'}</span>
                </div>
              </div>

              <div className="pt-3 border-t border-slate-200 flex justify-end">
                <Button
                  variant="outline"
                  size="sm"
                  onClick={() => setSelectedIncident(null)}
                >
                  Close
                </Button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

