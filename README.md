# TOAE209/TOAH209 — Thiết kế và Phân tích Thuật toán
## Design and Analysis of Algorithms — Course Materials

**Foreign Trade University | Department of Technology & Data Science**

---

## Directory Structure

```
algorithms_course/
├── README.md                    ← You are here
├── week01/  Introduction & Efficiency
│   ├── slides.tex               ← Beamer LaTeX slides
│   ├── exercises.md             ← Exercise sheet
│   ├── demo.py                  ← Demonstration code
│   ├── starter.py               ← Student starter code (with auto-grader)
│   └── solution.py              ← Instructor solution (do not distribute early)
├── week02/  Asymptotic Notation & Complexity Classes
├── week03/  Divide and Conquer I
├── week04/  Divide and Conquer II
├── week05/  Greedy Algorithms I
├── week06/  Greedy Algorithms II
├── week07/  Dynamic Programming I
├── week08/  Dynamic Programming II (+ Midterm)
├── week09/  Dynamic Programming III
├── week10/  Graph Algorithms I
├── week11/  Graph Algorithms II
├── week12/  Advanced Topics I (Network Flow, String Matching)
├── week13/  Advanced Topics II (Approximation, NP)
├── week14/  Randomised Algorithms
└── week15/  Heuristics (GA, Simulated Annealing)
```

---

## Course Schedule

| Week | Topics | Key Algorithms | Reading (CLRS) |
|------|--------|----------------|----------------|
| 1 | Introduction, Time/Space Complexity | Insertion Sort | Ch. 1–2 |
| 2 | Big-O/Omega/Theta, P/NP Classes | — | Ch. 3, App. |
| 3 | Divide & Conquer I | Merge Sort, Quick Sort | Ch. 2, 7 |
| 4 | Divide & Conquer II, Master Theorem | Karatsuba, Strassen | Ch. 4 |
| 5 | Greedy I: Principles | Activity Selection, Huffman | Ch. 16 |
| 6 | Greedy II: Graph Applications | Dijkstra, Kruskal, Prim | Ch. 23–24 |
| 7 | Dynamic Programming I | Knapsack, LCS | Ch. 15 |
| 8 | **Midterm** + DP II | Edit Distance, LIS | Ch. 15 |
| 9 | Dynamic Programming III | Tabulation, Bitmask DP | Ch. 15 |
| 10 | Graph Algorithms I | BFS, DFS, Bellman-Ford | Ch. 22–24 |
| 11 | Graph Algorithms II | Prim, Topo Sort, SCC | Ch. 22–23, 25 |
| 12 | Advanced: Flow + String | Ford-Fulkerson, KMP | Ch. 26, 32 |
| 13 | Advanced: Approx + NP | Rabin-Karp, Vertex Cover | Ch. 34–35 |
| 14 | Randomised Algorithms | Rand. QuickSort, QuickSelect | Ch. 5, 9 |
| 15 | Heuristics | Genetic Algorithms, Simulated Annealing | Ch. 27 |

---

## How to Use the Materials

### For Students

1. **Before class**: Read the assigned CLRS chapters
2. **During class**: Follow the Beamer slides (`slides.tex`, compile with `pdflatex`)
3. **After class**: Run `demo.py` to see algorithms in action
4. **Exercises**: Attempt `exercises.md` problems independently
5. **Programming**: Implement functions in `starter.py`, run to see your score:
   ```bash
   python starter.py
   ```
6. **After deadline**: Compare your work with `solution.py`

### For Instructors

- Compile slides: `pdflatex slides.tex` (run twice for cross-references)
- Solutions in `solution.py` — do not distribute until after submission deadline
- Auto-grader in `starter.py` tests correctness automatically
- Modify test cases in the `_run_tests()` function as needed

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

1. **[Primary]** Thomas H. Cormen et al., *Introduction to Algorithms*, 4th ed. (CLRS), MIT Press 2022
2. **[Secondary]** Nguyễn Đức Nghĩa, *Cấu trúc dữ liệu và giải thuật*, NXB ĐHBK 2013
3. **[Supplementary]** Jeff Erickson, *Algorithms* (free): https://jeffe.cs.illinois.edu/teaching/algorithms/
4. **[C++ Reference]** Deitel & Deitel, *C++ How to Program*, 7th ed.

---

## Online Resources

- **VisuAlgo**: https://visualgo.net — interactive algorithm visualisations
- **MIT OpenCourseWare 6.006**: https://ocw.mit.edu/6-006
- **LeetCode / Codeforces** — practice problems
- **Python Tutor**: https://pythontutor.com — step-by-step code execution

---

## Requirements

```
Python 3.8+
matplotlib (for demos)   pip install matplotlib
```

No other external libraries required for the core algorithms.

---

*Last updated: 2024–2025 Academic Year*
*Department of Technology & Data Science, Foreign Trade University*
