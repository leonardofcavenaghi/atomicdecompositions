import re

with open('gwflags/gui.py', 'r') as f:
    content = f.read()

# Replace the HTML body with a highly structured card layout
old_main = r'<div id="controls">.*?</div>\n<div id="results">'
new_main = r"""<div id="controls">
  <div class="control-card">
    <div class="card-header">1. Space Definition</div>
    <label>Preset Library</label>
    <select id="preset"><option value="">— choose a pre-configured example —</option></select>
    <label>Lie Algebra</label>
    <input id="algebra" value="A2" placeholder="e.g., A2, B3, A3xA3, G2">
    <div class="row">
      <div>
        <label>Kept Simple Roots</label>
        <input id="keep" value="1" placeholder="e.g., 1,2">
      </div>
      <div>
        <label>Twisting Bundle K</label>
        <input id="K" placeholder="e.g., taut_quot(X, 2) or 1,1;2,2">
      </div>
    </div>
  </div>

  <div class="control-card">
    <div class="card-header">2. Execution Options</div>
    <div class="row">
      <div>
        <label>Evaluate y (Novikov)</label>
        <input id="eval_y" placeholder="e.g., y1=2, y2=-1">
      </div>
      <div>
        <label>Parallel Workers</label>
        <input id="workers" value="8">
      </div>
    </div>
    <button id="bsqm" class="primary-btn">Compute c&#8321;(TX)&#8902; Matrix</button>
    <button id="binfo" class="secondary">View Space Info</button>
  </div>

  <div class="control-card" id="gwbox">
    <div class="card-header">3. GW Invariants (Advanced)</div>
    <label>Curve Class &beta;</label>
    <input id="beta" placeholder="one integer per root, e.g., 1,0">
    <label>Insertions (separated by |)</label>
    <input id="classes" placeholder="e.g., pt | id | 2,1,3">
    <button id="bgw" class="secondary" style="width:100%; margin-top:12px;">Compute Invariant</button>
  </div>
  
  <div id="log">System ready. Waiting for input...</div>
</div>
<div id="results">"""

content = re.sub(old_main, new_main, content, flags=re.DOTALL)

# Add CSS for the cards
old_css = r'#controls \{'
new_css = r"""
.control-card {
  background: var(--panel);
  border: 1px solid var(--edge);
  border-radius: var(--radius);
  padding: 20px;
  margin-bottom: 24px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}
.card-header {
  font-size: 14px;
  font-weight: 700;
  color: #fff;
  margin-bottom: 16px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--edge);
  letter-spacing: -0.2px;
}
.primary-btn { width: 100%; margin-right: 0; margin-bottom: 8px; }
#controls {"""
content = content.replace(old_css, new_css)

# Remove the old #gwbox border top since it's now a card
content = re.sub(r'#gwbox \{.*?\}', r'#gwbox { margin-top: 0; padding-top: 20px; }', content, flags=re.DOTALL)

with open('gwflags/gui.py', 'w') as f:
    f.write(content)

print("UX patched!")
