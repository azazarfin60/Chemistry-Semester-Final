# ⚡ REVISION CHEATSHEET — Part 1 of 3
## Phases 01–04: The Four GUARANTEED Chapters (100% Exam Frequency)

> **Purpose:** Ultra-condensed revision for the Chemistry Semester Final. Read all 3 parts to cover the entire syllabus. Designed for a **quick 2–3 hour revision sprint**.

---

# 🔴 PHASE 01 — CHEMICAL KINETICS

## 1.1 Rate & Rate Law
- **Rate of Reaction** = Change in molar concentration per unit time: $\pm \frac{dC}{dt}$. Unit: $mol \cdot L^{-1} \cdot s^{-1}$
- **Rate Law** (experimental): $\text{Rate} = k[A]^x[B]^y$ — exponents are NOT necessarily stoichiometric coefficients
- **5 Factors affecting rate:** Nature of reactants, Surface area, Concentration (Law of Mass Action), Temperature (Maxwell-Boltzmann), Catalyst (alternate pathway, lower $E_a$)

## 1.2 Order vs Molecularity ⭐ (5/7 exams — MEMORIZE THE TABLE)

| Feature | Order | Molecularity |
|:--------|:------|:-------------|
| **Nature** | Experimental | Theoretical |
| **Values** | Integer, zero, fraction, negative | Always positive integer (1, 2, 3) |
| **Applies to** | Overall reaction | Elementary step only |
| **Derivation** | Cannot deduce from equation | Read from mechanism |
| **Conditions** | Can change (pseudo-order) | Fixed for a step |

**Pseudo-order:** When one reactant is in **large excess** → its concentration stays constant → absorbed into $k$.
- Example: Hydrolysis of ester: $Rate = k'[Ester]$ (pseudo-1st order because $[H_2O] \gg [Ester]$)

## 1.3 First-Order Reactions ⭐ (CRITICAL — derivation asked 4 times)

**Integrated Rate Equation:**
$$k = \frac{2.303}{t} \log \left( \frac{a}{a-x} \right)$$

**Between two time intervals** (asked 2024):
$$K = \frac{2.303}{t_2 - t_1} \log \frac{a-x_1}{a-x_2}$$

**Key Properties:**

| Property | Formula/Value |
|:---------|:-------------|
| Unit of k | time⁻¹ (e.g., s⁻¹) — independent of concentration |
| Half-life | t₁/₂ = 0.693 / k — **constant**, independent of *a* |
| Fractional time | t = (1/k) ln(1/(1−f)) — independent of *a* |
| 100% completion | t = ∞ → **never completed** |

**Quick tricks:**
- 75% completion = **2 half-lives** (50% → 25% remaining)
- 87.5% completion = **3 half-lives**
- 99% completion: $t_{99} = \frac{2.303 \times 2}{k}$

## 1.4 Second-Order Reactions ⭐ (4/7 exams)

**Type 1: $2A \rightarrow P$ (or $a = b$):**
$$k = \frac{1}{t} \cdot \frac{x}{a(a-x)}$$
- Half-life: $t_{1/2} = \frac{1}{ka}$ → **inversely proportional** to initial concentration
- Unit of $k$: $L \cdot mol^{-1} \cdot s^{-1}$

**Type 2: $A + B \rightarrow P$ (where $a \neq b$):**
$$k = \frac{1}{t(a-b)} \ln \frac{b(a-x)}{a(b-x)}$$
- Uses **partial fractions**: $\frac{1}{(a-x)(b-x)} = \frac{1}{a-b}\left[\frac{1}{b-x} - \frac{1}{a-x}\right]$

**Pseudo-1st order proof:** If $a \gg b$, then $(a-x) \approx a$ and $(a-b) \approx a$ → equation reduces to $k' = \frac{1}{t}\ln\frac{b}{b-x}$

## 1.5 Methods of Order Determination

| Method | How it works |
|:-------|:------------|
| **Integration** | Plug data into each order's equation; constant k = correct order |
| **Graphical** | Plot rate vs (a−x)ⁿ; straight line = order n |
| **Van't Hoff** | log(−dc/dt) vs log c; slope = order n |
| **Ostwald Isolation** | Keep all but one reactant in excess; find partial orders |
| **Half-life** | t₁/₂ ∝ 1/aⁿ⁻¹; slope of log(t₁/₂) vs log(a) = (1−n) |

## 1.6 Temperature & Arrhenius Equation
- **Temperature Coefficient:** $\frac{k_{T+10}}{k_T} \approx 2\text{–}3$ (10°C rise doubles/triples rate)
- **Why?** NOT more collisions — it's the **Maxwell-Boltzmann distribution** shifting → more molecules exceed $E_a$
- **Arrhenius Equation:** $k = Ae^{-E_a/RT}$
- **Two-temperature form:** $\ln\frac{k_2}{k_1} = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$

## 1.7 Activated Complex Theory
- Reactants → must acquire **Activation Energy** ($E_a$) → form unstable **Activated Complex** at energy peak → decompose to products (or back to reactants)
- **Catalyst** lowers $E_a$ but doesn't change $\Delta H$
- **Draw the PE diagram:** Label $E_R$, $E_P$, $E_a$, Activated Complex peak, $\Delta H$

---

# 🔴 PHASE 02 — CHEMICAL EQUILIBRIUM

## 2.1 Reversible Reactions ⭐ (7/7 exams)

| Feature | Reversible | Irreversible |
|:--------|:-----------|:------------|
| Direction | Both ($\rightleftharpoons$) | One ($\rightarrow$) |
| Completion | Never 100% | Goes to completion |
| Vessel | Closed | Open |
| Equilibrium | Attains dynamic eq. | Never |

**Chemical Equilibrium:** $R_f = R_b$ → no net macroscopic change, but reactions continue microscopically → **"dynamic"**

**6 Characteristics:** (1) $R_f = R_b$ (2) Constant properties (3) Dynamic nature (4) Same state from either direction (5) Closed system required (6) Catalyst doesn't change position, only speeds attainment

## 2.2 Law of Mass Action ⭐ (5/7 exams)
**Guldberg & Waage:** "Rate ∝ product of active masses, each raised to stoichiometric power."

For $aA + bB \rightleftharpoons cC + dD$:
$$K_c = \frac{[C]^c[D]^d}{[A]^a[B]^b} = \frac{k_f}{k_b}$$

**Active mass:** Molar concentration for solutions, partial pressure for gases, **unity (1) for pure solids/liquids**.

## 2.3 Equilibrium Constant Derivations ⭐ (4/7 exams)

**Three expressions:**
$$K_c = \frac{C_M^m C_N^n}{C_A^a C_B^b}, \quad K_p = \frac{P_M^m P_N^n}{P_A^a P_B^b}, \quad K_x = \frac{X_M^m X_N^n}{X_A^a X_B^b}$$

**Key Relations** (where $\Delta n = \text{moles products} - \text{moles reactants}$, gaseous only):
$$\boxed{K_p = K_c(RT)^{\Delta n}} \qquad \boxed{K_p = K_x P^{\Delta n}}$$

**If $\Delta n = 0$:** $K_p = K_c = K_x$

**PCl₅ Dissociation** (asked 2017, 2018):
$$PCl_5 \rightleftharpoons PCl_3 + Cl_2 \quad (1 \text{ mol} \rightarrow 1+\alpha \text{ total moles})$$
$$K_c = \frac{\alpha^2}{(1-\alpha)V} \qquad K_p = \frac{\alpha^2 P}{1-\alpha^2}$$

**NH₃ Synthesis** (asked 2024):
$$K_p = \frac{4x^2(a+b-2x)^2}{(a-x)(b-3x)^3 P^2}$$

> ⚠️ **Always draw the ICE table** (Initial, Change, Equilibrium) before every derivation!

## 2.4 Le Chatelier's Principle ⭐ (3/7 exams)

**Statement:** System at equilibrium shifts to counteract any imposed change.

| Change | System Response |
|:-------|:---------------|
| ↑ Concentration (reactant) | Shifts → forward |
| ↑ Pressure | Shifts toward **fewer gas moles** |
| ↑ Temperature | Shifts toward **endothermic** direction |
| Catalyst | **NO shift** — only faster attainment |

**Haber Process** ($N_2 + 3H_2 \rightleftharpoons 2NH_3$, $\Delta H = -92.4$ kJ):
- **Temp:** Compromise **450–500°C** (low temp = high yield but slow rate)
- **Pressure:** **200–250 atm** (4 moles → 2 moles, high P favors forward)
- **Catalyst:** Finely divided **Fe** with **Mo** promoter
- Excess $N_2 + H_2$ pumped in; $NH_3$ continuously removed by liquefaction

## 2.5 Gibbs Free Energy

**Reaction Isotherm:**
$$\boxed{\Delta G^\circ = -2.303\,RT\log K_p}$$
- $\Delta G^\circ \ll 0$ → $K_p \gg 1$ (products favored, spontaneous)
- $\Delta G^\circ \gg 0$ → $K_p \ll 1$ (reactants favored)
- At equilibrium: $\Delta G = 0$ (NOT $\Delta G^\circ = 0$!)

**Van't Hoff Equation** (Temperature dependence of $K$):
$$\log\frac{K_{p2}}{K_{p1}} = \frac{\Delta H^\circ}{2.303R}\left(\frac{T_2 - T_1}{T_1 T_2}\right)$$

## 2.6 The $K_p$ Numerical ⭐ (asked 2018, 2019)
**Problem:** $\Delta G^\circ = -20 \text{ kcal/mol}$, $T = 25°C$. Find $K_p$.
- Convert: $-20 \text{ kcal} = -20{,}000 \text{ cal}$; use $R = 1.987 \text{ cal/K·mol}$; $T = 298.15$ K
- $\log K_p = \frac{20000}{2.303 \times 1.987 \times 298.15} = 14.659$
- **$K_p = 4.56 \times 10^{14}$**

---

# 🔴 PHASE 03 — CHEMICAL BONDING

## 3.1 Types of Chemical Bonds ⭐ (5/7 exams)

**Chemical Bond:** Attractive force holding atoms together to achieve stable noble gas configuration.

**Strong bonds:** Ionic (transfer), Covalent (sharing), Coordinate (one-sided sharing), Metallic (electron sea)
**Weak bonds:** Hydrogen bond (F, O, N...H), van der Waals forces

**Ionic bond conditions:** Low IE (metal) + High EA (non-metal) + High Lattice Energy + $\Delta EN > 1.7$
**Covalent bond conditions:** High IE + High EA + $\Delta EN < 1.7$

## 3.2 Ionic vs Covalent ⭐ (4/7 exams — MEMORIZE THIS TABLE)

| Property | Ionic | Covalent |
|:---------|:------|:---------|
| **State** | Hard crystalline solids | Gases, liquids, soft solids |
| **MP/BP** | Very high (strong lattice) | Low (weak intermolecular forces) |
| **Solubility** | Polar solvents (water) | Non-polar solvents (benzene) |
| **Conductivity** | ✗ solid, ✓ molten/aqueous (mobile ions) | ✗ all states (no free ions) |
| **Directionality** | Non-directional | Highly directional |

**Dissolution rule:** Hydration Energy > Lattice Energy → dissolves (e.g., NaCl). Hydration < Lattice → insoluble (e.g., BaSO₄).

## 3.3 Intermolecular Forces
- **H-bonding:** F, O, N bonded to H → strong dipole-dipole (explains high BP of water)
- **van der Waals:** London dispersion (all molecules), dipole-dipole, dipole-induced dipole

## 3.4 Hybridization & VSEPR ⭐

**σ vs π bonds:**

| Feature | σ (sigma) | π (pi) |
|:--------|:----------|:-------|
| Overlap | Head-on (axial) | Lateral (sideways) |
| Strength | Strong | Weak |
| Rotation | Free | Restricted |
| Independence | Can exist alone | Only after σ exists |

**VSEPR Repulsion Order:** LP–LP > LP–BP > BP–BP

| Molecule | Hybrid | LP | Geometry | Bond Angle |
|:---------|:-------|:---|:---------|:-----------|
| CH₄ | sp³ | 0 | Tetrahedral | 109°28' |
| NH₃ | sp³ | 1 | Trigonal Pyramidal | 107° |
| H₂O | sp³ | 2 | Bent/V-shape | 104.5° |

## 3.5 Molecular Orbital Theory (MOT) ⭐ (Rising trend 2023–2024)

**Key postulates:** LCAO method → atomic orbitals combine → Bonding MO (lower energy, additive) + Antibonding MO* (higher energy, subtractive)

**Bond Order:**
$$\boxed{B.O. = \frac{N_b - N_a}{2}}$$
- B.O. = 0 → molecule doesn't exist | B.O. > 0 → stable | Unpaired electrons → paramagnetic

**VBT vs MOT** (asked 2024):

| Feature | VBT | MOT |
|:--------|:----|:----|
| Electrons | Localized | Delocalized (whole molecule) |
| Identity | Atoms keep identity | Atoms lose identity |
| Method | Overlapping, hybridization | LCAO → BMO + ABMO |
| O₂ magnetism | ✗ Fails (predicts diamagnetic) | ✓ Correctly predicts paramagnetic |

## 3.6–3.7 MO Diagrams & Metallic Bond
- **Key MO diagrams to know:** O₂ (B.O.=2, paramagnetic), N₂ (B.O.=3, diamagnetic), CO, NO
- **Metallic bond:** Positive kernels + delocalized electron sea → explains conductivity, malleability, lustre
- **Band Theory:** Valence band, conduction band, band gap → conductor/semiconductor/insulator

---

# 🔴 PHASE 04 — COLLIGATIVE PROPERTIES & SOLUTIONS

## 4.1 Raoult's Law & Vapor Pressure Lowering
$$P = P^\circ \cdot X_{\text{solvent}} = P^\circ(1 - X_{\text{solute}})$$
$$\frac{\Delta P}{P^\circ} = X_{\text{solute}} = \frac{n_2}{n_1 + n_2}$$
- **Relative lowering** of VP = mole fraction of solute (for non-volatile, non-electrolyte solute)
- VP lowering is a **colligative property** — depends only on number of particles

## 4.2–4.3 BP Elevation & FP Depression
$$\Delta T_b = K_b \cdot m \qquad \Delta T_f = K_f \cdot m$$
- $K_b, K_f$ = molal constants (depend on solvent only)
- **Molecular weight from colligative:** $M_2 = \frac{K \cdot W_2 \cdot 1000}{\Delta T \cdot W_1}$

## 4.4 Osmotic Pressure ⭐ (8/7 exams — THE MOST TESTED TOPIC)

**Osmosis:** Solvent moves through semi-permeable membrane from low → high solute concentration.

**Osmotic Pressure ($\pi$):** External pressure needed to stop osmosis.

**Van't Hoff Equation:**
$$\boxed{\pi = CRT}$$
where $C$ = **Molarity** (mol/L), $R = 0.0821$ L·atm/K·mol, $T$ = Kelvin

**Molecular weight from osmotic pressure:**
$$M = \frac{W \cdot R \cdot T}{\pi \cdot V}$$

**Definitions:**
- **Reverse Osmosis:** Apply $P > \pi$ → forces solvent OUT of concentrated solution (desalination)
- **Isotonic Solutions:** Same $\pi$ → no net flow ($\pi_1 = \pi_2 \implies C_1 = C_2$)

**Berkeley & Hartley Method:** External pressure applied via piston until capillary meniscus stops → reading = $\pi$

## 4.5 The 5% Glucose Numerical ⭐⭐ (Appeared 2019, 2020, 2021, 2023)

**MEMORIZE THIS SOLUTION:**
- "5% solution" = 5 g in 100 mL = 5 g in 0.1 L
- $M_{\text{glucose}} = 180$ g/mol
- $n = 5/180 = 0.02778$ mol → $C = 0.02778/0.1 = 0.2778$ M
- At 18°C: $\pi = 0.2778 \times 0.0821 \times 291.15 = \mathbf{6.64 \text{ atm}}$
- At 20°C: $\pi = 0.2778 \times 0.0821 \times 293.15 = \mathbf{6.68 \text{ atm}}$

**Abnormal Colligative — Van't Hoff Factor ($i$):**
- $i > 1$ → dissociation (NaCl → Na⁺ + Cl⁻, $i ≈ 2$)
- $i < 1$ → association (acetic acid dimers in benzene)
- $i = 1$ → normal (glucose, sucrose)

---

> **End of Part 1.** Continue to [Part 2](Revision_Cheatsheet_Part2.md) for Phases 05–08 (Atomic Structure, Thermochemistry, Electrochemistry, Solutions).
