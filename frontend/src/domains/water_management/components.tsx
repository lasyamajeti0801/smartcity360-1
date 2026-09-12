/**
 * SmartCity360 - Municipal Water Supply & Quality UI Dashboard Components
 * Domain: water_management
 */

import React, { useState, useEffect } from 'react';

export const WaterManagementPanel01: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-01?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 01</h3>
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

export const WaterManagementPanel02: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-02?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 02</h3>
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

export const WaterManagementPanel03: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-03?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 03</h3>
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

export const WaterManagementPanel04: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-04?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 04</h3>
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

export const WaterManagementPanel05: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-05?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 05</h3>
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

export const WaterManagementPanel06: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-06?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 06</h3>
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

export const WaterManagementPanel07: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-07?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 07</h3>
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

export const WaterManagementPanel08: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-08?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 08</h3>
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

export const WaterManagementPanel09: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-09?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 09</h3>
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

export const WaterManagementPanel10: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-10?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 10</h3>
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

export const WaterManagementPanel11: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-11?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 11</h3>
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

export const WaterManagementPanel12: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-12?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 12</h3>
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

export const WaterManagementPanel13: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-13?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 13</h3>
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

export const WaterManagementPanel14: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-14?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 14</h3>
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

export const WaterManagementPanel15: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-15?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 15</h3>
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

export const WaterManagementPanel16: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-16?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 16</h3>
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

export const WaterManagementPanel17: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-17?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 17</h3>
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

export const WaterManagementPanel18: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-18?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 18</h3>
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

export const WaterManagementPanel19: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-19?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 19</h3>
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

export const WaterManagementPanel20: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-20?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 20</h3>
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

export const WaterManagementPanel21: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-21?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 21</h3>
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

export const WaterManagementPanel22: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-22?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 22</h3>
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

export const WaterManagementPanel23: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-23?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 23</h3>
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

export const WaterManagementPanel24: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-24?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 24</h3>
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

export const WaterManagementPanel25: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-25?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 25</h3>
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

export const WaterManagementPanel26: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-26?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 26</h3>
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

export const WaterManagementPanel27: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-27?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 27</h3>
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

export const WaterManagementPanel28: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-28?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 28</h3>
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

export const WaterManagementPanel29: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-29?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 29</h3>
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

export const WaterManagementPanel30: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-30?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 30</h3>
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

export const WaterManagementPanel31: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-31?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 31</h3>
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

export const WaterManagementPanel32: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-32?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 32</h3>
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

export const WaterManagementPanel33: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-33?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 33</h3>
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

export const WaterManagementPanel34: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-34?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 34</h3>
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

export const WaterManagementPanel35: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-35?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 35</h3>
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

export const WaterManagementPanel36: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-36?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 36</h3>
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

export const WaterManagementPanel37: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-37?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 37</h3>
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

export const WaterManagementPanel38: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-38?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 38</h3>
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

export const WaterManagementPanel39: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-39?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 39</h3>
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

export const WaterManagementPanel40: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-40?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 40</h3>
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

export const WaterManagementPanel41: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-41?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 41</h3>
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

export const WaterManagementPanel42: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-42?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 42</h3>
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

export const WaterManagementPanel43: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-43?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 43</h3>
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

export const WaterManagementPanel44: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-44?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 44</h3>
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

export const WaterManagementPanel45: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-45?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 45</h3>
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

export const WaterManagementPanel46: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-46?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 46</h3>
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

export const WaterManagementPanel47: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-47?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 47</h3>
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

export const WaterManagementPanel48: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-48?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 48</h3>
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

export const WaterManagementPanel49: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-49?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 49</h3>
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

export const WaterManagementPanel50: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-50?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 50</h3>
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

export const WaterManagementPanel51: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-51?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 51</h3>
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

export const WaterManagementPanel52: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-52?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 52</h3>
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

export const WaterManagementPanel53: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-53?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 53</h3>
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

export const WaterManagementPanel54: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-54?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 54</h3>
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

export const WaterManagementPanel55: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-55?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 55</h3>
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

export const WaterManagementPanel56: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-56?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 56</h3>
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

export const WaterManagementPanel57: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-57?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 57</h3>
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

export const WaterManagementPanel58: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-58?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 58</h3>
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

export const WaterManagementPanel59: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-59?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 59</h3>
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

export const WaterManagementPanel60: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/water-management/endpoint-60?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Municipal Water Supply & Quality — Panel 60</h3>
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
