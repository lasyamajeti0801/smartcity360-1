import React, { useState } from 'react';
import { Outlet } from 'react-router-dom';
import { MunicipalNavbar } from './MunicipalNavbar';
import { MunicipalSidebar } from './MunicipalSidebar';
import { Footer } from './Footer';
import { ReportIssueModal } from '../../features/citizen/ReportIssueModal';
import { useCityData } from '../../context/CityDataContext';
import { useToast } from '../../context/ToastContext';

export const DashboardLayout: React.FC = () => {
  const [isReportModalOpen, setIsReportModalOpen] = useState(false);
  const { categories, addComplaint } = useCityData();
  const { success, error } = useToast();

  const handleCreateComplaint = async (newComplaintData: any) => {
    try {
      const created = await addComplaint(newComplaintData);
      success('Civic Grievance Registered', `Ticket ${created.ticket_number} created with active SAKALA SLA tracking.`);
      setIsReportModalOpen(false);
    } catch (err: any) {
      error('Registration Failed', err?.message || 'Unable to submit report.');
    }
  };

  return (
    <div className="min-h-screen flex flex-col bg-city-ivory text-city-charcoal font-sans">
      <MunicipalNavbar onReportClick={() => setIsReportModalOpen(true)} />

      <div className="flex flex-1">
        <MunicipalSidebar />

        <main className="flex-1 p-4 sm:p-6 lg:p-8 max-w-7xl mx-auto w-full overflow-y-auto">
          <Outlet context={{ onOpenReportModal: () => setIsReportModalOpen(true) }} />
        </main>
      </div>

      <Footer />

      {/* Global Citizen Grievance Lodgment Modal */}
      <ReportIssueModal
        isOpen={isReportModalOpen}
        onClose={() => setIsReportModalOpen(false)}
        categories={categories}
        onSubmit={handleCreateComplaint}
      />
    </div>
  );
};
