[⬅ 06-Thermochemistry](06-Thermochemistry.md) | [🏠 Index](index.md) | [08-Solutions ➡](08-Solutions.md)

---

# Electrochemistry
**Priority:** 🟠 HIGH | **Frequency:** 13 sub-parts across 5/7 exams + CT04

> **Topics Covered:** Electrolytes classification, electrolytic conduction, Faraday's laws, Nernst equation, electrochemical vs electrolytic cells, Debye-Hückel theory, conductance, Kohlrausch's law, activity coefficients.

---

## 📄 Source: 2024 Exam

### Q.7(a) Define electronic conductors and electrolytic conductors with suitable examples of each. (03)

**Answer:**

**Electronic (Metallic) Conductors:**
These are substances that conduct electricity through the flow of free, delocalized electrons without undergoing any chemical decomposition. The conductivity generally decreases with an increase in temperature due to increased lattice vibrations hindering electron flow.
*   **Examples:** All metals (e.g., Copper, Silver, Iron), alloys, and graphite.

**Electrolytic Conductors (Electrolytes):**
These are substances that conduct electricity in their molten state or in an aqueous solution through the movement of ions (cations and anions). The conduction process is accompanied by the physical transfer of matter and a chemical decomposition at the electrodes (electrolysis). Their conductivity generally increases with temperature due to increased ion mobility.
*   **Examples:** Aqueous solutions of acids ($HCl$, $H_2SO_4$), bases ($NaOH$, $KOH$), and salts ($NaCl$, $CuSO_4$); fused/molten salts.

---

---

### Q.7(b) Discuss the mechanism of electrolytic conduction with proper terms and reactions of electrolysis of aqueous solution of NaCl. (04)

**Answer:**

**Mechanism of Electrolytic Conduction:**
According to Arrhenius' theory of electrolytic dissociation, when an electrolyte is dissolved in a solvent like water, it splits into positively charged ions (cations) and negatively charged ions (anions). This process is called **ionization**. 
When an electric potential difference is applied across two electrodes dipped in this solution, the ions experience an electrostatic force. The positively charged cations migrate towards the negatively charged electrode (the **cathode**), and the negatively charged anions migrate towards the positively charged electrode (the **anode**). This directed movement of ions constitutes the electric current within the solution.

At the electrodes, ions undergo redox reactions (chemical decomposition):
*   **At Cathode:** Cations gain electrons and are reduced.
*   **At Anode:** Anions lose electrons and are oxidized.

**Electrolysis of Aqueous Solution of NaCl:**
In an aqueous solution of NaCl, there are four types of ions present due to the dissociation of NaCl and the weak ionization of water:
1.  From NaCl: $Na^+$ and $Cl^-$
2.  From $H_2O$: $H^+$ and $OH^-$

When current is passed, two competing reactions can happen at each electrode.
*   **At the Cathode (Reduction):** Both $Na^+$ and $H^+$ migrate here. Since the standard reduction potential of $H^+$ ($0.00 \text{ V}$) is much higher than that of $Na^+$ ($-2.71 \text{ V}$), $H^+$ ions are preferentially reduced to form hydrogen gas.
    $$2H^+(aq) + 2e^- \rightarrow H_2(g)$$
*   **At the Anode (Oxidation):** Both $Cl^-$ and $OH^-$ migrate here. Although the oxidation potential of $OH^-$ is slightly higher, due to the phenomenon of "overvoltage" required to liberate $O_2$ gas from water, $Cl^-$ is preferentially oxidized to form chlorine gas.
    $$2Cl^-(aq) \rightarrow Cl_2(g) + 2e^-$$

**Overall Result:**
Hydrogen gas is liberated at the cathode, chlorine gas is liberated at the anode, and the solution gradually becomes alkaline due to the accumulation of $Na^+$ and $OH^-$ ions (forming $NaOH$).

---

---

### Q.7(c) Calculate the standard electrode potential of $Ni^{2+}/Ni$ electrode, if the cell potential of the following cell is 0.59 V.
$Ni | Ni^{2+} (0.01 M) || Cu^{2+} | Cu$ (03)

**Answer:**

**Given Data:**
*   Cell Representation: $Ni(s) | Ni^{2+} (0.01 \text{ M}) || Cu^{2+} (aq) | Cu(s)$
*   Cell Potential, $E_{cell} = 0.59 \text{ V}$
*   Concentration of $Ni^{2+}$, $[Ni^{2+}] = 0.01 \text{ M}$
*   *Assumption:* Since the concentration of $Cu^{2+}$ is not specified, we assume standard state conditions for it: $[Cu^{2+}] = 1 \text{ M}$. We also use the known standard reduction potential for copper, $E^\circ_{Cu^{2+}/Cu} = +0.34 \text{ V}$.

**To Find:**
*   Standard electrode potential of Nickel, $E^\circ_{Ni^{2+}/Ni}$

**Solution:**
From the cell representation, Oxidation (Anode) occurs at Nickel, and Reduction (Cathode) occurs at Copper.
*   **Anode Reaction:** $Ni(s) \rightarrow Ni^{2+}(aq) + 2e^-$
*   **Cathode Reaction:** $Cu^{2+}(aq) + 2e^- \rightarrow Cu(s)$
*   **Overall Reaction:** $Ni(s) + Cu^{2+}(aq) \rightarrow Ni^{2+}(aq) + Cu(s)$
Number of electrons transferred, $n = 2$.

According to the Nernst Equation for the cell:
$$E_{cell} = E^\circ_{cell} - \frac{0.0591}{n} \log \frac{[\text{Products}]}{[\text{Reactants}]}$$
$$E_{cell} = E^\circ_{cell} - \frac{0.0591}{2} \log \frac{[Ni^{2+}]}{[Cu^{2+}]}$$

Substituting the given values:
$$0.59 = E^\circ_{cell} - \frac{0.0591}{2} \log \left( \frac{0.01}{1} \right)$$
$$0.59 = E^\circ_{cell} - 0.02955 \log (10^{-2})$$
$$0.59 = E^\circ_{cell} - 0.02955 \times (-2)$$
$$0.59 = E^\circ_{cell} + 0.0591$$

Calculate Standard Cell Potential ($E^\circ_{cell}$):
$$E^\circ_{cell} = 0.59 - 0.0591 = 0.5309 \text{ V}$$

We know that $E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode}$
$$E^\circ_{cell} = E^\circ_{Cu^{2+}/Cu} - E^\circ_{Ni^{2+}/Ni}$$
$$0.5309 = +0.34 - E^\circ_{Ni^{2+}/Ni}$$
$$E^\circ_{Ni^{2+}/Ni} = 0.34 - 0.5309$$
$$E^\circ_{Ni^{2+}/Ni} = -0.1909 \text{ V}$$

*(Note: If the cell potential 0.59 V provided in the question was intended to be the **Standard** Cell Potential ($E^\circ_{cell} = 0.59 \text{ V}$), ignoring the $0.01M$ non-standard condition, the calculation would be: $0.59 = 0.34 - E^\circ_{Ni^{2+}/Ni} \implies E^\circ_{Ni^{2+}/Ni} = -0.25 \text{ V}$, which exactly matches the literature value. However, rigorously applying the Nernst equation with the given data yields -0.19 V).*

**Final Answer:** The calculated standard electrode potential of the $Ni^{2+}/Ni$ electrode is **$-0.19 \text{ V}$**.

---

---

## 📄 Source: 2021 Exam

### Q.4(a) What is electrolysis? State and explain Faraday's law of electrolysis. (05)

**Answer:**

**Electrolysis:**
Electrolysis is the process of chemical decomposition of an electrolyte (in aqueous solution or molten state) caused by the passage of a direct electric current through it. It involves non-spontaneous redox reactions driven by electrical energy, where cations are reduced at the cathode and anions are oxidized at the anode.

**Faraday's Laws of Electrolysis:**
Michael Faraday formulated two quantitative laws governing the extent of chemical change during electrolysis:

**1. Faraday's First Law:**
*   **Statement:** The mass ($W$) of any substance deposited or liberated at an electrode during electrolysis is directly proportional to the quantity of electricity ($Q$) passed through the electrolyte.
*   **Explanation:** Since electric charge $Q = I \times t$ (Current in Amperes $\times$ time in seconds), we can write:
    $W \propto Q \implies W \propto It$
    $W = ZIt$
    Where $Z$ is a constant known as the **Electrochemical Equivalent** of the substance. It is defined as the mass of substance deposited when exactly 1 Ampere of current flows for 1 second (i.e., 1 Coulomb of charge).

**2. Faraday's Second Law:**
*   **Statement:** When the same quantity of electricity is passed through solutions of different electrolytes connected in series, the masses of the substances deposited at the respective electrodes are directly proportional to their equivalent weights ($E$).
*   **Explanation:** If $W_1$ and $W_2$ are the masses of two different metals deposited, and $E_1$ and $E_2$ are their respective equivalent weights, then:
    $W \propto E$
    $\frac{W_1}{W_2} = \frac{E_1}{E_2}$
    This law establishes that 1 Faraday of charge ($96,485 \text{ Coulombs}$) deposits exactly one gram-equivalent weight of any substance.

---

---

### Q.4(b) Give the Debye-Huckel-Onsager equation and explain the terms involved. (03)

**Answer:**

**Debye-Huckel-Onsager Equation:**
This equation describes the variation of equivalent conductance ($\Lambda_c$) of strong electrolytes with concentration due to interionic attractive forces (relaxation and electrophoretic effects).
The mathematical expression is:
$$\Lambda_c = \Lambda_0 - (A + B\Lambda_0)\sqrt{c}$$

**Explanation of Terms:**
*   $\Lambda_c$ = Equivalent conductance of the strong electrolyte at a given concentration $c$.
*   $\Lambda_0$ = Equivalent conductance at infinite dilution (where interionic attractions are zero).
*   $c$ = Concentration of the electrolyte in moles per liter.
*   $A$ = A constant that accounts for the **Electrophoretic effect** (the retardation of ion movement due to the opposite flow of the solvent molecules moving with the oppositely charged ionic atmosphere).
*   $B$ = A constant that accounts for the **Relaxation (or Asymmetry) effect** (the retardation caused by the time delay in the rebuilding of the oppositely charged ionic atmosphere behind a moving ion).
*(Both A and B depend on the nature of the solvent, namely its dielectric constant and viscosity, and the temperature).*

---

---

## 📄 Source: 2020 Exam

### Q.8(b) Explain the mechanism of electrolytic conduction. (04)

**Answer:**

**Mechanism of Electrolytic Conduction:**
Electrolytic conduction refers to the flow of electric current through an electrolyte (in molten state or aqueous solution) accompanied by the actual physical movement of matter (ions) and chemical decomposition.

1.  **Ion Availability:** In their solid, crystalline state, electrolytes (like NaCl) cannot conduct electricity because their ions are held rigidly in a crystal lattice by strong electrostatic forces. When the electrolyte is dissolved in water or melted, these bonds break, and the ions (cations and anions) become free and highly mobile.
2.  **Application of Potential:** When two electrodes (anode and cathode) are placed in the electrolyte and connected to a direct current (DC) battery, an electric field is established across the solution.
3.  **Ionic Migration:** Under the influence of this electric field, the freely moving ions experience an electrical force:
    *   The positively charged ions (**Cations**) are attracted to and migrate towards the negative electrode (**Cathode**).
    *   The negatively charged ions (**Anions**) are attracted to and migrate towards the positive electrode (**Anode**).
4.  **Chemical Reaction (Electrolysis):** Upon reaching the electrodes, the ions undergo oxidation-reduction reactions. Cations accept electrons from the cathode (reduction), and anions give up electrons to the anode (oxidation). This continuous flow of electrons into and out of the external circuit, facilitated by the internal movement of ions, constitutes the mechanism of electrolytic conduction.

---

---

## 📄 Source: 2019 Exam

### Q.8(a) State and explain the Faraday's laws of electrolysis. (04)

**Answer:**

**1. Faraday's First Law:**
*   **Statement:** The mass ($W$) of any substance deposited or liberated at an electrode during electrolysis is directly proportional to the total quantity of electricity ($Q$) passed through the electrolyte.
*   **Explanation:** Since electric charge $Q = I \times t$ (Current $\times$ time), then $W \propto I \times t \implies W = ZIt$.
    Where $Z$ is the Electrochemical Equivalent of the substance (the mass deposited by 1 Ampere of current flowing for 1 second).

**2. Faraday's Second Law:**
*   **Statement:** When the exact same quantity of electricity is passed through different electrolytic cells connected in series, the masses of the respective substances deposited at the electrodes are directly proportional to their chemical equivalent weights ($E$).
*   **Explanation:** If $W_1$ and $W_2$ are masses deposited, and $E_1$ and $E_2$ are their equivalent weights, then $W_1/W_2 = E_1/E_2$. This establishes that 1 Faraday of charge (96,485 Coulombs) deposits exactly one gram-equivalent weight of any substance.

---

---

### Q.8(c) 0.1978g of Cu is deposited by a current of 0.2 amp for 50 min. What is the electrochemical equivalent of Cu? (04)

**Answer:**

**Given Data:**
*   Mass of Copper deposited ($W$) = $0.1978 \text{ g}$
*   Current passed ($I$) = $0.2 \text{ Ampere}$
*   Time duration ($t$) = $50 \text{ minutes} = 50 \times 60 \text{ seconds} = 3000 \text{ seconds}$

**To Find:**
*   Electrochemical equivalent ($Z$) of Cu.

**Solution:**
According to Faraday's First Law of Electrolysis, the mass deposited is proportional to the current and time:
$$W = Z \times I \times t$$

Rearranging the formula to solve for the electrochemical equivalent ($Z$):
$$Z = \frac{W}{I \times t}$$

Substitute the given values into the equation:
$$Z = \frac{0.1978}{0.2 \times 3000}$$
$$Z = \frac{0.1978}{600}$$
$$Z = 0.0003296 \text{ g/C}$$ (or grams per Coulomb)

**Final Answer:** The electrochemical equivalent of Copper (Cu) is **$3.296 \times 10^{-4} \text{ g/C}$**.

---

## 📄 Source: 2018 Exam

### Q7(a) Define electrolytes and classify them with examples. (04)

**Answer:**
**Electrolytes:** These are chemical substances that, when dissolved in a polar solvent (like water) or when melted into a molten state, undergo chemical decomposition (dissociation or ionization) to yield freely moving, electrically charged ions. Because of these mobile ions, their solutions or melts are capable of conducting electricity.

**Classification:**
Based on the extent of their ionization/dissociation in aqueous solution, they are classified into two types:
1.  **Strong Electrolytes:** Substances that dissociate almost completely (nearly 100%) into ions when dissolved in water. They are excellent conductors of electricity.
    *   *Examples:* Strong acids ($HCl, H_2SO_4, HNO_3$), Strong bases ($NaOH, KOH$), and most soluble salts ($NaCl, KNO_3$).
2.  **Weak Electrolytes:** Substances that undergo only partial or very slight dissociation into ions in aqueous solution. An equilibrium exists between the un-ionized molecules and the dissociated ions. They are poor conductors of electricity.
    *   *Examples:* Weak acids ($CH_3COOH, HCN$), Weak bases ($NH_4OH$).

---

---

### Q7(b) Describe the mechanism of electrolytic conduction. (04)

**Answer:**
**Mechanism of Electrolytic Conduction:**
Electrolytic conduction is the flow of electric current through an electrolyte solution accompanied by the actual physical movement of matter (ions).
1.  **Ionization:** When an electrolyte (e.g., $NaCl$) dissolves in water, the crystal lattice breaks, and it dissociates into free, mobile cations ($Na^+$) and anions ($Cl^-$). In the absence of an electric field, these ions move randomly in all directions.
2.  **Application of Potential:** When two electrodes are inserted into the solution and connected to a DC power source (battery), an electric field is established.
3.  **Directional Migration:** The random movement stops, and the ions experience an electrostatic force.
    *   The positively charged **cations** are attracted to and migrate towards the negatively charged electrode (**Cathode**).
    *   The negatively charged **anions** are attracted to and migrate towards the positively charged electrode (**Anode**).
4.  **Electrolysis (Redox Reaction):** At the electrodes, a chemical reaction occurs. Cations gain electrons from the cathode (Reduction), and anions lose electrons to the anode (Oxidation). This continuous exchange of electrons at the electrodes, fueled by the physical transport of charges by the ions through the bulk of the solution, constitutes electrolytic conduction.

---

---

### Q7(c) Define with examples the electrochemical cell and electrolytic cell. (04)

**Answer:**

**1. Electrochemical Cell (Galvanic or Voltaic Cell):**
*   **Definition:** It is a device that is designed to convert the **chemical energy** released during a spontaneous redox reaction directly into **electrical energy**. In this cell, the reaction happens on its own, generating a voltage that can power external devices.
*   **Example:** A standard **Daniell Cell** (or a common AA battery). It consists of a Zinc anode in a $ZnSO_4$ solution and a Copper cathode in a $CuSO_4$ solution, connected by a salt bridge. Zinc spontaneously oxidizes, pushing electrons through a wire to reduce Copper, creating a current.

**2. Electrolytic Cell:**
*   **Definition:** It is a device that uses external **electrical energy** from a power source (like a battery) to force a highly non-spontaneous chemical reaction (electrolysis) to occur. It converts electrical energy into chemical energy.
*   **Example:** The **electrolysis of water** to produce Hydrogen and Oxygen gas, or the electrolysis of molten $NaCl$ to extract pure sodium metal and chlorine gas.

---

---

### (d) Velocity of ion and its experimental determination
**Velocity of an Ion (Ionic Mobility):** In an electrolytic solution, the velocity of an ion refers to the specific speed at which a particular ion migrates towards the oppositely charged electrode under the influence of an applied electric potential gradient. Because different ions have different masses, charge densities, and sizes of hydration spheres (how heavily they are clustered with water molecules), they move at very different velocities. The velocity of an ion under a standard potential gradient of $1 \text{ V/cm}$ is called its "Absolute Ionic Mobility."
**Experimental Determination (Moving Boundary Method):** The velocities of ions are related to their transport numbers, which are determined experimentally. A classic technique is the **Moving Boundary Method**. In a vertical tube, two different electrolyte solutions sharing a common ion (an indicator solution and a principal solution) are carefully layered so a sharp, distinct visible boundary forms between them due to differences in refractive index or color. When a current is passed, the ions migrate, and the visible boundary physically moves up the tube. By accurately measuring the distance this boundary moves over a specific time under a known current, the absolute velocity and transport number of the ion can be precisely calculated.

---

## 📄 Source: 2017 Exam

### Q6(a) The specific conductance decreases but equivalent conductance increases on dilution-explain. (04)

**Answer:**

1.  **Specific Conductance ($\kappa$) Decreases:**
    Specific conductance is the exact conductance offered by $1 \text{ cm}^3$ of the electrolyte solution. Conductivity depends directly on the number of charge-carrying ions present. When a solution is diluted by adding more solvent, the total volume increases significantly, but the total number of ions remains relatively similar. Consequently, the **number of current-carrying ions per unit volume ($1 \text{ cm}^3$) decreases drastically**. Therefore, specific conductance ($\kappa$) always decreases upon dilution.
2.  **Equivalent Conductance ($\Lambda_{eq}$) Increases:**
    Equivalent conductance is the total conductance of a volume ($V$) of solution that contains exactly one gram-equivalent of the dissolved electrolyte. It is given by: $\Lambda_{eq} = \kappa \times V$.
    Upon dilution, the specific conductance ($\kappa$) decreases, but the volume ($V$) containing that 1 gram-equivalent increases tremendously. The massive increase in volume ($V$) overwhelmingly overcompensates for the small drop in $\kappa$.
    *   *For Weak Electrolytes:* Dilution forces them to dissociate more (according to Ostwald's dilution law), increasing the total number of ions in the bulk volume.
    *   *For Strong Electrolytes:* They are already fully ionized, but dilution separates the crowded ions further apart. This greatly reduces inter-ionic electrostatic attractions (retardation forces), allowing the ions to migrate much faster.
    Thus, equivalent conductance increases with dilution for both types.

---

---

### Q6(b) Mention the main assumptions of Debye-Huckel limiting theory of strong electrolytes. (04)

**Answer:**
The Debye-Hückel theory explains the deviation of strong electrolytes from ideal behavior at higher concentrations. Its main assumptions are:

1.  **Complete Ionization:** Strong electrolytes are assumed to be completely (100%) dissociated into ions in the solution at all times, regardless of the concentration. There are no un-ionized molecules.
2.  **Electrostatic Interactions:** The departure from ideal behavior is not due to incomplete ionization, but is entirely due to strong long-range electrical (electrostatic) forces of attraction and repulsion between the charged ions.
3.  **Ionic Atmosphere:** Every individual ion in the solution is not entirely free. Instead, it is continuously surrounded by a spherically symmetrical "ionic atmosphere" consisting on average of an excess of oppositely charged ions.
4.  **Retardation Effects:** When an external electric field is applied to conduct current, this symmetrical ionic atmosphere is distorted and moves in the opposite direction to the central ion. This creates two distinct drag forces—the **Asymmetric (Relaxation) Effect** and the **Electrophoretic Effect**—both of which violently retard the mobility of the central ion, thereby lowering the overall conductivity of the concentrated solution.

---

---

### Q6(c) Calculate the activity coefficients of ions of 0.01 molal solution of sodium sulphate in water. (04)

**Answer:**

**Given:**
*   Electrolyte: Sodium sulfate ($Na_2SO_4$). It dissociates as: $Na_2SO_4 \rightarrow 2Na^+ + SO_4^{2-}$
*   Molality of solution ($m$) = $0.01 \text{ molal}$

**1. Calculate Ionic Strength ($I$):**
Ionic strength is given by: $I = \frac{1}{2} \sum m_i z_i^2$
*   For $Na^+$ ion: Molality $m_1 = 2 \times 0.01 = 0.02$. Charge $z_1 = +1$.
*   For $SO_4^{2-}$ ion: Molality $m_2 = 1 \times 0.01 = 0.01$. Charge $z_2 = -2$.

$$I = \frac{1}{2} [m_1 z_1^2 + m_2 z_2^2]$$
$$I = \frac{1}{2} [(0.02)(1)^2 + (0.01)(-2)^2]$$
$$I = \frac{1}{2} [0.02 + 0.04] = \frac{0.06}{2} = 0.03$$

**2. Calculate Activity Coefficients using Debye-Hückel Limiting Law:**
The law is: $\log \gamma_i = -0.509 z_i^2 \sqrt{I}$

*   **For $Na^+$ ion ($\gamma_+$):**
    $$\log \gamma_+ = -0.509 \times (+1)^2 \times \sqrt{0.03}$$
    $$\log \gamma_+ = -0.509 \times 1 \times 0.1732 = -0.08816$$
    $$\gamma_+ = \text{antilog}(-0.08816) = 10^{-0.08816} = \mathbf{0.816}$$

*   **For $SO_4^{2-}$ ion ($\gamma_-$):**
    $$\log \gamma_- = -0.509 \times (-2)^2 \times \sqrt{0.03}$$
    $$\log \gamma_- = -0.509 \times 4 \times 0.1732 = -0.3526$$
    $$\gamma_- = \text{antilog}(-0.3526) = 10^{-0.3526} = \mathbf{0.444}$$

*(Optional: The Mean Ionic Activity Coefficient ($\gamma_{\pm}$) is $\log \gamma_{\pm} = -0.509 |z_+ z_-| \sqrt{I} = -0.509(2)(0.1732) = -0.1763 \implies \gamma_{\pm} = 0.666$)*.

---

---

## 📄 Source: ClassTests Exam

### Q.1 Define molar conductance and equivalent conductance. Apply Debye-Huckel theory to calculate the activity coefficients of $Na^+$ and $SO_4^{2-}$ ions of 0.01 molal $Na_2SO_4$ solution in water at room temperature. (10)
**Answer:**
*   **Molar Conductance ($\Lambda_m$):** It is defined as the total conductance of all the ions produced by dissolving exactly one mole of an electrolyte in a volume ($V$) of solution. ($\Lambda_m = \kappa \times \frac{1000}{M}$, where $M$ is molarity).
*   **Equivalent Conductance ($\Lambda_{eq}$):** It is defined as the total conductance of all the ions produced by dissolving exactly one gram-equivalent weight of an electrolyte in a volume ($V$) of solution. ($\Lambda_{eq} = \kappa \times \frac{1000}{N}$, where $N$ is normality).

**Debye-Hückel Calculation:**
*(Note: This is the exact same calculation requested in the 2017 Exam, Section B, Q6(c). The results are summarized below).*
1.  **Calculate Ionic Strength ($I$):**
    For 0.01m $Na_2SO_4$, $I = \frac{1}{2} [ (0.02)(+1)^2 + (0.01)(-2)^2 ] = 0.03$.
2.  **Calculate Activity Coefficients ($\gamma$) using $\log \gamma_i = -0.509 z_i^2 \sqrt{I}$:**
    *   **For $Na^+$ ion:** $\log \gamma_+ = -0.509(1)^2\sqrt{0.03} = -0.08816 \implies \mathbf{\gamma_+ = 0.816}$
    *   **For $SO_4^{2-}$ ion:** $\log \gamma_- = -0.509(-2)^2\sqrt{0.03} = -0.3526 \implies \mathbf{\gamma_- = 0.444}$

---

### Q.2 State Kohlrausch's law. Derive the equation to find out the $k_w$ of water by using the law. (10)
**Answer:**
**Kohlrausch’s Law of Independent Migration of Ions:**
It states that at infinite dilution, where dissociation is 100% complete and inter-ionic electrostatic forces are exactly zero, each individual ion migrates independently and makes a definite, fixed contribution to the total equivalent conductance of the electrolyte, regardless of the nature of the other ion it is associated with.
Mathematically: $\Lambda^\circ_{\text{eq}} = \lambda^\circ_+ + \lambda^\circ_-$

**Derivation of Ionic Product of Water ($K_w$):**
Water is an extremely weak electrolyte that ionizes slightly:
$$H_2O \rightleftharpoons H^+ + OH^-$$
Let the degree of dissociation of water be $\alpha$. According to Arrhenius theory, the degree of dissociation is the ratio of molar conductance at a given concentration ($\Lambda_v$) to the molar conductance at infinite dilution ($\Lambda^\circ$):
$$\alpha = \frac{\Lambda_v}{\Lambda^\circ}$$
1.  **Finding $\Lambda^\circ$:** By applying Kohlrausch's law, the molar conductance of water at infinite dilution is the sum of its ionic mobilities (which are known constants from strong electrolytes):
    $$\Lambda^\circ_{H_2O} = \lambda^\circ_{H^+} + \lambda^\circ_{OH^-}$$
2.  **Finding $\Lambda_v$:** The actual molar conductance of pure water can be found experimentally using its highly sensitive specific conductance ($\kappa$). If $C$ is the molar concentration of pure water ($1000 \text{ g/L} / 18 \text{ g/mol} = 55.55 \text{ mol/L}$), then:
    $$\Lambda_v = \kappa \times \frac{1000}{C}$$
3.  **Substituting into $\alpha$:**
    $$\alpha = \frac{\kappa \times \frac{1000}{C}}{\lambda^\circ_{H^+} + \lambda^\circ_{OH^-}} = \frac{1000 \cdot \kappa}{C (\lambda^\circ_{H^+} + \lambda^\circ_{OH^-})}$$
4.  **Calculating $K_w$:** The ionic product of water is defined as $K_w = [H^+][OH^-]$.
    From the ionization equation, $[H^+] = C\alpha$ and $[OH^-] = C\alpha$.
    $$K_w = (C\alpha) \times (C\alpha) = C^2 \alpha^2$$
    Substitute the full expression for $\alpha$ into the $K_w$ equation:
    $$K_w = C^2 \left[ \frac{1000 \cdot \kappa}{C (\lambda^\circ_{H^+} + \lambda^\circ_{OH^-})} \right]^2$$
    $$K_w = C^2 \frac{(1000 \cdot \kappa)^2}{C^2 (\lambda^\circ_{H^+} + \lambda^\circ_{OH^-})^2}$$
    The $C^2$ terms perfectly cancel out, yielding the final equation:
    **$$K_w = \left[ \frac{1000 \cdot \kappa}{\lambda^\circ_{H^+} + \lambda^\circ_{OH^-}} \right]^2$$**
This derived equation elegantly allows the determination of the fundamental constant $K_w$ by simply measuring the specific conductance ($\kappa$) of ultra-pure water.

---


---

[⬅ 06-Thermochemistry](06-Thermochemistry.md) | [🏠 Index](index.md) | [08-Solutions ➡](08-Solutions.md)
