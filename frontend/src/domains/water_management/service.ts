/**
 * SmartCity360 - Municipal Water Supply & Quality Client API Service
 * Domain: water_management
 */

import { WaterManagementStatus } from './types';

const API_BASE = '/api/v1/water-management';

export async function fetchWaterManagementMetric01(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-01?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 01: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric02(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-02?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 02: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric03(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-03?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 03: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric04(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-04?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 04: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric05(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-05?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 05: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric06(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-06?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 06: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric07(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-07?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 07: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric08(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-08?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 08: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric09(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-09?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 09: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric10(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-10?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 10: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric11(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-11?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 11: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric12(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-12?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 12: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric13(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-13?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 13: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric14(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-14?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 14: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric15(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-15?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 15: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric16(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-16?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 16: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric17(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-17?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 17: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric18(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-18?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 18: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric19(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-19?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 19: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric20(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-20?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 20: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric21(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-21?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 21: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric22(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-22?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 22: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric23(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-23?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 23: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric24(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-24?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 24: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric25(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-25?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 25: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric26(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-26?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 26: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric27(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-27?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 27: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric28(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-28?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 28: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric29(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-29?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 29: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric30(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-30?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 30: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric31(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-31?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 31: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric32(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-32?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 32: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric33(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-33?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 33: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric34(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-34?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 34: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric35(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-35?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 35: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric36(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-36?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 36: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric37(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-37?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 37: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric38(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-38?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 38: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric39(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-39?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 39: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric40(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-40?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 40: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric41(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-41?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 41: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric42(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-42?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 42: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric43(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-43?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 43: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric44(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-44?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 44: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric45(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-45?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 45: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric46(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-46?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 46: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric47(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-47?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 47: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric48(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-48?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 48: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric49(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-49?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 49: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric50(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-50?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 50: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric51(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-51?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 51: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric52(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-52?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 52: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric53(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-53?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 53: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric54(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-54?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 54: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric55(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-55?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 55: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric56(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-56?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 56: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric57(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-57?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 57: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric58(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-58?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 58: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric59(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-59?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 59: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchWaterManagementMetric60(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-60?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Water Supply & Quality metric 60: ${response.statusText}`);
  }
  return response.json();
}
