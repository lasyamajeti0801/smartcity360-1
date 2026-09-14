import React, { useState } from 'react';
import { Button } from '../../components/ui/Button';
import { useToast } from '../../context/ToastContext';
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
  const { addToast } = useToast();
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
      targetAudience: 'Ward 3, 5, 8',
    },
    {
      id: 'n3',
      category: 'PUBLIC_WORKS',
      title: 'Smart LED Streetlighting Phase 3 Infield Commissioning',
      message: 'Retrofitting of 450 sodium-vapor poles with automated dusk-to-dawn LED luminaires completed along Outer Ring Road Corridor.',
      timestamp: '5 hours ago',
      isRead: true,
      priority: 'LOW',
      targetAudience: 'Public Notice',
    },
    {
      id: 'n4',
      category: 'EMERGENCY',
      title: 'Hazardous Chemical Containment Drill - Industrial Area Ward 12',
      message: 'Civil defence mock response drill scheduled for tomorrow at 11:00 AM. Emergency sirens may sound intermittently.',
      timestamp: '1 day ago',
      isRead: true,
      priority: 'HIGH',
      targetAudience: 'Ward 12 Industrial Zone',
    },
  ]);

  const markAllRead = () => {
    setNotifications((prev) => prev.map((n) => ({ ...n, isRead: true })));
    addToast('All municipal alerts marked as read', 'info');
  };

  const filtered = notifications.filter((n) => {
    if (filter === 'ALL') return true;
    return n.category === filter;
  });

  return (
    <div className="space-y-6">
      {/* Header Banner */}
      <div className="bg-gradient-to-r from-city-forest to-city-charcoal text-white rounded-xl p-5 border border-city-forest/40 shadow-md flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <Megaphone className="h-5 w-5 text-city-amber" />
            <h1 className="text-lg font-bold tracking-tight text-white">
              Municipal Public Alerts & Notifications Command
            </h1>
          </div>
          <p className="text-xs text-city-ivory/80 mt-1">
            Official emergency public warnings, scheduled utility outage alerts, and civic broadcast feeds.
          </p>
        </div>

        <div className="flex items-center space-x-2">
          <Button
            size="sm"
            variant="outline"
            onClick={markAllRead}
            className="bg-white/10 hover:bg-white/20 text-city-ivory border-white/20 text-xs"
          >
            Mark All as Read
          </Button>
          <Button
            size="sm"
            variant="primary"
            onClick={() => addToast('Advisory authoring composer queued for authorization', 'info')}
            className="bg-city-terracotta hover:bg-city-terracotta/90 text-white font-semibold text-xs border-0"
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
                ? 'bg-city-terracotta text-white border-city-terracotta shadow-sm'
                : 'bg-surface-card text-city-charcoal/80 border-surface-border hover:bg-city-sand/30'
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
                ? 'bg-surface-card border-city-terracotta/50 shadow-sm ring-1 ring-city-terracotta/20'
                : 'bg-surface-card/60 border-surface-border text-city-charcoal/70'
            }`}
          >
            <div className="flex items-start justify-between gap-4">
              <div className="flex items-start space-x-3">
                <div
                  className={`h-9 w-9 rounded-lg flex items-center justify-center shrink-0 mt-0.5 ${
                    item.category === 'EMERGENCY'
                      ? 'bg-red-100 text-red-700'
                      : item.category === 'UTILITY'
                      ? 'bg-purple-100 text-purple-800'
                      : 'bg-purple-50 text-purple-950'
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
                          ? 'bg-purple-50 text-purple-800 border border-purple-200'
                          : 'bg-purple-100/60 text-purple-950 border border-purple-200'
                      }`}
                    >
                      {item.category}
                    </span>
                    <span className="text-[11px] text-city-charcoal/50 font-mono">• {item.timestamp}</span>
                    <span className="text-[10px] bg-city-sand/40 text-city-charcoal/70 px-1.5 py-0.5 rounded font-medium border border-surface-border">
                      Audience: {item.targetAudience}
                    </span>
                  </div>

                  <h3 className="text-sm font-bold text-city-charcoal mt-1">{item.title}</h3>
                  <p className="text-xs text-city-charcoal/70 mt-1 leading-relaxed">{item.message}</p>
                </div>
              </div>

              {!item.isRead && (
                <span className="h-2.5 w-2.5 rounded-full bg-city-terracotta shrink-0 mt-2" title="Unread"></span>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
