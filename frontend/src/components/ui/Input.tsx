import React from 'react';

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
  helperText?: string;
}

export const Input: React.FC<InputProps> = ({
  label,
  error,
  helperText,
  id,
  className = '',
  ...props
}) => {
  const inputId = id || (label ? label.toLowerCase().replace(/\s+/g, '-') : undefined);

  return (
    <div className="w-full space-y-1">
      {label && (
        <label htmlFor={inputId} className="block text-xs font-semibold text-city-charcoal">
          {label} {props.required && <span className="text-city-danger">*</span>}
        </label>
      )}
      <input
        id={inputId}
        className={`w-full rounded-md border ${
          error ? 'border-city-danger focus:ring-city-danger' : 'border-surface-border focus:ring-city-terracotta'
        } bg-white px-3 py-2 text-sm text-city-charcoal placeholder:text-city-charcoal/40 focus:outline-none focus:ring-2 focus:border-transparent transition-colors disabled:bg-surface-muted disabled:cursor-not-allowed ${className}`}
        {...props}
      />
      {helperText && !error && <p className="text-xs text-city-charcoal/60">{helperText}</p>}
      {error && <p className="text-xs text-city-danger font-medium">{error}</p>}
    </div>
  );
};
