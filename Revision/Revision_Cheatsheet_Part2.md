# ⚡ REVISION CHEATSHEET — Part 2 of 3
## Phases 05–08: Very Likely + Likely Chapters

---

# 🟠 PHASE 05 — ATOMIC STRUCTURE (71% exam frequency)

## 5.1 Bohr's Atomic Model ⭐ (3/7 exams)

**Postulates:**
1. Electrons revolve in fixed circular orbits (shells) around the nucleus without radiating energy
2. Each orbit has a definite energy → **stationary states** (quantized)
3. Angular momentum is quantized: $mvr = \frac{nh}{2\pi}$ (where $n = 1, 2, 3...$)
4. Energy is emitted/absorbed ONLY when electron jumps between orbits: $\Delta E = E_2 - E_1 = h\nu$

**Key equations:**
$$r_n = \frac{n^2 h^2}{4\pi^2 m k Z e^2} = 0.529 \times \frac{n^2}{Z} \text{ Å}$$
$$E_n = -\frac{2\pi^2 m k^2 Z^2 e^4}{n^2 h^2} = -13.6 \times \frac{Z^2}{n^2} \text{ eV}$$

**Limitations:**
1. Cannot explain spectra of multi-electron atoms (only works for H-like species)
2. Cannot explain fine structure (splitting of spectral lines)
3. Cannot explain Zeeman effect (magnetic field splitting) or Stark effect (electric field splitting)
4. Violates Heisenberg's Uncertainty Principle (treats electron as particle with definite orbit)
5. Cannot explain chemical bonding or molecular formation

## 5.2 Quantum Numbers ⭐ (3/7 exams)

| Quantum # | Symbol | Values | Significance |
|:-----------|:-------|:-------|:------------|
| **Principal** | $n$ | 1, 2, 3, ... | Shell, size, energy level |
| **Azimuthal** | $l$ | 0 to $(n-1)$ | Subshell, shape (s=0, p=1, d=2, f=3) |
| **Magnetic** | $m_l$ | $-l$ to $+l$ | Orientation of orbital in space |
| **Spin** | $m_s$ | $+\frac{1}{2}$ or $-\frac{1}{2}$ | Spin direction of electron |

**For $n = 4$:** $l$ = 0,1,2,3 → subshells: 4s, 4p, 4d, 4f
- Total orbitals = $n^2 = 16$
- Total electrons = $2n^2 = 32$

## 5.3 Electronic Configuration Rules

| Rule | Statement |
|:-----|:---------|
| **Aufbau** | Fill lowest energy orbital first; order by $(n+l)$ value, then lower $n$ first |
| **Pauli Exclusion** | Max 2 electrons per orbital, with opposite spins |
| **Hund's Rule** | In degenerate orbitals, singly occupy each before pairing |

**Filling order:** 1s → 2s → 2p → 3s → 3p → 4s → 3d → 4p → 5s → 4d → 5p → 6s → 4f → 5d → 6p → 7s → 5f → 6d → 7p

**Why 4s fills before 3d:** 4s has $(n+l) = 4+0 = 4$; 3d has $(n+l) = 3+2 = 5$. Lower $(n+l)$ fills first.

## 5.4 Atomic Spectra ⭐

- **Emission spectrum:** Electron drops from higher to lower orbit → emits photon → bright lines on dark background
- **Absorption spectrum:** Electron absorbs photon → jumps up → dark lines on bright background (exact complement of emission)
- **Line spectrum:** From individual atoms (e.g., H, Na) — sharp, discrete lines
- **Band spectrum:** From molecules — closely spaced lines merging into bands (due to vibrational + rotational energy levels)

## 5.5 Wave Mechanics

**de Broglie equation** (matter has wave nature):
$$\lambda = \frac{h}{mv} = \frac{h}{p}$$

**Heisenberg Uncertainty Principle:**
$$\Delta x \cdot \Delta p \geq \frac{h}{4\pi}$$
(Cannot simultaneously know exact position AND momentum of an electron)

**Schrödinger Wave Equation:**
$$\frac{\partial^2 \psi}{\partial x^2} + \frac{\partial^2 \psi}{\partial y^2} + \frac{\partial^2 \psi}{\partial z^2} + \frac{8\pi^2 m}{h^2}(E - V)\psi = 0$$
- $\psi$ = wave function; $|\psi|^2$ = probability density of finding electron

## 5.6 Orbit vs Orbital ⭐ (asked 2023)

| Feature | Orbit (Bohr) | Orbital (QM) |
|:--------|:-------------|:-------------|
| **Nature** | Well-defined circular path | 3D probability region ($|\psi|^2$) |
| **Shape** | Always circular | s(sphere), p(dumbbell), d(clover), f(complex) |
| **Electrons** | Can hold $2n^2$ | Max 2 electrons |
| **Principle** | Violates uncertainty | Consistent with uncertainty |
| **Applicability** | Only H-like atoms | All atoms |

---

# 🟠 PHASE 06 — THERMOCHEMISTRY (86% exam frequency)

## 6.1 Laws of Thermochemistry ⭐

**Lavoisier-Laplace Law:** Heat evolved in formation = heat absorbed in decomposition (opposite signs).

**Hess's Law** ⭐ (asked 2024):
> "Total $\Delta H$ is the same whether reaction occurs in 1 step or multiple steps (same initial & final states)."

$$\Delta H = \Delta H_1 + \Delta H_2 + \Delta H_3$$

- **Why?** Enthalpy is a **state function** (path-independent)
- **Draw the cycle diagram** for full marks: Direct path ($\Delta H$) vs indirect path ($\Delta H_1 + \Delta H_2 + \Delta H_3$)

## 6.2 Types of Heat of Reaction ⭐ (4/7 exams)

| Type | Definition |
|:-----|:----------|
| **Heat of Formation** | Heat change when 1 mole of compound formed from elements in standard states |
| **Heat of Combustion** | Heat change when 1 mole of substance completely burns in excess O₂ |
| **Heat of Neutralization** | Heat change when 1 g-eq of acid neutralizes 1 g-eq of base. Strong+Strong = **−13.7 kcal/mol** |
| **Heat of Solution** | Heat change when 1 mole of solute dissolves in excess solvent |

## 6.3 Enthalpy Derivation

From 1st Law of Thermodynamics: $\Delta U = q - W$
- At constant volume: $q_V = \Delta U$
- At constant pressure: $q_P = \Delta U + P\Delta V = \Delta H$ (Enthalpy)
- **Relation:** $\Delta H = \Delta U + \Delta n_g RT$ (where $\Delta n_g$ = change in gaseous moles)
- If $\Delta n_g = 0$: $\Delta H = \Delta U$

## 6.4 Kirchhoff's Equation ⭐

**Effect of temperature on heat of reaction:**
$$\Delta H_2 - \Delta H_1 = \Delta C_p (T_2 - T_1) \quad \text{(constant pressure)}$$
$$\Delta U_2 - \Delta U_1 = \Delta C_v (T_2 - T_1) \quad \text{(constant volume)}$$
- $\Delta C_p = \sum C_p(\text{products}) - \sum C_p(\text{reactants})$

## 6.5 Bomb Calorimeter
- Measures $\Delta U$ (constant volume), NOT $\Delta H$ directly
- Convert: $\Delta H = \Delta U + \Delta n_g RT$
- **Hess's Law numerical:** $\Delta H_{\text{rxn}} = \sum \Delta H_c(\text{reactants}) - \sum \Delta H_c(\text{products})$

---

# 🟠 PHASE 07 — ELECTROCHEMISTRY (86% exam frequency)

## 7.1 Conductors & Electrolytes

| Type | Carrier | Examples |
|:-----|:--------|:--------|
| **Metallic (electronic)** | Electrons | Cu, Ag, graphite |
| **Electrolytic (ionic)** | Ions | NaCl(aq), HCl(aq) |

- **Strong electrolytes:** Completely dissociate (NaCl, HCl, NaOH)
- **Weak electrolytes:** Partially dissociate (CH₃COOH, NH₄OH)

## 7.2 Mechanism of Electrolytic Conduction ⭐ (4/7 exams)

**4 Steps:**
1. **Ion Availability:** Dissolving/melting breaks lattice → ions free
2. **Potential Applied:** DC creates electric field across solution
3. **Migration:** Cations → Cathode (−), Anions → Anode (+)
4. **Redox at Electrodes:** Cations reduced at cathode, Anions oxidized at anode

**Electrolysis of aqueous NaCl:**
- Cathode: $2H^+ + 2e^- \rightarrow H_2$ (H⁺ reduced, not Na⁺ — lower reduction potential)
- Anode: $2Cl^- \rightarrow Cl_2 + 2e^-$ (Cl⁻ oxidized, not OH⁻ — due to **overvoltage**)
- Solution becomes alkaline (NaOH accumulates)

## 7.3 Faraday's Laws ⭐ (3/7 exams)

**1st Law:** $W = Z \cdot I \cdot t$ (mass ∝ total charge)
- $Z$ = electrochemical equivalent (g/C)
- $Z = E/F$ where $F = 96485$ C/mol (Faraday constant)

**2nd Law:** Same charge → masses ∝ equivalent weights
$$\frac{W_1}{W_2} = \frac{E_1}{E_2}$$

**1 Faraday** = 96,485 C = charge of 1 mol electrons → deposits 1 gram-equivalent weight

> ⚠️ Always convert time to **seconds** before using $W = ZIt$!

## 7.4 Conductance & Kohlrausch

| Term | Symbol | Definition | Unit |
|:-----|:-------|:-----------|:-----|
| **Specific Conductance** | $\kappa$ | Conductance of 1 cm³ cube | S/cm |
| **Equivalent Conductance** | $\Lambda_{eq}$ | $\kappa \times 1000/C_N$ | S·cm²/eq |
| **Molar Conductance** | $\Lambda_m$ | $\kappa \times 1000/C_M$ | S·cm²/mol |

**Kohlrausch's Law:** At infinite dilution, $\Lambda_0$ = sum of individual ionic conductances:
$$\Lambda_0 = \lambda_0^+ + \lambda_0^-$$

**Application:** Calculate $\Lambda_0$ for weak electrolytes (CH₃COOH) from strong electrolytes:
$$\Lambda_0(CH_3COOH) = \Lambda_0(CH_3COONa) + \Lambda_0(HCl) - \Lambda_0(NaCl)$$

## 7.5 Electrochemical Cells & Nernst Equation ⭐ (Rising trend)

**Galvanic vs Electrolytic:**

| Feature | Galvanic | Electrolytic |
|:--------|:---------|:------------|
| Energy | Chemical → Electrical | Electrical → Chemical |
| Spontaneity | $\Delta G < 0$ (spontaneous) | $\Delta G > 0$ (forced) |
| Anode polarity | Negative | Positive |

**Nernst Equation** (at 25°C):
$$\boxed{E_{cell} = E^\circ_{cell} - \frac{0.0591}{n}\log\frac{[\text{Anode ion}]}{[\text{Cathode ion}]}}$$

- $E^\circ_{cell} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}}$
- Pure solids have activity = 1
- **Relation with Gibbs:** $\Delta G^\circ = -nFE^\circ$

## 7.6 Debye-Hückel Theory ⭐ (3/7 exams)

**4 Assumptions of strong electrolytes:**
1. **Complete ionization** in solution
2. Strong **electrostatic interactions** between ions
3. Each ion surrounded by an **ionic atmosphere** of opposite charge
4. **Retardation effects:** Relaxation effect + Electrophoretic effect slow ions

**Debye-Hückel-Onsager Equation:**
$$\Lambda_c = \Lambda_0 - (A + B\Lambda_0)\sqrt{c}$$
- Explains why conductance decreases with concentration for strong electrolytes
- $A$ = relaxation effect; $B\Lambda_0$ = electrophoretic effect

**Ionic Strength:**
$$\mu = \frac{1}{2}\sum c_i z_i^2$$

**Activity coefficient** ($\gamma$): $\log \gamma_\pm = -A|z_+ z_-|\sqrt{\mu}$

---

# 🟠 PHASE 08 — SOLUTIONS (100% combined with Phase 04)

## 8.1 Solution Definitions ⭐ (4/7 exams)

**Solution:** A homogeneous mixture of two or more substances.

**9 Types of solutions** (by physical state):

| Solute State | Solvent State | Example |
|:-------------|:-------------|:--------|
| Gas | Gas | Air (O₂ in N₂) |
| Gas | Liquid | Soda water (CO₂ in H₂O) |
| Gas | Solid | H₂ in Pd |
| Liquid | Liquid | Alcohol in water |
| Liquid | Gas | Water vapor in air |
| Liquid | Solid | Hg in Au (amalgam) |
| Solid | Liquid | Sugar in water |
| Solid | Solid | Cu in Au (alloy) |
| Solid | Gas | Camphor in air |

**Concentration units:**

| Unit | Formula | Temp. dependent? |
|:-----|:--------|:----------------|
| **Molarity (M)** | mol solute / L solution | ✓ Yes (volume changes) |
| **Molality (m)** | mol solute / kg solvent | ✗ No (mass doesn't change) |
| **Normality (N)** | equivalents / L solution | ✓ Yes |
| **Mole fraction** | $X_i = n_i / \sum n$ | ✗ No |
| **ppm** | mg solute / kg solution | ✗ No |

> ⚠️ **Molality is temperature-independent** (uses mass); **Molarity is temperature-dependent** (uses volume, which expands/contracts).

## 8.2 Henry's Law ⭐ (4/7 exams)

**Statement:** "At constant temperature, the mass of gas dissolved in a definite volume of liquid is directly proportional to the pressure of the gas above the liquid."
$$m = k \cdot P \quad \text{or} \quad P = K_H \cdot X_{\text{gas}}$$

**Limitations:**
1. Only applies at **low pressures** (gas must not liquefy)
2. Temperature must remain **constant**
3. Gas must **NOT react** with solvent (e.g., HCl in water fails — it ionizes)
4. Gas must behave **ideally**

**Volume independence proof:** Using $PV = nRT$ and $m = kP$, the volume of dissolved gas at a given temperature is independent of pressure (pressure terms cancel).

## 8.3 Ideal vs Non-Ideal Solutions

| Feature | Ideal Solution | Non-Ideal Solution |
|:--------|:--------------|:-------------------|
| **Raoult's Law** | Obeyed exactly | Shows deviations |
| **ΔH_mix** | Zero | Non-zero (positive or negative) |
| **ΔV_mix** | Zero | Non-zero |
| **Interactions** | A-B same as A-A and B-B | A-B different from A-A or B-B |
| **Example** | Benzene + Toluene | Ethanol + Water (+ve deviation) |

- **Positive deviation:** Weaker A–B forces → VP higher than Raoult's → minimum boiling azeotrope
- **Negative deviation:** Stronger A–B forces → VP lower than Raoult's → maximum boiling azeotrope

## 8.4 Solubility & Temperature ⭐

**Solid in Liquid:**
- Most solids: solubility ↑ with temperature (endothermic dissolution)
- Some exceptions: $CaSO_4$, $Ce_2(SO_4)_3$ solubility ↓ with temperature

**Gas in Liquid:**
- Solubility ↓ with ↑ temperature (dissolution of gas is exothermic → Le Chatelier shifts backward)

**Supersaturation:** Unstable solution holding more solute than saturation allows. Adding a **seed crystal** triggers instant crystallization of excess solute.

---

> **End of Part 2.** Continue to [Part 3](Revision_Cheatsheet_Part3.md) for Phases 09–11 (Periodic Table, Acid-Base, Miscellaneous) + Final Exam Strategy.
