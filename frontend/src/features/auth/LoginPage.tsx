import React, { useState } from 'react';
import { useNavigate, useLocation, Link } from 'react-router-dom';
import {
  Building2,
  Lock,
  Mail,
  ArrowRight,
  ShieldCheck,
  User,
  HardHat,
  Activity,
  AlertCircle
} from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { useToast } from '../../context/ToastContext';
import { PrimaryRole } from '../../types';

export const LoginPage: React.FC = () => {
  const { login, loginAsDemo } = useAuth();
  const { success, error: toastError } = useToast();
  const navigate = useNavigate();
  const location = useLocation();

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(true);
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const from = (location.state as any)?.from?.pathname;

  const redirectUser = (role: PrimaryRole) => {
    if (from && from !== '/login') {
      navigate(from, { replace: true });
      return;
    }
    switch (role) {
      case 'Admin':
        navigate('/admin/dashboard', { replace: true });
        break;
      case 'Staff':
        navigate('/staff/dashboard', { replace: true });
        break;
      case 'Citizen':
      default:
        navigate('/citizen/dashboard', { replace: true });
        break;
    }
  };

  const handleFormSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setErrorMessage(null);

    if (!email.trim() || !password.trim()) {
      setErrorMessage('Please enter your municipal email or registered ID and password.');
      return;
    }

    setIsLoading(true);
    try {
      const res = await login(email, password);
      if (res.success && res.role) {
        success('Authentication Successful', `Welcome back to SmartCity360.`);
        redirectUser(res.role);
      } else {
        setErrorMessage(res.error || 'Invalid credentials. Please verify and try again.');
        toastError('Authentication Failed', res.error || 'Please check your login details.');
      }
    } finally {
      setIsLoading(false);
    }
  };

  const handleDemoLogin = (role: PrimaryRole) => {
    loginAsDemo(role);
    success(`Signed In as ${role}`, `Loaded demo session for ${role}.`);
    redirectUser(role);
  };

  return (
    <div className="min-h-screen bg-city-ivory flex flex-col justify-center select-none font-sans">
      <div className="max-w-6xl w-full mx-auto p-4 sm:p-6 lg:p-8">
        <div className="bg-white rounded-2xl border border-surface-border shadow-civic-lg overflow-hidden grid grid-cols-1 lg:grid-cols-12">
          {/* Left: City-Themed Visual Panel */}
          <div className="lg:col-span-5 bg-gradient-to-b from-[#1F0A38] via-[#38125E] to-[#18082B] p-8 sm:p-10 text-white flex flex-col justify-between relative overflow-hidden border-b lg:border-b-0 lg:border-r border-purple-900/40">
            {/* SVG Background Motif */}
            <div className="absolute inset-0 opacity-15 pointer-events-none">
              <svg className="w-full h-full" xmlns="http://www.w3.org/2000/svg">
                <defs>
                  <pattern id="grid-login" width="36" height="36" patternUnits="userSpaceOnUse">
                    <path d="M 36 0 L 0 0 0 36" fill="none" stroke="#C084FC" strokeWidth="0.75" />
                  </pattern>
                </defs>
                <rect width="100%" height="100%" fill="url(#grid-login)" />
              </svg>
            </div>

            {/* Top branding */}
            <div className="relative space-y-6">
              <Link to="/" className="inline-flex items-center space-x-2.5 group">
                <div className="w-10 h-10 rounded-lg bg-purple-600 border border-purple-400/40 flex items-center justify-center shadow-civic">
                  <Building2 className="w-5 h-5 text-purple-200" />
                </div>
                <div>
                  <span className="text-xl font-bold tracking-tight text-white">
                    SmartCity<span className="text-purple-300">360</span>
                  </span>
                  <p className="text-[10px] text-purple-200/70 uppercase tracking-widest font-mono">
                    MUNICIPAL GATEWAY
                  </p>
                </div>
              </Link>

              <div className="space-y-2 pt-4">
                <span className="text-[11px] font-mono uppercase px-2 py-0.5 rounded bg-purple-950/60 text-purple-200 border border-purple-400/30 font-semibold">
                  MUNICIPAL ACCESS PROTOCOL
                </span>
                <h2 className="text-2xl font-extrabold text-city-ivory leading-tight">
                  One City. <br />
                  One Connected Platform.
                </h2>
                <p className="text-xs text-city-concrete/90 leading-relaxed pt-1">
                  Connecting citizens, municipal departments, field technicians, and city leadership through verified, auditable workflows.
                </p>
              </div>
            </div>

            {/* Middle: Live telemetry indicators */}
            <div className="relative py-6 space-y-3">
              <div className="p-3 rounded-lg bg-black/20 border border-white/10 flex items-center justify-between text-xs">
                <span className="text-city-concrete/80">Active Municipal Wards</span>
                <span className="font-mono font-bold text-city-amber">198 Wards Live</span>
              </div>
              <div className="p-3 rounded-lg bg-black/20 border border-white/10 flex items-center justify-between text-xs">
                <span className="text-city-concrete/80">SAKALA Public SLA</span>
                <span className="font-mono font-bold text-city-sand">94.2% On-Time</span>
              </div>
            </div>

            {/* Bottom civic charter badge */}
            <div className="relative pt-4 border-t border-white/15 flex items-center space-x-2 text-[11px] text-city-concrete/80">
              <ShieldCheck className="w-4 h-4 text-city-amber shrink-0" />
              <span>Governed under Karnataka Municipal Corporations Act & e-Governance Standards.</span>
            </div>
          </div>

          {/* Right: Authentication Form & Demo Logins */}
          <div className="lg:col-span-7 p-8 sm:p-10 bg-white flex flex-col justify-between">
            <div>
              <div className="space-y-1">
                <h3 className="text-xl font-bold text-city-forest">Welcome back</h3>
                <p className="text-xs text-city-charcoal/70">
                  Enter your credentials to access your municipal workspace.
                </p>
              </div>

              {errorMessage && (
                <div className="mt-4 p-3.5 bg-red-50 border border-city-danger/30 rounded-lg flex items-start space-x-2.5 text-xs text-city-danger">
                  <AlertCircle className="w-4 h-4 shrink-0 mt-0.5" />
                  <p className="leading-snug">{errorMessage}</p>
                </div>
              )}

              {/* Login Form */}
              <form onSubmit={handleFormSubmit} className="mt-6 space-y-4">
                <div>
                  <label className="block text-xs font-semibold text-city-charcoal mb-1">
                    Email / Municipal Employee ID / Citizen ID
                  </label>
                  <div className="relative">
                    <Mail className="w-4 h-4 text-city-charcoal/40 absolute left-3 top-3" />
                    <input
                      type="text"
                      value={email}
                      onChange={(e) => setEmail(e.target.value)}
                      placeholder="e.g. citizen@smartcity360.local or CIT-10482"
                      className="w-full pl-9 pr-3 py-2.5 rounded-lg border border-surface-border text-xs text-city-charcoal placeholder-city-charcoal/40 focus:outline-none focus:ring-2 focus:ring-city-terracotta focus:border-transparent transition-all"
                      required
                    />
                  </div>
                </div>

                <div>
                  <div className="flex items-center justify-between mb-1">
                    <label className="block text-xs font-semibold text-city-charcoal">
                      Password
                    </label>
                    <button
                      type="button"
                      onClick={() => alert('For local demo, use the 1-click Quick Access buttons below or password: Password2026!')}
                      className="text-[11px] text-city-terracotta hover:underline font-medium"
                    >
                      Forgot password?
                    </button>
                  </div>
                  <div className="relative">
                    <Lock className="w-4 h-4 text-city-charcoal/40 absolute left-3 top-3" />
                    <input
                      type="password"
                      value={password}
                      onChange={(e) => setPassword(e.target.value)}
                      placeholder="••••••••••••"
                      className="w-full pl-9 pr-3 py-2.5 rounded-lg border border-surface-border text-xs text-city-charcoal placeholder-city-charcoal/40 focus:outline-none focus:ring-2 focus:ring-city-terracotta focus:border-transparent transition-all"
                      required
                    />
                  </div>
                </div>

                <div className="flex items-center justify-between text-xs text-city-charcoal/80 pt-1">
                  <label className="flex items-center space-x-2 cursor-pointer">
                    <input
                      type="checkbox"
                      checked={rememberMe}
                      onChange={(e) => setRememberMe(e.target.checked)}
                      className="rounded border-surface-border text-city-terracotta focus:ring-city-terracotta"
                    />
                    <span>Remember this session</span>
                  </label>
                </div>

                <button
                  type="submit"
                  disabled={isLoading}
                  className="w-full mt-2 py-2.5 rounded-lg bg-city-terracotta hover:bg-city-terracotta-dark text-white text-xs font-bold shadow-civic border border-city-amber/30 flex items-center justify-center space-x-2 transition-all disabled:opacity-50"
                >
                  {isLoading ? (
                    <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin" />
                  ) : (
                    <>
                      <span>Sign In to Workspace</span>
                      <ArrowRight className="w-3.5 h-3.5" />
                    </>
                  )}
                </button>
              </form>

              {/* Segregated Demo Quick Access Section */}
              <div className="mt-8 pt-6 border-t border-surface-border">
                <div className="flex items-center justify-between mb-3">
                  <p className="text-[11px] font-bold uppercase tracking-wider text-city-charcoal/70 font-mono">
                    Development & Demo Quick Access
                  </p>
                  <span className="text-[10px] bg-city-sand/40 text-city-forest font-bold px-2 py-0.5 rounded font-mono border border-city-sand">
                    1-Click Role Launch
                  </span>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
                  {/* Citizen Demo */}
                  <button
                    onClick={() => handleDemoLogin('Citizen')}
                    type="button"
                    className="p-3 rounded-lg border border-surface-border bg-city-ivory/50 hover:bg-city-sand/30 hover:border-city-terracotta text-left transition-all group shadow-sm"
                  >
                    <div className="flex items-center space-x-2">
                      <div className="p-1.5 rounded bg-city-terracotta text-white shadow-sm">
                        <User className="w-3.5 h-3.5" />
                      </div>
                      <span className="text-xs font-bold text-city-forest group-hover:text-city-terracotta">
                        Citizen
                      </span>
                    </div>
                    <p className="text-[11px] text-city-charcoal font-semibold mt-1.5">Priya Sharma</p>
                    <p className="text-[10px] text-city-charcoal/60">Ward 04, Greenfield</p>
                  </button>

                  {/* Staff Demo */}
                  <button
                    onClick={() => handleDemoLogin('Staff')}
                    type="button"
                    className="p-3 rounded-lg border border-surface-border bg-city-ivory/50 hover:bg-city-sand/30 hover:border-city-amber text-left transition-all group shadow-sm"
                  >
                    <div className="flex items-center space-x-2">
                      <div className="p-1.5 rounded bg-city-amber text-city-charcoal shadow-sm">
                        <HardHat className="w-3.5 h-3.5" />
                      </div>
                      <span className="text-xs font-bold text-city-forest group-hover:text-city-amber">
                        Field Staff
                      </span>
                    </div>
                    <p className="text-[11px] text-city-charcoal font-semibold mt-1.5">Arjun Kumar</p>
                    <p className="text-[10px] text-city-charcoal/60">Roads & Works Desk</p>
                  </button>

                  {/* Admin Demo */}
                  <button
                    onClick={() => handleDemoLogin('Admin')}
                    type="button"
                    className="p-3 rounded-lg border border-surface-border bg-city-ivory/50 hover:bg-city-sand/30 hover:border-city-forest text-left transition-all group shadow-sm"
                  >
                    <div className="flex items-center space-x-2">
                      <div className="p-1.5 rounded bg-city-forest text-city-sand shadow-sm">
                        <Activity className="w-3.5 h-3.5" />
                      </div>
                      <span className="text-xs font-bold text-city-forest">
                        City Admin
                      </span>
                    </div>
                    <p className="text-[11px] text-city-charcoal font-semibold mt-1.5">Ananya Rao</p>
                    <p className="text-[10px] text-city-charcoal/60">Operations Centre</p>
                  </button>
                </div>
              </div>
            </div>

            <div className="pt-6 text-center text-xs text-city-charcoal/60">
              <Link to="/" className="text-city-terracotta hover:underline font-medium">
                ← Return to Public Landing Page
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
