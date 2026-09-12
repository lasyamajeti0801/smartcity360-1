import React, { useEffect, useRef, useState } from 'react';
import L from 'leaflet';
import { Complaint, Facility, EmergencyIncident } from '../../types';
import { Layers, MapPin } from 'lucide-react';

interface CityMapProps {
  complaints?: Complaint[];
  facilities?: Facility[];
  emergencies?: EmergencyIncident[];
  center?: [number, number];
  zoom?: number;
  onLocationSelect?: (lat: number, lng: number, addressSuggestion?: string) => void;
  interactiveSelectMode?: boolean;
}

export const CityMap: React.FC<CityMapProps> = ({
  complaints = [],
  facilities = [],
  emergencies = [],
  center = [12.9716, 77.5946],
  zoom = 13,
  onLocationSelect,
  interactiveSelectMode = false,
}) => {
  const mapContainerRef = useRef<HTMLDivElement>(null);
  const mapInstanceRef = useRef<L.Map | null>(null);
  const markersLayerRef = useRef<L.LayerGroup | null>(null);
  const selectionMarkerRef = useRef<L.Marker | null>(null);

  const [showComplaints, setShowComplaints] = useState(true);
  const [showFacilities, setShowFacilities] = useState(true);
  const [showEmergencies, setShowEmergencies] = useState(true);
  const [selectedCoord, setSelectedCoord] = useState<[number, number] | null>(null);

  // Initialize Map
  useEffect(() => {
    if (!mapContainerRef.current || mapInstanceRef.current) return;

    const map = L.map(mapContainerRef.current, {
      center: center,
      zoom: zoom,
      zoomControl: true,
    });

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      maxZoom: 19,
    }).addTo(map);

    const markerGroup = L.layerGroup().addTo(map);
    markersLayerRef.current = markerGroup;
    mapInstanceRef.current = map;

    // Handle Map Click for Location Selection
    if (interactiveSelectMode) {
      map.on('click', (e: L.LeafletMouseEvent) => {
        const { lat, lng } = e.latlng;
        setSelectedCoord([lat, lng]);

        if (selectionMarkerRef.current) {
          selectionMarkerRef.current.setLatLng([lat, lng]);
        } else {
          const pinIcon = L.divIcon({
            className: 'custom-pin',
            html: `<div style="background-color: #0284c7; width: 24px; height: 24px; border-radius: 50%; border: 3px solid white; box-shadow: 0 2px 4px rgba(0,0,0,0.3); display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 10px;">★</div>`,
            iconSize: [24, 24],
            iconAnchor: [12, 12],
          });
          selectionMarkerRef.current = L.marker([lat, lng], { icon: pinIcon }).addTo(map);
        }

        if (onLocationSelect) {
          onLocationSelect(lat, lng, `Lat: ${lat.toFixed(4)}, Lon: ${lng.toFixed(4)}`);
        }
      });
    }

    return () => {
      map.remove();
      mapInstanceRef.current = null;
    };
  }, [interactiveSelectMode]);

  // Update Markers Layer
  useEffect(() => {
    if (!markersLayerRef.current || !mapInstanceRef.current) return;
    markersLayerRef.current.clearLayers();

    // 1. Plot Complaints
    if (showComplaints) {
      complaints.forEach((c) => {
        const color =
          c.priority === 'CRITICAL' || c.priority === 'HIGH' ? '#dc2626' : c.status === 'RESOLVED' ? '#16a34a' : '#d97706';
        const icon = L.divIcon({
          className: 'complaint-icon',
          html: `<div style="background-color: ${color}; width: 14px; height: 14px; border-radius: 50%; border: 2px solid white; box-shadow: 0 1px 3px rgba(0,0,0,0.3);"></div>`,
          iconSize: [14, 14],
          iconAnchor: [7, 7],
        });

        const marker = L.marker([c.latitude, c.longitude], { icon });
        marker.bindPopup(`
          <div style="font-family: inherit; font-size: 12px; line-height: 1.4;">
            <div style="font-weight: 700; color: #0f172a; margin-bottom: 2px;">${c.title}</div>
            <div style="color: #64748b; font-size: 11px; margin-bottom: 4px;">Ticket: <strong>${c.ticket_number}</strong> | Ward ${c.ward_number || 'N/A'}</div>
            <div style="display: inline-block; padding: 2px 6px; font-size: 10px; font-weight: 600; border-radius: 4px; background: #f1f5f9; border: 1px solid #cbd5e1;">Status: ${c.status}</div>
          </div>
        `);
        marker.addTo(markersLayerRef.current!);
      });
    }

    // 2. Plot Facilities
    if (showFacilities) {
      facilities.forEach((f) => {
        const icon = L.divIcon({
          className: 'facility-icon',
          html: `<div style="background-color: #0284c7; width: 18px; height: 18px; border-radius: 4px; border: 2px solid white; box-shadow: 0 1px 3px rgba(0,0,0,0.3); display: flex; align-items: center; justify-content: center; color: white; font-size: 10px; font-weight: bold;">H</div>`,
          iconSize: [18, 18],
          iconAnchor: [9, 9],
        });

        const marker = L.marker([f.latitude, f.longitude], { icon });
        marker.bindPopup(`
          <div style="font-family: inherit; font-size: 12px;">
            <div style="font-weight: 700; color: #0f172a;">${f.name}</div>
            <div style="color: #64748b; font-size: 11px;">Category: ${f.category}</div>
            <div style="color: #475569; font-size: 11px; margin-top: 4px;">Phone: ${f.contact_phone}</div>
          </div>
        `);
        marker.addTo(markersLayerRef.current!);
      });
    }

    // 3. Plot Emergencies
    if (showEmergencies) {
      emergencies.forEach((em) => {
        const icon = L.divIcon({
          className: 'emergency-icon',
          html: `<div style="background-color: #991b1b; width: 20px; height: 20px; border-radius: 50%; border: 2px solid #fee2e2; box-shadow: 0 0 8px rgba(220,38,38,0.8); display: flex; align-items: center; justify-content: center; color: white; font-size: 10px; font-weight: bold; animation: pulse 1.5s infinite;">!</div>`,
          iconSize: [20, 20],
          iconAnchor: [10, 10],
        });

        const marker = L.marker([em.latitude, em.longitude], { icon });
        marker.bindPopup(`
          <div style="font-family: inherit; font-size: 12px;">
            <div style="font-weight: 700; color: #991b1b;">EMERGENCY: ${em.title}</div>
            <div style="color: #64748b; font-size: 11px;">Severity: <strong>${em.severity}</strong></div>
            <div style="color: #475569; font-size: 11px;">Status: ${em.status}</div>
          </div>
        `);
        marker.addTo(markersLayerRef.current!);
      });
    }
  }, [complaints, facilities, emergencies, showComplaints, showFacilities, showEmergencies]);

  return (
    <div className="relative w-full h-full min-h-[420px] rounded-md overflow-hidden border border-slate-200 bg-slate-100 shadow-sm flex flex-col">
      {/* Layer Control Header Bar */}
      <div className="absolute top-3 right-3 z-20 bg-white/95 backdrop-blur-sm border border-slate-200 rounded-md shadow-sm p-2 flex items-center space-x-3 text-xs font-medium text-slate-700">
        <div className="flex items-center space-x-1 text-slate-500 mr-1">
          <Layers className="h-3.5 w-3.5" />
          <span>Layers:</span>
        </div>
        <label className="flex items-center space-x-1.5 cursor-pointer hover:text-slate-900">
          <input
            type="checkbox"
            checked={showComplaints}
            onChange={(e) => setShowComplaints(e.target.checked)}
            className="rounded border-slate-300 text-sky-600 focus:ring-sky-500"
          />
          <span>Complaints ({complaints.length})</span>
        </label>
        <label className="flex items-center space-x-1.5 cursor-pointer hover:text-slate-900">
          <input
            type="checkbox"
            checked={showFacilities}
            onChange={(e) => setShowFacilities(e.target.checked)}
            className="rounded border-slate-300 text-sky-600 focus:ring-sky-500"
          />
          <span>Facilities ({facilities.length})</span>
        </label>
        <label className="flex items-center space-x-1.5 cursor-pointer hover:text-slate-900">
          <input
            type="checkbox"
            checked={showEmergencies}
            onChange={(e) => setShowEmergencies(e.target.checked)}
            className="rounded border-slate-300 text-red-600 focus:ring-red-500"
          />
          <span className="text-red-700">Emergencies ({emergencies.length})</span>
        </label>
      </div>

      {interactiveSelectMode && (
        <div className="absolute bottom-3 left-3 z-20 bg-slate-900/90 text-white rounded-md px-3 py-1.5 text-xs font-medium shadow-md flex items-center space-x-2">
          <MapPin className="h-4 w-4 text-sky-400 animate-bounce" />
          <span>
            {selectedCoord
              ? `Pinned Location: ${selectedCoord[0].toFixed(4)}, ${selectedCoord[1].toFixed(4)}`
              : 'Click anywhere on the city grid to set GPS location for your report'}
          </span>
        </div>
      )}

      {/* Leaflet DOM Anchor */}
      <div ref={mapContainerRef} className="w-full h-full flex-1" />
    </div>
  );
};
