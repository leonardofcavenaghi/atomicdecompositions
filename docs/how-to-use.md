# How to Use `gwflags`

This guide bridges the theoretical framework of Quantum Cohomology with practical computation using the `gwflags` package. 

You can run these computations either directly through the Command Line Interface (CLI) or by launching the Graphical User Interface (GUI).

## Launching the Interface

To start the interface, open your terminal (inside the `atomicdecompositions` folder) and run:
```bash
python3 -m gwflags.gui
```
This will start a local server. Open your web browser to the provided `localhost` URL (usually `http://127.0.0.1:8000`).

---

## Task 1: Testing Quantum Rationality Criteria (Fano Fourfolds)

The primary application of this software is testing rationality conjectures (e.g., Conjecture $\mathcal{O}$) for Fano fourfolds by computing the small quantum multiplication operator by the first Chern class.

**Important Note on Eigenvalues:** When computing the spectrum of the quantum connection, the software sets the **Novikov parameters ($y_i$ or $q_i$) to $1$**.

### Case A: Cubic Fourfolds
**Goal:** Verify the Jordan defect constraint for a cubic fourfold in $\mathbb{P}^5$.
- **Algebra:** `A5`
- **Keep Nodes:** `1`
- **Bundle:** `O(3)`
- **GUI:** Select "Quantum Multiplication", input parameters, and click **Compute SQM**.

### Case B: Ordinary Gushel–Mukai Fourfolds
**Goal:** Investigate the semisimple spectrum of Gushel-Mukai fourfolds in $Gr(2,5)$.
- **Algebra:** `A4`
- **Keep Nodes:** `2`
- **Bundle:** `osum(O(1), O(2))`

---

## Task 2: Computing Individual Gromov-Witten Invariants

While the quantum matrices calculate the aggregate structural invariants, you can also use `gwflags` to compute single genus-zero Gromov-Witten invariants directly using Atiyah-Bott localization.

**Example:** Computing the 2-point invariant $\langle pt, pt \rangle_{d=1} = 1$ on $\mathbb{P}^2$.

**In the GUI:**
1. Switch the operation mode from "Quantum Multiplication" to **"Single GW Invariant"**
2. **Algebra:** `A2`
3. **Keep Nodes:** `1`
4. **Beta (Curve Class):** `1, 0`
5. **Insertions:** `pt | pt`
6. Click **Compute GW Invariant**.

*(Alternatively, from the CLI: `python3 -m gwflags.cli A2 --keep 1 gw --beta "1,0" --classes "pt|pt"`)*

---

## Task 3: Exploring Exceptional Groups and Spinors

The software fully supports exceptional groups ($G_2$, $F_4$, $E_6$, etc.) and Orthogonal/Symplectic groups.

**Example:** The flag variety $G_2/P_2$
- **Algebra:** `G2`
- **Keep Nodes:** `2`
- **Bundle:** Leave empty (for the flag variety itself) or specify `O(1)` for a hypersuface.

*(For a full guide on mapping these Lie algebra strings to standard geometric spaces, read our [Lie Algebras Guide](lie-algebras.md)).*
