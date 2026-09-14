import React, { useState } from 'react';
import {
  CheckSquare,
  Square,
  MapPin,
  Camera,
  CheckCircle2,
  ShieldCheck
} from 'lucide-react';
import { Badge } from '../../components/ui/Badge';
import { useCityData } from '../../context/CityDataContext';
import { useToast } from '../../context/ToastContext';
import { WorkOrderTask } from '../../types';

export const WorkOrderQueue: React.FC = () => {
  const { workOrders, updateWorkOrderStatus } = useCityData();
  const { success, info } = useToast();

  const [selectedId, setSelectedId] = useState<string>(workOrders[0]?.id || '');
  const [filter, setFilter] = useState<string>('ALL');

  // Selected Order
  const activeOrder = workOrders.find((w) => w.id === selectedId) || workOrders[0];

  // Checklist state per active order
  const [tasks, setTasks] = useState<WorkOrderTask[]>([
    { id: 't1', title: 'Deploy orange safety cones & perimeter warning signage', completed: true },
    { id: 't2', title: 'Conduct initial structural depth inspection & measure boundary', completed: true },
    { id: 't3', title: 'Saw-cut square edge and clear subgrade loose aggregates', completed: false },
    { id: 't4', title: 'Apply hot bitumen tack coat and mechanical roller compaction', completed: false },
    { id: 't5', title: 'Capture high-resolution completion evidence photo', completed: false },
  ]);

  const [notes, setNotes] = useState<string>(activeOrder?.field_notes || '');
  const [hasEvidence, setHasEvidence] = useState<boolean>(false);

  const filteredOrders = workOrders.filter((wo) => {
    if (filter === 'ALL') return true;
    if (filter === 'ACTIVE') return wo.status !== 'COMPLETED' && wo.status !== 'VERIFICATION';
    if (filter === 'COMPLETED') return wo.status === 'COMPLETED' || wo.status === 'VERIFICATION';
    return true;
  });

  const handleToggleTask = (taskId: string) => {
    const updated = tasks.map((t) => (t.id === taskId ? { ...t, completed: !t.completed } : t));
    setTasks(updated);

    const completedCount = updated.filter((t) => t.completed).length;
    const pct = Math.round((completedCount / updated.length) * 100);

    if (activeOrder) {
      const nextStatus = pct === 100 ? 'COMPLETED' : 'IN_PROGRESS';
      updateWorkOrderStatus(activeOrder.id, nextStatus, pct, notes);
      if (pct === 100) {
        success('Work Order Completed', `All tasks verified for ${activeOrder.order_number}. Complaint resolved.`);
      }
    }
  };

  const handleStatusStep = (newStatus: string) => {
    if (!activeOrder) return;
    const pct = newStatus === 'COMPLETED' ? 100 : activeOrder.completion_percentage;
    updateWorkOrderStatus(activeOrder.id, newStatus, pct, notes);
    success('Status Updated', `Work Order ${activeOrder.order_number} transitioned to ${newStatus}.`);
  };

  const workflowSteps = [
    'ASSIGNED',
    'ACCEPTED',
    'EN_ROUTE',
    'ON_SITE',
    'IN_PROGRESS',
    'COMPLETED',
  ];

  return (
    <div className="space-y-4 select-none font-sans">
      {/* Header & Filter */}
      <div className="bg-white p-4 rounded-xl border border-surface-border shadow-civic flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div>
          <h2 className="text-base font-bold text-city-forest">
            Municipal Work Order Dispatch Queue
          </h2>
          <p className="text-xs text-city-charcoal/70 mt-0.5">
            Real-time field execution desk linked directly to citizen complaints & admin audit ledger.
          </p>
        </div>

        <div className="flex items-center space-x-1.5 bg-surface-muted p-1 rounded-lg border border-surface-border">
          {(['ALL', 'ACTIVE', 'COMPLETED'] as const).map((f) => (
            <button
              key={f}
              onClick={() => setFilter(f)}
              className={`px-3 py-1 rounded text-xs font-semibold transition-colors ${
                filter === f
                  ? 'bg-city-forest text-white shadow-sm'
                  : 'text-city-charcoal/70 hover:text-city-charcoal'
              }`}
            >
              {f === 'ALL' ? 'All Jobs' : f === 'ACTIVE' ? 'Active Jobs' : 'Completed'}
            </button>
          ))}
        </div>
      </div>

      {/* Main Split Grid: Left List, Right Inspector */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-5">
        {/* Left: Work Order Cards List */}
        <div className="lg:col-span-5 space-y-2.5">
          {filteredOrders.length === 0 ? (
            <div className="bg-white p-8 rounded-xl border border-surface-border text-center text-xs text-city-charcoal/60">
              No work orders match the selected filter.
            </div>
          ) : (
            filteredOrders.map((wo) => {
              const isSelected = activeOrder?.id === wo.id;
              return (
                <div
                  key={wo.id}
                  onClick={() => {
                    setSelectedId(wo.id);
                    setNotes(wo.field_notes || '');
                  }}
                  className={`p-4 rounded-xl border transition-all cursor-pointer text-left space-y-2.5 ${
                    isSelected
                      ? 'bg-city-terracotta/10 border-city-terracotta ring-1 ring-city-terracotta shadow-civic'
                      : 'bg-white border-surface-border hover:border-city-terracotta/40 shadow-sm'
                  }`}
                >
                  <div className="flex items-center justify-between">
                    <span className="font-mono text-xs font-bold text-city-terracotta">
                      {wo.order_number}
                    </span>
                    <Badge status={wo.status}>{wo.status}</Badge>
                  </div>

                  <div>
                    <h3 className="text-xs font-bold text-city-forest leading-snug">{wo.title}</h3>
                    <p className="text-[11px] text-city-charcoal/70 mt-0.5 flex items-center space-x-1">
                      <MapPin className="w-3 h-3 text-city-terracotta shrink-0" />
                      <span className="truncate">{wo.location_address}</span>
                    </p>
                  </div>

                  <div className="pt-2 border-t border-surface-border flex items-center justify-between text-[11px]">
                    <div className="flex items-center space-x-2">
                      <span className="text-city-charcoal/60">Progress:</span>
                      <div className="w-16 bg-surface-muted h-1.5 rounded-full overflow-hidden">
                        <div
                          className="bg-city-terracotta h-full rounded-full"
                          style={{ width: `${wo.completion_percentage}%` }}
                        />
                      </div>
                      <span className="font-mono font-bold text-city-forest">{wo.completion_percentage}%</span>
                    </div>

                    <span className="font-semibold text-city-amber font-mono">
                      {wo.priority}
                    </span>
                  </div>
                </div>
              );
            })
          )}
        </div>

        {/* Right: Selected Order Detailed Inspector Panel */}
        <div className="lg:col-span-7">
          {activeOrder ? (
            <div className="bg-white rounded-xl border border-surface-border p-6 shadow-civic space-y-6">
              {/* Top Order Title & Badges */}
              <div className="pb-4 border-b border-surface-border flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div>
                  <div className="flex items-center space-x-2">
                    <span className="font-mono text-xs font-extrabold text-city-terracotta">
                      {activeOrder.order_number}
                    </span>
                    <Badge status={activeOrder.status}>{activeOrder.status}</Badge>
                    <Badge status={activeOrder.priority}>{activeOrder.priority}</Badge>
                  </div>
                  <h3 className="text-base font-bold text-city-forest mt-1">
                    {activeOrder.title}
                  </h3>
                </div>

                <div className="text-left sm:text-right">
                  <span className="text-[10px] text-city-charcoal/60 block">SLA DEADLINE</span>
                  <span className="text-xs font-mono font-bold text-city-terracotta">
                    {activeOrder.due_date ? new Date(activeOrder.due_date).toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit' }) : '14 Sep 14:00'}
                  </span>
                </div>
              </div>

              {/* Status Progression Bar */}
              <div>
                <p className="text-xs font-semibold text-city-forest mb-2">
                  Operational Workflow State Transition
                </p>
                <div className="grid grid-cols-3 sm:grid-cols-6 gap-1.5">
                  {workflowSteps.map((step) => {
                    const isCurrent = activeOrder.status === step;
                    return (
                      <button
                        key={step}
                        type="button"
                        onClick={() => handleStatusStep(step)}
                        className={`py-1.5 px-2 rounded text-[10px] font-mono font-bold transition-all border ${
                          isCurrent
                            ? 'bg-city-terracotta text-white border-city-terracotta shadow-sm ring-2 ring-city-amber/30'
                            : 'bg-surface-card text-city-charcoal/70 border-surface-border hover:bg-city-sand/30'
                        }`}
                      >
                        {step}
                      </button>
                    );
                  })}
                </div>
              </div>

              {/* Field Verification Checklist */}
              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <p className="text-xs font-bold text-city-forest flex items-center space-x-1.5">
                    <CheckCircle2 className="w-4 h-4 text-city-terracotta" />
                    <span>Field Procedure & Safety Checklist</span>
                  </p>
                  <span className="text-xs font-mono text-city-forest font-bold">
                    {activeOrder.completion_percentage}% Done
                  </span>
                </div>

                <div className="space-y-2 bg-surface-card p-3.5 rounded-xl border border-surface-border">
                  {tasks.map((task) => (
                    <button
                      key={task.id}
                      type="button"
                      onClick={() => handleToggleTask(task.id)}
                      className="w-full flex items-start space-x-2.5 p-1.5 rounded text-left hover:bg-white transition-colors"
                    >
                      {task.completed ? (
                        <CheckSquare className="w-4 h-4 text-city-terracotta shrink-0 mt-0.5" />
                      ) : (
                        <Square className="w-4 h-4 text-city-charcoal/40 shrink-0 mt-0.5" />
                      )}
                      <span
                        className={`text-xs ${
                          task.completed
                            ? 'line-through text-city-charcoal/50'
                            : 'text-city-charcoal font-medium'
                        }`}
                      >
                        {task.title}
                      </span>
                    </button>
                  ))}
                </div>
              </div>

              {/* Evidence Capture & Notes UI */}
              <div className="space-y-3 pt-2">
                <p className="text-xs font-bold text-city-forest">
                  Field Evidence & Completion Photo
                </p>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div
                    onClick={() => {
                      setHasEvidence(true);
                      info('Evidence Uploaded', 'Asphalt compaction photo attached to work order record.');
                    }}
                    className={`p-4 rounded-xl border-2 border-dashed flex flex-col items-center justify-center text-center cursor-pointer transition-colors ${
                      hasEvidence
                        ? 'border-city-success bg-city-sand/30'
                        : 'border-surface-border bg-surface-card hover:bg-city-sand/20'
                    }`}
                  >
                    <Camera className="w-6 h-6 text-city-forest mb-1" />
                    <span className="text-xs font-semibold text-city-forest">
                      {hasEvidence ? 'Evidence Photo Attached ✓' : 'Upload Field Evidence Photo'}
                    </span>
                    <span className="text-[10px] text-city-charcoal/60 mt-0.5">
                      JPG/PNG with GPS EXIF timestamp
                    </span>
                  </div>

                  <div className="space-y-1">
                    <label className="block text-[11px] font-semibold text-city-charcoal">
                      Field Notes / Crew Observations
                    </label>
                    <textarea
                      rows={3}
                      value={notes}
                      onChange={(e) => setNotes(e.target.value)}
                      placeholder="Enter details on weather conditions, materials used, compaction tests..."
                      className="w-full p-2.5 rounded-lg border border-surface-border text-xs text-city-charcoal focus:outline-none focus:ring-1 focus:ring-city-terracotta"
                    />
                  </div>
                </div>
              </div>

              {/* Action Submit */}
              <div className="pt-4 border-t border-surface-border flex items-center justify-between">
                <div className="text-xs text-city-charcoal/60 flex items-center space-x-1.5">
                  <ShieldCheck className="w-4 h-4 text-city-leaf" />
                  <span>Syncs automatically with Citizen complaint & Admin command radar.</span>
                </div>

                <button
                  type="button"
                  onClick={() => handleStatusStep('COMPLETED')}
                  className="px-5 py-2.5 rounded-lg bg-city-terracotta hover:bg-city-terracotta-dark text-white text-xs font-bold shadow-civic border border-city-amber/30 transition-colors flex items-center space-x-2"
                >
                  <CheckCircle2 className="w-4 h-4" />
                  <span>Mark Work Order Completed</span>
                </button>
              </div>
            </div>
          ) : (
            <div className="bg-white p-12 rounded-xl border border-surface-border text-center text-xs text-city-charcoal/60">
              Select a work order from the left to view operational details and update status.
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
