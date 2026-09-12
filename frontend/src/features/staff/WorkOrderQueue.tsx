import React, { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { Badge } from '../../components/ui/Badge';
import { Button } from '../../components/ui/Button';
import { Table, Column } from '../../components/ui/Table';
import { WorkOrder } from '../../types';
import { CheckSquare, Square, MapPin, Camera, CheckCircle2 } from 'lucide-react';

export const WorkOrderQueue: React.FC = () => {
  const [workOrders] = useState<WorkOrder[]>([
    {
      id: 'wo-1',
      order_number: 'WO-20260912-001',
      title: 'Pothole Excavation & Cold Mix Asphalt Remediation',
      description: 'Excavate 15cm road crater, clear loose debris, compact subgrade, and lay asphalt binder.',
      priority: 'HIGH',
      status: 'IN_PROGRESS',
      completion_percentage: 65,
      department_id: 'ROADS',
      assigned_technician_id: 'tech-01',
      latitude: 12.9716,
      longitude: 77.5946,
      location_address: 'MG Road Junction, Ward 4',
      due_date: '2026-09-13T14:00:00Z',
      created_at: '2026-09-12T08:45:00Z',
    },
    {
      id: 'wo-2',
      order_number: 'WO-20260912-002',
      title: 'High-Output LED Luminaire Module Replacement',
      description: 'Replace 4 burnt out 60W LED fixtures on Street Poles #402 through #405.',
      priority: 'MEDIUM',
      status: 'ACCEPTED',
      completion_percentage: 15,
      department_id: 'ELECTRICAL',
      assigned_technician_id: 'tech-02',
      latitude: 12.9684,
      longitude: 77.5891,
      location_address: 'Elm Avenue, Sector 7',
      due_date: '2026-09-14T10:00:00Z',
      created_at: '2026-09-12T09:10:00Z',
    },
  ]);

  const [selectedOrder, setSelectedOrder] = useState<WorkOrder>(workOrders[0]);
  const [tasks, setTasks] = useState<{ id: string; title: string; completed: boolean }[]>([
    { id: 't1', title: 'Deploy orange safety cones and warning signage', completed: true },
    { id: 't2', title: 'Saw-cut square perimeter around damaged asphalt crater', completed: true },
    { id: 't3', title: 'Pave hot asphalt mix and mechanical roller compaction', completed: false },
    { id: 't4', title: 'Capture high-resolution completion evidence photo', completed: false },
  ]);

  const handleToggleTask = (taskId: string) => {
    const updated = tasks.map((t) => (t.id === taskId ? { ...t, completed: !t.completed } : t));
    setTasks(updated);
    const completedCount = updated.filter((t) => t.completed).length;
    const pct = Math.round((completedCount / updated.length) * 100);

    setSelectedOrder((prev) => ({
      ...prev,
      completion_percentage: pct,
      status: pct === 100 ? 'VERIFICATION' : 'IN_PROGRESS',
    }));
  };

  const columns: Column<WorkOrder>[] = [
    {
      key: 'order_number',
      header: 'Order #',
      render: (wo) => <span className="font-mono font-bold text-sky-700">{wo.order_number}</span>,
    },
    {
      key: 'title',
      header: 'Assigned Task',
      render: (wo) => (
        <div>
          <div className="font-medium text-slate-900">{wo.title}</div>
          <div className="text-xs text-slate-500">{wo.location_address}</div>
        </div>
      ),
    },
    {
      key: 'priority',
      header: 'Priority',
      render: (wo) => <Badge status={wo.priority}>{wo.priority}</Badge>,
    },
    {
      key: 'status',
      header: 'Status',
      render: (wo) => <Badge status={wo.status}>{wo.status}</Badge>,
    },
    {
      key: 'completion_percentage',
      header: 'Progress',
      render: (wo) => (
        <div className="flex items-center space-x-2">
          <div className="w-16 bg-slate-200 h-2 rounded-full overflow-hidden">
            <div className="bg-sky-600 h-full" style={{ width: `${wo.completion_percentage}%` }} />
          </div>
          <span className="text-xs font-mono font-medium text-slate-700">{wo.completion_percentage}%</span>
        </div>
      ),
    },
  ];

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between border-b border-slate-200 pb-4">
        <div>
          <h1 className="text-xl font-bold text-slate-900 tracking-tight">Field Staff Work Order Queue</h1>
          <p className="text-xs text-slate-500 mt-0.5">
            Operational work tickets dispatched to maintenance crews with field checklist verification.
          </p>
        </div>
        <Badge status="IN_PROGRESS">{workOrders.length} Dispatched Tasks</Badge>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left 7 cols: Work Order List */}
        <div className="lg:col-span-7">
          <Card title="Dispatched Work Orders" subtitle="Select a task to review checklist and update status.">
            <Table
              columns={columns}
              data={workOrders}
              keyExtractor={(wo) => wo.id}
              onRowClick={(wo) => setSelectedOrder(wo)}
            />
          </Card>
        </div>

        {/* Right 5 cols: Active Work Order Details & Checklist */}
        <div className="lg:col-span-5">
          <Card
            title={selectedOrder.order_number}
            subtitle={selectedOrder.title}
            action={<Badge status={selectedOrder.status}>{selectedOrder.status}</Badge>}
          >
            <div className="space-y-4">
              <div className="p-3 bg-slate-50 rounded-md border border-slate-200 text-xs text-slate-600 space-y-1.5">
                <div className="flex items-center text-slate-700 font-medium">
                  <MapPin className="h-3.5 w-3.5 text-sky-600 mr-1.5 shrink-0" />
                  <span>{selectedOrder.location_address}</span>
                </div>
                <p className="leading-relaxed">{selectedOrder.description}</p>
              </div>

              {/* Progress bar */}
              <div>
                <div className="flex items-center justify-between text-xs font-semibold mb-1">
                  <span className="text-slate-700">Task Completion Progress</span>
                  <span className="font-mono text-sky-700">{selectedOrder.completion_percentage}%</span>
                </div>
                <div className="w-full bg-slate-200 h-2.5 rounded-full overflow-hidden">
                  <div
                    className="bg-sky-600 h-full transition-all duration-300"
                    style={{ width: `${selectedOrder.completion_percentage}%` }}
                  />
                </div>
              </div>

              {/* Interactive checklist */}
              <div className="space-y-2 pt-2 border-t border-slate-200">
                <h4 className="text-xs font-bold uppercase tracking-wider text-slate-600">
                  Field Execution Checklist
                </h4>
                <div className="space-y-2">
                  {tasks.map((task) => (
                    <div
                      key={task.id}
                      onClick={() => handleToggleTask(task.id)}
                      className={`flex items-start space-x-2.5 p-2 rounded-md border cursor-pointer transition-colors ${
                        task.completed
                          ? 'bg-emerald-50/60 border-emerald-200 text-emerald-900'
                          : 'bg-white border-slate-200 text-slate-700 hover:bg-slate-50'
                      }`}
                    >
                      {task.completed ? (
                        <CheckSquare className="h-4 w-4 text-emerald-600 mt-0.5 shrink-0" />
                      ) : (
                        <Square className="h-4 w-4 text-slate-400 mt-0.5 shrink-0" />
                      )}
                      <span className={`text-xs font-medium ${task.completed ? 'line-through text-slate-500' : ''}`}>
                        {task.title}
                      </span>
                    </div>
                  ))}
                </div>
              </div>

              {/* Action buttons */}
              <div className="pt-3 border-t border-slate-200 flex items-center space-x-2">
                <Button size="sm" variant="outline" className="w-1/2">
                  <Camera className="h-3.5 w-3.5 mr-1" />
                  Attach Evidence
                </Button>
                <Button
                  size="sm"
                  variant="primary"
                  className="w-1/2 bg-emerald-700 hover:bg-emerald-800"
                  disabled={selectedOrder.completion_percentage < 100}
                >
                  <CheckCircle2 className="h-3.5 w-3.5 mr-1" />
                  Submit for Approval
                </Button>
              </div>
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
};
