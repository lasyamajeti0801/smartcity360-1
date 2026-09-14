import React, { createContext, useContext, useState, useEffect } from 'react';
import {
  Complaint,
  WorkOrder,
  Facility,
  CityKPIs,
  ComplaintCategory,
  CivicNotification
} from '../types';
import { apiClient } from '../services/api';

interface CityDataContextType {
  complaints: Complaint[];
  workOrders: WorkOrder[];
  facilities: Facility[];
  categories: ComplaintCategory[];
  kpis: CityKPIs;
  notifications: CivicNotification[];
  isLoading: boolean;
  addComplaint: (payload: {
    category_id: string;
    title: string;
    description: string;
    location_address: string;
    ward_number: number;
    latitude: number;
    longitude: number;
    priority?: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
  }) => Promise<Complaint>;
  updateWorkOrderStatus: (
    orderId: string,
    newStatus: string,
    percentage?: number,
    notes?: string
  ) => void;
  addCitizenFeedback: (complaintId: string, rating: number, feedback: string) => void;
  markNotificationAsRead: (notificationId: string) => void;
  refreshData: () => Promise<void>;
}

const CityDataContext = createContext<CityDataContextType | undefined>(undefined);

// Initial Rich Municipal Seed Dataset
const INITIAL_CATEGORIES: ComplaintCategory[] = [
  { id: '1', code: 'POTHOLE', name: 'Pothole & Asphalt Damage', default_department_code: 'ROADS', default_sla_hours: 48, icon_name: 'Hammer', description: 'Road crater, asphalt subsidence, or pothole on carriageway.' },
  { id: '2', code: 'GARBAGE', name: 'Garbage & Waste Overflow', default_department_code: 'SANITATION', default_sla_hours: 24, icon_name: 'Trash2', description: 'Uncollected community dumpster, commercial dumping, or litter.' },
  { id: '3', code: 'STREETLIGHT_OUT', name: 'Streetlight Malfunction', default_department_code: 'ELECTRICAL', default_sla_hours: 36, icon_name: 'LightbulbOff', description: 'Non-functional lamp post, flickering fixture, or dark corridor.' },
  { id: '4', code: 'WATER_LEAK', name: 'Water Pipe Burst / Leakage', default_department_code: 'WATER', default_sla_hours: 24, icon_name: 'Droplets', description: 'Underground pipeline rupture, drinking water waste, or pressure failure.' },
  { id: '5', code: 'DRAINAGE_BLOCK', name: 'Storm Drain Clogging / Flooding', default_department_code: 'ROADS', default_sla_hours: 24, icon_name: 'Waves', description: 'Debris blockage in roadside monsoon gutters causing water accumulation.' },
  { id: '6', code: 'TRAFFIC_SIGNAL', name: 'Traffic Signal Grid Outage', default_department_code: 'ELECTRICAL', default_sla_hours: 12, icon_name: 'TrafficCone', description: 'Intersectional traffic light power failure or unsynchronized phasing.' },
];

const INITIAL_COMPLAINTS: Complaint[] = [
  {
    id: 'c1',
    ticket_number: 'CMP-20260912-A8F1',
    citizen_id: 'cit-10482',
    category_id: '1',
    department_id: 'ROADS',
    title: 'Severe asphalt crater near Ward 4 Metro Gate 2',
    description: '15cm crater in left carriageway creating hazard for two-wheelers and buses during rush hours.',
    priority: 'HIGH',
    status: 'IN_PROGRESS',
    latitude: 12.9716,
    longitude: 77.5946,
    location_address: 'MG Road Junction, Ward 4',
    ward_number: 4,
    sla_due_at: '2026-09-14T14:00:00Z',
    is_escalated: false,
    created_at: '2026-09-12T08:30:00Z',
    updated_at: '2026-09-12T09:15:00Z',
  },
  {
    id: 'c2',
    ticket_number: 'CMP-20260912-B42C',
    citizen_id: 'cit-10482',
    category_id: '2',
    department_id: 'SANITATION',
    title: 'Overflowing commercial waste container on Market Street',
    description: 'Public secondary dumpster overflowing for over 36 hours obstructing pedestrian footpath.',
    priority: 'MEDIUM',
    status: 'UNDER_REVIEW',
    latitude: 12.9752,
    longitude: 77.5984,
    location_address: 'Market Street Gate 3, Ward 4',
    ward_number: 4,
    sla_due_at: '2026-09-13T18:00:00Z',
    is_escalated: false,
    created_at: '2026-09-12T07:10:00Z',
    updated_at: '2026-09-12T07:10:00Z',
  },
  {
    id: 'c3',
    ticket_number: 'CMP-20260911-E994',
    citizen_id: 'cit-10482',
    category_id: '3',
    department_id: 'ELECTRICAL',
    title: 'Dark zone: 4 consecutive LED street poles extinguished',
    description: 'Streetlight poles #402 through #405 non-operational causing safety concern for night commuters.',
    priority: 'LOW',
    status: 'RESOLVED',
    latitude: 12.9684,
    longitude: 77.5891,
    location_address: 'Elm Avenue, Sector 7, Ward 4',
    ward_number: 4,
    sla_due_at: '2026-09-12T20:00:00Z',
    is_escalated: false,
    citizen_rating: 5,
    citizen_feedback: 'Technician replaced the LED drivers promptly. Well done!',
    created_at: '2026-09-11T14:20:00Z',
    updated_at: '2026-09-12T06:00:00Z',
  },
];

const INITIAL_WORK_ORDERS: WorkOrder[] = [
  {
    id: 'wo-1',
    order_number: 'WO-20260912-001',
    complaint_id: 'c1',
    title: 'Emergency Pothole Milling & Cold Mix Compaction',
    description: 'Excavate 15cm crater, clean loose debris, apply tack coat, and compact binder mix.',
    priority: 'HIGH',
    status: 'IN_PROGRESS',
    completion_percentage: 65,
    department_id: 'ROADS',
    assigned_technician_id: 'stf-2087',
    latitude: 12.9716,
    longitude: 77.5946,
    location_address: 'MG Road Junction, Ward 4',
    due_date: '2026-09-14T14:00:00Z',
    field_notes: 'Safety cones deployed. Base compaction completed. Applying surface wear layer.',
    created_at: '2026-09-12T08:45:00Z',
  },
  {
    id: 'wo-2',
    order_number: 'WO-20260912-002',
    complaint_id: 'c3',
    title: 'High-Output LED Driver Replacement - Elm Avenue',
    description: 'Replace faulty photocell sensor and burnt 60W LED fixtures on poles #402-405.',
    priority: 'LOW',
    status: 'COMPLETED',
    completion_percentage: 100,
    department_id: 'ELECTRICAL',
    assigned_technician_id: 'tech-02',
    latitude: 12.9684,
    longitude: 77.5891,
    location_address: 'Elm Avenue, Sector 7, Ward 4',
    due_date: '2026-09-12T20:00:00Z',
    field_notes: 'All 4 luminaire modules verified operational with illuminance test.',
    created_at: '2026-09-11T15:00:00Z',
  },
];

const INITIAL_NOTIFICATIONS: CivicNotification[] = [
  {
    id: 'notif-1',
    title: 'Work Order Dispatched',
    message: 'Roads maintenance crew has been dispatched for Pothole near Metro Gate 2.',
    timestamp: '15 mins ago',
    targetRole: 'Citizen',
    type: 'info',
    isRead: false,
  },
  {
    id: 'notif-2',
    title: 'New High Priority Assignment',
    message: 'Work Order WO-20260912-001 assigned to Central Zone team. SLA remaining: 6h.',
    timestamp: '45 mins ago',
    targetRole: 'Staff',
    type: 'warning',
    isRead: false,
  },
  {
    id: 'notif-3',
    title: 'Department SLA Compliance: 94.2%',
    message: 'Roads & Infrastructure cleared 14 complaints in the last 24-hour cycle.',
    timestamp: '1 hour ago',
    targetRole: 'Admin',
    type: 'success',
    isRead: false,
  },
  {
    id: 'notif-4',
    title: 'Municipal Water Main Calibration',
    message: 'Scheduled pressure optimization in Wards 4 & 5 starting midnight.',
    timestamp: '2 hours ago',
    targetRole: 'ALL',
    type: 'info',
    isRead: true,
  },
];

export const CityDataProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [complaints, setComplaints] = useState<Complaint[]>(() => {
    const saved = localStorage.getItem('smartcity360_complaints');
    return saved ? JSON.parse(saved) : INITIAL_COMPLAINTS;
  });

  const [workOrders, setWorkOrders] = useState<WorkOrder[]>(() => {
    const saved = localStorage.getItem('smartcity360_work_orders');
    return saved ? JSON.parse(saved) : INITIAL_WORK_ORDERS;
  });

  const [categories, setCategories] = useState<ComplaintCategory[]>(INITIAL_CATEGORIES);
  const [facilities, setFacilities] = useState<Facility[]>([]);
  const [notifications, setNotifications] = useState<CivicNotification[]>(() => {
    const saved = localStorage.getItem('smartcity360_notifications');
    return saved ? JSON.parse(saved) : INITIAL_NOTIFICATIONS;
  });

  const [isLoading, setIsLoading] = useState<boolean>(true);

  // Sync to localStorage
  useEffect(() => {
    localStorage.setItem('smartcity360_complaints', JSON.stringify(complaints));
  }, [complaints]);

  useEffect(() => {
    localStorage.setItem('smartcity360_work_orders', JSON.stringify(workOrders));
  }, [workOrders]);

  useEffect(() => {
    localStorage.setItem('smartcity360_notifications', JSON.stringify(notifications));
  }, [notifications]);

  // Derived KPIs reconciling complaints & work orders
  const totalComplaints = complaints.length;
  const resolvedComplaints = complaints.filter(
    (c) => c.status === 'RESOLVED' || c.status === 'CLOSED'
  ).length;
  const activeComplaints = totalComplaints - resolvedComplaints;
  const resolutionRate = totalComplaints > 0 ? Math.round((resolvedComplaints / totalComplaints) * 1000) / 10 : 0;
  const activeWorkOrders = workOrders.filter(
    (w) => w.status !== 'COMPLETED' && w.status !== 'VERIFICATION'
  ).length;

  const kpis: CityKPIs = {
    total_complaints: totalComplaints,
    resolved_complaints: resolvedComplaints,
    active_complaints: activeComplaints,
    resolution_rate_percentage: resolutionRate,
    sla_compliance_percentage: 94.2,
    active_emergencies: 2,
    active_work_orders: activeWorkOrders,
    average_resolution_hours: 22.4,
  };

  const refreshData = async () => {
    try {
      const [fetchedFacilities, fetchedCategories] = await Promise.all([
        apiClient.getFacilities(),
        apiClient.getCategories(),
      ]);
      if (fetchedFacilities?.length) setFacilities(fetchedFacilities);
      if (fetchedCategories?.length) setCategories(fetchedCategories);
    } catch {
      // Keep existing
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    refreshData();
  }, []);

  // Interconnected Workflow: Citizen adds complaint -> Auto creates Work Order & Notifies Staff/Admin
  const addComplaint = async (payload: {
    category_id: string;
    title: string;
    description: string;
    location_address: string;
    ward_number: number;
    latitude: number;
    longitude: number;
    priority?: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
  }): Promise<Complaint> => {
    const category = categories.find((c) => c.id === payload.category_id) || categories[0];
    const deptCode = category.default_department_code || 'ROADS';
    const randomHex = Math.random().toString(16).substring(2, 6).toUpperCase();
    const ticketNumber = `CMP-20260912-${randomHex}`;
    const orderNumber = `WO-20260912-${randomHex}`;

    const now = new Date();
    const slaHours = category.default_sla_hours || 48;
    const slaDue = new Date(now.getTime() + slaHours * 60 * 60 * 1000).toISOString();

    const newComplaint: Complaint = {
      id: `cmp_${Date.now()}`,
      ticket_number: ticketNumber,
      citizen_id: 'cit-10482',
      category_id: payload.category_id,
      department_id: deptCode,
      title: payload.title,
      description: payload.description,
      priority: payload.priority || 'HIGH',
      status: 'ASSIGNED',
      latitude: payload.latitude,
      longitude: payload.longitude,
      location_address: payload.location_address,
      ward_number: payload.ward_number,
      sla_due_at: slaDue,
      is_escalated: false,
      created_at: now.toISOString(),
      updated_at: now.toISOString(),
    };

    // Automatically create matching Field Work Order for Municipal Staff
    const newWorkOrder: WorkOrder = {
      id: `wo_${Date.now()}`,
      order_number: orderNumber,
      complaint_id: newComplaint.id,
      title: `${category.name}: ${payload.title}`,
      description: payload.description,
      priority: newComplaint.priority,
      status: 'ASSIGNED',
      completion_percentage: 0,
      department_id: deptCode,
      assigned_technician_id: 'stf-2087',
      latitude: payload.latitude,
      longitude: payload.longitude,
      location_address: payload.location_address,
      due_date: slaDue,
      field_notes: `Awaiting field inspection in Ward ${payload.ward_number}. Standard ${slaHours}h SLA.`,
      created_at: now.toISOString(),
    };

    // Role-specific notifications
    const newStaffNotif: CivicNotification = {
      id: `notif_${Date.now()}_1`,
      title: `New Dispatch: ${orderNumber}`,
      message: `New ${deptCode} task assigned in Ward ${payload.ward_number}: "${payload.title}"`,
      timestamp: 'Just now',
      targetRole: 'Staff',
      type: 'warning',
      isRead: false,
    };

    const newAdminNotif: CivicNotification = {
      id: `notif_${Date.now()}_2`,
      title: `Civic Request Registered: ${ticketNumber}`,
      message: `${newComplaint.priority} priority incident logged in Ward ${payload.ward_number} -> ${deptCode}.`,
      timestamp: 'Just now',
      targetRole: 'Admin',
      type: 'info',
      isRead: false,
    };

    setComplaints((prev) => [newComplaint, ...prev]);
    setWorkOrders((prev) => [newWorkOrder, ...prev]);
    setNotifications((prev) => [newStaffNotif, newAdminNotif, ...prev]);

    return newComplaint;
  };

  // Staff updates work order -> Synchronizes linked complaint & Admin metrics
  const updateWorkOrderStatus = (
    orderId: string,
    newStatus: string,
    percentage?: number,
    notes?: string
  ) => {
    let targetComplaintId: string | undefined;

    setWorkOrders((prev) =>
      prev.map((wo) => {
        if (wo.id === orderId) {
          targetComplaintId = wo.complaint_id;
          const resolvedPct = percentage !== undefined ? percentage : (newStatus === 'COMPLETED' ? 100 : wo.completion_percentage);
          return {
            ...wo,
            status: newStatus,
            completion_percentage: resolvedPct,
            field_notes: notes !== undefined ? notes : wo.field_notes,
          };
        }
        return wo;
      })
    );

    // If order is completed or updated, reflect state in linked Citizen Complaint
    if (targetComplaintId) {
      setComplaints((prev) =>
        prev.map((cmp) => {
          if (cmp.id === targetComplaintId) {
            let nextStatus = cmp.status;
            if (newStatus === 'COMPLETED' || newStatus === 'VERIFICATION') {
              nextStatus = 'RESOLVED';
            } else if (newStatus === 'IN_PROGRESS' || newStatus === 'ON_SITE') {
              nextStatus = 'IN_PROGRESS';
            } else if (newStatus === 'ACCEPTED' || newStatus === 'EN_ROUTE') {
              nextStatus = 'ASSIGNED';
            }
            return {
              ...cmp,
              status: nextStatus,
              updated_at: new Date().toISOString(),
            };
          }
          return cmp;
        })
      );

      if (newStatus === 'COMPLETED') {
        const citizenNotif: CivicNotification = {
          id: `notif_${Date.now()}_cit`,
          title: 'Civic Complaint Resolved',
          message: `Field teams have completed work on your complaint. Please inspect and leave your feedback.`,
          timestamp: 'Just now',
          targetRole: 'Citizen',
          type: 'success',
          isRead: false,
        };
        const adminNotif: CivicNotification = {
          id: `notif_${Date.now()}_adm`,
          title: `Resolution Verified: ${orderId}`,
          message: `Work Order completed with verified field checklist and evidence.`,
          timestamp: 'Just now',
          targetRole: 'Admin',
          type: 'success',
          isRead: false,
        };
        setNotifications((prev) => [citizenNotif, adminNotif, ...prev]);
      }
    }
  };

  const addCitizenFeedback = (complaintId: string, rating: number, feedback: string) => {
    setComplaints((prev) =>
      prev.map((cmp) => {
        if (cmp.id === complaintId) {
          return {
            ...cmp,
            citizen_rating: rating,
            citizen_feedback: feedback,
            updated_at: new Date().toISOString(),
          };
        }
        return cmp;
      })
    );

    const feedbackNotif: CivicNotification = {
      id: `notif_${Date.now()}_fb`,
      title: 'Citizen Feedback Received',
      message: `Citizen gave a ${rating}-star rating for resolved complaint.`,
      timestamp: 'Just now',
      targetRole: 'Admin',
      type: 'info',
      isRead: false,
    };
    setNotifications((prev) => [feedbackNotif, ...prev]);
  };

  const markNotificationAsRead = (notificationId: string) => {
    setNotifications((prev) =>
      prev.map((n) => (n.id === notificationId ? { ...n, isRead: true } : n))
    );
  };

  return (
    <CityDataContext.Provider
      value={{
        complaints,
        workOrders,
        facilities,
        categories,
        kpis,
        notifications,
        isLoading,
        addComplaint,
        updateWorkOrderStatus,
        addCitizenFeedback,
        markNotificationAsRead,
        refreshData,
      }}
    >
      {children}
    </CityDataContext.Provider>
  );
};

export const useCityData = (): CityDataContextType => {
  const context = useContext(CityDataContext);
  if (!context) {
    throw new Error('useCityData must be used within a CityDataProvider');
  }
  return context;
};
