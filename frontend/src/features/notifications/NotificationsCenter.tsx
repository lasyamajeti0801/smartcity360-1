import React, { useState } from 'react';
import { Button } from '../../components/ui/Button';
import {
  AlertTriangle,
  Info,
  Radio,
  PlusCircle,
  Megaphone
} from 'lucide-react';

interface NotificationItem {
  id: string;
  category: 'EMERGENCY' | 'UTILITY' | 'PUBLIC_WORKS' | 'GOVERNANCE';
  title: string;
  message: string;
  timestamp: string;
  isRead: boolean;
  priority: 'HIGH' | 'MEDIUM' | 'LOW';
  targetAudience: string;
}

export const NotificationsCenter: React.FC = () => {
  const [filter, setFilter] = useState<'ALL' | 'EMERGENCY' | 'UTILITY' | 'PUBLIC_WORKS'>('ALL');
  const [notifications, setNotifications] = useState<NotificationItem[]>([
    {
      id: 'n1',
      category: 'EMERGENCY',
      title: 'Monsoon Heavy Precipitation & Waterlogging Warning',
      message: 'Meteorological department predicts heavy squalls (40-60 mm/hr). Emergency pumping squads deployed at low-lying underpasses in Ward 4 and Ward 7.',
      timestamp: '15 minutes ago',
      isRead: false,
      priority: 'HIGH',
      targetAudience: 'City-Wide Broadcast',
    },
    {
      id: 'n2',
      category: 'UTILITY',
      title: 'Scheduled Trunk Pipeline Maintenance - 100ft Road',
      message: 'Water supply will be regulated between 10:00 PM and 4:00 AM on Sunday for valve calibration. Citizens are requested to store adequate water.',
      timestamp: '2 hours ago',
      isRead: false,
      priority: 'MEDIUM',
      targetAudience: 'Ward 4 (Indiranagar)',
    },
    {
      id: 'n3',
      category: 'PUBLIC_WORKS',
      title: 'Smart LED Streetlighting Upgrade Complete',
      message: 'Conversion of 850 sodium vapor streetlights to IoT energy-saving smart dimmable LEDs completed along Airport Expressway.',
      timestamp: '1 day ago',
      isRead: true,
      priority: 'LOW',
      targetAudience: 'North Sector Residents',
    },
    {
      id: 'n4',
      category: 'GOVERNANCE',
      title: 'Municipal Property Tax Rebate Window Extended',
      message: 'Early-bird 5% rebate on annual civic property tax payments extended through the end of the current quarter.',
      timestamp: '2 days ago',
      isRead: true,
      priority: 'LOW',
      targetAudience: 'All Property Taxpayers',
    },
  ]);

  const markAllRead = () => {
    setNotifications((prev) => prev.map((n) => ({ ...n, isRead: true })));
  };

  const filtered = notifications.filter((n) => {
    if (filter === 'ALL') return true;
    return n.category === filter;
  });

  return (
    <div className="space-y-6">
      {/* Header Banner */}
      <div className="bg-slate-900 text-white rounded-xl p-5 border border-slate-800 shadow-md flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <Megaphone className="h-5 w-5 text-teal-400" />
            <h1 className="text-lg font-bold tracking-tight text-white">
              Municipal Public Alerts & Notifications Command
            </h1>
          </div>
          <p className="text-xs text-slate-300 mt-1">
            Official emergency public warnings, scheduled utility outage alerts, and civic broadcast feeds.
          </p>
        </div>

        <div className="flex items-center space-x-2">
          <Button
            size="sm"
            variant="outline"
            onClick={markAllRead}
            className="bg-slate-800 hover:bg-slate-700 text-slate-200 border-slate-700 text-xs"
          >
            Mark All as Read
          </Button>
          <Button
            size="sm"
            variant="primary"
            onClick={() => alert('Broadcast advisory authoring modal opened')}
            className="bg-teal-600 hover:bg-teal-500 text-xs"
          >
            <PlusCircle className="h-3.5 w-3.5 mr-1" />
            Publish New Broadcast
          </Button>
        </div>
      </div>

      {/* Filter Tabs */}
      <div className="flex flex-wrap gap-2">
        {(['ALL', 'EMERGENCY', 'UTILITY', 'PUBLIC_WORKS'] as const).map((cat) => (
          <button
            key={cat}
            onClick={() => setFilter(cat)}
            className={`px-3 py-1 rounded-full text-xs font-semibold border transition-all ${
              filter === cat
                ? 'bg-slate-900 text-white border-slate-900 shadow-sm'
                : 'bg-white text-slate-600 border-slate-300 hover:bg-slate-50'
            }`}
          >
            {cat}
          </button>
        ))}
      </div>

      {/* Notifications List */}
      <div className="space-y-3">
        {filtered.map((item) => (
          <div
            key={item.id}
            className={`p-4 rounded-xl border transition-all ${
              !item.isRead
                ? 'bg-white border-teal-500/40 shadow-sm ring-1 ring-teal-500/20'
                : 'bg-slate-50/70 border-slate-200 text-slate-600'
            }`}
          >
            <div className="flex items-start justify-between gap-4">
              <div className="flex items-start space-x-3">
                <div
                  className={`h-9 w-9 rounded-lg flex items-center justify-center shrink-0 mt-0.5 ${
                    item.category === 'EMERGENCY'
                      ? 'bg-red-100 text-red-700'
                      : item.category === 'UTILITY'
                      ? 'bg-sky-100 text-sky-700'
                      : 'bg-teal-100 text-teal-700'
                  }`}
                >
                  {item.category === 'EMERGENCY' ? (
                    <AlertTriangle className="h-5 w-5" />
                  ) : item.category === 'UTILITY' ? (
                    <Radio className="h-5 w-5" />
                  ) : (
                    <Info className="h-5 w-5" />
                  )}
                </div>

                <div>
                  <div className="flex items-center space-x-2">
                    <span
                      className={`text-[10px] font-bold px-2 py-0.5 rounded uppercase font-mono ${
                        item.category === 'EMERGENCY'
                          ? 'bg-red-50 text-red-800 border border-red-200'
                          : item.category === 'UTILITY'
                          ? 'bg-sky-50 text-sky-800 border border-sky-200'
                          : 'bg-slate-100 text-slate-800 border border-slate-200'
                      }`}
                    >
                      {item.category}
                    </span>
                    <span className="text-[11px] text-slate-400 font-mono">• {item.timestamp}</span>
                    <span className="text-[10px] bg-slate-100 text-slate-600 px-1.5 py-0.5 rounded font-medium">
                      Audience: {item.targetAudience}
                    </span>
                  </div>

                  <h3 className="text-sm font-bold text-slate-900 mt-1">{item.title}</h3>
                  <p className="text-xs text-slate-600 mt-1 leading-relaxed">{item.message}</p>
                </div>
              </div>

              {!item.isRead && (
                <span className="h-2.5 w-2.5 rounded-full bg-teal-600 shrink-0 mt-2" title="Unread"></span>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
