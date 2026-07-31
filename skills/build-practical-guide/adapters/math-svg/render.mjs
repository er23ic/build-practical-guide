#!/usr/bin/env node

import fs from 'node:fs/promises';
import path from 'node:path';
import {loadMathJax} from './runtime.mjs';

function option(name) {
  const index = process.argv.indexOf(name);
  return index >= 0 ? process.argv[index + 1] : undefined;
}

function fail(code, error, details = {}) {
  console.error(JSON.stringify({error, ...details}, null, 2));
  process.exit(code);
}

const source = option('--source');
const output = option('--output');
const idPrefix = option('--id-prefix');
const display = process.argv.includes('--display');

if (!source || !output) {
  fail(2, 'invalid-arguments', {
    usage: 'node render.mjs --source <formal-source> --output <file.svg> [--display]'
  });
}

if (idPrefix && !/^[A-Za-z_][A-Za-z0-9_.-]*$/u.test(idPrefix)) {
  fail(2, 'invalid-id-prefix', {
    message: 'Use an XML-safe prefix beginning with a letter or underscore.'
  });
}

const runtime = await loadMathJax();
if (!runtime.available) {
  fail(3, 'capability-unavailable', {
    capability: 'formal-math-svg',
    fallback: 'Use supported Markdown math or leave the figure pending.'
  });
}

const MathJax = runtime.MathJax;
await MathJax.init({
  loader: {load: ['input/tex', 'output/svg']},
  output: {linebreaks: {inline: false}},
  svg: {fontCache: 'local'}
});

const container = await MathJax.tex2svgPromise(source, {display});
const svgNodes = MathJax.startup.adaptor.tags(container, 'svg');
if (svgNodes.length !== 1) {
  fail(1, 'renderer-output-invalid', {
    message: `Math renderer output contained ${svgNodes.length} SVG roots; expected exactly one.`
  });
}

let svg = MathJax.startup.adaptor.serializeXML(svgNodes[0]);
const errorMatch = svg.match(
  /data-mml-node="merror"[^>]*data-mjx-error="([^"]+)"/u
);
if (errorMatch) {
  fail(1, 'invalid-formal-source', {
    message: errorMatch[1]
  });
}

const viewBox = svg.match(/viewBox="([^"]+)"/u)?.[1];
if (!viewBox) {
  fail(1, 'renderer-output-invalid', {
    message: 'Math renderer output did not contain a viewBox.'
  });
}

if (idPrefix) {
  const ids = [...svg.matchAll(/\bid="([^"]+)"/gu)].map((match) => match[1]);
  if (new Set(ids).size !== ids.length) {
    fail(1, 'renderer-output-invalid', {
      message: 'Math renderer output contained duplicate definition IDs.'
    });
  }

  const replacements = new Map(
    ids.map((id) => [id, `${idPrefix}-${id}`])
  );
  svg = svg
    .replace(/\bid="([^"]+)"/gu, (match, id) => (
      replacements.has(id) ? `id="${replacements.get(id)}"` : match
    ))
    .replace(/\b(xlink:href|href)="#([^"]+)"/gu, (match, attribute, id) => (
      replacements.has(id)
        ? `${attribute}="#${replacements.get(id)}"`
        : match
    ))
    .replace(/url\(#([^)]+)\)/gu, (match, id) => (
      replacements.has(id) ? `url(#${replacements.get(id)})` : match
    ));
}

const outputPath = path.resolve(output);
const outputDirectory = path.dirname(outputPath);
const temporaryPath = path.join(
  outputDirectory,
  `.${path.basename(outputPath)}.${process.pid}.tmp`
);

await fs.mkdir(outputDirectory, {recursive: true});
try {
  await fs.writeFile(temporaryPath, `${svg}\n`, 'utf8');
  await fs.rename(temporaryPath, outputPath);
} catch (error) {
  await fs.rm(temporaryPath, {force: true});
  fail(1, 'output-write-failed', {
    message: error instanceof Error ? error.message : String(error)
  });
}

console.log(JSON.stringify({
  capability: 'formal-math-svg',
  output: outputPath,
  display,
  idPrefix: idPrefix ?? null,
  viewBox
}, null, 2));
