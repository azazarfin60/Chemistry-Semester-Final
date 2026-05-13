[⬅ 05-Atomic-Structure](05-Atomic-Structure.md) | [🏠 Index](index.md) | [07-Electrochemistry ➡](07-Electrochemistry.md)

---

# Thermochemistry
**Priority:** 🟠 HIGH | **Frequency:** 14 sub-parts across 5/7 exams

> **Topics Covered:** Thermochemistry definitions, Hess's Law, heat of combustion/formation/neutralization/sublimation, Kirchhoff's equation, bomb calorimeter, ΔH=qp, constant P vs V.

---

## 📄 Source: 2024 Exam

### Q.4(a) State and explain the Hess's law of heat summation. (05)

**Answer:**

**Statement of Hess's Law:**
Hess's Law of Constant Heat Summation states that *"The total enthalpy change ($\Delta H$) accompanying a chemical reaction is the same, whether the reaction takes place in a single step or in multiple intermediate steps, provided the initial and final states (and conditions) of the system are identical."*

**Explanation:**
Enthalpy ($H$) is a state function, meaning its change depends only on the initial reactants and the final products, not on the path taken.
Suppose a reactant $A$ can be converted to a product $Z$ directly in one step, or indirectly through intermediates $B$ and $C$.

*   **Path 1 (Direct):** $A \rightarrow Z$, Enthalpy change = $\Delta H$
*   **Path 2 (Indirect):**
    *   Step 1: $A \rightarrow B$, Enthalpy change = $\Delta H_1$
    *   Step 2: $B \rightarrow C$, Enthalpy change = $\Delta H_2$
    *   Step 3: $C \rightarrow Z$, Enthalpy change = $\Delta H_3$

According to Hess's Law, the total heat evolved or absorbed in both paths must be equal:
$$\Delta H = \Delta H_1 + \Delta H_2 + \Delta H_3$$

This law is a direct consequence of the First Law of Thermodynamics (Law of Conservation of Energy). If $\Delta H$ for the direct path was less than the indirect path, one could cycle through the forward and reverse reactions to create energy out of nothing, which is impossible.

---

---

### Q.4(b) Define the following with suitable examples. i) Heat of combustion ii) Heat of sublimation (02)

**Answer:**

**i) Heat of Combustion ($\Delta H_c$):**
It is the total amount of heat evolved (change in enthalpy) when exactly 1 mole of a substance is completely burned or oxidized in the presence of excess oxygen at standard conditions.
*   *Example:* The combustion of 1 mole of methane ($CH_4$):
    $CH_4(g) + 2O_2(g) \rightarrow CO_2(g) + 2H_2O(l); \quad \Delta H_c = -890.3 \text{ kJ/mol}$

**ii) Heat of Sublimation ($\Delta H_{sub}$):**
It is the total amount of heat absorbed (change in enthalpy) required to convert exactly 1 mole of a solid directly into its gaseous state at a constant temperature, without passing through the liquid phase.
*   *Example:* The sublimation of solid iodine:
    $I_2(s) \rightarrow I_2(g); \quad \Delta H_{sub} = +62.4 \text{ kJ/mol}$

---

---

### Q.4(c) The heat of combustion of $CH_4$ is 212.0 kcal. If the heat of formation of $CO_2$ and $H_2O$ is 94.3 kcal and 68.5 kcal respectively. Calculate the heat of formation of $CH_4$. (03)

**Answer:**

**Given Data:**
1.  Heat of combustion of $CH_4$, $\Delta H_c(CH_4) = -212.0 \text{ kcal/mol}$ (combustion is exothermic, so sign is negative).
2.  Heat of formation of $CO_2$, $\Delta H_f(CO_2) = -94.3 \text{ kcal/mol}$.
3.  Heat of formation of $H_2O$, $\Delta H_f(H_2O) = -68.5 \text{ kcal/mol}$.

**To Find:**
*   Heat of formation of $CH_4$, $\Delta H_f(CH_4)$

**Solution:**
The balanced chemical equation for the combustion of methane is:
$$CH_4(g) + 2O_2(g) \rightarrow CO_2(g) + 2H_2O(l)$$

According to Hess's law, the enthalpy of reaction ($\Delta H_{rxn}$) can be calculated from the enthalpies of formation of the products and reactants:
$$\Delta H_{rxn} = \sum \Delta H_f(\text{Products}) - \sum \Delta H_f(\text{Reactants})$$

For the combustion reaction, $\Delta H_{rxn} = \Delta H_c(CH_4)$.
$$\Delta H_c(CH_4) = [\Delta H_f(CO_2) + 2 \times \Delta H_f(H_2O)] - [\Delta H_f(CH_4) + 2 \times \Delta H_f(O_2)]$$

By convention, the standard heat of formation of an element in its standard state (like $O_2$ gas) is zero. So, $\Delta H_f(O_2) = 0$.

Substituting the values:
$$-212.0 = [-94.3 + 2(-68.5)] - [\Delta H_f(CH_4) + 0]$$
$$-212.0 = [-94.3 - 137.0] - \Delta H_f(CH_4)$$
$$-212.0 = -231.3 - \Delta H_f(CH_4)$$
$$\Delta H_f(CH_4) = -231.3 + 212.0$$
$$\Delta H_f(CH_4) = -19.3 \text{ kcal/mol}$$

**Final Answer:**
The heat of formation of methane ($CH_4$) is **-19.3 kcal/mol**.

---

## SECTION-B

---

## 📄 Source: 2023 Exam

### Q.4(a) Define enthalpy of combustion and calorific value. (02)

**Answer:**

**Enthalpy of Combustion ($\Delta H_c$):**
It is defined as the total amount of heat evolved (change in enthalpy) when exactly 1 mole of a substance is completely oxidized or burnt in the presence of excess oxygen at standard conditions. It is always an exothermic process (negative $\Delta H$).

**Calorific Value:**
It is defined as the total amount of heat energy released when a unit mass (usually 1 gram or 1 kilogram) or a unit volume of a fuel or food is completely burnt. It is used to compare the efficiency of different fuels and is typically expressed in units like $kJ/g$ or $kcal/kg$.

---

---

### Q.4(b) Draw and describe the operation procedures of a bomb calorie meter. (04)

**Answer:**

**Operation Procedure of a Bomb Calorimeter:**
A Bomb Calorimeter is a highly insulated device used to measure the heat of combustion of a substance at a constant volume ($\Delta U$).

1.  **Sample Preparation:** A known mass ($m$) of the combustible substance (fuel/food) is weighed accurately and placed in a small platinum crucible.
2.  **Assembling the "Bomb":** The crucible is placed inside a strong, heavy-walled steel vessel called the "bomb." A fine platinum ignition wire is connected to the crucible to initiate combustion.
3.  **Pressurization:** The bomb is sealed air-tight and filled with excess pure Oxygen gas at a high pressure (usually 20-25 atmospheres) to ensure complete combustion.
4.  **Water Bath:** The sealed bomb is immersed in a larger, heavily insulated outer vessel containing a precisely known mass of water ($W$). The outer vessel is equipped with a mechanical stirrer and a highly sensitive Beckman thermometer.
5.  **Initial Reading:** The stirrer ensures uniform temperature. The initial temperature ($t_1$) of the water is noted.
6.  **Ignition:** An electric current is passed through the platinum wire, which glows and ignites the sample. The sample burns completely in the pressurized oxygen.
7.  **Final Reading:** The heat evolved from the combustion is transferred through the steel walls of the bomb to the surrounding water. The water temperature rises. The maximum temperature reached by the water ($t_2$) is recorded.

*(Note: In the exam, draw a sketch showing the strong inner bomb vessel, the sample cup, ignition wires, the surrounding water bath, the thermometer, stirrer, and insulated outer jacket).*

---

---

### Q.4(c) Find the mathematical equation of enthalpy of combustion. (04)

**Answer:**

**Mathematical Derivation:**
From the Bomb Calorimeter experiment, the combustion occurs in a closed, rigid vessel, meaning the volume is constant ($\Delta V = 0$). Therefore, the heat measured is the heat at constant volume ($q_v$), which is equal to the change in internal energy ($\Delta U$).

**Step 1: Calculate $\Delta U$**
Let $W_w$ = mass of water in the calorimeter
Let $w_c$ = water equivalent of the calorimeter setup (bomb, stirrer, thermometer)
Let $m$ = mass of the substance burnt
Let $M$ = Molar mass of the substance
Let $\Delta T = (t_2 - t_1)$ = Rise in temperature
Let $s$ = specific heat of water (usually $4.184 \text{ J/g}^\circ\text{C}$)

The total heat absorbed by the calorimeter and water ($q_v$) is:
$$q_v = (W_w + w_c) \times s \times \Delta T$$
This heat corresponds to the burning of $m$ grams of the substance.
For 1 mole ($M$ grams) of the substance, the internal energy change ($\Delta U$) is:
$$\Delta U = - \frac{(W_w + w_c) \times s \times \Delta T}{m} \times M$$
*(The negative sign indicates the reaction is exothermic).*

**Step 2: Calculate Enthalpy of Combustion ($\Delta H_c$)**
The relationship between enthalpy change ($\Delta H$) and internal energy change ($\Delta U$) is given by the First Law of Thermodynamics:
$$\Delta H_c = \Delta U + P\Delta V$$
For reactions involving ideal gases at constant temperature and pressure:
$$P\Delta V = \Delta n_g RT$$
Where:
*   $\Delta n_g = (\text{Total moles of gaseous products}) - (\text{Total moles of gaseous reactants})$
*   $R$ = Universal gas constant ($8.314 \text{ J/(mol K)}$)
*   $T$ = Absolute temperature in Kelvin

Substituting $P\Delta V$ into the enthalpy equation gives the final mathematical equation for the Enthalpy of Combustion:
$$\Delta H_c = \Delta U + \Delta n_g RT$$

By calculating $\Delta U$ from the calorimeter data and finding $\Delta n_g$ from the balanced chemical equation, the enthalpy of combustion ($\Delta H_c$) can be easily determined.

---

## SECTION-B

---

## 📄 Source: 2021 Exam

### Q.7(a) Define and explain the following terms with suitable examples. (i) Heat of reaction (ii) Heat of neutralization (04)

**Answer:**

**(i) Heat of Reaction ($\Delta H$):**
It is defined as the amount of heat evolved or absorbed when molar quantities of reactants, exactly as represented by a balanced chemical equation, react completely to form products. 
*   **Explanation:** It indicates the difference in total enthalpy between products and reactants. If heat is released, $\Delta H$ is negative (exothermic). If heat is absorbed, $\Delta H$ is positive (endothermic).
*   **Example:** $C(s) + O_2(g) \rightarrow CO_2(g); \quad \Delta H = -393.5 \text{ kJ/mol}$ (Heat is evolved).

**(ii) Heat of Neutralization:**
It is defined as the amount of heat evolved (always exothermic) when exactly one gram-equivalent of an acid is completely neutralized by one gram-equivalent of a base in dilute aqueous solution.
*   **Explanation:** Because strong acids and strong bases ionize completely in water, their neutralization is simply the reaction between $H^+$ and $OH^-$ to form water. The heat of neutralization for any strong acid and strong base is a constant value of approximately $-13.7 \text{ kcal/mol}$ (or $-57.1 \text{ kJ/mol}$).
*   **Example:** $HCl(aq) + NaOH(aq) \rightarrow NaCl(aq) + H_2O(l); \quad \Delta H = -13.7 \text{ kcal/mol}$.

---

---

### Q.7(b) The heat of the reaction: $\frac{1}{2}H_2 + \frac{1}{2}Cl_2 \rightarrow HCl$ at $27^\circ C$ is -22.1kCal. Calculate the heat of reaction at $77^\circ C$. The molar heat capacities at constant pressure at $27^\circ C$ for hydrogen, chlorine and HCl are: 6.82, 7.70, 6.80 $\text{Cal mol}^{-1}$ respectively. (04)

**Answer:**

**Given Data:**
*   Reaction: $\frac{1}{2}H_2 + \frac{1}{2}Cl_2 \rightarrow HCl$
*   Initial Temperature, $T_1 = 27^\circ C = 27 + 273 = 300 \text{ K}$
*   Final Temperature, $T_2 = 77^\circ C = 77 + 273 = 350 \text{ K}$
*   Heat of reaction at $T_1$, $\Delta H_1 = -22.1 \text{ kcal} = -22100 \text{ cal}$
*   Molar heat capacities ($C_p$):
    *   $C_p(H_2) = 6.82 \text{ cal/K mol}$
    *   $C_p(Cl_2) = 7.70 \text{ cal/K mol}$
    *   $C_p(HCl) = 6.80 \text{ cal/K mol}$

**To Find:** Heat of reaction at $T_2$ ($\Delta H_2$)

**Solution:**
**Step 1: Calculate the change in heat capacity ($\Delta C_p$) for the reaction**
$$\Delta C_p = \sum C_p(\text{Products}) - \sum C_p(\text{Reactants})$$
$$\Delta C_p = C_p(HCl) - \left[ \frac{1}{2} C_p(H_2) + \frac{1}{2} C_p(Cl_2) \right]$$
$$\Delta C_p = 6.80 - \left[ \frac{1}{2}(6.82) + \frac{1}{2}(7.70) \right]$$
$$\Delta C_p = 6.80 - [3.41 + 3.85]$$
$$\Delta C_p = 6.80 - 7.26$$
$$\Delta C_p = -0.46 \text{ cal/K mol}$$

**Step 2: Apply Kirchhoff's Equation**
Kirchhoff's equation relates the variation of heat of reaction with temperature:
$$\frac{\Delta H_2 - \Delta H_1}{T_2 - T_1} = \Delta C_p$$
$$\Delta H_2 - \Delta H_1 = \Delta C_p \times (T_2 - T_1)$$
$$\Delta H_2 - (-22100) = -0.46 \times (350 - 300)$$
$$\Delta H_2 + 22100 = -0.46 \times 50$$
$$\Delta H_2 + 22100 = -23$$
$$\Delta H_2 = -22100 - 23$$
$$\Delta H_2 = -22123 \text{ cal}$$
$$\Delta H_2 = -22.123 \text{ kcal}$$

**Final Answer:** The heat of reaction at $77^\circ C$ is **$-22.123 \text{ kCal}$**.

---

---

### Q.7(c) Discuss the applications of the heat of combustion. (04)

**Answer:**

The heat of combustion has several crucial theoretical and practical applications in chemistry and engineering:

1.  **Calculation of Heat of Formation:** Heats of formation for many organic compounds cannot be measured directly in the laboratory because their constituent elements do not directly combine to form them easily. However, their heats of combustion can be measured accurately using a bomb calorimeter. Hess's law can then be applied to calculate the heat of formation from these combustion values.
2.  **Calorific Value of Fuels and Foods:** The heat of combustion is used to determine the calorific value of various fuels (like coal, petroleum, natural gas) and food items. This allows engineers and nutritionists to compare their efficiency and energy-yielding capacities (usually expressed in kcal/g or kJ/kg).
3.  **Elucidation of Chemical Structure:** Heats of combustion can be used to distinguish between structural isomers. Because isomeric compounds have the same molecular formula, any difference in their heats of combustion is solely due to differences in their structural stability. The isomer with a higher (more negative) heat of combustion is generally less stable.
4.  **Calculation of Bond Energies:** Experimental heat of combustion data can be combined with heat of atomization data to calculate the average bond dissociation energies of various chemical bonds within molecules.

---

---

## 📄 Source: 2020 Exam

### Q.5(a) Define thermochemistry. Point out its importance. (04)

**Answer:**

**Thermochemistry:**
Thermochemistry is the branch of physical chemistry which deals with the study of thermal or heat changes (energy changes) that accompany chemical reactions and physical transformations.

**Importance of Thermochemistry:**
1.  **Bond Energy Determination:** The energy changes in chemical reactions are primarily due to the breaking of existing bonds in reactants and the formation of new bonds in products. Thermochemistry provides the crucial data needed to calculate these precise bond dissociation energies.
2.  **Feasibility of Reactions:** While thermodynamics as a whole dictates reaction spontaneity, thermochemical data ($\Delta H$) is a key component (along with entropy) in calculating the Gibbs Free Energy ($\Delta G$), which determines if a reaction is feasible.
3.  **Industrial Applications:** It helps engineers calculate the calorific value of various fuels and determine the heat of combustion, which is vital for designing engines, furnaces, and industrial chemical synthesis plants (e.g., maintaining optimum temperatures in the Haber process).
4.  **Heat of Formation:** It allows for the theoretical calculation of the heat of formation of compounds that cannot be synthesized directly from their constituent elements in the lab, utilizing Hess's Law.

---

---

### Q.5(b) Derive the expression for the heat of reaction at constant pressure and at constant volume. (04)

**Answer:**

**1. Heat of Reaction at Constant Volume ($q_v$):**
According to the First Law of Thermodynamics:
$$q = \Delta E + W$$
Where $q$ is the heat absorbed, $\Delta E$ is the change in internal energy, and $W$ is the work of expansion ($W = P \cdot \Delta V$).
If a reaction is carried out in a closed vessel at constant volume, the change in volume ($\Delta V$) is zero. Therefore, no work of expansion is done ($W = P \times 0 = 0$).
$$q_v = \Delta E + 0$$
$$q_v = \Delta E$$
Thus, the **heat of reaction at constant volume is equal to the change in internal energy ($\Delta E$)** of the system.

**2. Heat of Reaction at Constant Pressure ($q_p$):**
When a reaction occurs at constant pressure (like in an open beaker), the system may expand or contract, meaning work is done.
$$q_p = \Delta E + P\Delta V \quad \dots (i)$$
To study heat changes at constant pressure, the thermodynamic function **Enthalpy ($H$)** is introduced, defined as:
$$H = E + PV$$
The change in enthalpy ($\Delta H$) at constant pressure is:
$$\Delta H = \Delta E + P\Delta V \quad \dots (ii)$$
Comparing equations (i) and (ii):
$$q_p = \Delta H$$
Thus, the **heat of reaction at constant pressure is equal to the change in enthalpy ($\Delta H$)** of the system.

*(Relationship for gases: Since $PV = nRT$, $P\Delta V = \Delta n_g RT$. Therefore, $\Delta H = \Delta E + \Delta n_g RT$).*

---

---

### Q.5(c) Heat of combustion of ethylene at $17^\circ C$ and at constant volume is -332.19 KCals. Calculate the heat of combustion at constant volume considering water to be in the liquid state. [$R = 2 \text{ Cal/}^\circ\text{C-mole}$] (04)

**Answer:**

*(Note: The question asks to calculate heat at constant volume but provides the heat at constant volume. This is a common typographical error in exam papers. It intends to ask for the heat of combustion at **constant pressure** ($\Delta H$) given the heat at constant volume ($\Delta E$)).*

**Given Data:**
*   Heat of combustion at constant volume ($\Delta E$) = $-332.19 \text{ kcal}$
*   Temperature ($T$) = $17^\circ C = 17 + 273 = 290 \text{ K}$
*   Universal gas constant ($R$) = $2 \text{ cal K}^{-1} \text{mol}^{-1} = 2 \times 10^{-3} \text{ kcal K}^{-1} \text{mol}^{-1}$

**Solution:**
The balanced chemical equation for the combustion of ethylene ($C_2H_4$) is:
$$C_2H_4(g) + 3O_2(g) \rightarrow 2CO_2(g) + 2H_2O(l)$$

To find $\Delta n_g$ (change in the number of moles of gaseous substances):
*   Moles of gaseous products = $2 \text{ (from } CO_2)$ *(Water is liquid, so it is ignored)*
*   Moles of gaseous reactants = $1 \text{ (from } C_2H_4) + 3 \text{ (from } O_2) = 4$
$$\Delta n_g = 2 - 4 = -2$$

Using the thermodynamic relation:
$$\Delta H = \Delta E + \Delta n_g RT$$
$$\Delta H = -332.19 + [(-2) \times (2 \times 10^{-3}) \times 290]$$
$$\Delta H = -332.19 + [-4 \times 10^{-3} \times 290]$$
$$\Delta H = -332.19 + [-1.160]$$
$$\Delta H = -333.35 \text{ kcal}$$

**Final Answer:** The heat of combustion at constant pressure is **$-333.35 \text{ kcal}$**.

---

---

## 📄 Source: 2019 Exam

### Q.8(b) Define thermochemistry. Why is it important to study? (04)

**Answer:**

**Thermochemistry:** It is the branch of physical chemistry that deals with the quantitative study of thermal energy (heat) changes that accompany chemical reactions and physical transformations (like melting or boiling).

**Importance:**
1.  It provides necessary experimental data to calculate exact **bond dissociation energies**.
2.  It allows the theoretical calculation of the **heat of formation** for complex compounds that cannot be prepared directly in the lab via Hess's Law.
3.  It is heavily used in engineering to calculate the **calorific values** of fuels and foods, determining which are most efficient.
4.  Along with entropy, thermochemical data ($\Delta H$) dictates the thermodynamic **feasibility and spontaneity** of industrial chemical reactions.

---

---

## 📄 Source: 2017 Exam

### Q2(a) What is heat of reaction? Explain the effect of temperature on heat of reaction. (05)

**Answer:**
**Heat of Reaction:** It is defined as the total amount of thermal energy (heat) either evolved or absorbed during a chemical reaction when the quantities of the reacting substances specified in the balanced chemical equation have completely reacted. It is denoted by $\Delta H$ (enthalpy change at constant pressure) or $\Delta E$ (internal energy change at constant volume).

**Effect of Temperature on Heat of Reaction (Kirchhoff's Equation):**
The heat of a reaction does not remain strictly constant; it changes when the temperature at which the reaction is carried out changes. This variation is explained by **Kirchhoff's equation**.
The effect occurs because the heat capacity (the amount of heat required to raise the temperature by $1^\circ C$) of the products is generally not identical to the heat capacity of the reactants. 

According to Kirchhoff's equation, the change in the heat of reaction ($\Delta H$) for every one-degree change in temperature is exactly equal to the difference in the heat capacities of the products and reactants at constant pressure ($\Delta C_p$):
$$\frac{\Delta H_2 - \Delta H_1}{T_2 - T_1} = \Delta C_p = (C_p)_{\text{products}} - (C_p)_{\text{reactants}}$$
*   **If $\Delta C_p$ is positive** (heat capacity of products > reactants): The heat of reaction ($\Delta H$) will **increase** as temperature increases.
*   **If $\Delta C_p$ is negative** (heat capacity of products < reactants): The heat of reaction ($\Delta H$) will **decrease** as temperature increases.
*   **If $\Delta C_p$ is zero:** The heat of reaction remains independent of temperature.

---

---

### Q2(b) Derive $\Delta H = q_p$. Explain the exothermic and endothermic reaction with suitable examples. (04)

**Answer:**

**1. Derivation of $\Delta H = q_p$:**
According to the First Law of Thermodynamics, the heat ($q$) absorbed by a system is used to increase its internal energy ($\Delta E$) and to do work of expansion ($W$).
$$q = \Delta E + W$$
If a chemical reaction is carried out at **constant pressure** (like in an open beaker), the system may expand or contract against the atmosphere. The work done is pressure-volume work ($W = P \cdot \Delta V$). Let this heat be denoted as $q_p$.
$$q_p = \Delta E + P\Delta V \quad \dots \text{(Equation i)}$$
To study heat changes specifically at constant pressure, a new thermodynamic state function called **Enthalpy ($H$)** is defined as the sum of internal energy and pressure-volume energy:
$$H = E + PV$$
The change in enthalpy ($\Delta H$) at constant pressure is:
$$\Delta H = \Delta E + P\Delta V \quad \dots \text{(Equation ii)}$$
Comparing Equation (i) and Equation (ii), it is clearly evident that:
**$$q_p = \Delta H$$**
Thus, the heat of reaction measured at constant pressure is mathematically equal to the change in enthalpy.

**2. Exothermic and Endothermic Reactions:**
*   **Exothermic Reaction:** A chemical reaction that is accompanied by the **release or evolution of heat** energy into the surroundings. The enthalpy of the products is less than the reactants, so $\Delta H$ is **negative**. The temperature of the reaction mixture rises.
    *   *Example:* Combustion of Methane. $CH_4(g) + 2O_2(g) \rightarrow CO_2(g) + 2H_2O(l); \Delta H = -890.3 \text{ kJ/mol}$
*   **Endothermic Reaction:** A chemical reaction that is accompanied by the **absorption of heat** energy from the surroundings. The enthalpy of the products is greater than the reactants, so $\Delta H$ is **positive**. The temperature of the reaction mixture drops unless external heat is supplied.
    *   *Example:* Thermal decomposition of Calcium Carbonate. $CaCO_3(s) \rightarrow CaO(s) + CO_2(g); \Delta H = +178 \text{ kJ/mol}$

---

---

### Q2(c) Calculate the enthalpy of $C_2H_4(g) + H_2(g) \rightarrow C_2H_6(g)$ reaction at $25^\circ C$. The heat of combustion of ethylene, hydrogen and ethane are -1410 kJ, -286.2 kJ and -1560.6 kJ respectively at $25^\circ C$. (03)

**Answer:**

**Target Reaction:**
$$C_2H_4(g) + H_2(g) \rightarrow C_2H_6(g) \quad \Delta H_{\text{reaction}} = ?$$

**Given Data (Heat of Combustion, $\Delta H_c$):**
*   $\Delta H_c (C_2H_4) = -1410 \text{ kJ/mol}$
*   $\Delta H_c (H_2) = -286.2 \text{ kJ/mol}$
*   $\Delta H_c (C_2H_6) = -1560.6 \text{ kJ/mol}$

**Solution:**
According to Hess's Law, the enthalpy change of a reaction can be calculated directly from the heats of combustion of the reactants and products using the following formula:
$$\Delta H_{\text{reaction}} = \sum \Delta H_c (\text{Reactants}) - \sum \Delta H_c (\text{Products})$$

Substitute the given values into the formula:
$$\Delta H_{\text{reaction}} = [\Delta H_c(C_2H_4) + \Delta H_c(H_2)] - [\Delta H_c(C_2H_6)]$$
$$\Delta H_{\text{reaction}} = [(-1410) + (-286.2)] - [-1560.6]$$
$$\Delta H_{\text{reaction}} = [-1696.2] + 1560.6$$
$$\Delta H_{\text{reaction}} = -135.6 \text{ kJ/mol}$$

**Final Answer:** The enthalpy of the reaction is **$-135.6 \text{ kJ/mol}$**.

---

---

## 📄 Source: 2017 Exam (Short Notes)

### (a) Laws of Thermochemistry.
**Answer:**

Thermochemistry is governed by two fundamental laws, both of which are direct consequences of the First Law of Thermodynamics (Conservation of Energy):
1.  **Lavoisier and Laplace's Law (1782):** It states that the heat energy evolved during the synthesis of a compound is exactly equal to, but opposite in sign, to the heat energy absorbed when that exact compound decomposes back into its constituent elements. (If $A \rightarrow B, \Delta H = -X$, then $B \rightarrow A, \Delta H = +X$).
2.  **Hess's Law of Constant Heat Summation (1840):** It states that the total enthalpy change (evolution or absorption of heat) in a chemical reaction is absolutely constant, regardless of whether the reaction is accomplished in a single step or through a complex series of multiple intermediate steps. This law is crucial because it allows thermochemical equations to be treated algebraically, enabling the calculation of heats of formation that cannot be measured experimentally.

---



---

[⬅ 05-Atomic-Structure](05-Atomic-Structure.md) | [🏠 Index](index.md) | [07-Electrochemistry ➡](07-Electrochemistry.md)
