# TOAE209/TOAH209 — Thiết kế và Phân tích Thuật toán
## Design and Analysis of Algorithms — Course Materials

**Foreign Trade University | Department of Technology & Data Science**

> This course follows the structure and content of *Algorithm Design* by Jon Kleinberg
> and Éva Tardos. The original lecture slides (by Kevin Wayne, Princeton University,
> https://www.cs.princeton.edu/~wayne/kleinberg-tardos/) are distributed as reference
> material inside each week's `original_slides/` folder. Slides that do not map onto
> one of the 15 teaching weeks are kept in `further_reading/`.

---

## Directory Structure

```
algorithm_undergrad_course_ftu/
├── README.md                              ← You are here
├── LEETCODE.md                            ← Curated LeetCode practice problems for every week
├── further_reading/                       ← Reference slides not covered in the 15-week plan
│   ├── AmortizedAnalysis.pdf
│   ├── BinomialHeaps.pdf
│   ├── FibonacciHeaps.pdf
│   ├── IntractabilityIII.pdf
│   ├── LinearProgrammingI.pdf
│   ├── LinearProgrammingII.pdf
│   └── LinearProgrammingIII.pdf
├── week01_intro_stable_matching/
├── week02_algorithm_analysis/
├── week03_graphs_union_find/
├── week04_greedy_i/
├── week05_greedy_ii/
├── week06_divide_and_conquer_i/
├── week07_divide_and_conquer_ii/
├── week08_dynamic_programming_i/
├── week09_dynamic_programming_ii/
├── week10_network_flow_i/
├── week11_network_flow_ii_iii/
├── week12_intractability/
├── week13_pspace_extending_tractability/
├── week14_approximation_local_search/
└── week15_randomized_algorithms/
```

### Per-week layout

Each `weekNN_topic/` folder is organized into sub-folders by file role:

```
weekNN_topic/
├── original_slides/              ← Reference Kleinberg-Tardos slides (Kevin Wayne, Princeton)
├── notes/
│   ├── lecture_notes.tex          ← Beamer-free lecture notes (compiled with pdflatex)
│   └── lecture_notes.pdf
├── theory/
│   ├── theoretical_questions.tex  ← theory questions + 10-question quiz, solutions at the end
│   └── theoretical_questions.pdf
├── exercises/
│   ├── practical_exercises.tex    ← coding problems + a LeetCode practice section
│   ├── practical_exercises.pdf
│   └── starter_code_problemNN.py  ← Per-problem starter (one per exercise)
├── solutions/
│   └── solution_problemNN.py      ← Per-problem reference solution
└── starter_code.py                ← Shared helper module imported by the per-problem files
```

---

## Course Schedule

| Week | Folder | Topics | Key Algorithms | Reading (Kleinberg-Tardos) |
|------|--------|--------|-----------------|------------------------------|
| 1 | week01_intro_stable_matching | Introduction, Stable Matching | Gale-Shapley | Ch. 1 |
| 2 | week02_algorithm_analysis | Algorithm Analysis, Asymptotics | Binary Search | Ch. 2 |
| 3 | week03_graphs_union_find | Graphs, Union-Find | BFS, DFS, Union-Find | Ch. 3, App. B |
| 4 | week04_greedy_i | Greedy Algorithms I | Interval Scheduling, Partitioning | Ch. 4 |
| 5 | week05_greedy_ii | Greedy Algorithms II | Dijkstra, MST (Kruskal/Prim) | Ch. 4 |
| 6 | week06_divide_and_conquer_i | Divide & Conquer I | Merge Sort, Recurrences | Ch. 5 |
| 7 | week07_divide_and_conquer_ii | Divide & Conquer II | Closest Pair, FFT | Ch. 5 |
| 8 | week08_dynamic_programming_i | Dynamic Programming I (**Midterm**) | Weighted Interval Scheduling, Knapsack | Ch. 6 |
| 9 | week09_dynamic_programming_ii | Dynamic Programming II | Sequence Alignment, Shortest Paths | Ch. 6 |
| 10 | week10_network_flow_i | Network Flow I | Ford-Fulkerson, Max-Flow Min-Cut | Ch. 7 |
| 11 | week11_network_flow_ii_iii | Network Flow II/III | Bipartite Matching, Flow Applications | Ch. 7 |
| 12 | week12_intractability | Intractability (NP-Completeness) | Reductions, NP-Complete Problems | Ch. 8 |
| 13 | week13_pspace_extending_tractability | PSPACE & Extending Tractability | Vertex Cover (FPT), Branch & Bound | Ch. 9–10 |
| 14 | week14_approximation_local_search | Approximation & Local Search | Vertex Cover, Hill Climbing | Ch. 11–12 |
| 15 | week15_randomized_algorithms | Randomized Algorithms | RandQuickSort, Contention Resolution | Ch. 13 |

---

## How to Use the Materials

### For Students

1. **Before class**: Read `notes/lecture_notes.pdf` for the week.
2. **During class**: Follow along with the reference slides in `original_slides/`.
3. **Practical exercises**: Read `exercises/practical_exercises.pdf`, then implement each
   problem in its `exercises/starter_code_problemNN.py` file:
   ```bash
   cd weekNN_topic/exercises
   python starter_code_problem01.py
   ```
4. **Theory**: Attempt `theory/theoretical_questions.pdf` independently before checking
   the solutions printed at the end of the document.
5. **After deadline**: Compare your work with `solutions/solution_problemNN.py`.
6. **Extra practice**: Work through the week's curated LeetCode problems, listed both in
   [`LEETCODE.md`](LEETCODE.md) and in the "LeetCode Practice" section of each week's
   `exercises/practical_exercises.pdf`.

### For Instructors

- Compile PDFs: `pdflatex <file>.tex` (run twice for cross-references/TOC).
- Solutions (`solutions/solution_problemNN.py`, theory-question answers) — do not
  distribute until after the submission deadline.
- `starter_code.py` (at the week root) gives students a common scaffold (imports,
  helper functions, test harness conventions) used across all problems for the week.

---

## Grading Policy

| Component | Weight |
|-----------|--------|
| Attendance (Chuyên cần) | 10% |
| Midterm (Week 8) | 30% |
| Final Exam / Project | 60% |

- Minimum 80% attendance required
- Midterm score ≥ 4/10 required

---

## Key Textbooks

1. **[Primary]** Jon Kleinberg & Éva Tardos, *Algorithm Design*, Pearson 2005
2. **[Secondary]** Thomas H. Cormen et al., *Introduction to Algorithms*, 4th ed. (CLRS), MIT Press 2022
3. **[Secondary]** Nguyễn Đức Nghĩa, *Cấu trúc dữ liệu và giải thuật*, NXB ĐHBK 2013
4. **[Supplementary]** Jeff Erickson, *Algorithms* (free): https://jeffe.cs.illinois.edu/teaching/algorithms/

---

## Online Resources

- **Original slide source**: https://www.cs.princeton.edu/~wayne/kleinberg-tardos/
- **VisuAlgo**: https://visualgo.net — interactive algorithm visualisations
- **MIT OpenCourseWare 6.006**: https://ocw.mit.edu/6-006
- **LeetCode** — see [`LEETCODE.md`](LEETCODE.md) for problems mapped to each week
- **Codeforces** — additional competitive-programming practice
- **Python Tutor**: https://pythontutor.com — step-by-step code execution

---

## Requirements

```
Python 3.10+
matplotlib (for demos)   pip install matplotlib
```

No other external libraries required for the core algorithms.

LaTeX (with `pdflatex`) is required to compile `lecture_notes.tex`,
`practical_exercises.tex`, and `theoretical_questions.tex`.

---

## Progress

| Week | Status |
|------|--------|
| 1–15 | ✅ Complete (lecture notes, theory, exercises, solutions, LeetCode practice) |

Weeks 1–4 each contain 17–22 practical problems; weeks 5–15 each contain 12 practical
problems. Every reference solution is tested (`python solutions/solution_problemNN.py`
prints `All tests passed!`), and all `.tex` documents compile with `pdflatex`.

---

*Last updated: 2025–2026 Academic Year*
*Department of Technology & Data Science, Foreign Trade University*
