/**
 * SmartCity360 - Emergency Medical Services & Triage Client API Service
 * Domain: emergency_medical
 */

import { EmergencyMedicalStatus } from './types';

const API_BASE = '/api/v1/emergency-medical';

export async function fetchEmergencyMedicalMetric01(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-01?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 01: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric02(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-02?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 02: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric03(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-03?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 03: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric04(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-04?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 04: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric05(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-05?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 05: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric06(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-06?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 06: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric07(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-07?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 07: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric08(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-08?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 08: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric09(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-09?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 09: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric10(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-10?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 10: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric11(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-11?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 11: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric12(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-12?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 12: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric13(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-13?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 13: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric14(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-14?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 14: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric15(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-15?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 15: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric16(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-16?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 16: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric17(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-17?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 17: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric18(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-18?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 18: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric19(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-19?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 19: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric20(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-20?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 20: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric21(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-21?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 21: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric22(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-22?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 22: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric23(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-23?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 23: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric24(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-24?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 24: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric25(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-25?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 25: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric26(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-26?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 26: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric27(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-27?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 27: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric28(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-28?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 28: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric29(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-29?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 29: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric30(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-30?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 30: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric31(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-31?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 31: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric32(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-32?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 32: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric33(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-33?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 33: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric34(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-34?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 34: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric35(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-35?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 35: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric36(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-36?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 36: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric37(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-37?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 37: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric38(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-38?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 38: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric39(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-39?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 39: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric40(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-40?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 40: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric41(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-41?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 41: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric42(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-42?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 42: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric43(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-43?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 43: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric44(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-44?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 44: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric45(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-45?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 45: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric46(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-46?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 46: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric47(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-47?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 47: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric48(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-48?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 48: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric49(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-49?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 49: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric50(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-50?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 50: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric51(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-51?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 51: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric52(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-52?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 52: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric53(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-53?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 53: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric54(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-54?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 54: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric55(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-55?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 55: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric56(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-56?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 56: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric57(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-57?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 57: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric58(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-58?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 58: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric59(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-59?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 59: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric60(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-60?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 60: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric61(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-61?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 61: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric62(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-62?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 62: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric63(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-63?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 63: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric64(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-64?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 64: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric65(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-65?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 65: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric66(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-66?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 66: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric67(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-67?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 67: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric68(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-68?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 68: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric69(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-69?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 69: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric70(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-70?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 70: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric71(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-71?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 71: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric72(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-72?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 72: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric73(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-73?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 73: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric74(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-74?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 74: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric75(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-75?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 75: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric76(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-76?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 76: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric77(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-77?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 77: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric78(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-78?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 78: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric79(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-79?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 79: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric80(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-80?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 80: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric81(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-81?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 81: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric82(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-82?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 82: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric83(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-83?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 83: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric84(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-84?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 84: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric85(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-85?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 85: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric86(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-86?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 86: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric87(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-87?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 87: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric88(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-88?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 88: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric89(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-89?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 89: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchEmergencyMedicalMetric90(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-90?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Emergency Medical Services & Triage metric 90: ${response.statusText}`);
  }
  return response.json();
}
