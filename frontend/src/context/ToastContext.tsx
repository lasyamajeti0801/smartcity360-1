import React, { createContext, useContext, useState, useCallback } from 'react';
import { CheckCircle2, AlertTriangle, AlertCircle, Info, X } from 'lucide-react';

export type ToastType = 'success' | 'warning' | 'error' | 'info';

export interface Toast {
  id: string;
  title: string;
  message?: string;
  type: ToastType;
  duration?: number;
}

interface ToastContextType {
  showToast: (toast: Omit<Toast, 'id'>) => void;
  addToast: (title: string, type?: ToastType, message?: string) => void;
  success: (title: string, message?: string) => void;
  error: (title: string, message?: string) => void;
  warning: (title: string, message?: string) => void;
  info: (title: string, message?: string) => void;
}

const ToastContext = createContext<ToastContextType | undefined>(undefined);

export const ToastProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [toasts, setToasts] = useState<Toast[]>([]);

  const removeToast = useCallback((id: string) => {
    setToasts((prev) => prev.filter((t) => t.id !== id));
  }, []);

  const showToast = useCallback(({ title, message, type, duration = 4000 }: Omit<Toast, 'id'>) => {
    const id = `toast_${Date.now()}_${Math.random().toString(36).substring(2, 6)}`;
    const newToast: Toast = { id, title, message, type, duration };
    setToasts((prev) => [newToast, ...prev.slice(0, 4)]);

    setTimeout(() => {
      removeToast(id);
    }, duration);
  }, [removeToast]);

  const addToast = useCallback((title: string, type: ToastType = 'info', message?: string) => {
    showToast({ title, message, type });
  }, [showToast]);

  const success = useCallback((title: string, message?: string) => {
    showToast({ title, message, type: 'success' });
  }, [showToast]);

  const error = useCallback((title: string, message?: string) => {
    showToast({ title, message, type: 'error' });
  }, [showToast]);

  const warning = useCallback((title: string, message?: string) => {
    showToast({ title, message, type: 'warning' });
  }, [showToast]);

  const info = useCallback((title: string, message?: string) => {
    showToast({ title, message, type: 'info' });
  }, [showToast]);

  return (
    <ToastContext.Provider value={{ showToast, addToast, success, error, warning, info }}>
      {children}
      {/* Toast Render Container */}
      <div
        className="fixed bottom-5 right-5 z-[9999] flex flex-col space-y-2.5 max-w-sm w-full pointer-events-none"
        aria-live="polite"
      >
        {toasts.map((toast) => {
          let bg = 'bg-purple-50 border-purple-300 text-purple-900';
          let Icon = Info;
          let iconColor = 'text-purple-600';

          if (toast.type === 'success') {
            bg = 'bg-emerald-50 border-emerald-300 text-emerald-900';
            Icon = CheckCircle2;
            iconColor = 'text-emerald-600';
          } else if (toast.type === 'warning') {
            bg = 'bg-amber-50 border-amber-300 text-amber-900';
            Icon = AlertTriangle;
            iconColor = 'text-amber-600';
          } else if (toast.type === 'error') {
            bg = 'bg-rose-50 border-rose-300 text-rose-900';
            Icon = AlertCircle;
            iconColor = 'text-rose-600';
          }

          return (
            <div
              key={toast.id}
              className={`pointer-events-auto flex items-start space-x-3 p-3.5 rounded-lg border shadow-civic-lg transition-all transform translate-y-0 opacity-100 ${bg}`}
              role="alert"
            >
              <Icon className={`w-5 h-5 shrink-0 mt-0.5 ${iconColor}`} />
              <div className="flex-1 min-w-0">
                <p className="text-xs font-semibold">{toast.title}</p>
                {toast.message && <p className="text-[11px] mt-0.5 text-city-charcoal/80 leading-snug">{toast.message}</p>}
              </div>
              <button
                onClick={() => removeToast(toast.id)}
                className="text-city-charcoal/60 hover:text-city-charcoal shrink-0 p-0.5 rounded transition-colors"
                aria-label="Dismiss toast"
              >
                <X className="w-3.5 h-3.5" />
              </button>
            </div>
          );
        })}
      </div>
    </ToastContext.Provider>
  );
};

export const useToast = (): ToastContextType => {
  const context = useContext(ToastContext);
  if (!context) {
    throw new Error('useToast must be used within a ToastProvider');
  }
  return context;
};
