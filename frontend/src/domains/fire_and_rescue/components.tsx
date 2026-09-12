/**
 * SmartCity360 - Fire Protection & Hazardous Materials UI Dashboard Components
 * Domain: fire_and_rescue
 */

import React, { useState, useEffect } from 'react';

export const FireAndRescuePanel01: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-01?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 01</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel02: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-02?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 02</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel03: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-03?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 03</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel04: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-04?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 04</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel05: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-05?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 05</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel06: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-06?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 06</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel07: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-07?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 07</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel08: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-08?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 08</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel09: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-09?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 09</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel10: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-10?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 10</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel11: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-11?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 11</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel12: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-12?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 12</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel13: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-13?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 13</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel14: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-14?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 14</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel15: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-15?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 15</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel16: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-16?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 16</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel17: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-17?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 17</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel18: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-18?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 18</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel19: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-19?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 19</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel20: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-20?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 20</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel21: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-21?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 21</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel22: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-22?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 22</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel23: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-23?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 23</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel24: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-24?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 24</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel25: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-25?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 25</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel26: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-26?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 26</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel27: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-27?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 27</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel28: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-28?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 28</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel29: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-29?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 29</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel30: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-30?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 30</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel31: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-31?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 31</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel32: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-32?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 32</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel33: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-33?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 33</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel34: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-34?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 34</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel35: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-35?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 35</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel36: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-36?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 36</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel37: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-37?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 37</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel38: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-38?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 38</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel39: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-39?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 39</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel40: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-40?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 40</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel41: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-41?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 41</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel42: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-42?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 42</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel43: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-43?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 43</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel44: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-44?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 44</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel45: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-45?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 45</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel46: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-46?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 46</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel47: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-47?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 47</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel48: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-48?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 48</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel49: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-49?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 49</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel50: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-50?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 50</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel51: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-51?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 51</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel52: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-52?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 52</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel53: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-53?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 53</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel54: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-54?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 54</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel55: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-55?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 55</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel56: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-56?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 56</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel57: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-57?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 57</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel58: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-58?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 58</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel59: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-59?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 59</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};

export const FireAndRescuePanel60: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/fire-and-rescue/endpoint-60?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Fire Protection & Hazardous Materials — Panel 60</h3>
      <p className='mt-1 text-xs text-slate-500'>Jurisdictional Ward: {wardId} | System Status: Active</p>
      <div className='mt-4 grid grid-cols-2 gap-4'>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Records Evaluated</span>
          <div className='text-lg font-bold text-slate-900'>{data?.records_evaluated ?? 0}</div>
        </div>
        <div className='rounded border border-slate-100 bg-slate-50 p-3'>
          <span className='text-xs text-slate-500'>Compliance Rate</span>
          <div className='text-lg font-bold text-emerald-600'>{data?.compliance_rate_pct ?? 100}%</div>
        </div>
      </div>
    </div>
  );
};
