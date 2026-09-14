import React, { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';
import { useToast } from '../../context/ToastContext';
import {
  Settings,
  Server,
  Save,
  CheckCircle2
} from 'lucide-react';

export const CitySettings: React.FC = () => {
  const { addToast } = useToast();
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
    addToast('Municipal platform settings saved & committed successfully', 'success');
    setTimeout(() => setIsSaved(false), 3500);
  };

  return (
    <div className="space-y-6">
      {/* Header Banner */}
      <div className="bg-gradient-to-r from-city-forest to-city-charcoal text-white rounded-xl p-5 border border-city-forest/40 shadow-md flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <Settings className="h-5 w-5 text-city-amber" />
            <h1 className="text-lg font-bold tracking-tight text-white">
              Municipal Platform Configuration & Administration
            </h1>
          </div>
          <p className="text-xs text-city-ivory/80 mt-1">
            Configure city jurisdiction metadata, SLA statutory thresholds, SCADA sensors, and backend API connections.
          </p>
        </div>

        {isSaved && (
          <div className="flex items-center space-x-1.5 bg-city-forest text-white border border-city-forest/60 px-3 py-1.5 rounded-lg text-xs font-semibold shadow-sm">
            <CheckCircle2 className="h-4 w-4 text-city-amber" />
            <span>Settings Saved & Applied</span>
          </div>
        )}
      </div>

      <form onSubmit={handleSave} className="space-y-6">
        {/* Jurisdiction Card */}
        <Card title="Municipal Jurisdiction Profile" subtitle="Statutory city details and administrative identifiers.">
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
            <div>
              <label className="block font-bold text-city-charcoal mb-1">Platform / Corporation Name</label>
              <input
                type="text"
                value={cityName}
                onChange={(e) => setCityName(e.target.value)}
                className="w-full bg-surface-card border border-surface-border rounded-md p-2 text-xs text-city-charcoal focus:ring-2 focus:ring-city-terracotta focus:border-city-terracotta outline-none transition-all"
              />
            </div>
            <div>
              <label className="block font-bold text-city-charcoal mb-1">Jurisdiction Code</label>
              <input
                type="text"
                value={jurisdictionCode}
                onChange={(e) => setJurisdictionCode(e.target.value)}
                className="w-full bg-surface-card border border-surface-border rounded-md p-2 text-xs text-city-charcoal font-mono focus:ring-2 focus:ring-city-terracotta focus:border-city-terracotta outline-none transition-all"
              />
            </div>
            <div>
              <label className="block font-bold text-city-charcoal mb-1">Central Operations Helpline</label>
              <input
                type="text"
                defaultValue="1800-425-3600 (Toll Free)"
                className="w-full bg-surface-card border border-surface-border rounded-md p-2 text-xs text-city-charcoal focus:ring-2 focus:ring-city-terracotta outline-none"
              />
            </div>
            <div>
              <label className="block font-bold text-city-charcoal mb-1">GIS Coordinate Datum</label>
              <input
                type="text"
                defaultValue="WGS 84 (EPSG:4326) / OpenStreetMap"
                disabled
                className="w-full bg-city-sand/30 border border-surface-border rounded-md p-2 text-xs text-city-charcoal/60 font-mono"
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
                  className="w-full bg-surface-card border border-surface-border rounded-md p-2 text-xs text-city-charcoal font-mono focus:ring-2 focus:ring-city-terracotta outline-none"
                />
                <span className="text-city-charcoal/60 font-bold">Hours</span>
              </div>
            </div>
            <div>
              <label className="block font-bold text-purple-700 mb-1">High (Pipeline / Power Fault)</label>
              <div className="flex items-center space-x-2">
                <input
                  type="number"
                  value={slaHighHours}
                  onChange={(e) => setSlaHighHours(e.target.value)}
                  className="w-full bg-surface-card border border-surface-border rounded-md p-2 text-xs text-city-charcoal font-mono focus:ring-2 focus:ring-city-terracotta outline-none"
                />
                <span className="text-city-charcoal/60 font-bold">Hours</span>
              </div>
            </div>
            <div>
              <label className="block font-bold text-city-charcoal mb-1">Standard (Sanitation / Potholes)</label>
              <div className="flex items-center space-x-2">
                <input
                  type="number"
                  value={slaMediumHours}
                  onChange={(e) => setSlaMediumHours(e.target.value)}
                  className="w-full bg-surface-card border border-surface-border rounded-md p-2 text-xs text-city-charcoal font-mono focus:ring-2 focus:ring-city-terracotta outline-none"
                />
                <span className="text-city-charcoal/60 font-bold">Hours</span>
              </div>
            </div>
          </div>
        </Card>

        {/* Telemetry Endpoints Card */}
        <Card title="Microservice Infrastructure & Telemetry" subtitle="Active REST endpoints and IoT telemetry streams.">
          <div className="space-y-3 text-xs">
            <div>
              <label className="block font-bold text-city-charcoal mb-1">Core FastAPI Gateway Endpoint</label>
              <input
                type="text"
                value={backendUrl}
                onChange={(e) => setBackendUrl(e.target.value)}
                className="w-full bg-surface-card border border-surface-border rounded-md p-2 text-xs text-city-charcoal font-mono focus:ring-2 focus:ring-city-terracotta focus:border-city-terracotta outline-none transition-all"
              />
            </div>
            <div className="p-3 bg-city-forest/5 border border-city-forest/20 rounded-lg flex items-center justify-between">
              <div className="flex items-center space-x-2">
                <Server className="h-4 w-4 text-city-forest" />
                <span className="font-semibold text-city-charcoal">FastAPI Telemetry Gateway: Operational</span>
              </div>
              <span className="text-[10px] bg-city-forest/15 text-city-forest font-mono font-bold px-2 py-0.5 rounded border border-city-forest/20">
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
            className="bg-city-terracotta hover:bg-city-terracotta/90 text-white font-bold px-6 py-2.5 text-xs shadow-md border-0"
          >
            <Save className="h-4 w-4 mr-1.5" />
            Save Platform Settings
          </Button>
        </div>
      </form>
    </div>
  );
};
