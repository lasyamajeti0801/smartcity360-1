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
    default: 'bg-purple-50 text-purple-900 border-purple-200',
    neutral: 'bg-purple-50/50 text-purple-800 border-purple-100',
    info: 'bg-purple-100 text-purple-800 border-purple-200',
    warning: 'bg-amber-50 text-amber-800 border-amber-200',
    success: 'bg-emerald-50 text-emerald-800 border-emerald-200',
    danger: 'bg-rose-50 text-rose-800 border-rose-200',
  };

  return (
    <span
      className={`inline-flex items-center px-2 py-0.5 rounded text-xs font-semibold border ${variantStyles[computedVariant]} ${className}`}
    >
      {children}
    </span>
  );
};
