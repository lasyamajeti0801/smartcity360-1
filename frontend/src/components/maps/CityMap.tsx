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
            html: `<div style="background-color: #7C3AED; width: 24px; height: 24px; border-radius: 50%; border: 3px solid white; box-shadow: 0 2px 8px rgba(124,58,237,0.5); display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 10px;">★</div>`,
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
          c.priority === 'CRITICAL' || c.priority === 'HIGH' ? '#EF4444' : c.status === 'RESOLVED' ? '#7C3AED' : '#A855F7';
        const icon = L.divIcon({
          className: 'complaint-icon',
          html: `<div style="background-color: ${color}; width: 14px; height: 14px; border-radius: 50%; border: 2px solid white; box-shadow: 0 1px 4px rgba(124,58,237,0.4);"></div>`,
          iconSize: [14, 14],
          iconAnchor: [7, 7],
        });

        const marker = L.marker([c.latitude, c.longitude], { icon });
        marker.bindPopup(`
          <div style="font-family: inherit; font-size: 12px; line-height: 1.4;">
            <div style="font-weight: 700; color: #3B0764; margin-bottom: 2px;">${c.title}</div>
            <div style="color: #6B7280; font-size: 11px; margin-bottom: 4px;">Ticket: <strong>${c.ticket_number}</strong> | Ward ${c.ward_number || 'N/A'}</div>
            <div style="display: inline-block; padding: 2px 6px; font-size: 10px; font-weight: 600; border-radius: 4px; background: #FAF5FF; border: 1px solid #E9D5FF; color: #6B21A8;">Status: ${c.status}</div>
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
          html: `<div style="background-color: #5B21B6; width: 18px; height: 18px; border-radius: 4px; border: 2px solid white; box-shadow: 0 1px 4px rgba(91,33,182,0.4); display: flex; align-items: center; justify-content: center; color: #F3E8FF; font-size: 10px; font-weight: bold;">H</div>`,
          iconSize: [18, 18],
          iconAnchor: [9, 9],
        });

        const marker = L.marker([f.latitude, f.longitude], { icon });
        marker.bindPopup(`
          <div style="font-family: inherit; font-size: 12px;">
            <div style="font-weight: 700; color: #3B0764;">${f.name}</div>
            <div style="color: #6B7280; font-size: 11px;">Category: ${f.category}</div>
            <div style="color: #374151; font-size: 11px; margin-top: 4px;">Phone: ${f.contact_phone}</div>
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
          html: `<div style="background-color: #E11D48; width: 20px; height: 20px; border-radius: 50%; border: 2px solid #FFE4E6; box-shadow: 0 0 8px rgba(225,29,72,0.8); display: flex; align-items: center; justify-content: center; color: white; font-size: 10px; font-weight: bold; animation: pulse 1.5s infinite;">!</div>`,
          iconSize: [20, 20],
          iconAnchor: [10, 10],
        });

        const marker = L.marker([em.latitude, em.longitude], { icon });
        marker.bindPopup(`
          <div style="font-family: inherit; font-size: 12px;">
            <div style="font-weight: 700; color: #E11D48;">EMERGENCY: ${em.title}</div>
            <div style="color: #6B7280; font-size: 11px;">Severity: <strong>${em.severity}</strong></div>
            <div style="color: #374151; font-size: 11px;">Status: ${em.status}</div>
          </div>
        `);
        marker.addTo(markersLayerRef.current!);
      });
    }
  }, [complaints, facilities, emergencies, showComplaints, showFacilities, showEmergencies]);

  return (
    <div className="relative w-full h-full min-h-[420px] rounded-xl border border-purple-200/80 bg-purple-50/30 shadow-sm flex flex-col overflow-hidden">
      {/* Layer Control Header Bar */}
      <div className="absolute top-3 right-3 z-20 bg-white/95 backdrop-blur-sm border border-purple-200 rounded-lg shadow-md p-2 flex items-center space-x-3 text-xs font-medium text-purple-950">
        <div className="flex items-center space-x-1 text-purple-700 mr-1">
          <Layers className="h-3.5 w-3.5 text-purple-600" />
          <span>Layers:</span>
        </div>
        <label className="flex items-center space-x-1.5 cursor-pointer hover:text-purple-600">
          <input
            type="checkbox"
            checked={showComplaints}
            onChange={(e) => setShowComplaints(e.target.checked)}
            className="rounded border-purple-300 text-purple-600 focus:ring-purple-600"
          />
          <span>Complaints ({complaints.length})</span>
        </label>
        <label className="flex items-center space-x-1.5 cursor-pointer hover:text-purple-800">
          <input
            type="checkbox"
            checked={showFacilities}
            onChange={(e) => setShowFacilities(e.target.checked)}
            className="rounded border-purple-300 text-purple-700 focus:ring-purple-700"
          />
          <span>Facilities ({facilities.length})</span>
        </label>
        <label className="flex items-center space-x-1.5 cursor-pointer hover:text-rose-600">
          <input
            type="checkbox"
            checked={showEmergencies}
            onChange={(e) => setShowEmergencies(e.target.checked)}
            className="rounded border-purple-300 text-rose-600 focus:ring-rose-500"
          />
          <span className="text-rose-600 font-semibold">Emergencies ({emergencies.length})</span>
        </label>
      </div>

      {interactiveSelectMode && (
        <div className="absolute bottom-3 left-3 z-20 bg-[#15052A]/95 text-purple-100 border border-purple-500/30 rounded-lg px-3 py-1.5 text-xs font-medium shadow-lg flex items-center space-x-2">
          <MapPin className="h-4 w-4 text-purple-400 animate-bounce" />
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
