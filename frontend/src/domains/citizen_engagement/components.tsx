/**
 * SmartCity360 - Citizen Participation & Open Democracy UI Dashboard Components
 * Domain: citizen_engagement
 */

import React, { useState, useEffect } from 'react';

export const CitizenEngagementPanel01: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-01?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 01</h3>
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

export const CitizenEngagementPanel02: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-02?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 02</h3>
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

export const CitizenEngagementPanel03: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-03?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 03</h3>
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

export const CitizenEngagementPanel04: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-04?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 04</h3>
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

export const CitizenEngagementPanel05: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-05?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 05</h3>
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

export const CitizenEngagementPanel06: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-06?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 06</h3>
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

export const CitizenEngagementPanel07: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-07?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 07</h3>
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

export const CitizenEngagementPanel08: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-08?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 08</h3>
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

export const CitizenEngagementPanel09: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-09?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 09</h3>
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

export const CitizenEngagementPanel10: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-10?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 10</h3>
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

export const CitizenEngagementPanel11: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-11?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 11</h3>
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

export const CitizenEngagementPanel12: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-12?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 12</h3>
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

export const CitizenEngagementPanel13: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-13?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 13</h3>
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

export const CitizenEngagementPanel14: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-14?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 14</h3>
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

export const CitizenEngagementPanel15: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-15?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 15</h3>
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

export const CitizenEngagementPanel16: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-16?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 16</h3>
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

export const CitizenEngagementPanel17: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-17?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 17</h3>
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

export const CitizenEngagementPanel18: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-18?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 18</h3>
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

export const CitizenEngagementPanel19: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-19?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 19</h3>
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

export const CitizenEngagementPanel20: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-20?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 20</h3>
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

export const CitizenEngagementPanel21: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-21?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 21</h3>
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

export const CitizenEngagementPanel22: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-22?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 22</h3>
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

export const CitizenEngagementPanel23: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-23?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 23</h3>
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

export const CitizenEngagementPanel24: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-24?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 24</h3>
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

export const CitizenEngagementPanel25: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-25?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 25</h3>
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

export const CitizenEngagementPanel26: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-26?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 26</h3>
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

export const CitizenEngagementPanel27: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-27?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 27</h3>
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

export const CitizenEngagementPanel28: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-28?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 28</h3>
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

export const CitizenEngagementPanel29: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-29?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 29</h3>
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

export const CitizenEngagementPanel30: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-30?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 30</h3>
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

export const CitizenEngagementPanel31: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-31?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 31</h3>
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

export const CitizenEngagementPanel32: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-32?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 32</h3>
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

export const CitizenEngagementPanel33: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-33?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 33</h3>
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

export const CitizenEngagementPanel34: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-34?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 34</h3>
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

export const CitizenEngagementPanel35: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-35?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 35</h3>
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

export const CitizenEngagementPanel36: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-36?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 36</h3>
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

export const CitizenEngagementPanel37: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-37?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 37</h3>
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

export const CitizenEngagementPanel38: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-38?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 38</h3>
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

export const CitizenEngagementPanel39: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-39?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 39</h3>
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

export const CitizenEngagementPanel40: React.FC<{ wardId?: number }> = ({ wardId = 1 }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/v1/citizen-engagement/endpoint-40?ward_id=${wardId}&limit=10`)
      .then(res => res.json())
      .then(json => { setData(json); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [wardId]);

  if (loading) return <div className='p-4 text-sm text-slate-500'>Loading {title} operational telemetry...</div>;
  if (error) return <div className='p-4 text-sm text-rose-600 font-medium'>Operational Telemetry Error: {error}</div>;

  return (
    <div className='rounded-lg border border-slate-200 bg-white p-6 shadow-sm'>
      <h3 className='text-base font-semibold text-slate-900'>Citizen Participation & Open Democracy — Panel 40</h3>
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
