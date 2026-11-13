
const escapeText = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const originalRender = render;
render = function(action,res){
  if(action==='hodge'){
    const r=res.hodge;
    let html='<h2>Hodge diamond</h2>';
    if(r.hodge_certified){
      html+='<div style="text-align:center;font:18px monospace;line-height:2">';
      r.hodge_diamond.forEach(row=>html+='<div>'+row.map(escapeText).join(' &nbsp; ')+'</div>');
      html+='</div><p>Dimension '+r.dimension+' · Euler characteristic '+r.euler+'</p>';
    } else html+='<p>The Hodge diamond is undetermined.</p>';
    html+='<p>'+r.assumptions.map(escapeText).join('; ')+'.</p><p>'+escapeText(r.scope)+'</p>';
    $('out').innerHTML=html;
    return;
  }
  originalRender(action==='analysis'?'sqm':action,res);
  if(res.analysis){
    const a=res.analysis;
    let html='<h2>Unit cyclic determinant at selected Novikov values</h2><p>For multiplication M: '+escapeText(a.cyclic_determinant || a.cyclic_error)+'</p>';
    html+='<p>At '+escapeText(JSON.stringify(a.specialization))+': '+escapeText(a.cyclic_determinant_at_specialization)+'</p>';
    html+='<p>For the connection K = −M: '+escapeText(a.connection_cyclic_determinant)+'</p>';
    html+='<h2>Specialized eigenvalues</h2><table><tr><th>Real</th><th>Imaginary</th><th>Multiplicity</th></tr>';
    a.eigenvalues.forEach(e=>html+='<tr><td>'+escapeText(e.real)+'</td><td>'+escapeText(e.imag)+'</td><td>'+e.multiplicity+'</td></tr>');
    html+='</table>';
    const c=res.connection;
    html+='<h2>Regularized exponent multisets</h2><p>'+escapeText(c.convention || c.reason)+'</p><table><tr><th>Factor of K</th><th>Rank per root</th><th>Exponent : multiplicity (mod Z)</th><th>Status</th></tr>';
    c.sectors.forEach(s=>html+='<tr><td>'+escapeText(s.eigenvalue_factor_K)+'</td><td>'+s.multiplicity_per_root+'</td><td>'+escapeText(s.status==='computed'?JSON.stringify(s.classes_mod_Z):s.reason)+'</td><td>'+escapeText(s.status)+'</td></tr>');
    html+='</table><p>'+escapeText(res.scope)+'. No rationality verdict is inferred.</p>';
    $('out').insertAdjacentHTML('beforeend',html);
  }
};
$('bhodge').onclick=()=>run('hodge');
$('banalysis').onclick=()=>run('analysis');
$('bstop').onclick=()=>{if(currentJob) fetch('/api/stop?id='+currentJob);};
