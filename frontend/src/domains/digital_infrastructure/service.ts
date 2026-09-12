/**
 * SmartCity360 - Smart City Cyber-Physical Infrastructure Client API Service
 * Domain: digital_infrastructure
 */

import { DigitalInfrastructureStatus } from './types';

const API_BASE = '/api/v1/digital-infrastructure';

export async function fetchDigitalInfrastructureMetric01(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-01?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 01: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric02(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-02?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 02: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric03(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-03?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 03: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric04(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-04?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 04: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric05(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-05?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 05: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric06(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-06?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 06: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric07(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-07?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 07: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric08(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-08?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 08: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric09(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-09?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 09: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric10(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-10?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 10: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric11(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-11?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 11: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric12(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-12?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 12: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric13(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-13?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 13: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric14(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-14?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 14: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric15(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-15?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 15: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric16(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-16?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 16: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric17(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-17?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 17: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric18(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-18?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 18: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric19(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-19?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 19: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric20(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-20?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 20: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric21(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-21?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 21: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric22(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-22?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 22: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric23(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-23?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 23: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric24(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-24?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 24: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric25(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-25?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 25: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric26(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-26?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 26: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric27(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-27?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 27: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric28(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-28?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 28: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric29(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-29?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 29: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric30(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-30?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 30: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric31(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-31?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 31: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric32(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-32?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 32: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric33(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-33?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 33: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric34(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-34?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 34: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric35(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-35?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 35: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric36(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-36?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 36: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric37(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-37?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 37: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric38(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-38?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 38: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric39(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-39?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 39: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric40(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-40?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 40: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric41(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-41?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 41: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric42(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-42?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 42: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric43(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-43?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 43: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric44(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-44?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 44: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric45(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-45?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 45: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric46(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-46?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 46: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric47(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-47?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 47: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric48(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-48?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 48: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric49(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-49?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 49: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric50(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-50?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 50: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric51(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-51?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 51: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric52(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-52?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 52: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric53(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-53?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 53: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric54(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-54?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 54: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric55(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-55?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 55: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric56(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-56?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 56: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric57(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-57?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 57: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric58(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-58?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 58: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric59(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-59?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 59: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric60(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-60?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 60: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric61(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-61?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 61: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric62(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-62?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 62: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric63(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-63?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 63: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric64(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-64?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 64: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric65(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-65?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 65: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric66(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-66?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 66: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric67(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-67?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 67: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric68(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-68?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 68: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric69(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-69?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 69: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric70(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-70?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 70: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric71(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-71?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 71: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric72(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-72?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 72: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric73(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-73?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 73: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric74(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-74?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 74: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric75(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-75?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 75: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric76(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-76?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 76: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric77(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-77?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 77: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric78(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-78?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 78: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric79(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-79?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 79: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric80(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-80?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 80: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric81(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-81?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 81: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric82(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-82?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 82: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric83(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-83?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 83: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric84(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-84?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 84: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric85(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-85?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 85: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric86(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-86?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 86: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric87(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-87?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 87: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric88(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-88?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 88: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric89(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-89?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 89: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchDigitalInfrastructureMetric90(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-90?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Smart City Cyber-Physical Infrastructure metric 90: ${response.statusText}`);
  }
  return response.json();
}
