window.MathJax = {
  tex: {
    inlineMath: [
      ["$", "$"],
      ["\\(", "\\)"],
    ],
    displayMath: [
      ["$$", "$$"],
      ["\\[", "\\]"],
    ],
    macros : {
        // example... usage $\bold{wef}$.
        bold: ["{\\bf #1}", 1], 
        ab: ["\\langle #1 \\rangle", 1],
        OO: ["\\{0, 1\\}", 0],
        U: ["\\mathcal{U}", 0],
        P: ["\\text{P}", 0],
        NP: ["\\text{NP}", 0],
        L: ["\\text{L}", 0],
        NL: ["\\text{NL}", 0],
        coNP: ["\\text{co-NP}", 0],
        DTIME: ["\\text{DTIME}", 0],
        NTIME: ["\\text{NTIME}", 0],
        SPACE: ["\\text{SPACE}", 0],
        BPP: ["\\text{BPP}", 0],
        PH: ["\\text{PH}", 0],
        RP: ["\\text{RP}", 0],
        coRP: ["\\text{coRP}", 0],
        PPOLY: ["\\text{P/poly}", 0],
        ZPP: ["\\text{ZPP}", 0],
        BPTIME: ["\\text{BPTIME}", 0],
        NSPACE: ["\\text{NSPACE}", 0],
        PSPACE: ["\\text{PSPACE}", 0],
        NPSPACE: ["\\text{NSPACE}", 0],
        TQBF: ["\\text{TQBF}", 0],
        STCON: ["\\text{STCON}", 0],
        QEQ: ["\\stackrel{?}{=}", 0],
        st: ["\\text{ s.t. }", 0],
        pr: ["\\leq_p", 0],
        SAT: ["\\text{SAT}", 0],
        SIZE: ["\\text{SIZE}", 0],
        N: ["\\mathbb{N}", 0],
    }
  },
  svg: {
    fontCache: "global",
  },
};

(function () {
  var script = document.createElement("script");
  script.src = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js";
  script.async = true;
  document.head.appendChild(script);
})();
