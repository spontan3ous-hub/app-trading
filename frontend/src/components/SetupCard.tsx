type SetupCardProps = {
  symbol: string;
  direction: "BUY" | "SELL";
  entry: number;
  stopLoss: number;
  takeProfit: number;
  riskPct: number;
  aiBias: string;
  aiConfidence: number;
  confluenceScore: number;
};

export default function SetupCard({
  symbol,
  direction,
  entry,
  stopLoss,
  takeProfit,
  riskPct,
  aiBias,
  aiConfidence,
  confluenceScore,
}: SetupCardProps) {
  return (
    <div className="rounded-2xl border border-slate-700 bg-slate-900 p-5 shadow-lg">
      <div className="flex items-center justify-between">
        <h2 className="text-xl font-semibold text-white">{symbol}</h2>
        <span className={`rounded-full px-2 py-1 text-xs font-bold ${direction === "BUY" ? "bg-emerald-500/20 text-emerald-300" : "bg-rose-500/20 text-rose-300"}`}>
          {direction}
        </span>
      </div>

      <div className="mt-4 grid grid-cols-2 gap-3 text-sm text-slate-300">
        <div>Entry: {entry}</div>
        <div>SL: {stopLoss}</div>
        <div>TP: {takeProfit}</div>
        <div>Risk: {riskPct}%</div>
      </div>

      <div className="mt-4 rounded-xl bg-slate-800 p-3">
        <div className="flex justify-between text-sm text-slate-300">
          <span>AI Bias</span>
          <span>{aiBias} ({aiConfidence}%)</span>
        </div>
        <div className="mt-2 flex justify-between text-sm text-slate-300">
          <span>Confluence</span>
          <span>{confluenceScore}/100</span>
        </div>
      </div>

      <div className="mt-5 flex gap-3">
        <button className="flex-1 rounded-xl bg-emerald-500 px-4 py-2 font-semibold text-white hover:bg-emerald-400">
          ✅ Execute
        </button>
        <button className="flex-1 rounded-xl bg-slate-700 px-4 py-2 font-semibold text-white hover:bg-slate-600">
          ❌ Skip
        </button>
        <button className="flex-1 rounded-xl bg-amber-500 px-4 py-2 font-semibold text-slate-950 hover:bg-amber-400">
          ✏️ Modify
        </button>
      </div>
    </div>
  );
}
