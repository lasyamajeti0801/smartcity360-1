/**
 * SmartCity360 - Social Welfare & Community Support Client API Service
 * Domain: social_services
 */

import { SocialServicesStatus } from './types';

const API_BASE = '/api/v1/social-services';

export async function fetchSocialServicesMetric01(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-01?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 01: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric02(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-02?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 02: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric03(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-03?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 03: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric04(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-04?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 04: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric05(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-05?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 05: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric06(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-06?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 06: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric07(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-07?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 07: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric08(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-08?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 08: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric09(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-09?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 09: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric10(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-10?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 10: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric11(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-11?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 11: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric12(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-12?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 12: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric13(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-13?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 13: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric14(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-14?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 14: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric15(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-15?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 15: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric16(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-16?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 16: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric17(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-17?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 17: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric18(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-18?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 18: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric19(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-19?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 19: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric20(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-20?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 20: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric21(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-21?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 21: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric22(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-22?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 22: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric23(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-23?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 23: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric24(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-24?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 24: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric25(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-25?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 25: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric26(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-26?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 26: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric27(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-27?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 27: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric28(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-28?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 28: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric29(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-29?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 29: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric30(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-30?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 30: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric31(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-31?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 31: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric32(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-32?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 32: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric33(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-33?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 33: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric34(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-34?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 34: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric35(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-35?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 35: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric36(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-36?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 36: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric37(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-37?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 37: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric38(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-38?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 38: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric39(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-39?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 39: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric40(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-40?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 40: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric41(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-41?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 41: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric42(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-42?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 42: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric43(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-43?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 43: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric44(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-44?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 44: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric45(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-45?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 45: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric46(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-46?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 46: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric47(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-47?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 47: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric48(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-48?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 48: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric49(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-49?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 49: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric50(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-50?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 50: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric51(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-51?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 51: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric52(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-52?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 52: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric53(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-53?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 53: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric54(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-54?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 54: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric55(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-55?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 55: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric56(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-56?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 56: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric57(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-57?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 57: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric58(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-58?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 58: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric59(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-59?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 59: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric60(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-60?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 60: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric61(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-61?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 61: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric62(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-62?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 62: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric63(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-63?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 63: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric64(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-64?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 64: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric65(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-65?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 65: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric66(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-66?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 66: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric67(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-67?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 67: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric68(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-68?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 68: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric69(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-69?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 69: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric70(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-70?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 70: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric71(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-71?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 71: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric72(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-72?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 72: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric73(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-73?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 73: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric74(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-74?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 74: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric75(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-75?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 75: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric76(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-76?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 76: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric77(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-77?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 77: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric78(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-78?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 78: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric79(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-79?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 79: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric80(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-80?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 80: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric81(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-81?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 81: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric82(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-82?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 82: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric83(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-83?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 83: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric84(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-84?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 84: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric85(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-85?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 85: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric86(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-86?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 86: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric87(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-87?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 87: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric88(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-88?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 88: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric89(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-89?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 89: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchSocialServicesMetric90(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-90?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Social Welfare & Community Support metric 90: ${response.statusText}`);
  }
  return response.json();
}
