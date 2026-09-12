/**
 * SmartCity360 - Fire Protection & Hazardous Materials Client API Service
 * Domain: fire_and_rescue
 */

import { FireAndRescueStatus } from './types';

const API_BASE = '/api/v1/fire-and-rescue';

export async function fetchFireAndRescueMetric01(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-01?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 01: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric02(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-02?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 02: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric03(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-03?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 03: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric04(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-04?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 04: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric05(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-05?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 05: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric06(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-06?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 06: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric07(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-07?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 07: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric08(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-08?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 08: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric09(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-09?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 09: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric10(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-10?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 10: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric11(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-11?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 11: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric12(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-12?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 12: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric13(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-13?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 13: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric14(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-14?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 14: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric15(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-15?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 15: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric16(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-16?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 16: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric17(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-17?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 17: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric18(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-18?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 18: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric19(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-19?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 19: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric20(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-20?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 20: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric21(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-21?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 21: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric22(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-22?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 22: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric23(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-23?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 23: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric24(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-24?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 24: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric25(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-25?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 25: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric26(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-26?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 26: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric27(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-27?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 27: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric28(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-28?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 28: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric29(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-29?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 29: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric30(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-30?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 30: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric31(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-31?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 31: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric32(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-32?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 32: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric33(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-33?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 33: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric34(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-34?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 34: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric35(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-35?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 35: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric36(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-36?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 36: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric37(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-37?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 37: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric38(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-38?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 38: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric39(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-39?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 39: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric40(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-40?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 40: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric41(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-41?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 41: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric42(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-42?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 42: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric43(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-43?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 43: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric44(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-44?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 44: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric45(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-45?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 45: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric46(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-46?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 46: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric47(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-47?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 47: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric48(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-48?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 48: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric49(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-49?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 49: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric50(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-50?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 50: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric51(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-51?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 51: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric52(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-52?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 52: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric53(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-53?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 53: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric54(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-54?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 54: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric55(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-55?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 55: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric56(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-56?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 56: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric57(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-57?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 57: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric58(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-58?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 58: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric59(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-59?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 59: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric60(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-60?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 60: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric61(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-61?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 61: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric62(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-62?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 62: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric63(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-63?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 63: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric64(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-64?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 64: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric65(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-65?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 65: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric66(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-66?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 66: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric67(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-67?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 67: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric68(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-68?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 68: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric69(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-69?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 69: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric70(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-70?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 70: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric71(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-71?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 71: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric72(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-72?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 72: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric73(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-73?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 73: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric74(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-74?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 74: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric75(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-75?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 75: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric76(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-76?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 76: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric77(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-77?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 77: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric78(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-78?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 78: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric79(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-79?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 79: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric80(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-80?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 80: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric81(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-81?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 81: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric82(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-82?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 82: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric83(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-83?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 83: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric84(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-84?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 84: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric85(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-85?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 85: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric86(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-86?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 86: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric87(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-87?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 87: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric88(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-88?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 88: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric89(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-89?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 89: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchFireAndRescueMetric90(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-90?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Fire Protection & Hazardous Materials metric 90: ${response.statusText}`);
  }
  return response.json();
}
