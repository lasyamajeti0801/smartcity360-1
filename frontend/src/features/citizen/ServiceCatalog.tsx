import React, { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';
import { Badge } from '../../components/ui/Badge';
import { Search, Clock, ArrowRight } from 'lucide-react';

interface ServiceItem {
  id: string;
  department: string;
  category: string;
  title: string;
  description: string;
  eligibility: string;
  fee: number;
  slaDays: number;
  online: boolean;
}

const CATALOG_DATA: ServiceItem[] = [
  {
    id: 's1',
    department: 'Water Supply & Sewerage',
    category: 'Utilities',
    title: 'New Domestic Drinking Water Connection',
    description: 'Application for laying and connecting fresh water municipal pipeline to residential property.',
    eligibility: 'Property ownership deed or verified registered lease deed with municipal clearance.',
    fee: 150.0,
    slaDays: 10,
    online: true,
  },
  {
    id: 's2',
    department: 'Roads & Infrastructure',
    category: 'Permits',
    title: 'Utility Road Trenching & Cutting Permission',
    description: 'Statutory approval for underground telecom conduit or plumbing pipe excavation across city roads.',
    eligibility: 'Licensed contractor registration certificate and traffic mitigation bond.',
    fee: 500.0,
    slaDays: 7,
    online: true,
  },
  {
    id: 's3',
    department: 'Sanitation & Waste',
    category: 'Sanitation',
    title: 'Bulk Electronic & Hazardous Waste Disposal',
    description: 'Scheduled door-to-door municipal collection for bulky appliances, furniture, and e-waste.',
    eligibility: 'All verified municipal residential taxpayers within city limits.',
    fee: 25.0,
    slaDays: 3,
    online: true,
  },
  {
    id: 's4',
    department: 'Urban Planning & Housing',
    category: 'Building',
    title: 'Residential Building Completion Certificate',
    description: 'Official municipal engineering inspection and occupancy certificate for newly erected dwellings.',
    eligibility: 'Approved architectural floor plan and structural safety certificate.',
    fee: 200.0,
    slaDays: 14,
    online: true,
  },
];

export const ServiceCatalog: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<string>('ALL');

  const filtered = CATALOG_DATA.filter((s) => {
    const matchesSearch =
      s.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      s.description.toLowerCase().includes(searchTerm.toLowerCase()) ||
      s.department.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesCat = selectedCategory === 'ALL' || s.category === selectedCategory;
    return matchesSearch && matchesCat;
  });

  return (
    <div className="space-y-6 select-none font-sans">
      <div className="bg-white p-5 rounded-xl border border-surface-border shadow-civic flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-city-forest tracking-tight">Municipal Civic Service Directory</h1>
          <p className="text-xs text-city-charcoal/70 mt-0.5">
            Discover verified city services, check eligibility requirements, statutory fees, and SLA timelines.
          </p>
        </div>
        <div className="relative w-full md:w-72">
          <Search className="absolute left-3 top-2.5 h-4 w-4 text-city-charcoal/40" />
          <input
            type="text"
            placeholder="Search service title or keywords..."
            className="w-full bg-white border border-surface-border rounded-lg pl-9 pr-3 py-2 text-xs text-city-charcoal placeholder-city-charcoal/40 focus:outline-none focus:ring-1 focus:ring-city-terracotta"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>
      </div>

      {/* Category Pills */}
      <div className="flex flex-wrap gap-2">
        {['ALL', 'Utilities', 'Permits', 'Sanitation', 'Building'].map((cat) => (
          <button
            key={cat}
            onClick={() => setSelectedCategory(cat)}
            className={`px-3 py-1.5 rounded-full text-xs font-semibold border transition-all ${
              selectedCategory === cat
                ? 'bg-city-terracotta text-white border-city-terracotta shadow-civic'
                : 'bg-white text-city-charcoal border-surface-border hover:bg-city-sand/30'
            }`}
          >
            {cat}
          </button>
        ))}
      </div>

      {/* Grid of Services */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {filtered.map((service) => (
          <Card key={service.id} className="flex flex-col justify-between hover:border-city-terracotta transition-all shadow-civic">
            <div>
              <div className="flex items-center justify-between gap-2 mb-2">
                <span className="text-[11px] font-mono font-bold text-city-forest bg-city-sand/40 px-2 py-0.5 rounded border border-city-sand">
                  {service.department}
                </span>
                <Badge variant="neutral">{service.category}</Badge>
              </div>
              <h3 className="text-sm font-bold text-city-forest">{service.title}</h3>
              <p className="text-xs text-city-charcoal/80 mt-1.5 leading-relaxed">{service.description}</p>

              <div className="mt-4 pt-3 border-t border-surface-border space-y-1.5 text-xs text-city-charcoal/80">
                <div>
                  <span className="font-semibold text-city-forest">Eligibility: </span>
                  {service.eligibility}
                </div>
              </div>
            </div>

            <div className="mt-5 pt-3 border-t border-surface-border flex items-center justify-between">
              <div className="flex items-center space-x-3 text-xs">
                <div className="flex items-center text-city-charcoal/70">
                  <Clock className="h-3.5 w-3.5 mr-1 text-city-amber" />
                  <span>{service.slaDays} Days Turnaround</span>
                </div>
                <span className="font-mono font-bold text-city-forest">Fee: ₹{(service.fee * 80).toFixed(0)}</span>
              </div>
              <Button size="sm" variant="primary">
                Apply Online
                <ArrowRight className="h-3.5 w-3.5 ml-1" />
              </Button>
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
};
