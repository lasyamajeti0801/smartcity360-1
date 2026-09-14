import React from 'react';
import { Link } from 'react-router-dom';
import { ShieldAlert, Home } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';

export const UnauthorizedPage: React.FC = () => {
  const { user } = useAuth();

  const getDashboardPath = () => {
    if (!user) return '/login';
    switch (user.role) {
      case 'Admin':
        return '/admin/dashboard';
      case 'Staff':
        return '/staff/dashboard';
      case 'Citizen':
      default:
        return '/citizen/dashboard';
    }
  };

  return (
    <div className="min-h-screen bg-city-ivory flex items-center justify-center p-4">
      <div className="max-w-md w-full bg-white p-8 rounded-2xl border border-surface-border shadow-civic-lg text-center space-y-4">
        <div className="w-16 h-16 mx-auto rounded-full bg-city-danger/10 text-city-danger flex items-center justify-center">
          <ShieldAlert className="w-8 h-8" />
        </div>

        <div className="space-y-2">
          <h2 className="text-xl font-bold text-city-forest">
            Restricted Municipal Area
          </h2>
          <p className="text-xs text-city-charcoal/70 leading-relaxed">
            Your authenticated role ({user?.role || 'Guest'}) does not have security clearance to access this department console.
          </p>
        </div>

        <div className="pt-4 flex flex-col sm:flex-row items-center justify-center gap-3">
          <Link
            to={getDashboardPath()}
            className="w-full sm:w-auto px-4 py-2.5 rounded-lg bg-city-green hover:bg-city-forest text-white text-xs font-semibold shadow-sm transition-colors flex items-center justify-center space-x-1.5"
          >
            <Home className="w-4 h-4" />
            <span>Return to My Workspace</span>
          </Link>
          <Link
            to="/login"
            className="w-full sm:w-auto px-4 py-2.5 rounded-lg border border-surface-border text-xs text-city-charcoal hover:bg-city-sage/30 transition-colors"
          >
            Switch Role
          </Link>
        </div>
      </div>
    </div>
  );
};
