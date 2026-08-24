module.exports = {
  content: ["_site/**/*.html"],
  css: ["_site/assets/css/**/*.css"],
  output: "_site/assets/css",
  safelist: {
    standard: [/^highlight/, /^language-/, /^rouge/, /^mermaid/, /^katex/],
    deep: [/dark/, /light/],
  },
};
