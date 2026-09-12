// SmartCity360 - API Client Service & Fallback Provider

import {
  Complaint,
  ComplaintCategory,
  CityKPIs,
  Facility
} from '../types';

const API_BASE_URL = '/api/v1';

// Initial Sample Seed Data for instant frontend interactivity
const MOCK_CATEGORIES: ComplaintCategory[] = [
  { id: '1', code: 'POTHOLE', name: 'Pothole & Road Damage', default_department_code: 'ROADS', default_sla_hours: 48, icon_name: 'Hammer', description: 'Road crater or asphalt failure' },
  { id: '2', code: 'GARBAGE', name: 'Garbage & Waste Overflow', default_department_code: 'SANITATION', default_sla_hours: 24, icon_name: 'Trash2', description: 'Uncollected public garbage' },
  { id: '3', code: 'STREETLIGHT_OUT', name: 'Broken Streetlight', default_department_code: 'ELECTRICAL', default_sla_hours: 36, icon_name: 'LightbulbOff', description: 'Dark lamp post or street outage' },
  { id: '4', code: 'WATER_LEAK', name: 'Water Pipe Leakage', default_department_code: 'WATER', default_sla_hours: 24, icon_name: 'Droplets', description: 'Main pipe burst or water wastage' },
  { id: '5', code: 'TRAFFIC_SIGNAL', name: 'Traffic Signal Malfunction', default_department_code: 'ELECTRICAL', default_sla_hours: 12, icon_name: 'TrafficCone', description: 'Signals off or flashing error' },
];

let mockComplaints: Complaint[] = [
  {
    id: 'c1',
    ticket_number: 'CMP-20260912-A8F1',
    citizen_id: 'cit-1',
    category_id: '1',
    department_id: 'ROADS',
    title: 'Deep asphalt pothole near Metro Station Gate 2',
    description: '15cm crater in the left carriage lane creating severe hazard for two-wheelers and buses.',
    priority: 'HIGH',
    status: 'IN_PROGRESS',
    latitude: 12.9716,
    longitude: 77.5946,
    location_address: 'MG Road Junction, Ward 4',
    ward_number: 4,
    sla_due_at: '2026-09-14T11:00:00Z',
    is_escalated: false,
    created_at: '2026-09-12T08:30:00Z',
    updated_at: '2026-09-12T09:15:00Z',
  },
  {
    id: 'c2',
    ticket_number: 'CMP-20260912-B42C',
    citizen_id: 'cit-1',
    category_id: '2',
    department_id: 'SANITATION',
    title: 'Overflowing commercial waste bin on sidewalk',
    description: 'Trash container overflowing for 48 hours blocking pedestrian walkway.',
    priority: 'MEDIUM',
    status: 'UNDER_REVIEW',
    latitude: 12.9752,
    longitude: 77.5984,
    location_address: 'Market Street Gate 3, Ward 4',
    ward_number: 4,
    sla_due_at: '2026-09-13T12:00:00Z',
    is_escalated: false,
    created_at: '2026-09-12T07:10:00Z',
    updated_at: '2026-09-12T07:10:00Z',
  },
  {
    id: 'c3',
    ticket_number: 'CMP-20260911-E994',
    citizen_id: 'cit-2',
    category_id: '3',
    department_id: 'ELECTRICAL',
    title: 'Cluster of 4 streetlights dark along residential boulevard',
    description: 'Entire residential block completely dark during night hours.',
    priority: 'LOW',
    status: 'RESOLVED',
    latitude: 12.9684,
    longitude: 77.5891,
    location_address: 'Elm Avenue, Sector 7',
    ward_number: 7,
    sla_due_at: '2026-09-12T18:00:00Z',
    is_escalated: false,
    citizen_rating: 5,
    citizen_feedback: 'Technician arrived and replaced the LED modules promptly. Thank you!',
    created_at: '2026-09-11T14:20:00Z',
    updated_at: '2026-09-12T06:00:00Z',
  }
];

export const apiClient = {
  async getKPIs(): Promise<CityKPIs> {
    try {
      const res = await fetch(`${API_BASE_URL}/analytics/kpis`);
      if (res.ok) return await res.json();
    } catch {}
    return {
      total_complaints: mockComplaints.length,
      resolved_complaints: mockComplaints.filter(c => c.status === 'RESOLVED' || c.status === 'CLOSED').length,
      active_complaints: mockComplaints.filter(c => c.status !== 'RESOLVED' && c.status !== 'CLOSED').length,
      resolution_rate_percentage: 66.7,
      sla_compliance_percentage: 94.2,
      active_emergencies: 2,
      active_work_orders: 5,
      average_resolution_hours: 28.5,
    };
  },

  async getCategories(): Promise<ComplaintCategory[]> {
    try {
      const res = await fetch(`${API_BASE_URL}/complaints/categories`);
      if (res.ok) return await res.json();
    } catch {}
    return MOCK_CATEGORIES;
  },

  async getComplaints(): Promise<Complaint[]> {
    try {
      const res = await fetch(`${API_BASE_URL}/complaints`);
      if (res.ok) return await res.json();
    } catch {}
    return mockComplaints;
  },

  async createComplaint(payload: {
    category_id: string;
    title: string;
    description: string;
    latitude: number;
    longitude: number;
    location_address: string;
    ward_number?: number;
  }): Promise<Complaint> {
    const newComp: Complaint = {
      id: `c_${Date.now()}`,
      ticket_number: `CMP-20260912-${Math.random().toString(16).substring(2, 6).toUpperCase()}`,
      citizen_id: 'cit-current',
      category_id: payload.category_id,
      department_id: 'ROADS',
      title: payload.title,
      description: payload.description,
      priority: 'MEDIUM',
      status: 'NEW',
      latitude: payload.latitude,
      longitude: payload.longitude,
      location_address: payload.location_address,
      ward_number: payload.ward_number || 4,
      is_escalated: false,
      created_at: new Date().toISOString(),
      updated_at: new Date().toISOString(),
    };
    mockComplaints = [newComp, ...mockComplaints];
    return newComp;
  },

  async getFacilities(): Promise<Facility[]> {
    return [
      { id: 'f1', facility_code: 'FAC-HOSP-01', name: 'Metropolitan General Hospital', category: 'HOSPITAL', address: '100 Hospital Drive, Ward 2', latitude: 12.9740, longitude: 77.5920, contact_phone: '+1-555-019-1111', operating_hours: '24/7', is_operational: true, is_wheelchair_accessible: true },
      { id: 'f2', facility_code: 'FAC-FIRE-01', name: 'Central Fire & Rescue Station #1', category: 'FIRE_STATION', address: '45 Civic Center Plaza', latitude: 12.9725, longitude: 77.5948, contact_phone: '+1-555-019-2222', operating_hours: '24/7', is_operational: true, is_wheelchair_accessible: true },
      { id: 'f3', facility_code: 'FAC-POLICE-01', name: 'Central Police Precinct HQ', category: 'POLICE', address: '12 Justice Boulevard', latitude: 12.9710, longitude: 77.5960, contact_phone: '+1-555-019-3333', operating_hours: '24/7', is_operational: true, is_wheelchair_accessible: true },
    ];
  }
};
