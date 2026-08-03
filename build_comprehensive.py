
import json

# Load the data
with open('/app/data/所有对话/主对话/健康/健康看板/accounting_data.json', 'r') as f:
    data = json.load(f)

transactions_json = json.dumps(data['transactions'], ensure_ascii=False)
income_json = json.dumps(data['income'], ensure_ascii=False)
cat_totals_json = json.dumps(data['cat_totals'], ensure_ascii=False)

html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<meta name="theme-color" content="#0f1115">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<title>综合工作台</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}}
html{{font-size:16px;-webkit-text-size-adjust:100%}}
body{{font-family:-apple-system,'SF Pro Text','PingFang SC','Helvetica Neue',sans-serif;background:#0f1115;color:#e0e0e0;line-height:1.5;overflow-x:hidden;-webkit-font-smoothing:antialiased}}
:root{{--bg:#0f1115;--card:#1a1d24;--inset:#12141a;--t1:#e8e8e8;--t2:#8a8a8a;--t3:#555;--blue:#4a9eff;--green:#34c759;--orange:#ff9500;--red:#ff3b30;--purple:#af52de;--teal:#5ac8fa;--yellow:#ffcc00;--pink:#ff2d55;--bdr:rgba(255,255,255,0.06);--bdr2:rgba(255,255,255,0.15);--r:14px;--rs:10px}}
.container{{max-width:480px;margin:0 auto;padding:0 16px 80px}}
.header{{position:sticky;top:0;z-index:100;background:rgba(15,17,21,0.92);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid var(--bdr);padding:12px 16px;display:flex;align-items:center;justify-content:space-between}}
.header-left{{display:flex;align-items:center;gap:10px}}
.avatar{{width:36px;height:36px;border-radius:10px;background:linear-gradient(135deg,var(--blue),var(--purple));display:flex;align-items:center;justify-content:center;font-weight:700;font-size:15px;color:#fff}}
.header-title{{font-size:15px;font-weight:600;color:var(--t1)}}
.header-sub{{font-size:11px;color:var(--t2);margin-top:1px}}
.header-date{{font-size:11px;color:var(--t3);text-align:right}}
.main-tabs{{position:sticky;top:56px;z-index:99;background:rgba(15,17,21,0.92);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);display:flex;gap:0;padding:10px 16px 0;overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:none;border-bottom:1px solid var(--bdr)}}
.main-tabs::-webkit-scrollbar{{display:none}}
.main-tab{{flex-shrink:0;padding:10px 24px;border-radius:12px 12px 0 0;font-size:14px;font-weight:600;color:var(--t2);background:transparent;border:1px solid transparent;border-bottom:none;cursor:pointer;transition:all 0.2s}}
.main-tab.active{{color:var(--t1);background:var(--card);border-color:var(--bdr2)}}
.main-panel{{display:none}}
.main-panel.active{{display:block}}
.sub-tabs{{display:flex;gap:6px;padding:12px 0;overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:none}}
.sub-tabs::-webkit-scrollbar{{display:none}}
.sub-tab{{flex-shrink:0;padding:6px 14px;border-radius:20px;font-size:12px;font-weight:500;color:var(--t2);background:transparent;border:1px solid transparent;transition:all 0.2s;white-space:nowrap;cursor:pointer}}
.sub-tab.active{{color:var(--t1);background:var(--card);border-color:var(--bdr2)}}
.sub-panel{{display:none}}
.sub-panel.active{{display:block;animation:fadeUp 0.3s ease}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(10px)}}to{{opacity:1;transform:translateY(0)}}}}
.card{{background:var(--card);border-radius:var(--r);padding:18px;margin-bottom:12px;border:1px solid var(--bdr)}}
.card-title{{font-size:14px;font-weight:600;color:var(--t1);margin-bottom:14px;display:flex;align-items:center;gap:6px}}
.big-num{{font-size:36px;font-weight:800;color:var(--t1);line-height:1.1}}
.big-num .unit{{font-size:14px;font-weight:400;color:var(--t2)}}
.big-sub{{font-size:12px;color:var(--t2);margin-top:4px}}
.kpi-grid{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px}}
.kpi-item{{background:var(--inset);border-radius:var(--rs);padding:16px 12px;text-align:center}}
.kpi-value{{font-size:22px;font-weight:700}}
.kpi-value.income{{color:var(--green)}}
.kpi-value.expense{{color:var(--red)}}
.kpi-value.balance{{color:var(--blue)}}
.kpi-label{{font-size:11px;color:var(--t2);margin-top:4px}}
.cat-grid{{display:grid;grid-template-columns:1fr 1fr;gap:10px}}
.cat-item{{background:var(--inset);border-radius:var(--rs);padding:14px;position:relative;overflow:hidden}}
.cat-item::before{{content:'';position:absolute;top:0;left:0;width:4px;height:100%;border-radius:4px 0 0 4px}}
.cat-icon{{font-size:16px;margin-bottom:4px}}
.cat-name{{font-size:12px;color:var(--t2);margin-bottom:2px}}
.cat-amount{{font-size:18px;font-weight:700;color:var(--t1)}}
.cat-pct{{font-size:11px;color:var(--t3);margin-top:2px}}
.tx-list{{display:flex;flex-direction:column;gap:0}}
.tx-item{{display:flex;align-items:center;padding:12px 0;border-bottom:1px solid var(--bdr)}}
.tx-item:last-child{{border-bottom:none}}
.tx-left{{flex:1;min-width:0}}
.tx-name{{font-size:13px;color:var(--t1);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.tx-meta{{font-size:11px;color:var(--t3);margin-top:2px}}
.tx-amount{{font-size:15px;font-weight:600;white-space:nowrap;margin-left:12px}}
.tx-amount.income{{color:var(--green)}}
.tx-amount.expense{{color:var(--t2)}}
.tx-emoji{{width:32px;height:32px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:16px;background:var(--inset);margin-right:10px;flex-shrink:0}}
.section-title{{font-size:13px;font-weight:600;color:var(--blue);margin:16px 0 10px;padding-left:2px}}
.empty-state{{text-align:center;padding:40px 20px;color:var(--t3);font-size:13px}}
.empty-state .icon{{font-size:40px;margin-bottom:12px;opacity:0.5}}
.date-filter{{display:flex;gap:8px;align-items:center;margin-bottom:14px}}
.date-filter input{{background:var(--inset);color:var(--t1);border:1px solid var(--bdr);border-radius:8px;padding:8px 10px;font-size:13px;outline:none;flex:1}}
.date-filter span{{color:var(--t3);font-size:12px;flex-shrink:0}}
.date-filter select{{background:var(--inset);color:var(--t1);border:1px solid var(--bdr);border-radius:8px;padding:8px 10px;font-size:13px;outline:none}}
.day-summary{{background:var(--inset);border-radius:var(--rs);padding:14px;margin-bottom:12px}}
.day-summary .row{{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}}
.day-summary .row:last-child{{margin-bottom:0}}
.day-summary .label{{font-size:12px;color:var(--t2)}}
.day-summary .val{{font-size:16px;font-weight:700}}
.day-summary .val.inc{{color:var(--green)}}
.day-summary .val.exp{{color:var(--red)}}
.month-compare{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px}}
.month-card{{background:var(--inset);border-radius:var(--rs);padding:16px;text-align:center}}
.month-card .month-name{{font-size:12px;color:var(--t2);margin-bottom:8px}}
.month-card .month-exp{{font-size:20px;font-weight:700;color:var(--red);margin-bottom:4px}}
.month-card .month-inc{{font-size:14px;font-weight:600;color:var(--green)}}
.month-card .month-bal{{font-size:12px;color:var(--t3);margin-top:4px}}
.income-section{{background:var(--inset);border-radius:var(--rs);padding:14px;margin-top:12px}}
.income-row{{display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:1px solid var(--bdr)}}
.income-row:last-child{{border-bottom:none}}
.income-row .name{{font-size:13px;color:var(--t2)}}
.income-row .amt{{font-size:14px;font-weight:600;color:var(--green)}}
.income-total{{display:flex;justify-content:space-between;align-items:center;padding-top:10px;margin-top:6px;border-top:1px solid var(--bdr2)}}
.income-total .name{{font-size:14px;font-weight:600;color:var(--t1)}}
.income-total .amt{{font-size:18px;font-weight:700;color:var(--green)}}
.progress-bar{{height:6px;background:var(--inset);border-radius:3px;overflow:hidden;margin-top:6px}}
.progress-fill{{height:100%;border-radius:3px;transition:width 0.6s ease}}
.pz-placeholder{{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:60px 20px;color:var(--t3);text-align:center}}
.pz-placeholder .icon{{font-size:60px;margin-bottom:16px;opacity:0.3}}
.pz-placeholder .title{{font-size:16px;color:var(--t2);margin-bottom:8px}}
.pz-placeholder .desc{{font-size:12px}}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <div class="header-left">
      <div class="avatar">综</div>
      <div>
        <div class="header-title">综合工作台</div>
        <div class="header-sub">排盘 · 记账</div>
      </div>
    </div>
    <div class="header-date" id="headerDate"></div>
  </div>

  <div class="main-tabs">
    <div class="main-tab" data-main="paipan" onclick="switchMain('paipan')">排盘</div>
    <div class="main-tab active" data-main="jizhang" onclick="switchMain('jizhang')">记账</div>
  </div>

  <!-- 排盘 Panel -->
  <div class="main-panel" id="panel-paipan">
    <div class="pz-placeholder">
      <div class="icon">🔮</div>
      <div class="title">排盘功能</div>
      <div class="desc">由独立模块提供，正在建设中</div>
    </div>
  </div>

  <!-- 记账 Panel -->
  <div class="main-panel active" id="panel-jizhang">
    <div class="sub-tabs">
      <div class="sub-tab active" data-sub="overview" onclick="switchSub('overview')">总览</div>
      <div class="sub-tab" data-sub="today" onclick="switchSub('today')">当日</div>
      <div class="sub-tab" data-sub="week" onclick="switchSub('week')">当周</div>
      <div class="sub-tab" data-sub="month" onclick="switchSub('month')">当月</div>
      <div class="sub-tab" data-sub="detail" onclick="switchSub('detail')">明细</div>
    </div>

    <!-- 总览 -->
    <div class="sub-panel active" id="sub-overview"></div>

    <!-- 当日 -->
    <div class="sub-panel" id="sub-today"></div>

    <!-- 当周 -->
    <div class="sub-panel" id="sub-week"></div>

    <!-- 当月 -->
    <div class="sub-panel" id="sub-month"></div>

    <!-- 明细 -->
    <div class="sub-panel" id="sub-detail"></div>
  </div>
</div>

<script>
// ========== DATA ==========
const transactions = {transactions_json};
const incomeRecords = {income_json};
const catTotals = {cat_totals_json};
const totalIncome = {data['total_income']};
const totalExpense = {data['total_expense']};
const balance = {data['balance']};
const startDate = '2026-06-01';

const catConfig = {{
  '固定支出': {{emoji:'🏠',color:'#ff6b6b'}},
  '餐饮': {{emoji:'🍜',color:'#ffa502'}},
  '补剂': {{emoji:'💊',color:'#2ed573'}},
  '训练': {{emoji:'🏋️',color:'#1e90ff'}},
  '个人护理': {{emoji:'🧴',color:'#ff6b81'}},
  '交通': {{emoji:'🚗',color:'#747d8c'}},
  '娱乐': {{emoji:'🎮',color:'#a55eea'}},
  '医疗': {{emoji:'💊',color:'#ff4757'}},
  '穿戴': {{emoji:'👟',color:'#ff7f50'}},
  '个人生活': {{emoji:'🚬',color:'#57606f'}},
  '数码产品': {{emoji:'📱',color:'#3742fa'}}
}};

const allCatOrder = ['固定支出','餐饮','补剂','训练','个人护理','交通','娱乐','医疗','穿戴','个人生活','数码产品'];

// ========== HELPERS ==========
function fmt(n) {{ return n.toLocaleString('zh-CN', {{minimumFractionDigits:2, maximumFractionDigits:2}}); }}

function formatDate(d) {{
  const parts = d.split('-');
  return parseInt(parts[1]) + '/' + parseInt(parts[2]);
}}

function isToday(dateStr) {{
  const now = new Date();
  const y = now.getFullYear(), m = String(now.getMonth()+1).padStart(2,'0'), d = String(now.getDate()).padStart(2,'0');
  return dateStr === `${{y}}-${{m}}-${{d}}`;
}}

function getWeekRange() {{
  const now = new Date();
  const day = now.getDay() || 7;
  const mon = new Date(now);
  mon.setDate(now.getDate() - day + 1);
  const sun = new Date(mon);
  sun.setDate(mon.getDate() + 6);
  const f = d => d.toISOString().slice(0,10);
  return [f(mon), f(sun)];
}}

function getMonthRange() {{
  const now = new Date();
  const y = now.getFullYear(), m = String(now.getMonth()+1).padStart(2,'0');
  const start = `${{y}}-${{m}}-01`;
  const lastDay = new Date(y, parseInt(m), 0).getDate();
  const end = `${{y}}-${{m}}-${{String(lastDay).padStart(2,'0')}}`;
  return [start, end];
}}

function filterByDate(items, start, end) {{
  return items.filter(t => t.date >= start && t.date <= end);
}}

function calcExpense(list) {{ return list.reduce((s,t) => s + t.amount, 0); }}
function calcIncome(list) {{ return list.reduce((s,t) => s + t.amount, 0); }}

function groupByCategory(list) {{
  const g = {{}};
  list.forEach(t => {{ g[t.category] = (g[t.category]||0) + t.amount; }});
  return g;
}}

function daysSinceStart() {{
  const s = new Date(startDate);
  const n = new Date();
  return Math.max(1, Math.floor((n - s) / 86400000) + 1);
}}

// ========== RENDER: 总览 ==========
function renderOverview() {{
  const days = daysSinceStart();
  const dailyAvg = totalExpense / days;
  const catOrder = allCatOrder.filter(c => catTotals[c] && catTotals[c] > 0).sort((a,b) => catTotals[b] - catTotals[a]);

  let html = `
    <div class="card">
      <div class="card-title">📊 记账总览</div>
      <div class="kpi-grid">
        <div class="kpi-item">
          <div class="kpi-value income">¥${{fmt(totalIncome)}}</div>
          <div class="kpi-label">总收入</div>
        </div>
        <div class="kpi-item">
          <div class="kpi-value expense">¥${{fmt(totalExpense)}}</div>
          <div class="kpi-label">总支出</div>
        </div>
        <div class="kpi-item">
          <div class="kpi-value balance">¥${{fmt(balance)}}</div>
          <div class="kpi-label">结余</div>
        </div>
      </div>
      <div style="margin-top:14px;font-size:12px;color:var(--t3)">
        记账天数 ${{days}} 天 · 日均支出 ¥${{fmt(dailyAvg)}}
      </div>
    </div>

    <div class="card">
      <div class="card-title">📂 支出分类</div>
      <div class="cat-grid">`;

  catOrder.forEach(cat => {{
    const cfg = catConfig[cat] || {{emoji:'📦',color:'#888'}};
    const amt = catTotals[cat] || 0;
    const pct = totalExpense > 0 ? (amt / totalExpense * 100).toFixed(1) : 0;
    html += `
        <div class="cat-item" style="--cat-color:${{cfg.color}}">
          <div style="position:absolute;top:0;left:0;width:4px;height:100%;border-radius:4px 0 0 4px;background:${{cfg.color}}"></div>
          <div class="cat-icon">${{cfg.emoji}}</div>
          <div class="cat-name">${{cat}}</div>
          <div class="cat-amount">¥${{fmt(amt)}}</div>
          <div class="cat-pct">${{pct}}%</div>
          <div class="progress-bar"><div class="progress-fill" style="width:${{pct}}%;background:${{cfg.color}}"></div></div>
        </div>`;
  }});

  html += `</div></div>`;

  // Income section
  html += `
    <div class="card">
      <div class="card-title">💰 收入明细</div>
      <div class="income-section">`;
  incomeRecords.forEach(r => {{
    html += `<div class="income-row"><span class="name">${{formatDate(r.date)}} ${{r.item}}</span><span class="amt">+¥${{fmt(r.amount)}}</span></div>`;
  }});
  html += `
        <div class="income-total"><span class="name">累计收入</span><span class="amt">+¥${{fmt(totalIncome)}}</span></div>
      </div>
    </div>`;

  document.getElementById('sub-overview').innerHTML = html;
}}

// ========== RENDER: Period (当日/当周/当月) ==========
function renderPeriod(panelId, start, end, label) {{
  const panel = document.getElementById(panelId);
  const txs = filterByDate(transactions, start, end);
  const incs = filterByDate(incomeRecords.map(r => ({{date:r.date, category:'收入', item:r.item, amount:r.amount}})), start, end);

  if (txs.length === 0 && incs.length === 0) {{
    panel.innerHTML = `
      <div class="empty-state">
        <div class="icon">📭</div>
        <div>${{label}}暂无记录</div>
        <div style="margin-top:8px;font-size:12px;color:var(--t3)">记账数据从 2026/6/1 开始</div>
      </div>`;
    return;
  }}

  const expTotal = calcExpense(txs);
  const incTotal = calcIncome(incs);
  const grouped = groupByCategory(txs);
  const catOrder = Object.keys(grouped).sort((a,b) => grouped[b] - grouped[a]);

  let html = `
    <div class="day-summary">
      <div class="row"><span class="label">${{label}}支出</span><span class="val exp">¥${{fmt(expTotal)}}</span></div>
      <div class="row"><span class="label">${{label}}收入</span><span class="val inc">¥${{fmt(incTotal)}}</span></div>
      <div class="row"><span class="label">${{label}}笔数</span><span class="val" style="color:var(--t1)">${{txs.length}} 笔</span></div>
    </div>`;

  if (catOrder.length > 0) {{
    html += `<div class="card"><div class="card-title">分类汇总</div><div class="cat-grid">`;
    catOrder.forEach(cat => {{
      const cfg = catConfig[cat] || {{emoji:'📦',color:'#888'}};
      const amt = grouped[cat];
      const pct = expTotal > 0 ? (amt/expTotal*100).toFixed(1) : 0;
      html += `
        <div class="cat-item">
          <div style="position:absolute;top:0;left:0;width:4px;height:100%;border-radius:4px 0 0 4px;background:${{cfg.color}}"></div>
          <div class="cat-icon">${{cfg.emoji}}</div>
          <div class="cat-name">${{cat}}</div>
          <div class="cat-amount">¥${{fmt(amt)}}</div>
          <div class="cat-pct">${{pct}}%</div>
        </div>`;
    }});
    html += `</div></div>`;
  }}

  if (txs.length > 0) {{
    html += `<div class="card"><div class="card-title">支出明细</div><div class="tx-list">`;
    txs.slice().reverse().forEach(t => {{
      const cfg = catConfig[t.category] || {{emoji:'📦',color:'#888'}};
      html += `
        <div class="tx-item">
          <div class="tx-emoji">${{cfg.emoji}}</div>
          <div class="tx-left">
            <div class="tx-name">${{t.item}}</div>
            <div class="tx-meta">${{formatDate(t.date)}} · ${{t.category}}</div>
          </div>
          <div class="tx-amount expense">-¥${{fmt(t.amount)}}</div>
        </div>`;
    }});
    html += `</div></div>`;
  }}

  if (incs.length > 0) {{
    html += `<div class="card"><div class="card-title">💰 收入</div><div class="tx-list">`;
    incs.slice().reverse().forEach(r => {{
      html += `
        <div class="tx-item">
          <div class="tx-emoji">💰</div>
          <div class="tx-left">
            <div class="tx-name">${{r.item}}</div>
            <div class="tx-meta">${{formatDate(r.date)}}</div>
          </div>
          <div class="tx-amount income">+¥${{fmt(r.amount)}}</div>
        </div>`;
    }});
    html += `</div></div>`;
  }}

  panel.innerHTML = html;
}}

// ========== RENDER: 当月 ==========
function renderMonth() {{
  const [mStart, mEnd] = getMonthRange();
  renderPeriod('sub-month', mStart, mEnd, '本月');

  // Add month comparison at top
  const panel = document.getElementById('sub-month');
  const existing = panel.innerHTML;

  // Calculate June vs July
  const juneTxs = transactions.filter(t => t.date >= '2026-06-01' && t.date <= '2026-06-30');
  const julyTxs = transactions.filter(t => t.date >= '2026-07-01' && t.date <= '2026-07-31');
  const juneExp = calcExpense(juneTxs);
  const julyExp = calcExpense(julyTxs);
  const juneInc = calcIncome(incomeRecords.filter(r => r.date >= '2026-06-01' && r.date <= '2026-06-30'));
  const julyInc = calcIncome(incomeRecords.filter(r => r.date >= '2026-07-01' && r.date <= '2026-07-31'));

  // Check if current month has data
  const curMonthTxs = filterByDate(transactions, mStart, mEnd);
  if (curMonthTxs.length === 0) {{
    panel.innerHTML = `
      <div class="month-compare">
        <div class="month-card">
          <div class="month-name">6月</div>
          <div class="month-exp">¥${{fmt(juneExp)}}</div>
          <div class="month-inc">收入 ¥${{fmt(juneInc)}}</div>
          <div class="month-bal">结余 ¥${{fmt(juneInc - juneExp)}}</div>
        </div>
        <div class="month-card">
          <div class="month-name">7月</div>
          <div class="month-exp">¥${{fmt(julyExp)}}</div>
          <div class="month-inc">收入 ¥${{fmt(julyInc)}}</div>
          <div class="month-bal">结余 ¥${{fmt(julyInc - julyExp)}}</div>
        </div>
      </div>
      <div class="empty-state">
        <div class="icon">📭</div>
        <div>本月暂无记录</div>
        <div style="margin-top:8px;font-size:12px;color:var(--t3)">以上为历史月份对比</div>
      </div>`;
  }} else {{
    const header = `
      <div class="month-compare">
        <div class="month-card">
          <div class="month-name">6月</div>
          <div class="month-exp">¥${{fmt(juneExp)}}</div>
          <div class="month-inc">收入 ¥${{fmt(juneInc)}}</div>
          <div class="month-bal">结余 ¥${{fmt(juneInc - juneExp)}}</div>
        </div>
        <div class="month-card">
          <div class="month-name">7月</div>
          <div class="month-exp">¥${{fmt(julyExp)}}</div>
          <div class="month-inc">收入 ¥${{fmt(julyInc)}}</div>
          <div class="month-bal">结余 ¥${{fmt(julyInc - julyExp)}}</div>
        </div>
      </div>` + existing;
    panel.innerHTML = header;
  }}
}}

// ========== RENDER: 明细 ==========
function renderDetail() {{
  const panel = document.getElementById('sub-detail');
  let html = `
    <div class="date-filter">
      <select id="filterPreset" onchange="onPresetChange()">
        <option value="all">全部</option>
        <option value="jun">6月</option>
        <option value="jul">7月</option>
        <option value="custom">自定义</option>
      </select>
      <input type="date" id="filterStart" style="display:none" onchange="applyFilter()">
      <span id="filterSep" style="display:none">至</span>
      <input type="date" id="filterEnd" style="display:none" onchange="applyFilter()">
    </div>
    <div id="detailList"></div>`;
  panel.innerHTML = html;
  applyFilter();
}}

function onPresetChange() {{
  const v = document.getElementById('filterPreset').value;
  const s = document.getElementById('filterStart');
  const e = document.getElementById('filterEnd');
  const sep = document.getElementById('filterSep');

  if (v === 'custom') {{
    s.style.display = '';
    e.style.display = '';
    sep.style.display = '';
    s.value = '2026-06-01';
    e.value = '2026-07-31';
    applyFilter();
  }} else {{
    s.style.display = 'none';
    e.style.display = 'none';
    sep.style.display = 'none';
    applyFilter();
  }}
}}

function applyFilter() {{
  const preset = document.getElementById('filterPreset').value;
  let start = '', end = '9999-12-31';

  if (preset === 'jun') {{ start = '2026-06-01'; end = '2026-06-30'; }}
  else if (preset === 'jul') {{ start = '2026-07-01'; end = '2026-07-31'; }}
  else if (preset === 'custom') {{
    start = document.getElementById('filterStart').value || '2026-06-01';
    end = document.getElementById('filterEnd').value || '2026-07-31';
  }}

  const txs = filterByDate(transactions, start || '0000-01-01', end);
  const incs = filterByDate(incomeRecords, start || '0000-01-01', end);

  // Combine and sort
  const all = [
    ...txs.map(t => ({{...t, type:'expense'}})),
    ...incs.map(r => ({{date:r.date, item:r.item, amount:r.amount, category:'收入', type:'income'}}))
  ].sort((a,b) => b.date.localeCompare(a.date) || (a.type === 'income' ? -1 : 1));

  const expTotal = calcExpense(txs);
  const incTotal = calcIncome(incs.map(r => ({{amount:r.amount}})));

  let html = `
    <div class="day-summary">
      <div class="row"><span class="label">支出合计</span><span class="val exp">¥${{fmt(expTotal)}}</span></div>
      <div class="row"><span class="label">收入合计</span><span class="val inc">¥${{fmt(incTotal)}}</span></div>
      <div class="row"><span class="label">共 ${{all.length}} 笔</span><span class="val" style="color:var(--t3);font-size:13px">${{start||'起始'}} ~ ${{end==='9999-12-31'?'至今':end}}</span></div>
    </div>
    <div class="card"><div class="tx-list">`;

  all.forEach(t => {{
    if (t.type === 'income') {{
      html += `
        <div class="tx-item">
          <div class="tx-emoji">💰</div>
          <div class="tx-left">
            <div class="tx-name">${{t.item}}</div>
            <div class="tx-meta">${{formatDate(t.date)}} · 收入</div>
          </div>
          <div class="tx-amount income">+¥${{fmt(t.amount)}}</div>
        </div>`;
    }} else {{
      const cfg = catConfig[t.category] || {{emoji:'📦',color:'#888'}};
      html += `
        <div class="tx-item">
          <div class="tx-emoji">${{cfg.emoji}}</div>
          <div class="tx-left">
            <div class="tx-name">${{t.item}}</div>
            <div class="tx-meta">${{formatDate(t.date)}} · ${{t.category}}</div>
          </div>
          <div class="tx-amount expense">-¥${{fmt(t.amount)}}</div>
        </div>`;
    }}
  }});

  html += `</div></div>`;
  document.getElementById('detailList').innerHTML = html;
}}

// ========== TAB SWITCHING ==========
function switchMain(name) {{
  document.querySelectorAll('.main-tab').forEach(el => el.classList.toggle('active', el.dataset.main === name));
  document.querySelectorAll('.main-panel').forEach(el => el.classList.toggle('active', el.id === 'panel-' + name));
}}

function switchSub(name) {{
  document.querySelectorAll('.sub-tab').forEach(el => el.classList.toggle('active', el.dataset.sub === name));
  document.querySelectorAll('.sub-panel').forEach(el => el.classList.toggle('active', el.id === 'sub-' + name));
}}

// ========== INIT ==========
function init() {{
  // Set header date
  const now = new Date();
  document.getElementById('headerDate').textContent = now.toISOString().slice(0,10);

  renderOverview();
  renderPeriod('sub-today', now.toISOString().slice(0,10), now.toISOString().slice(0,10), '今日');
  const [wStart, wEnd] = getWeekRange();
  renderPeriod('sub-week', wStart, wEnd, '本周');
  renderMonth();
  renderDetail();
}}

init();
</script>
</body>
</html>'''

# Write the file
output_path = '/app/data/所有对话/主对话/健康/健康看板/comprehensive-dashboard.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"HTML generated: {{output_path}}")
print(f"File size: {{len(html)}} bytes")
