(function(root){
 'use strict';
 const cos2=(degrees)=>Math.cos(degrees*Math.PI/180)**2;
 function order(state,a,b){
  const pa=cos2(state-a),pb=cos2(state-b),same=cos2(a-b);
  const ab=[pa*same,pa*(1-same),(1-pa)*(1-same),(1-pa)*same];
  const ba=[pb*same,(1-pb)*(1-same),pb*(1-same),(1-pb)*same];
  return {ab,ba,aFirst:pa,aAfterB:ba[0]+ba[1],bFirst:pb,bAfterA:ab[0]+ab[2],q:ab[0]+ab[3]-ba[0]-ba[3]};
 }
 function mixture(w,yes,no,direct){const assessed=w*yes+(1-w)*no;return {assessed,difference:direct-assessed,low:Math.min(yes,no),high:Math.max(yes,no),outside:direct<Math.min(yes,no)||direct>Math.max(yes,no)};}
 function interval(low,high,tolerance){if(![low,high,tolerance].every(Number.isFinite)||low>high||tolerance<0)return 'invalid';if(low>=-tolerance&&high<=tolerance)return 'within';if(low>tolerance||high< -tolerance)return 'beyond';return 'unresolved';}
 const api={cos2,order,mixture,interval};if(typeof module!=='undefined')module.exports=api;else root.QC=api;
})(typeof window!=='undefined'?window:globalThis);
