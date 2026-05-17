[🏠 Index](00-index.md)

---

# 📐 All Formulas — Quick Reference

> A single-page collection of every mathematical formula from the boss_notes, organized by chapter. Use this for rapid revision before the exam.

---

## Chapter 1 — Chemical Kinetics

### Rate Law
$$\text{Rate} = k[A]^x[B]^y$$

### First-Order Rate Constant
$$k = \frac{2.303}{t} \log \left(\frac{a}{a-x}\right)$$

**General form (between two time points):**
$$K = \frac{2.303}{t_2 - t_1} \log \frac{a-x_1}{a-x_2}$$

### First-Order Half-Life
$$t_{1/2} = \frac{0.693}{k}$$

### Time for Fractional Completion (First Order)
$$t = \frac{1}{k} \ln \left( \frac{1}{1 - f} \right)$$

### Second-Order Rate Constant (Equal Concentrations, $a = b$)
$$k = \frac{1}{t} \left[ \frac{x}{a(a - x)} \right]$$

### Second-Order Rate Constant (Unequal Concentrations, $a \neq b$)
$$k = \frac{1}{t(a-b)} \ln \left[ \frac{b(a-x)}{a(b-x)} \right]$$

### Order Determination — Differential Method
$$\log\left(-\frac{dc}{dt}\right) = \log k + n \log c$$

$$n = \frac{\log(r_1) - \log(r_2)}{\log(c_1) - \log(c_2)}$$

### Order Determination — Half-Life Method
$$t_{1/2} \propto \frac{1}{a^{n-1}}$$

$$n = 1 + \frac{\log(t_{1/2})_1 - \log(t_{1/2})_2}{\log a_2 - \log a_1}$$

### Arrhenius Equation
$$k = A \cdot e^{-E_a / RT}$$

---

## Chapter 2 — Chemical Equilibrium

### Equilibrium Constants ($K_c$, $K_p$, $K_x$)
$$K_c = \frac{[M]^m [N]^n}{[A]^a [B]^b}$$

$$K_p = \frac{P_M^m P_N^n}{P_A^a P_B^b}$$

$$K_x = \frac{X_M^m X_N^n}{X_A^a X_B^b}$$

### Relation Between $K_p$ and $K_c$
$$K_p = K_c (RT)^{\Delta n}$$
*Where $\Delta n = (m+n) - (a+b)$ = moles of gaseous products − moles of gaseous reactants.*

### Relation Between $K_p$ and $K_x$
$$K_p = K_x P^{\Delta n}$$

### Partial Pressure (Mole Fraction Method)
$$p_i = X_i \times P = \left(\frac{n_i}{n_{total}}\right) \times P$$

### $K_p$ for $N_2 + 3H_2 \rightleftharpoons 2NH_3$
$$K_p = \frac{4x^2 (a + b - 2x)^2}{(a - x)(b - 3x)^3 P^2}$$

### $K_c$ and $K_p$ for $PCl_5$ Dissociation
$$K_c = \frac{\alpha^2}{(1 - \alpha)V}$$

$$K_p = \frac{\alpha^2 P}{1 - \alpha^2}$$

### Gibbs Free Energy and Equilibrium
$$\Delta G = \Delta G^\circ + RT \ln Q$$

$$\Delta G^\circ = -2.303 RT \log K_p$$

### Van't Hoff Equation
$$\log \left( \frac{K_{p2}}{K_{p1}} \right) = \frac{\Delta H^\circ}{2.303 R} \left( \frac{T_2 - T_1}{T_1 T_2} \right)$$

---

## Chapter 3 — Chemical Bonding

### Bond Order (Molecular Orbital Theory)
$$B.O. = \frac{N_b - N_a}{2}$$
*Where $N_b$ = electrons in bonding MOs, $N_a$ = electrons in anti-bonding MOs.*

---

## Chapter 4 — Colligative Properties

### Raoult's Law (Ideal Solutions)
$$P_A = P_A^\circ \cdot x_A$$

### Relative Lowering of Vapor Pressure
$$\frac{P_o - P}{P_o} = \frac{n}{n + N} \approx \frac{n}{N} \quad \text{(for dilute solutions)}$$

### Molecular Weight from Vapor Pressure Lowering
$$M_2 = \frac{w_2 \cdot M_1 \cdot P_o}{w_1(P_o - P)}$$

### Boiling Point Elevation
$$\Delta T_b = K_b \cdot m$$

$$\Delta T_b = \frac{1000 \cdot K_b \cdot w_2}{M_2 \cdot w_1}$$

### Freezing Point Depression
$$\Delta T_f = K_f \cdot m$$

$$M_2 = \frac{1000 \cdot K_f \cdot w_2}{\Delta T_f \cdot w_1}$$

### Osmotic Pressure
$$\pi = CRT$$

$$\pi V = nRT$$

$$M = \frac{W \cdot R \cdot T}{\pi \cdot V}$$

### Van't Hoff Factor
$$i = \frac{\text{Observed Colligative Property}}{\text{Calculated (Normal) Colligative Property}}$$

---

## Chapter 5 — Atomic Structure

### Bohr's Quantization Condition
$$mvr = \frac{nh}{2\pi}$$

### Energy of Photon (Transition)
$$\Delta E = E_{higher} - E_{lower} = h\nu$$

### Schrödinger Wave Equation
$$\frac{\partial^2\psi}{\partial x^2} + \frac{\partial^2\psi}{\partial y^2} + \frac{\partial^2\psi}{\partial z^2} + \frac{8\pi^2m}{h^2}(E - V)\psi = 0$$

### de Broglie Wavelength
$$\lambda = \frac{h}{mv} = \frac{h}{p}$$

---

## Chapter 6 — Thermochemistry

### Hess's Law
$$\Delta H = \Delta H_1 + \Delta H_2 + \Delta H_3$$

### First Law of Thermodynamics
$$q = \Delta E + W$$

### Heat at Constant Volume
$$q_v = \Delta E$$

### Heat at Constant Pressure (Enthalpy)
$$q_p = \Delta H$$

### Relation Between $\Delta H$ and $\Delta E$
$$\Delta H = \Delta E + \Delta n_g RT$$

### Kirchhoff's Equation
$$\frac{\Delta H_2 - \Delta H_1}{T_2 - T_1} = \Delta C_p$$

### Bomb Calorimeter — Heat Absorbed
$$q_v = (W_w + w_c) \times s \times \Delta T$$

### Enthalpy of Combustion from Internal Energy
$$\Delta H_c = \Delta U + \Delta n_g RT$$

### Enthalpy of Reaction from Formation Enthalpies
$$\Delta H_{rxn} = \sum \Delta H_f(\text{Products}) - \sum \Delta H_f(\text{Reactants})$$

---

## Chapter 7 — Electrochemistry

### Faraday's First Law
$$W = Z \cdot I \cdot t$$
*Where $W$ = mass deposited, $Z$ = electrochemical equivalent, $I$ = current, $t$ = time.*

### Faraday's Second Law
$$\frac{W_1}{W_2} = \frac{E_1}{E_2}$$

### Kohlrausch's Law (Limiting Molar Conductivity)
$$\Lambda^\circ_{\text{eq}} = \lambda^\circ_+ + \lambda^\circ_-$$

### Molar Conductivity from Specific Conductivity
$$\Lambda_v = \kappa \times \frac{1000}{C}$$

### Degree of Dissociation
$$\alpha = \frac{\Lambda_v}{\Lambda^\circ}$$

### Ionic Product of Water (from Conductance)
$$K_w = \left[ \frac{1000 \cdot \kappa}{\lambda^\circ_{H^+} + \lambda^\circ_{OH^-}} \right]^2$$

### Nernst Equation (General Form)
$$E = E^\circ - \frac{RT}{nF} \ln \frac{[\text{Reduced state}]}{[\text{Oxidized state}]}$$

### Nernst Equation (at 25°C)
$$E_{cell} = E^\circ_{cell} - \frac{0.0591}{n} \log \frac{[\text{Anode Ion}]}{[\text{Cathode Ion}]}$$

### Standard Cell EMF
$$E^\circ_{cell} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}}$$

### Debye-Hückel-Onsager Equation
$$\Lambda_c = \Lambda_0 - (A + B\Lambda_0)\sqrt{c}$$

### Ionic Strength
$$I = \frac{1}{2} \sum m_i z_i^2$$

### Debye-Hückel Limiting Law (Activity Coefficient)
$$\log \gamma_i = -0.509 \, z_i^2 \sqrt{I}$$

---

## Chapter 8 — Solutions

### Henry's Law
$$p = K_H \cdot x$$

### Volume of Dissolved Gas (from Henry's Law + Ideal Gas)
$$V = \frac{kRT}{M}$$

### Molality
$$m = \frac{w_2 \times 1000}{M_2 \times w_1}$$

---

## Chapter 9 — Periodic Table

### Effective Nuclear Charge
$$Z_{eff} = Z - \sigma$$

### Pauling's Electronegativity
$$X_A - X_B = 0.208 \sqrt{\Delta}$$

$$\Delta = E_{A-B} - \sqrt{E_{A-A} \times E_{B-B}}$$

*If $\Delta$ is in kJ/mol, use $0.1017$ instead of $0.208$.*

---

## Chapter 10 — Acid-Base & pH

### Ionic Product of Water
$$K_w = [H^+][OH^-] = 1.0 \times 10^{-14} \text{ mol}^2/\text{L}^2$$

### pH and pOH
$$pH = -\log_{10}[H^+]$$

$$pOH = -\log_{10}[OH^-]$$

$$pH + pOH = 14$$

### Henderson-Hasselbalch Equation (Acidic Buffer)
$$pH = pK_a + \log \frac{[\text{Salt}]}{[\text{Acid}]}$$

---

[🏠 Index](00-index.md)
