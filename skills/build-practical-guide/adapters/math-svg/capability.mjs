#!/usr/bin/env node

import {loadMathJax} from './runtime.mjs';

const runtime = await loadMathJax();
console.log(JSON.stringify({
  capability: 'formal-math-svg',
  available: runtime.available,
  renderer: runtime.available ? 'mathjax' : null
}, null, 2));

process.exit(runtime.available ? 0 : 3);
