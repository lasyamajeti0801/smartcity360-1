import React, { useState } from 'react';
import { Modal } from '../../components/ui/Modal';
import { Input } from '../../components/ui/Input';
import { Select } from '../../components/ui/Select';
import { Button } from '../../components/ui/Button';
import { CityMap } from '../../components/maps/CityMap';
import { ComplaintCategory, Complaint } from '../../types';
import { MapPin, CheckCircle } from 'lucide-react';

interface ReportIssueModalProps {
  isOpen: boolean;
  onClose: () => void;
  categories: ComplaintCategory[];
  onSubmit: (complaint: Partial<Complaint>) => Promise<void>;
}

export const ReportIssueModal: React.FC<ReportIssueModalProps> = ({
  isOpen,
  onClose,
  categories,
  onSubmit,
}) => {
  const [categoryId, setCategoryId] = useState(categories[0]?.id || '');
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [address, setAddress] = useState('');
  const [ward, setWard] = useState<number>(4);
  const [coords, setCoords] = useState<{ lat: number; lng: number }>({ lat: 12.9716, lng: 77.5946 });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim() || !description.trim() || !address.trim()) {
      setError('Please provide title, address, and issue description.');
      return;
    }

    setIsSubmitting(true);
    setError(null);

    try {
      await onSubmit({
        category_id: categoryId || categories[0]?.id,
        title,
        description,
        location_address: address,
        ward_number: Number(ward),
        latitude: coords.lat,
        longitude: coords.lng,
      });
      // Reset
      setTitle('');
      setDescription('');
      setAddress('');
      onClose();
    } catch (err: any) {
      setError(err?.message || 'Failed to submit report. Please try again.');
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleMapPin = (lat: number, lng: number, addressSuggestion?: string) => {
    setCoords({ lat, lng });
    if (addressSuggestion && !address) {
      setAddress(addressSuggestion);
    }
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title="Report a Civic Issue or Infrastructure Defect"
      subtitle="Your complaint is logged directly into the municipal department dispatch system with SLA tracking."
      maxWidth="xl"
    >
      <form onSubmit={handleSubmit} className="space-y-4">
        {error && (
          <div className="p-3 bg-red-50 border border-red-200 rounded-md text-xs text-red-700 font-medium">
            {error}
          </div>
        )}

        {/* Category & Ward */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <Select
            label="Issue Category"
            value={categoryId}
            onChange={(e) => setCategoryId(e.target.value)}
            options={categories.map((c) => ({ value: c.id, label: `${c.name} (${c.default_sla_hours}h SLA)` }))}
            required
          />

          <Select
            label="Municipal Ward"
            value={ward}
            onChange={(e) => setWard(Number(e.target.value))}
            options={[
              { value: 1, label: 'Ward 1 - Northern Tech Corridor' },
              { value: 2, label: 'Ward 2 - Hospital & University District' },
              { value: 3, label: 'Ward 3 - Historic West Suburb' },
              { value: 4, label: 'Ward 4 - Central Urban Metro' },
              { value: 5, label: 'Ward 5 - Industrial Logistics Hub' },
              { value: 6, label: 'Ward 6 - Eastern Lake Basin' },
              { value: 7, label: 'Ward 7 - South Residential Sector' },
            ]}
            required
          />
        </div>

        {/* Title */}
        <Input
          label="Subject / Headline"
          placeholder="e.g. Deep pothole on left lane near subway station"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />

        {/* Description */}
        <div className="space-y-1">
          <label className="block text-xs font-semibold text-slate-700">
            Detailed Description <span className="text-red-600">*</span>
          </label>
          <textarea
            rows={3}
            className="w-full rounded-md border border-slate-300 bg-white px-3 py-2 text-sm text-slate-900 placeholder:text-slate-400 focus:outline-none focus:ring-2 focus:ring-slate-900 focus:border-transparent transition-colors"
            placeholder="Describe the severity, exact landmark, and any immediate public hazard..."
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />
        </div>

        {/* Location Address */}
        <Input
          label="Street Address / Nearest Landmark"
          placeholder="e.g. 45 Park Avenue, opposite City General Hospital"
          value={address}
          onChange={(e) => setAddress(e.target.value)}
          required
        />

        {/* Interactive GPS Pin Picker */}
        <div className="space-y-1">
          <div className="flex items-center justify-between">
            <label className="block text-xs font-semibold text-slate-700 flex items-center space-x-1">
              <MapPin className="h-3.5 w-3.5 text-sky-600" />
              <span>Pinpoint Geographic Location on Map</span>
            </label>
            <span className="text-[11px] font-mono text-slate-500">
              GPS: {coords.lat.toFixed(4)}, {coords.lng.toFixed(4)}
            </span>
          </div>
          <div className="h-44 w-full rounded-md overflow-hidden border border-slate-300">
            <CityMap
              center={[coords.lat, coords.lng]}
              zoom={14}
              interactiveSelectMode={true}
              onLocationSelect={handleMapPin}
            />
          </div>
        </div>

        {/* Action Buttons */}
        <div className="pt-2 flex items-center justify-end space-x-3 border-t border-slate-200">
          <Button type="button" variant="outline" onClick={onClose} disabled={isSubmitting}>
            Cancel
          </Button>
          <Button type="submit" variant="primary" isLoading={isSubmitting} className="bg-sky-600 hover:bg-sky-500">
            <CheckCircle className="h-4 w-4 mr-1.5" />
            Submit Verified Report
          </Button>
        </div>
      </form>
    </Modal>
  );
};
