const defaultModule = 'mathjax';

export function moduleSpecifier() {
  return process.env.BUILD_PRACTICAL_GUIDE_MATHJAX_MODULE ?? defaultModule;
}

export async function loadMathJax() {
  const specifier = moduleSpecifier();
  try {
    const loaded = await import(specifier);
    return {
      available: true,
      specifier,
      MathJax: loaded.default ?? loaded
    };
  } catch {
    return {
      available: false,
      specifier,
      MathJax: null
    };
  }
}
