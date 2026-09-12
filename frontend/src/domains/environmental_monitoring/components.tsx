/**
 * SmartCity360 - Environmental Quality & Climate Resilience UI Dashboard Components
 * Domain: environmental_monitoring
 */

import React, { useState, useEffect } from 'react';

export const EnvironmentalMonitoringPanel01: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-01?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 01</h3>
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

export const EnvironmentalMonitoringPanel02: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-02?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 02</h3>
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

export const EnvironmentalMonitoringPanel03: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-03?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 03</h3>
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

export const EnvironmentalMonitoringPanel04: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-04?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 04</h3>
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

export const EnvironmentalMonitoringPanel05: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-05?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 05</h3>
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

export const EnvironmentalMonitoringPanel06: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-06?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 06</h3>
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

export const EnvironmentalMonitoringPanel07: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-07?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 07</h3>
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

export const EnvironmentalMonitoringPanel08: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-08?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 08</h3>
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

export const EnvironmentalMonitoringPanel09: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-09?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 09</h3>
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

export const EnvironmentalMonitoringPanel10: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-10?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 10</h3>
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

export const EnvironmentalMonitoringPanel11: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-11?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 11</h3>
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

export const EnvironmentalMonitoringPanel12: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-12?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 12</h3>
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

export const EnvironmentalMonitoringPanel13: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-13?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 13</h3>
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

export const EnvironmentalMonitoringPanel14: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-14?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 14</h3>
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

export const EnvironmentalMonitoringPanel15: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-15?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 15</h3>
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

export const EnvironmentalMonitoringPanel16: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-16?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 16</h3>
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

export const EnvironmentalMonitoringPanel17: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-17?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 17</h3>
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

export const EnvironmentalMonitoringPanel18: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-18?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 18</h3>
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

export const EnvironmentalMonitoringPanel19: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-19?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 19</h3>
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

export const EnvironmentalMonitoringPanel20: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-20?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 20</h3>
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

export const EnvironmentalMonitoringPanel21: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-21?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 21</h3>
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

export const EnvironmentalMonitoringPanel22: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-22?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 22</h3>
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

export const EnvironmentalMonitoringPanel23: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-23?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 23</h3>
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

export const EnvironmentalMonitoringPanel24: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-24?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 24</h3>
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

export const EnvironmentalMonitoringPanel25: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-25?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 25</h3>
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

export const EnvironmentalMonitoringPanel26: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-26?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 26</h3>
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

export const EnvironmentalMonitoringPanel27: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-27?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 27</h3>
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

export const EnvironmentalMonitoringPanel28: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-28?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 28</h3>
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

export const EnvironmentalMonitoringPanel29: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-29?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 29</h3>
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

export const EnvironmentalMonitoringPanel30: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-30?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 30</h3>
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

export const EnvironmentalMonitoringPanel31: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-31?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 31</h3>
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

export const EnvironmentalMonitoringPanel32: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-32?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 32</h3>
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

export const EnvironmentalMonitoringPanel33: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-33?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 33</h3>
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

export const EnvironmentalMonitoringPanel34: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-34?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 34</h3>
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

export const EnvironmentalMonitoringPanel35: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-35?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 35</h3>
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

export const EnvironmentalMonitoringPanel36: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-36?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 36</h3>
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

export const EnvironmentalMonitoringPanel37: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-37?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 37</h3>
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

export const EnvironmentalMonitoringPanel38: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-38?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 38</h3>
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

export const EnvironmentalMonitoringPanel39: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-39?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 39</h3>
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

export const EnvironmentalMonitoringPanel40: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-40?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 40</h3>
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

export const EnvironmentalMonitoringPanel41: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-41?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 41</h3>
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

export const EnvironmentalMonitoringPanel42: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-42?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 42</h3>
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

export const EnvironmentalMonitoringPanel43: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-43?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 43</h3>
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

export const EnvironmentalMonitoringPanel44: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-44?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 44</h3>
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

export const EnvironmentalMonitoringPanel45: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-45?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 45</h3>
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

export const EnvironmentalMonitoringPanel46: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-46?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 46</h3>
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

export const EnvironmentalMonitoringPanel47: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-47?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 47</h3>
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

export const EnvironmentalMonitoringPanel48: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-48?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 48</h3>
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

export const EnvironmentalMonitoringPanel49: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-49?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 49</h3>
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

export const EnvironmentalMonitoringPanel50: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-50?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 50</h3>
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

export const EnvironmentalMonitoringPanel51: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-51?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 51</h3>
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

export const EnvironmentalMonitoringPanel52: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-52?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 52</h3>
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

export const EnvironmentalMonitoringPanel53: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-53?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 53</h3>
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

export const EnvironmentalMonitoringPanel54: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-54?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 54</h3>
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

export const EnvironmentalMonitoringPanel55: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-55?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 55</h3>
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

export const EnvironmentalMonitoringPanel56: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-56?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 56</h3>
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

export const EnvironmentalMonitoringPanel57: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-57?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 57</h3>
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

export const EnvironmentalMonitoringPanel58: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-58?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 58</h3>
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

export const EnvironmentalMonitoringPanel59: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-59?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 59</h3>
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

export const EnvironmentalMonitoringPanel60: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/environmental-monitoring/endpoint-60?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading Environmental Quality & Climate Resilience operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Environmental Quality & Climate Resilience — Panel 60</h3>
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
