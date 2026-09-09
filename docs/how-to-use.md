# How to Use `gwflags`

This guide bridges the theoretical framework of the Quantum Cohomology of Complete Intersections in Flag Varieties with practical computation using the `gwflags` package. 

Because the software includes a built-in Graphical User Interface (GUI), you do not need to write Python code to compute these invariants. You can simply launch the local web app and use the interactive dashboard.

## Launching the Interface

To start the interface, open your terminal (inside the `atomicdecompositions` folder) and run:
```bash
python3 -m gwflags.gui
```
This will start a local server. Open your web browser to the provided `localhost` URL (usually `http://127.0.0.1:8000`).

## The Novikov Parameters

**Important Note on Eigenvalues:** When the software outputs eigenvalues or the full quantum multiplication matrix, it automatically sets the **Novikov parameters ($y_i$ or $q_i$) to $1$**. This complies with the standard conventions required to test Conjecture $\mathcal{O}$ and calculate the asymptotic spectrum of the quantum connection without bloating the output with large symbolic rings.

---

## Computing Individual Gromov-Witten Invariants

While the quantum matrices calculate the aggregate structural invariants, you can also use `gwflags` to compute single Gromov-Witten invariants directly.

**Example:** Computing the 2-point invariant $\langle pt, pt \rangle_{d=1} = 1$ on $\mathbb{P}^2$.

**In the GUI:**
1. Switch the operation mode from "Quantum Multiplication" to **"Single GW Invariant"**
2. **Algebra:** `A2` (representing $\mathbb{P}^2$)
3. **Keep Nodes:** `1`
4. **Beta (Curve Class):** `1, 0`
5. **Insertions:** `pt | pt`
6. Click **Compute GW Invariant**.

*(Alternatively, from the CLI: `python3 -m gwflags.cli A2 --keep 1 gw --beta "1,0" --classes "pt|pt"`)*

---

## Small Quantum Multiplication Examples

Below, we showcase how to input several prominent geometric spaces from the paper into the GUI to compute the projected flag-ambient part of small quantum multiplication by the first Chern class.

## The Novikov Parameters

**Important Note on Eigenvalues:** When the software outputs eigenvalues or the full quantum multiplication matrix, it automatically sets the **Novikov parameters ($y_i$ or $q_i$) to $1$**. This complies with the standard conventions required to calculate the spectrum of the quantum connection without bloating the output with large symbolic rings.

---

## Computing Individual Gromov-Witten Invariants

While the quantum matrices calculate the aggregate structural invariants, you can also use `gwflags` to compute single Gromov-Witten invariants directly.

**Example:** Computing the 2-point invariant $\langle pt, pt \rangle_{d=1} = 1$ on $\mathbb{P}^2$.

**In the GUI:**
1. Switch the operation mode from "Quantum Multiplication" to **"Single GW Invariant"**
2. **Algebra:** `A2` (representing $\mathbb{P}^2$)
3. **Keep Nodes:** `1`
4. **Beta (Curve Class):** `1, 0`
5. **Insertions:** `pt | pt`
6. Click **Compute GW Invariant**.

*(Alternatively, from the CLI: `python3 -m gwflags.cli A2 --keep 1 gw --beta "1,0" --classes "pt|pt"`)*

---

## Small Quantum Multiplication Examples

## 1. Cubic Fourfolds
**Theory:** $X = \mathcal{Z}(\mathbb{P}^5, \mathcal{O}_{\mathbb{P}^5}(3))$. 
The small quantum multiplication by $c_1(TX)$ yields an eigenvalue 0 with algebraic multiplicity 2 and geometric multiplicity 1 (Jordan defect 1). This is related to the rationality problem of Hodge-general cubic fourfolds and recovers uniform K3-center constraints.

**In the GUI:**
- **Algebra:** `A5` (representing $\mathbb{P}^5$)
- **Keep Nodes:** `1`
- **Bundle:** `O(3)`
- Click **Compute SQM** to generate the matrix and eigenvalues.

---

## 2. Küchle Fourfolds of type (c5)
**Theory:** $F = \text{Gr}(3,7)$, $X = \mathcal{Z}(F, \Lambda^2 \mathcal{U}^\vee \oplus \Lambda^3 \mathcal{Q} \oplus \mathcal{O}_F(1))$. 
This is a crucial counter-example where the ambient-completeness condition (AC) fails. 

**In the GUI:**
- **Algebra:** `A6` (representing $\text{Gr}(3,7)$)
- **Keep Nodes:** `3`
- **Bundle:** `osum(wedge(2, dual(taut_sub(X, 3))), wedge(3, taut_quot(X, 3)), O(X, 1))`
- Click **Compute SQM** to view the projected flag-ambient operator.

---

## 3. Ordinary Gushel–Mukai Fourfolds
**Theory:** $F = \text{Gr}(2,5)$, $X = \mathcal{Z}(F, \mathcal{O}_F(1) \oplus \mathcal{O}_F(2))$. 
The operator has 0 as a semisimple eigenvalue of multiplicity 2 (Jordan defect 0), plus four simple nonzero eigenvalues. 

**In the GUI:**
- **Algebra:** `A4` (representing $\text{Gr}(2,5)$)
- **Keep Nodes:** `2`
- **Bundle:** `osum(O(1), O(2))`
- Click **Compute SQM**.

---

## 4. Quartic Fourfolds
**Theory:** $X = \mathcal{Z}(\mathbb{P}^5, \mathcal{O}_{\mathbb{P}^5}(4))$. 
A Fano fourfold of index 2. The zero eigenvalue has algebraic multiplicity 3 and geometric multiplicity 1.

**In the GUI:**
- **Algebra:** `A5`
- **Keep Nodes:** `1`
- **Bundle:** `O(4)`

*(Alternatively, from the CLI: `python3 -m gwflags.cli A5 --keep 1 -K 4 sqm`)*

---

## 5. Intersections of a Quadric and a Cubic in $\mathbb{P}^6$
**Theory:** $X = \mathcal{Z}(\mathbb{P}^6, \mathcal{O}_{\mathbb{P}^6}(2) \oplus \mathcal{O}_{\mathbb{P}^6}(3))$. 

**In the GUI:**
- **Algebra:** `A6`
- **Keep Nodes:** `1`
- **Bundle:** `osum(O(2), O(3))`

*(Alternatively, from the CLI: `python3 -m gwflags.cli A6 --keep 1 -K "2;3" sqm`)*
