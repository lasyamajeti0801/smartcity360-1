import React, { createContext, useContext, useState, useEffect } from 'react';
import { PrimaryRole, UserIdentity } from '../types';

export const DEMO_IDENTITIES: Record<PrimaryRole, UserIdentity> = {
  Citizen: {
    id: 'cit-10482',
    email: 'citizen@smartcity360.local',
    fullName: 'Priya Sharma',
    role: 'Citizen',
    subRole: 'Verified Resident',
    badgeOrWard: 'Ward 04',
    zone: 'Greenfield Extension',
    phone: '+91 98765 43210',
    avatarInitials: 'PS',
  },
  Staff: {
    id: 'stf-2087',
    email: 'staff.roads@smartcity360.local',
    fullName: 'Arjun Kumar',
    role: 'Staff',
    subRole: 'Field Operations Officer (Roads & Works)',
    departmentCode: 'ROADS',
    badgeOrWard: 'ENG-RDS-2087',
    zone: 'Central Zone',
    phone: '+91 98765 12044',
    avatarInitials: 'AK',
  },
  Admin: {
    id: 'adm-001',
    email: 'admin@smartcity360.local',
    fullName: 'Ananya Rao',
    role: 'Admin',
    subRole: 'Municipal Operations Administrator',
    departmentCode: 'OPERATIONS',
    badgeOrWard: 'HQ-OPS-01',
    zone: 'Smart City Operations Centre',
    phone: '+91 98765 00001',
    avatarInitials: 'AR',
  },
};

interface AuthContextType {
  user: UserIdentity | null;
  token: string | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  login: (email: string, password: string) => Promise<{ success: boolean; role?: PrimaryRole; error?: string }>;
  loginAsDemo: (role: PrimaryRole) => void;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

const STORAGE_USER_KEY = 'smartcity360_user';
const STORAGE_TOKEN_KEY = 'smartcity360_token';

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<UserIdentity | null>(null);
  const [token, setToken] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  // Initialize session from storage
  useEffect(() => {
    try {
      const storedUser = localStorage.getItem(STORAGE_USER_KEY);
      const storedToken = localStorage.getItem(STORAGE_TOKEN_KEY);
      if (storedUser) {
        setUser(JSON.parse(storedUser));
        setToken(storedToken || 'demo_jwt_token');
      }
    } catch {
      localStorage.removeItem(STORAGE_USER_KEY);
      localStorage.removeItem(STORAGE_TOKEN_KEY);
    } finally {
      setIsLoading(false);
    }
  }, []);

  const saveSession = (newUser: UserIdentity, newToken: string) => {
    setUser(newUser);
    setToken(newToken);
    localStorage.setItem(STORAGE_USER_KEY, JSON.stringify(newUser));
    localStorage.setItem(STORAGE_TOKEN_KEY, newToken);
  };

  const loginAsDemo = (role: PrimaryRole) => {
    const identity = DEMO_IDENTITIES[role];
    saveSession(identity, `demo_token_${role.toLowerCase()}`);
  };

  const login = async (email: string, password: string): Promise<{ success: boolean; role?: PrimaryRole; error?: string }> => {
    const cleanEmail = email.trim().toLowerCase();

    // 1. Check local demo credentials first for seamless offline/dev experience
    if (cleanEmail.includes('citizen') || cleanEmail === 'citizen@smartcity360.local') {
      loginAsDemo('Citizen');
      return { success: true, role: 'Citizen' };
    }
    if (cleanEmail.includes('staff') || cleanEmail.includes('roads') || cleanEmail === 'staff.roads@smartcity360.local') {
      loginAsDemo('Staff');
      return { success: true, role: 'Staff' };
    }
    if (cleanEmail.includes('admin') || cleanEmail === 'admin@smartcity360.local') {
      loginAsDemo('Admin');
      return { success: true, role: 'Admin' };
    }

    // 2. Attempt real backend authentication
    try {
      const response = await fetch('/api/v1/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: cleanEmail, password }),
      });

      if (response.ok) {
        const data = await response.json();
        const apiUser = data.user;

        // Map backend roles to PrimaryRole
        let mappedRole: PrimaryRole = 'Citizen';
        const roleNames = (apiUser.roles || []).map((r: any) => (typeof r === 'string' ? r : r.name));
        if (roleNames.some((r: string) => r.includes('ADMIN'))) {
          mappedRole = 'Admin';
        } else if (roleNames.some((r: string) => r.includes('STAFF') || r.includes('OPERATOR'))) {
          mappedRole = 'Staff';
        }

        const resolvedIdentity: UserIdentity = {
          id: apiUser.id,
          email: apiUser.email,
          fullName: apiUser.full_name || cleanEmail.split('@')[0],
          role: mappedRole,
          subRole: roleNames[0] || mappedRole,
          badgeOrWard: apiUser.citizen_profile?.ward_number ? `Ward ${apiUser.citizen_profile.ward_number}` : apiUser.staff_profile?.employee_badge || 'Municipal ID',
          zone: apiUser.citizen_profile?.zone_name || 'Central Ward Zone',
          phone: apiUser.phone_number || '+91 98765 00000',
          avatarInitials: (apiUser.full_name || cleanEmail)
            .split(' ')
            .map((n: string) => n[0])
            .join('')
            .substring(0, 2)
            .toUpperCase(),
        };

        saveSession(resolvedIdentity, data.access_token);
        return { success: true, role: mappedRole };
      } else {
        const errJson = await response.json().catch(() => ({}));
        return { success: false, error: errJson.detail || 'Invalid email or password.' };
      }
    } catch {
      // Backend unavailable fallback
      return {
        success: false,
        error: 'Unable to reach authentication server. You may click one of the quick Demo Access buttons below.',
      };
    }
  };

  const logout = () => {
    setUser(null);
    setToken(null);
    localStorage.removeItem(STORAGE_USER_KEY);
    localStorage.removeItem(STORAGE_TOKEN_KEY);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        token,
        isAuthenticated: !!user,
        isLoading,
        login,
        loginAsDemo,
        logout,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = (): AuthContextType => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
