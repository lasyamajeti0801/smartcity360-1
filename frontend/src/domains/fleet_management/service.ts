/**
 * SmartCity360 - Municipal Vehicle Fleet & Telematics Client API Service
 * Domain: fleet_management
 */

import { FleetManagementStatus } from './types';

const API_BASE = '/api/v1/fleet-management';

export async function fetchFleetManagementMetric01(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-01?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 01: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric02(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-02?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 02: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric03(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-03?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 03: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric04(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-04?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 04: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric05(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-05?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 05: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric06(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-06?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 06: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric07(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-07?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 07: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric08(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-08?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 08: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric09(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-09?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 09: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric10(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-10?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 10: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric11(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-11?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 11: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric12(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-12?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 12: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric13(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-13?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 13: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric14(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-14?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 14: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric15(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-15?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 15: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric16(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-16?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 16: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric17(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-17?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 17: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric18(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-18?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 18: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric19(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-19?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 19: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric20(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-20?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 20: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric21(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-21?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 21: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric22(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-22?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 22: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric23(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-23?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 23: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric24(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-24?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 24: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric25(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-25?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 25: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric26(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-26?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 26: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric27(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-27?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 27: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric28(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-28?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 28: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric29(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-29?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 29: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric30(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-30?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 30: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric31(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-31?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 31: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric32(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-32?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 32: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric33(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-33?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 33: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric34(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-34?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 34: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric35(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-35?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 35: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric36(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-36?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 36: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric37(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-37?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 37: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric38(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-38?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 38: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric39(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-39?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 39: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric40(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-40?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 40: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric41(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-41?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 41: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric42(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-42?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 42: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric43(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-43?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 43: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric44(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-44?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 44: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric45(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-45?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 45: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric46(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-46?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 46: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric47(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-47?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 47: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric48(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-48?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 48: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric49(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-49?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 49: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric50(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-50?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 50: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric51(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-51?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 51: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric52(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-52?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 52: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric53(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-53?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 53: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric54(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-54?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 54: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric55(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-55?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 55: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric56(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-56?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 56: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric57(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-57?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 57: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric58(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-58?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 58: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric59(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-59?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 59: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFleetManagementMetric60(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-60?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Vehicle Fleet & Telematics metric 60: ${response.statusText}`);
  }
  return response.json();
}
