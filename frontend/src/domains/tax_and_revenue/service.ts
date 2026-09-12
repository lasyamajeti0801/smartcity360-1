/**
 * SmartCity360 - Municipal Taxation & Revenue Audit Client API Service
 * Domain: tax_and_revenue
 */

import { TaxAndRevenueStatus } from './types';

const API_BASE = '/api/v1/tax-and-revenue';

export async function fetchTaxAndRevenueMetric01(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-01?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 01: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric02(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-02?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 02: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric03(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-03?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 03: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric04(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-04?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 04: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric05(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-05?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 05: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric06(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-06?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 06: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric07(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-07?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 07: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric08(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-08?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 08: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric09(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-09?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 09: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric10(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-10?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 10: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric11(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-11?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 11: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric12(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-12?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 12: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric13(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-13?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 13: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric14(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-14?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 14: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric15(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-15?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 15: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric16(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-16?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 16: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric17(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-17?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 17: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric18(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-18?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 18: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric19(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-19?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 19: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric20(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-20?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 20: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric21(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-21?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 21: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric22(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-22?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 22: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric23(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-23?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 23: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric24(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-24?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 24: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric25(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-25?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 25: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric26(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-26?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 26: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric27(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-27?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 27: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric28(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-28?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 28: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric29(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-29?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 29: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric30(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-30?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 30: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric31(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-31?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 31: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric32(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-32?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 32: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric33(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-33?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 33: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric34(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-34?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 34: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric35(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-35?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 35: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric36(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-36?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 36: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric37(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-37?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 37: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric38(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-38?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 38: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric39(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-39?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 39: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric40(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-40?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 40: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric41(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-41?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 41: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric42(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-42?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 42: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric43(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-43?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 43: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric44(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-44?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 44: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric45(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-45?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 45: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric46(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-46?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 46: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric47(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-47?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 47: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric48(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-48?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 48: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric49(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-49?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 49: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric50(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-50?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 50: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric51(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-51?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 51: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric52(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-52?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 52: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric53(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-53?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 53: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric54(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-54?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 54: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric55(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-55?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 55: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric56(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-56?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 56: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric57(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-57?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 57: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric58(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-58?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 58: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric59(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-59?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 59: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTaxAndRevenueMetric60(wardId = 1, limit = 25): Promise<any> {
  const response = await fetch(`${API_BASE}/endpoint-60?ward_id=${wardId}&limit=${limit}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch Municipal Taxation & Revenue Audit metric 60: ${response.statusText}`);
  }
  return response.json();
}
