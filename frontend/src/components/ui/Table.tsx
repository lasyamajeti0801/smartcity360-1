import React from 'react';

export interface Column<T> {
  key: string;
  header: string;
  render?: (row: T) => React.ReactNode;
  align?: 'left' | 'center' | 'right';
  className?: string;
}

interface TableProps<T> {
  columns: Column<T>[];
  data: T[];
  keyExtractor: (row: T) => string | number;
  isLoading?: boolean;
  emptyMessage?: string;
  onRowClick?: (row: T) => void;
}

export function Table<T>({
  columns,
  data,
  keyExtractor,
  isLoading = false,
  emptyMessage = 'No municipal records found.',
  onRowClick,
}: TableProps<T>) {
  if (isLoading) {
    return (
      <div className="w-full py-12 flex flex-col items-center justify-center text-city-charcoal/60 bg-white rounded-xl border border-surface-border">
        <div className="w-6 h-6 border-2 border-city-terracotta border-t-transparent rounded-full animate-spin mb-2" />
        <span className="text-xs font-medium">Retrieving verified city records...</span>
      </div>
    );
  }

  if (data.length === 0) {
    return (
      <div className="w-full py-12 flex flex-col items-center justify-center text-city-charcoal/60 bg-white rounded-xl border border-surface-border">
        <p className="text-sm font-semibold text-city-forest">{emptyMessage}</p>
        <p className="text-xs text-city-charcoal/50 mt-1">Adjust search terms or filters to display data.</p>
      </div>
    );
  }

  return (
    <div className="w-full overflow-x-auto rounded-xl border border-surface-border bg-white shadow-civic">
      <table className="min-w-full divide-y divide-surface-border text-left text-sm">
        <thead className="bg-surface-card text-xs uppercase font-semibold text-city-charcoal/70 tracking-wider font-mono">
          <tr>
            {columns.map((col) => (
              <th
                key={col.key}
                scope="col"
                className={`px-4 py-3 ${
                  col.align === 'right' ? 'text-right' : col.align === 'center' ? 'text-center' : 'text-left'
                } ${col.className || ''}`}
              >
                {col.header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="divide-y divide-surface-border bg-white">
          {data.map((row) => (
            <tr
              key={keyExtractor(row)}
              onClick={() => onRowClick && onRowClick(row)}
              className={`transition-colors hover:bg-surface-card ${onRowClick ? 'cursor-pointer' : ''}`}
            >
              {columns.map((col) => (
                <td
                  key={col.key}
                  className={`px-4 py-3 text-city-charcoal whitespace-nowrap ${
                    col.align === 'right' ? 'text-right' : col.align === 'center' ? 'text-center' : 'text-left'
                  } ${col.className || ''}`}
                >
                  {col.render ? col.render(row) : (row as any)[col.key]}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
