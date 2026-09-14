import re

with open('gwflags/gui.py', 'r') as f:
    content = f.read()

old_style_pattern = r"<style>.*?</style>"

new_style = """<style>
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500&family=Inter:wght@400;500;600;700&display=swap');
:root { 
  --bg: #09090b; 
  --panel: #18181b; 
  --edge: #27272a; 
  --fg: #fafafa;
  --dim: #a1a1aa; 
  --acc: #3b82f6; 
  --acc-hover: #2563eb;
  --ok: #34d399; 
  --err: #f87171; 
  --radius: 8px;
}
* { box-sizing:border-box; margin: 0; padding: 0; }
body { 
  background:var(--bg); color:var(--fg);
  font-family: 'Inter', -apple-system, sans-serif;
  font-size: 14.5px; line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}
header { 
  padding: 16px 28px; 
  background: var(--panel);
  border-bottom: 1px solid var(--edge);
  display: flex; align-items: baseline; gap: 16px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
header h1 { font-size: 20px; font-weight: 700; color: #fff; letter-spacing: -0.5px; }
header span { color: var(--dim); font-size: 13.5px; font-weight: 400; }
main { 
  display: grid; grid-template-columns: 360px 1fr; gap: 0;
  min-height: calc(100vh - 61px); 
}
#controls { 
  padding: 24px 28px; 
  border-right: 1px solid var(--edge); 
  background: rgba(24, 24, 27, 0.4);
}
#results  { padding: 24px 32px; overflow-x: auto; }
label { 
  display: block; margin: 16px 0 6px; 
  color: var(--dim); font-size: 12px; font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.05em; 
}
input, select { 
  width: 100%; padding: 10px 12px; border-radius: var(--radius);
  border: 1px solid var(--edge); background: var(--panel); color: var(--fg);
  font-family: 'Fira Code', monospace; font-size: 13px;
  transition: all 0.2s; outline: none;
}
input:focus, select:focus { border-color: var(--acc); box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2); }
.row { display: flex; gap: 12px; }
.row > div { flex: 1; }
button { 
  margin-top: 20px; margin-right: 10px; padding: 10px 20px;
  border-radius: var(--radius); border: none; background: var(--acc);
  color: #fff; font-weight: 600; font-size: 13.5px; cursor: pointer;
  transition: all 0.2s; outline: none; box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}
button:hover { background: var(--acc-hover); transform: translateY(-1px); }
button.secondary { background: var(--panel); border: 1px solid var(--edge); color: var(--fg); box-shadow: none; }
button.secondary:hover { background: #27272a; }
button:disabled { opacity: 0.5; cursor: not-allowed; transform: none; }
#gwbox { 
  border-top: 1px solid var(--edge); margin-top: 24px; padding-top: 8px; 
}
#log { 
  margin-top: 24px; padding: 12px 16px; background: #000;
  border: 1px solid var(--edge); border-radius: var(--radius); max-height: 250px;
  overflow-y: auto; font-family: 'Fira Code', monospace; font-size: 12px;
  color: var(--ok); white-space: pre-wrap; box-shadow: inset 0 2px 6px rgba(0,0,0,0.3);
}
h2 { 
  font-size: 18px; font-weight: 600; margin: 24px 0 12px; color: #fff;
  letter-spacing: -0.3px; 
}
table { 
  border-collapse: collapse; margin: 12px 0 24px; 
  background: var(--panel); border-radius: var(--radius); overflow: hidden;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
td, th { 
  border: 1px solid var(--edge); padding: 10px 14px;
  font-family: 'Fira Code', monospace; font-size: 13px; text-align: center; 
}
th { color: var(--dim); font-weight: 600; background: rgba(255,255,255,0.02); }
tr:hover td { background: rgba(255,255,255,0.02); }
.badge { 
  display: inline-block; margin: 4px 12px 4px 0; padding: 4px 12px;
  border-radius: 20px; background: rgba(59, 130, 246, 0.15); border: 1px solid rgba(59, 130, 246, 0.3);
  color: var(--acc); font-size: 12.5px; font-weight: 500;
}
.dom { color: var(--ok); font-weight: 700; background: rgba(52, 211, 153, 0.1) !important; }
.err { color: var(--err); }
sup { font-size: 10px; font-weight: 600; }
</style>"""

content = re.sub(old_style_pattern, new_style, content, flags=re.DOTALL)

with open('gwflags/gui.py', 'w') as f:
    f.write(content)

print("Style updated successfully!")
