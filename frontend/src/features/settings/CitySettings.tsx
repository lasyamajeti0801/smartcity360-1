import React, { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';
import {
  Settings,
  Server,
  Save,
  CheckCircle2
} from 'lucide-react';

export const CitySettings: React.FC = () => {
  const [cityName, setCityName] = useState('Metropolis Smart City 360');
  const [jurisdictionCode, setJurisdictionCode] = useState('MC-360-KAR');
  const [slaCriticalHours, setSlaCriticalHours] = useState('4');
  const [slaHighHours, setSlaHighHours] = useState('24');
  const [slaMediumHours, setSlaMediumHours] = useState('48');
  const [backendUrl, setBackendUrl] = useState('http://127.0.0.1:8000/api/v1');
  const [isSaved, setIsSaved] = useState(false);

  const handleSave = (e: React.FormEvent) => {
    e.preventDefault();
    setIsSaved(true);
    setTimeout(() => setIsSaved(false), 3000);
  };

  return (
    <div className="space-y-6">
      {/* Header Banner */}
      <div className="bg-slate-900 text-white rounded-xl p-5 border border-slate-800 shadow-md flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <Settings className="h-5 w-5 text-teal-400" />
            <h1 className="text-lg font-bold tracking-tight text-white">
              Municipal Platform Configuration & Administration
            </h1>
          </div>
          <p className="text-xs text-slate-300 mt-1">
            Configure city jurisdiction metadata, SLA statutory thresholds, SCADA sensors, and backend API connections.
          </p>
        </div>

        {isSaved && (
          <div className="flex items-center space-x-1.5 bg-emerald-950 text-emerald-300 border border-emerald-700 px-3 py-1.5 rounded-lg text-xs font-semibold">
            <CheckCircle2 className="h-4 w-4 text-emerald-400" />
            <span>Settings Saved & Applied</span>
          </div>
        )}
      </div>

      <form onSubmit={handleSave} className="space-y-6">
        {/* Jurisdiction Card */}
        <Card title="Municipal Jurisdiction Profile" subtitle="Statutory city details and administrative identifiers.">
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
            <div>
              <label className="block font-bold text-slate-900 mb-1">Platform / Corporation Name</label>
              <input
                type="text"
                value={cityName}
                onChange={(e) => setCityName(e.target.value)}
                className="w-full bg-slate-50 border border-slate-300 rounded-md p-2 text-xs text-slate-900 focus:ring-2 focus:ring-teal-500"
              />
            </div>
            <div>
              <label className="block font-bold text-slate-900 mb-1">Jurisdiction Code</label>
              <input
                type="text"
                value={jurisdictionCode}
                onChange={(e) => setJurisdictionCode(e.target.value)}
                className="w-full bg-slate-50 border border-slate-300 rounded-md p-2 text-xs text-slate-900 font-mono focus:ring-2 focus:ring-teal-500"
              />
            </div>
            <div>
              <label className="block font-bold text-slate-900 mb-1">Central Operations Helpline</label>
              <input
                type="text"
                defaultValue="1800-425-3600 (Toll Free)"
                className="w-full bg-slate-50 border border-slate-300 rounded-md p-2 text-xs text-slate-900"
              />
            </div>
            <div>
              <label className="block font-bold text-slate-900 mb-1">GIS Coordinate Datum</label>
              <input
                type="text"
                defaultValue="WGS 84 (EPSG:4326) / OpenStreetMap"
                disabled
                className="w-full bg-slate-100 border border-slate-200 rounded-md p-2 text-xs text-slate-500 font-mono"
              />
            </div>
          </div>
        </Card>

        {/* SLA Limits Card */}
        <Card title="Civic SLA Resolution Limits" subtitle="Enforced turn-around times for municipal department engineers.">
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 text-xs">
            <div>
              <label className="block font-bold text-red-900 mb-1">Critical (Fire / Major Hazard)</label>
              <div className="flex items-center space-x-2">
                <input
                  type="number"
                  value={slaCriticalHours}
                  onChange={(e) => setSlaCriticalHours(e.target.value)}
                  className="w-full bg-slate-50 border border-slate-300 rounded-md p-2 text-xs text-slate-900 font-mono"
                />
                <span className="text-slate-500 font-bold">Hours</span>
              </div>
            </div>
            <div>
              <label className="block font-bold text-amber-900 mb-1">High (Pipeline / Power Fault)</label>
              <div className="flex items-center space-x-2">
                <input
                  type="number"
                  value={slaHighHours}
                  onChange={(e) => setSlaHighHours(e.target.value)}
                  className="w-full bg-slate-50 border border-slate-300 rounded-md p-2 text-xs text-slate-900 font-mono"
                />
                <span className="text-slate-500 font-bold">Hours</span>
              </div>
            </div>
            <div>
              <label className="block font-bold text-slate-900 mb-1">Standard (Sanitation / Potholes)</label>
              <div className="flex items-center space-x-2">
                <input
                  type="number"
                  value={slaMediumHours}
                  onChange={(e) => setSlaMediumHours(e.target.value)}
                  className="w-full bg-slate-50 border border-slate-300 rounded-md p-2 text-xs text-slate-900 font-mono"
                />
                <span className="text-slate-500 font-bold">Hours</span>
              </div>
            </div>
          </div>
        </Card>

        {/* Telemetry Endpoints Card */}
        <Card title="Microservice Infrastructure & Telemetry" subtitle="Active REST endpoints and IoT telemetry streams.">
          <div className="space-y-3 text-xs">
            <div>
              <label className="block font-bold text-slate-900 mb-1">Core FastAPI Gateway Endpoint</label>
              <input
                type="text"
                value={backendUrl}
                onChange={(e) => setBackendUrl(e.target.value)}
                className="w-full bg-slate-50 border border-slate-300 rounded-md p-2 text-xs text-slate-900 font-mono focus:ring-2 focus:ring-teal-500"
              />
            </div>
            <div className="p-3 bg-slate-50 border border-slate-200 rounded-lg flex items-center justify-between">
              <div className="flex items-center space-x-2">
                <Server className="h-4 w-4 text-emerald-600" />
                <span className="font-semibold text-slate-800">FastAPI Telemetry Gateway: Connected</span>
              </div>
              <span className="text-[10px] bg-emerald-100 text-emerald-800 font-mono font-bold px-2 py-0.5 rounded">
                HTTP 200 OK
              </span>
            </div>
          </div>
        </Card>

        {/* Save Button */}
        <div className="flex justify-end">
          <Button
            type="submit"
            variant="primary"
            className="bg-teal-700 hover:bg-teal-600 text-white px-5 py-2 text-xs font-bold"
          >
            <Save className="h-4 w-4 mr-1.5" />
            Save Platform Settings
          </Button>
        </div>
      </form>
    </div>
  );
};
