import SetupCard from "./components/SetupCard";

function StatCard({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-xl border border-slate-700 bg-slate-900 p-4">
      <div className="text-sm text-slate-400">{label}</div>
      <div className="mt-2 text-2xl font-semibold text-white">{value}</div>
    </div>
  );
}

export default function App() {
  return (
    <div className="min-h-screen bg-slate-950 p-6 text-white">
      <header className="mb-6 flex items-center justify-between">
        <h1 className="text-3xl font-bold">Trading Assistant</h1>
        <div className="rounded-full border border-amber-500/40 bg-amber-500/10 px-3 py-1 text-xs text-amber-300">
          Paper Trading
        </div>
      </header>

      <div className="mb-6 grid grid-cols-1 gap-4 md:grid-cols-4">
        <StatCard label="Balance" value="$25,000" />
        <StatCard label="Equity" value="$25,480" />
        <StatCard label="Daily P/L" value="+$420" />
        <StatCard label="Risk Used" value="0.8%" />
      </div>

      <SetupCard
        symbol="EURUSD"
        direction="BUY"
        entry={1.0872}
        stopLoss={1.0838}
        takeProfit={1.0938}
        riskPct={1.0}
        aiBias="bullish"
        aiConfidence={82}
        confluenceScore={88}
      />
    </div>
  );
}
