import React from 'react';
import {
  BrowserRouter,
  Routes,
  Route,
  Navigate,
  useOutletContext
} from 'react-router-dom';

// Context Providers
import { AuthProvider } from '../context/AuthContext';
import { CityDataProvider, useCityData } from '../context/CityDataContext';
import { ToastProvider } from '../context/ToastContext';

// Layout & Route Guards
import { DashboardLayout } from '../components/layout/DashboardLayout';
import { RoleGuard } from '../components/layout/RoleGuard';

// Gateways
import { LandingPage } from '../features/landing/LandingPage';
import { LoginPage } from '../features/auth/LoginPage';
import { UnauthorizedPage } from '../features/auth/UnauthorizedPage';

// Citizen Features
import { CitizenDashboard } from '../features/citizen/CitizenDashboard';
import { CitizenRequestsPage } from '../features/citizen/CitizenRequestsPage';
import { CitizenPaymentsPage } from '../features/citizen/CitizenPaymentsPage';
import { ServiceCatalog } from '../features/citizen/ServiceCatalog';

// Staff Features
import { StaffDashboard } from '../features/staff/StaffDashboard';
import { WorkOrderQueue } from '../features/staff/WorkOrderQueue';

// Admin Features
import { AdminDashboard } from '../features/admin/AdminDashboard';
import { EmergencyControlCenter } from '../features/emergency/EmergencyControlCenter';
import { CitizensDirectory } from '../features/citizens/CitizensDirectory';
import { TrafficTransitControl } from '../features/traffic/TrafficTransitControl';
import { WasteManagementSystem } from '../features/waste/WasteManagementSystem';
import { WaterTelemetrySystem } from '../features/water/WaterTelemetrySystem';
import { ReportsAnalytics } from '../features/reports/ReportsAnalytics';
import { NotificationsCenter } from '../features/notifications/NotificationsCenter';
import { CitySettings } from '../features/settings/CitySettings';

// Shared Features & Map
import { ProfilePage } from '../features/shared/ProfilePage';
import { CityMap } from '../components/maps/CityMap';

// Reusable GIS Map View
const MapWrapper: React.FC<{ title: string; subtitle: string }> = ({ title, subtitle }) => {
  const { complaints, facilities } = useCityData();
  return (
    <div className="bg-white p-5 rounded-xl border border-surface-border shadow-civic space-y-3">
      <div>
        <h2 className="text-base font-bold text-city-forest">{title}</h2>
        <p className="text-xs text-city-charcoal/70">{subtitle}</p>
      </div>
      <div className="h-[620px] w-full rounded-xl overflow-hidden border border-surface-border">
        <CityMap complaints={complaints} facilities={facilities} />
      </div>
    </div>
  );
};

// Citizen Dashboard Outlet Adapter
const CitizenDashboardWrapper: React.FC = () => {
  const { onOpenReportModal } = useOutletContext<{ onOpenReportModal?: () => void }>() || {};
  return <CitizenDashboard onOpenReportModal={onOpenReportModal} />;
};

const CitizenRequestsWrapper: React.FC = () => {
  const { onOpenReportModal } = useOutletContext<{ onOpenReportModal?: () => void }>() || {};
  return <CitizenRequestsPage onOpenReportModal={onOpenReportModal} />;
};

export const App: React.FC = () => {
  return (
    <ToastProvider>
      <AuthProvider>
        <CityDataProvider>
          <BrowserRouter>
            <Routes>
              {/* Public Entry Gateways */}
              <Route path="/" element={<LandingPage />} />
              <Route path="/login" element={<LoginPage />} />
              <Route path="/unauthorized" element={<UnauthorizedPage />} />

              {/* 1. CITIZEN ROLE WORKSPACE */}
              <Route
                path="/citizen"
                element={
                  <RoleGuard allowedRoles={['Citizen']}>
                    <DashboardLayout />
                  </RoleGuard>
                }
              >
                <Route index element={<Navigate to="/citizen/dashboard" replace />} />
                <Route path="dashboard" element={<CitizenDashboardWrapper />} />
                <Route path="my-requests" element={<CitizenRequestsWrapper />} />
                <Route path="report" element={<CitizenRequestsWrapper />} />
                <Route path="services" element={<ServiceCatalog />} />
                <Route
                  path="map"
                  element={
                    <MapWrapper
                      title="Ward 04 Public Infrastructure & Issue Radar"
                      subtitle="Interactive OpenStreetMap showing nearby clinics, public schools, and community reports."
                    />
                  }
                />
                <Route path="payments" element={<CitizenPaymentsPage />} />
                <Route path="notifications" element={<NotificationsCenter />} />
                <Route path="emergency" element={<EmergencyControlCenter />} />
                <Route path="profile" element={<ProfilePage />} />
              </Route>

              {/* 2. FIELD STAFF WORKSPACE */}
              <Route
                path="/staff"
                element={
                  <RoleGuard allowedRoles={['Staff']}>
                    <DashboardLayout />
                  </RoleGuard>
                }
              >
                <Route index element={<Navigate to="/staff/dashboard" replace />} />
                <Route path="dashboard" element={<StaffDashboard />} />
                <Route path="work-orders" element={<WorkOrderQueue />} />
                <Route
                  path="map"
                  element={
                    <MapWrapper
                      title="Field Operations Route & Infrastructure Map"
                      subtitle="GPS-tracked work orders, utility pipelines, and active dispatch markers."
                    />
                  }
                />
                <Route path="department" element={<WorkOrderQueue />} />
                <Route path="emergency-alerts" element={<EmergencyControlCenter />} />
                <Route path="reports" element={<ReportsAnalytics />} />
                <Route path="notifications" element={<NotificationsCenter />} />
                <Route path="profile" element={<ProfilePage />} />
              </Route>

              {/* 3. CITY ADMIN COMMAND CENTRE */}
              <Route
                path="/admin"
                element={
                  <RoleGuard allowedRoles={['Admin']}>
                    <DashboardLayout />
                  </RoleGuard>
                }
              >
                <Route index element={<Navigate to="/admin/dashboard" replace />} />
                <Route path="dashboard" element={<AdminDashboard />} />
                <Route path="requests" element={<CitizenRequestsWrapper />} />
                <Route path="work-orders" element={<WorkOrderQueue />} />
                <Route path="departments" element={<AdminDashboard />} />
                <Route path="staff" element={<CitizensDirectory />} />
                <Route path="citizens" element={<CitizensDirectory />} />
                <Route
                  path="map"
                  element={
                    <MapWrapper
                      title="City-Wide Master GIS Operational Command Radar"
                      subtitle="Comprehensive multi-layer GIS: active complaints, maintenance crews, and public emergency facilities."
                    />
                  }
                />
                <Route path="emergency" element={<EmergencyControlCenter />} />
                <Route path="traffic" element={<TrafficTransitControl />} />
                <Route path="water" element={<WaterTelemetrySystem />} />
                <Route path="waste" element={<WasteManagementSystem />} />
                <Route path="analytics" element={<ReportsAnalytics />} />
                <Route path="settings" element={<CitySettings />} />
                <Route path="notifications" element={<NotificationsCenter />} />
                <Route path="audit-logs" element={<CitySettings />} />
                <Route path="profile" element={<ProfilePage />} />
              </Route>

              {/* Fallback */}
              <Route path="*" element={<Navigate to="/" replace />} />
            </Routes>
          </BrowserRouter>
        </CityDataProvider>
      </AuthProvider>
    </ToastProvider>
  );
};
