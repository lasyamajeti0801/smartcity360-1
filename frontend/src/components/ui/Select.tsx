import React from 'react';

interface Option {
  value: string | number;
  label: string;
}

interface SelectProps extends React.SelectHTMLAttributes<HTMLSelectElement> {
  label?: string;
  options: Option[];
  error?: string;
  helperText?: string;
}

export const Select: React.FC<SelectProps> = ({
  label,
  options,
  error,
  helperText,
  id,
  className = '',
  ...props
}) => {
  const selectId = id || (label ? label.toLowerCase().replace(/\s+/g, '-') : undefined);

  return (
    <div className="w-full space-y-1">
      {label && (
        <label htmlFor={selectId} className="block text-xs font-semibold text-city-charcoal">
          {label} {props.required && <span className="text-city-danger">*</span>}
        </label>
      )}
      <select
        id={selectId}
        className={`w-full rounded-md border ${
          error ? 'border-city-danger focus:ring-city-danger' : 'border-surface-border focus:ring-city-terracotta'
        } bg-white px-3 py-2 text-sm text-city-charcoal focus:outline-none focus:ring-2 focus:border-transparent transition-colors disabled:bg-surface-muted disabled:cursor-not-allowed ${className}`}
        {...props}
      >
        {options.map((opt) => (
          <option key={opt.value} value={opt.value}>
            {opt.label}
          </option>
        ))}
      </select>
      {helperText && !error && <p className="text-xs text-city-charcoal/60">{helperText}</p>}
      {error && <p className="text-xs text-city-danger font-medium">{error}</p>}
    </div>
  );
};
