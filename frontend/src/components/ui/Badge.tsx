import React from 'react';

interface BadgeProps {
  status?: string;
  variant?: 'default' | 'success' | 'warning' | 'danger' | 'info' | 'neutral';
  children: React.ReactNode;
  className?: string;
}

export const Badge: React.FC<BadgeProps> = ({
  status,
  variant,
  children,
  className = '',
}) => {
  let computedVariant = variant || 'default';

  if (status) {
    const s = status.toUpperCase();
    if (['RESOLVED', 'COMPLETED', 'CLOSED', 'NORMAL', 'GOOD'].includes(s)) {
      computedVariant = 'success';
    } else if (['IN_PROGRESS', 'UNDER_REVIEW', 'ASSIGNED', 'MEDIUM', 'FAIR'].includes(s)) {
      computedVariant = 'warning';
    } else if (['CRITICAL', 'HIGH', 'REJECTED', 'POOR', 'FAILED'].includes(s)) {
      computedVariant = 'danger';
    } else if (['NEW', 'SUBMITTED', 'PENDING', 'ACTIVE'].includes(s)) {
      computedVariant = 'info';
    } else {
      computedVariant = 'neutral';
    }
  }

  const variantStyles = {
    default: 'bg-slate-100 text-slate-800 border-slate-200',
    neutral: 'bg-slate-100 text-slate-700 border-slate-300',
    info: 'bg-sky-50 text-sky-800 border-sky-300',
    warning: 'bg-amber-50 text-amber-900 border-amber-300',
    success: 'bg-emerald-50 text-emerald-900 border-emerald-300',
    danger: 'bg-red-50 text-red-900 border-red-300',
  };

  return (
    <span
      className={`inline-flex items-center px-2 py-0.5 rounded text-xs font-semibold border ${variantStyles[computedVariant]} ${className}`}
    >
      {children}
    </span>
  );
};
