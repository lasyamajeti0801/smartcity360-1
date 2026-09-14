import React from 'react';
import { Link } from 'react-router-dom';
import { ClipboardList } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { useCityData } from '../../context/CityDataContext';
import { WorkOrderQueue } from './WorkOrderQueue';

export const StaffDashboard: React.FC = () => {
  const { user } = useAuth();
  const { workOrders } = useCityData();

  // Filter orders for Staff department (default ROADS)
  const staffDept = user?.departmentCode || 'ROADS';
  const deptOrders = workOrders.filter(
    (wo) => wo.department_id === staffDept || wo.assigned_technician_id === user?.id
  );

  const assignedCount = deptOrders.filter((wo) => wo.status === 'ASSIGNED' || wo.status === 'ACCEPTED').length;
  const inProgressCount = deptOrders.filter((wo) => wo.status === 'IN_PROGRESS' || wo.status === 'EN_ROUTE' || wo.status === 'ON_SITE').length;
  const completedCount = deptOrders.filter((wo) => wo.status === 'COMPLETED' || wo.status === 'VERIFICATION').length;
  const dueTodayCount = deptOrders.filter((wo) => wo.priority === 'HIGH' && wo.status !== 'COMPLETED').length;

  return (
    <div className="space-y-6 select-none font-sans">
      {/* 1. Operational Shift Banner */}
      <div className="bg-gradient-to-r from-[#1F0A38] via-[#38125E] to-[#18082B] text-white p-5 rounded-xl border border-purple-800/40 shadow-md flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div className="space-y-1">
          <div className="flex items-center space-x-2.5">
            <h1 className="text-xl font-bold tracking-tight text-white">
              Good morning, {user?.fullName || 'Arjun'}
            </h1>
            <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-purple-900/80 text-purple-200 border border-purple-500/30 font-bold uppercase">
              ACTIVE SHIFT
            </span>
          </div>
          <p className="text-xs text-purple-200/80 flex items-center space-x-2">
            <span>{user?.subRole || 'Field Operations Officer'}</span>
            <span className="text-purple-400">•</span>
            <span className="text-purple-200 font-semibold">{user?.zone || 'Central Zone'}</span>
            <span className="text-purple-400">•</span>
            <span className="font-mono text-purple-300">{user?.badgeOrWard || 'STF-2087'}</span>
          </p>
        </div>

        <div className="flex items-center gap-3">
          <div className="text-right hidden sm:block">
            <span className="text-[10px] text-purple-300/60 block">SHIFT TIMING</span>
            <span className="text-xs font-mono font-bold text-purple-200">07:00 - 16:00 IST</span>
          </div>

          <Link
            to="/staff/work-orders"
            className="flex items-center space-x-1.5 px-4 py-2.5 rounded-lg bg-gradient-to-r from-purple-600 to-purple-700 hover:from-purple-500 hover:to-purple-600 text-white text-xs font-bold shadow-md border border-purple-400/30 transition-colors"
          >
            <ClipboardList className="w-4 h-4" />
            <span>Open Work Order Queue</span>
          </Link>
        </div>
      </div>

      {/* 2. Operational KPI Cards */}
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3">
        <div className="bg-white p-3.5 rounded-xl border border-surface-border shadow-civic">
          <span className="text-[11px] font-semibold text-city-charcoal/70 block">Assigned Today</span>
          <p className="text-2xl font-extrabold font-mono text-city-forest mt-1">{assignedCount}</p>
          <span className="text-[10px] text-city-charcoal/50">Dispatched jobs</span>
        </div>

        <div className="bg-white p-3.5 rounded-xl border border-surface-border shadow-civic">
          <span className="text-[11px] font-semibold text-city-charcoal/70 block">In Progress</span>
          <p className="text-2xl font-extrabold font-mono text-city-amber mt-1">{inProgressCount}</p>
          <span className="text-[10px] text-city-charcoal/50">Field crews on-site</span>
        </div>

        <div className="bg-white p-3.5 rounded-xl border border-surface-border shadow-civic">
          <span className="text-[11px] font-semibold text-city-charcoal/70 block">Due Today</span>
          <p className="text-2xl font-extrabold font-mono text-city-terracotta mt-1">{dueTodayCount}</p>
          <span className="text-[10px] text-city-charcoal/50">&lt; 12h SLA left</span>
        </div>

        <div className="bg-white p-3.5 rounded-xl border border-surface-border shadow-civic">
          <span className="text-[11px] font-semibold text-city-charcoal/70 block">Completed</span>
          <p className="text-2xl font-extrabold font-mono text-city-success mt-1">{completedCount}</p>
          <span className="text-[10px] text-city-charcoal/50">Verified resolutions</span>
        </div>

        <div className="bg-white p-3.5 rounded-xl border border-surface-border shadow-civic">
          <span className="text-[11px] font-semibold text-city-charcoal/70 block">SLA Compliance</span>
          <p className="text-2xl font-extrabold font-mono text-city-forest mt-1">94.2%</p>
          <span className="text-[10px] text-city-success font-medium">Within target</span>
        </div>

        <div className="bg-white p-3.5 rounded-xl border border-surface-border shadow-civic">
          <span className="text-[11px] font-semibold text-city-charcoal/70 block">SLA Risk Alerts</span>
          <p className="text-2xl font-extrabold font-mono text-city-danger mt-1">0</p>
          <span className="text-[10px] text-city-charcoal/50">Zero breaches</span>
        </div>
      </div>

      {/* 3. Embedded Main Operational Work Order Queue */}
      <WorkOrderQueue />
    </div>
  );
};
