import React, { useState, useEffect } from 'react';
import { Navbar } from '../components/layout/Navbar';
import { Sidebar } from '../components/layout/Sidebar';
import { Footer } from '../components/layout/Footer';
import { CitizenDashboard } from '../features/citizen/CitizenDashboard';
import { ServiceCatalog } from '../features/citizen/ServiceCatalog';
import { ReportIssueModal } from '../features/citizen/ReportIssueModal';
import { AdminDashboard } from '../features/admin/AdminDashboard';
import { WorkOrderQueue } from '../features/staff/WorkOrderQueue';
import { EmergencyControlCenter } from '../features/emergency/EmergencyControlCenter';
import { CitizensDirectory } from '../features/citizens/CitizensDirectory';
import { TrafficTransitControl } from '../features/traffic/TrafficTransitControl';
import { WasteManagementSystem } from '../features/waste/WasteManagementSystem';
import { WaterTelemetrySystem } from '../features/water/WaterTelemetrySystem';
import { ReportsAnalytics } from '../features/reports/ReportsAnalytics';
import { NotificationsCenter } from '../features/notifications/NotificationsCenter';
import { CitySettings } from '../features/settings/CitySettings';
import { CityMap } from '../components/maps/CityMap';
import { Card } from '../components/ui/Card';
import { apiClient } from '../services/api';
import {
  Complaint,
  ComplaintCategory,
  Facility,
  CityKPIs,
  UserRole
} from '../types';

export const App: React.FC = () => {
  const [currentRole, setCurrentRole] = useState<UserRole>('Citizen');
  const [activeTab, setActiveTab] = useState<string>('dashboard');
  const [isReportModalOpen, setIsReportModalOpen] = useState(false);

  // Application Data States
  const [complaints, setComplaints] = useState<Complaint[]>([]);
  const [categories, setCategories] = useState<ComplaintCategory[]>([]);
  const [facilities, setFacilities] = useState<Facility[]>([]);
  const [kpis, setKpis] = useState<CityKPIs>({
    total_complaints: 3,
    resolved_complaints: 1,
    active_complaints: 2,
    resolution_rate_percentage: 66.7,
    sla_compliance_percentage: 94.2,
    active_emergencies: 2,
    active_work_orders: 5,
    average_resolution_hours: 28.5,
  });

  // Load initial civic dataset
  useEffect(() => {
    const loadData = async () => {
      const [fetchedComplaints, fetchedCategories, fetchedFacilities, fetchedKpis] = await Promise.all([
        apiClient.getComplaints(),
        apiClient.getCategories(),
        apiClient.getFacilities(),
        apiClient.getKPIs(),
      ]);
      setComplaints(fetchedComplaints);
      setCategories(fetchedCategories);
      setFacilities(fetchedFacilities);
      setKpis(fetchedKpis);
    };
    loadData();
  }, []);

  const handleRoleChange = (newRole: UserRole) => {
    setCurrentRole(newRole);
    if (newRole === 'Emergency Operator') {
      setActiveTab('emergency');
    } else if (newRole === 'Field Staff' || newRole === 'Department Staff') {
      setActiveTab('workorders');
    } else {
      setActiveTab('dashboard');
    }
  };

  const handleCreateComplaint = async (newComplaintData: Partial<Complaint>) => {
    const created = await apiClient.createComplaint(newComplaintData as any);
    setComplaints((prev) => [created, ...prev]);
    setKpis((prev) => ({
      ...prev,
      total_complaints: prev.total_complaints + 1,
      active_complaints: prev.active_complaints + 1,
    }));
  };

  // Render view based on active tab & role
  const renderContent = () => {
    switch (activeTab) {
      case 'citizens':
        return <CitizensDirectory />;

      case 'services':
        return <ServiceCatalog />;

      case 'emergency':
        return <EmergencyControlCenter />;

      case 'traffic':
        return <TrafficTransitControl />;

      case 'waste':
        return <WasteManagementSystem />;

      case 'water':
        return <WaterTelemetrySystem />;

      case 'reports':
        return <ReportsAnalytics />;

      case 'notifications':
        return <NotificationsCenter />;

      case 'settings':
        return <CitySettings />;

      case 'workorders':
        return <WorkOrderQueue />;

      case 'map':
        return (
          <Card
            title="Municipal GIS Geospatial Asset & Infrastructure Radar"
            subtitle="Interactive OpenStreetMap layer with public facilities, medical clinics, and live reported issues."
          >
            <div className="h-[620px] w-full">
              <CityMap complaints={complaints} facilities={facilities} />
            </div>
          </Card>
        );

      case 'complaints':
        if (currentRole === 'City Administrator' || currentRole === 'System Administrator') {
          return <AdminDashboard kpis={kpis} complaints={complaints} />;
        }
        if (currentRole === 'Field Staff' || currentRole === 'Department Staff') {
          return <WorkOrderQueue />;
        }
        return (
          <CitizenDashboard
            complaints={complaints}
            facilities={facilities}
            onOpenReportModal={() => setIsReportModalOpen(true)}
            onNavigateToServices={() => setActiveTab('services')}
            onNavigateToTab={(t) => setActiveTab(t)}
          />
        );

      case 'dashboard':
      default:
        if (currentRole === 'Emergency Operator') {
          return <EmergencyControlCenter />;
        }
        if (currentRole === 'Field Staff' || currentRole === 'Department Staff') {
          return <WorkOrderQueue />;
        }
        if (currentRole === 'City Administrator' || currentRole === 'System Administrator') {
          return <AdminDashboard kpis={kpis} complaints={complaints} />;
        }
        return (
          <CitizenDashboard
            complaints={complaints}
            facilities={facilities}
            onOpenReportModal={() => setIsReportModalOpen(true)}
            onNavigateToServices={() => setActiveTab('services')}
            onNavigateToTab={(t) => setActiveTab(t)}
          />
        );
    }
  };

  return (
    <div className="min-h-screen flex flex-col bg-slate-100 text-slate-900 font-sans">
      <Navbar
        currentRole={currentRole}
        onRoleChange={handleRoleChange}
        onReportClick={() => setIsReportModalOpen(true)}
        activeTab={activeTab}
      />

      <div className="flex flex-1">
        <Sidebar
          currentRole={currentRole}
          activeTab={activeTab}
          onTabChange={(tab) => setActiveTab(tab)}
        />

        <main className="flex-1 p-6 max-w-7xl mx-auto w-full overflow-y-auto">
          {renderContent()}
        </main>
      </div>

      <Footer />

      {/* Global Citizen Issue Report Modal */}
      <ReportIssueModal
        isOpen={isReportModalOpen}
        onClose={() => setIsReportModalOpen(false)}
        categories={categories}
        onSubmit={handleCreateComplaint}
      />
    </div>
  );
};

