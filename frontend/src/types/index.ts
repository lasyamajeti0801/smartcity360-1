// SmartCity360 Core TypeScript Domain Types

export type UserRole =
  | 'Citizen'
  | 'Department Staff'
  | 'Field Staff'
  | 'Supervisor'
  | 'Emergency Operator'
  | 'Municipal Officer'
  | 'City Administrator'
  | 'System Administrator';

export type ComplaintStatus =
  | 'NEW'
  | 'UNDER_REVIEW'
  | 'ASSIGNED'
  | 'IN_PROGRESS'
  | 'ON_HOLD'
  | 'RESOLVED'
  | 'CLOSED'
  | 'REOPENED'
  | 'REJECTED';

export type ComplaintPriority = 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';

export interface ComplaintCategory {
  id: string;
  code: string;
  name: string;
  default_department_code: string;
  default_sla_hours: number;
  icon_name: string;
  description?: string;
}

export interface Complaint {
  id: string;
  ticket_number: string;
  citizen_id: string;
  category_id: string;
  department_id: string;
  assigned_staff_id?: string;
  title: string;
  description: string;
  priority: ComplaintPriority;
  status: ComplaintStatus;
  latitude: number;
  longitude: number;
  location_address: string;
  ward_number?: number;
  sla_due_at?: string;
  is_escalated: boolean;
  citizen_rating?: number;
  citizen_feedback?: string;
  evidence_image_url?: string;
  resolution_image_url?: string;
  created_at: string;
  updated_at: string;
}

export interface MunicipalDepartment {
  id: string;
  code: string;
  name: string;
  description: string;
  contact_email: string;
  contact_phone: string;
  head_official?: string;
  is_active: boolean;
}

export interface MunicipalService {
  id: string;
  department_id: string;
  category_id: string;
  code: string;
  title: string;
  description: string;
  eligibility_criteria: string;
  fee_amount: number;
  sla_turnaround_days: number;
  required_documents: string;
  is_online_submission: boolean;
}

export interface WorkOrder {
  id: string;
  order_number: string;
  complaint_id?: string;
  department_id: string;
  assigned_technician_id?: string;
  title: string;
  description: string;
  priority: string;
  status: string;
  completion_percentage: number;
  field_notes?: string;
  latitude: number;
  longitude: number;
  location_address: string;
  due_date?: string;
  created_at: string;
}

export interface EmergencyIncident {
  id: string;
  incident_number: string;
  incident_type: string;
  severity: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
  status: string;
  title: string;
  description: string;
  latitude: number;
  longitude: number;
  location_address: string;
  caller_name?: string;
  caller_phone?: string;
  created_at: string;
}

export interface Facility {
  id: string;
  facility_code: string;
  name: string;
  category: string;
  address: string;
  latitude: number;
  longitude: number;
  contact_phone: string;
  operating_hours: string;
  is_operational: boolean;
  is_wheelchair_accessible: boolean;
}

export interface CityKPIs {
  total_complaints: number;
  resolved_complaints: number;
  active_complaints: number;
  resolution_rate_percentage: number;
  sla_compliance_percentage: number;
  active_emergencies: number;
  active_work_orders: number;
  average_resolution_hours: number;
}
