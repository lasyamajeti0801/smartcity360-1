import React, { useState } from 'react';
import {
  CheckCircle2,
  Download,
  Receipt,
  ShieldCheck,
  ArrowRight,
  X
} from 'lucide-react';
import { Badge } from '../../components/ui/Badge';
import { useToast } from '../../context/ToastContext';

interface CivicBill {
  id: string;
  billNumber: string;
  serviceName: string;
  department: string;
  amount: number;
  dueDate: string;
  status: 'UNPAID' | 'PAID';
  period: string;
}

export const CitizenPaymentsPage: React.FC = () => {
  const { success } = useToast();

  const [bills, setBills] = useState<CivicBill[]>([
    {
      id: 'b1',
      billNumber: 'MUNC-2026-WTR-8821',
      serviceName: 'Quarterly Domestic Water Meter Assessment',
      department: 'Water Supply Board',
      amount: 450.0,
      dueDate: '2026-09-25',
      status: 'UNPAID',
      period: 'Q3 2026',
    },
    {
      id: 'b2',
      billNumber: 'MUNC-2026-TAX-0419',
      serviceName: 'Municipal Property Tax (Residential Ward 4)',
      department: 'Revenue & Finance',
      amount: 3200.0,
      dueDate: '2026-10-31',
      status: 'UNPAID',
      period: 'Annual 2026-27',
    },
    {
      id: 'b3',
      billNumber: 'MUNC-2026-PER-1102',
      serviceName: 'Utility Trenching & Road Digging Permit',
      department: 'Roads & Infrastructure',
      amount: 1500.0,
      dueDate: '2026-08-15',
      status: 'PAID',
      period: 'FY 2026',
    },
  ]);

  const [selectedBill, setSelectedBill] = useState<CivicBill | null>(null);
  const [isCheckoutOpen, setIsCheckoutOpen] = useState(false);
  const [paymentMethod, setPaymentMethod] = useState<'UPI' | 'CARD' | 'NET_BANKING'>('UPI');
  const [upiId, setUpiId] = useState('priya@okhdfcbank');
  const [isProcessing, setIsProcessing] = useState(false);
  const [receiptBill, setReceiptBill] = useState<CivicBill | null>(null);

  const handlePayClick = (bill: CivicBill) => {
    setSelectedBill(bill);
    setIsCheckoutOpen(true);
  };

  const handleProcessPayment = (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedBill) return;

    setIsProcessing(true);
    setTimeout(() => {
      setBills((prev) =>
        prev.map((b) => (b.id === selectedBill.id ? { ...b, status: 'PAID' } : b))
      );
      setIsProcessing(false);
      setIsCheckoutOpen(false);
      setReceiptBill(selectedBill);
      success('Payment Verified', `Receipt generated for ₹${selectedBill.amount}. Thank you!`);
    }, 1200);
  };

  return (
    <div className="space-y-6 select-none font-sans">
      {/* Header */}
      <div className="bg-white p-5 rounded-xl border border-surface-border shadow-civic flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-city-forest">Civic Payments & Municipal Receipts</h1>
          <p className="text-xs text-city-charcoal/70 mt-0.5">
            Transparent fee assessment, digital receipt repository, and secure municipal payments.
          </p>
        </div>

        <div className="flex items-center space-x-2 text-xs text-city-forest font-semibold bg-city-sage/40 px-3 py-1.5 rounded-lg border border-city-leaf/30">
          <ShieldCheck className="w-4 h-4 text-city-leaf" />
          <span>Zero External Gateway Surcharge</span>
        </div>
      </div>

      {/* Bill Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {bills.map((bill) => (
          <div
            key={bill.id}
            className="bg-white p-5 rounded-xl border border-surface-border shadow-civic flex flex-col justify-between space-y-4"
          >
            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <span className="font-mono text-xs font-bold text-city-charcoal/60">
                  {bill.billNumber}
                </span>
                <Badge status={bill.status === 'PAID' ? 'RESOLVED' : 'HIGH'}>
                  {bill.status}
                </Badge>
              </div>

              <h3 className="text-sm font-bold text-city-forest leading-snug">
                {bill.serviceName}
              </h3>
              <p className="text-xs text-city-charcoal/60">{bill.department} • {bill.period}</p>
            </div>

            <div className="pt-3 border-t border-surface-border flex items-center justify-between">
              <div>
                <span className="text-[10px] text-city-charcoal/60 block">Assessed Amount</span>
                <span className="text-lg font-extrabold font-mono text-city-forest">
                  ₹{bill.amount.toLocaleString('en-IN')}
                </span>
              </div>

              {bill.status === 'UNPAID' ? (
                <button
                  onClick={() => handlePayClick(bill)}
                  className="px-4 py-2 rounded-lg bg-city-terracotta hover:bg-city-terracotta-dark text-white text-xs font-bold shadow-civic transition-colors"
                >
                  Pay Now
                </button>
              ) : (
                <button
                  onClick={() => setReceiptBill(bill)}
                  className="px-3 py-2 rounded-lg border border-surface-border text-city-forest hover:bg-surface-muted text-xs font-semibold flex items-center space-x-1.5 transition-colors"
                >
                  <Receipt className="w-3.5 h-3.5 text-city-leaf" />
                  <span>Receipt</span>
                </button>
              )}
            </div>
          </div>
        ))}
      </div>

      {/* Payment Checkout Modal */}
      {isCheckoutOpen && selectedBill && (
        <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl border border-surface-border shadow-civic-lg max-w-md w-full p-6 space-y-5">
            <div className="flex items-center justify-between pb-3 border-b border-surface-border">
              <div>
                <span className="text-[10px] font-mono font-bold text-city-charcoal/60 uppercase">
                  MUNICIPAL CHECKOUT
                </span>
                <h3 className="text-base font-bold text-city-forest mt-0.5">
                  Confirm Fee Payment
                </h3>
              </div>
              <button
                onClick={() => setIsCheckoutOpen(false)}
                className="p-1.5 rounded-lg hover:bg-surface-muted text-city-charcoal/60"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            <div className="p-3 bg-surface-card rounded-xl border border-surface-border space-y-1 text-xs">
              <p className="font-semibold text-city-forest">{selectedBill.serviceName}</p>
              <div className="flex items-center justify-between pt-2 border-t border-surface-border text-sm">
                <span className="text-city-charcoal/70">Total Payable:</span>
                <span className="font-mono font-extrabold text-city-forest text-base">
                  ₹{selectedBill.amount.toLocaleString('en-IN')}
                </span>
              </div>
            </div>

            <form onSubmit={handleProcessPayment} className="space-y-4">
              <div className="space-y-2">
                <label className="block text-xs font-semibold text-city-charcoal">
                  Select Payment Method
                </label>
                <div className="grid grid-cols-3 gap-2">
                  {(['UPI', 'CARD', 'NET_BANKING'] as const).map((m) => (
                    <button
                      key={m}
                      type="button"
                      onClick={() => setPaymentMethod(m)}
                      className={`py-2 text-xs font-semibold rounded-lg border transition-all ${
                        paymentMethod === m
                          ? 'bg-city-terracotta text-white border-city-terracotta shadow-sm'
                          : 'bg-white border-surface-border text-city-charcoal hover:bg-surface-muted'
                      }`}
                    >
                      {m === 'UPI' ? 'UPI / QR' : m === 'CARD' ? 'Debit/Credit' : 'Net Banking'}
                    </button>
                  ))}
                </div>
              </div>

              {paymentMethod === 'UPI' && (
                <div>
                  <label className="block text-xs font-semibold text-city-charcoal mb-1">
                    Virtual Payment Address (VPA) / UPI ID
                  </label>
                  <input
                    type="text"
                    value={upiId}
                    onChange={(e) => setUpiId(e.target.value)}
                    className="w-full px-3 py-2 rounded-lg border border-surface-border text-xs text-city-charcoal focus:outline-none focus:ring-1 focus:ring-city-terracotta"
                    required
                  />
                </div>
              )}

              <button
                type="submit"
                disabled={isProcessing}
                className="w-full py-2.5 rounded-lg bg-city-terracotta hover:bg-city-terracotta-dark text-white text-xs font-bold shadow-civic border border-city-amber/30 transition-all flex items-center justify-center space-x-2 disabled:opacity-50"
              >
                {isProcessing ? (
                  <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin" />
                ) : (
                  <>
                    <span>Confirm Payment of ₹{selectedBill.amount}</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </>
                )}
              </button>
            </form>
          </div>
        </div>
      )}

      {/* Digital Receipt Modal */}
      {receiptBill && (
        <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl border border-surface-border shadow-civic-lg max-w-md w-full p-6 space-y-4">
            <div className="flex items-center justify-between pb-3 border-b border-surface-border">
              <div className="flex items-center space-x-2">
                <CheckCircle2 className="w-5 h-5 text-city-success" />
                <h3 className="text-base font-bold text-city-forest">Official Payment Receipt</h3>
              </div>
              <button
                onClick={() => setReceiptBill(null)}
                className="p-1 rounded-lg hover:bg-surface-muted"
              >
                <X className="w-4 h-4 text-city-charcoal/60" />
              </button>
            </div>

            <div className="bg-city-ivory p-4 rounded-xl border border-surface-border space-y-3 text-xs">
              <div className="text-center pb-2 border-b border-surface-border">
                <p className="font-bold text-city-forest">SMARTCITY360 MUNICIPAL CORPORATION</p>
                <p className="text-[10px] text-city-charcoal/60">Digital Financial Transaction Record</p>
              </div>

              <div className="space-y-1.5">
                <div className="flex justify-between">
                  <span className="text-city-charcoal/60">Receipt Number:</span>
                  <span className="font-mono font-bold text-city-forest">REC-2026-{(Math.random() * 90000 + 10000).toFixed(0)}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-city-charcoal/60">Service:</span>
                  <span className="font-semibold text-city-charcoal">{receiptBill.serviceName}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-city-charcoal/60">Amount Paid:</span>
                  <span className="font-mono font-bold text-city-success">₹{receiptBill.amount.toLocaleString('en-IN')}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-city-charcoal/60">Status:</span>
                  <span className="font-bold text-city-success">CLEARED & VERIFIED</span>
                </div>
              </div>
            </div>

            <div className="flex gap-2">
              <button
                onClick={() => {
                  success('Receipt Downloaded', 'Official receipt PDF downloaded to your device.');
                  setReceiptBill(null);
                }}
                className="flex-1 py-2.5 rounded-lg bg-city-terracotta hover:bg-city-terracotta-dark text-white text-xs font-bold shadow-civic flex items-center justify-center space-x-2 transition-colors"
              >
                <Download className="w-3.5 h-3.5" />
                <span>Download Official PDF</span>
              </button>
              <button
                onClick={() => setReceiptBill(null)}
                className="px-4 py-2.5 rounded-lg border border-surface-border text-xs font-semibold text-city-charcoal hover:bg-surface-muted transition-colors"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
