import React from 'react';

interface CardProps {
  children: React.ReactNode;
  className?: string;
  title?: string;
  subtitle?: string;
  action?: React.ReactNode;
}

export const Card: React.FC<CardProps> = ({
  children,
  className = '',
  title,
  subtitle,
  action,
}) => {
  return (
    <div className={`bg-white rounded-xl border border-surface-border shadow-civic overflow-hidden ${className}`}>
      {(title || action) && (
        <div className="px-4 py-3 border-b border-surface-border flex items-center justify-between bg-surface-card">
          <div>
            {title && <h3 className="text-sm font-bold text-city-forest tracking-tight">{title}</h3>}
            {subtitle && <p className="text-xs text-city-charcoal/60 mt-0.5">{subtitle}</p>}
          </div>
          {action && <div>{action}</div>}
        </div>
      )}
      <div className="p-4">{children}</div>
    </div>
  );
};
