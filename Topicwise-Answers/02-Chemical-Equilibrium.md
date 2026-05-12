# Chemical Equilibrium
**Priority:** 🔴 CRITICAL | **Frequency:** 17 sub-parts across 7/7 exams

> **Topics Covered:** Law of mass action, Kp/Kc/Kx derivations, Le Chatelier's principle, Haber process, van't Hoff equation, ΔG°=-2.303RTlogKp, reversible/irreversible reactions, dynamic equilibrium.

---

## 📄 Source: 2024 Exam

### Q.6(a) Define chemical equilibrium. (03)

**Answer:**

**Chemical Equilibrium:**
Chemical equilibrium is the state of a reversible reaction in a closed system where the rate of the forward reaction becomes exactly equal to the rate of the backward (reverse) reaction. At this state, there is no net change in the measurable macroscopic properties of the system, such as the concentrations of reactants and products, pressure, color, or temperature, over time. It is a dynamic state, meaning both forward and backward reactions continue to occur, but at identical rates, thus canceling out each other's macroscopic effects.

---

---

### Q.6(b) State and explain the law of mass action. (03)

**Answer:**

**Statement of the Law of Mass Action:**
The Law of Mass Action states that *"At a given constant temperature, the rate of a chemical reaction is directly proportional to the product of the active masses (molar concentrations or partial pressures) of the reacting substances, with each concentration term raised to a power equal to its stoichiometric coefficient in the balanced chemical equation."*

**Explanation:**
Consider a general reversible reaction:
$$aA + bB \rightleftharpoons cC + dD$$

According to the law of mass action, the rate of the forward reaction ($R_f$) is proportional to the active masses of reactants A and B:
$$R_f \propto [A]^a [B]^b \implies R_f = k_f [A]^a [B]^b$$
where $k_f$ is the rate constant for the forward reaction.

Similarly, the rate of the backward reaction ($R_b$) is proportional to the active masses of products C and D:
$$R_b \propto [C]^c [D]^d \implies R_b = k_b [C]^c [D]^d$$
where $k_b$ is the rate constant for the backward reaction.

At equilibrium, $R_f = R_b$:
$$k_f [A]^a [B]^b = k_b [C]^c [D]^d$$
$$\frac{k_f}{k_b} = \frac{[C]^c [D]^d}{[A]^a [B]^b} = K_c$$

Here, $K_c$ is the **Equilibrium Constant** expressed in terms of concentration. This derivation shows how the law of mass action quantitatively defines the equilibrium state of a system.

---

---

### Q.6(c) Deduce $K_p$ for the reaction: $N_2 + 3H_2 \rightleftharpoons 2NH_3$, using known amount of reactants initially. (04)

**Answer:**

**Derivation of $K_p$ for the Synthesis of Ammonia (Haber Process):**
Consider the formation of ammonia from nitrogen and hydrogen gases:
$$N_2(g) + 3H_2(g) \rightleftharpoons 2NH_3(g)$$

Let us start with $a$ moles of $N_2$ and $b$ moles of $H_2$ in a closed vessel. Let $x$ moles of $N_2$ react to reach equilibrium.
According to the stoichiometry (1:3:2 ratio), $x$ moles of $N_2$ will react with $3x$ moles of $H_2$ to form $2x$ moles of $NH_3$.

| State | $N_2$ | $H_2$ | $NH_3$ |
| :--- | :--- | :--- | :--- |
| **Initial Moles** | $a$ | $b$ | $0$ |
| **Equilibrium Moles** | $a - x$ | $b - 3x$ | $2x$ |

Total number of moles at equilibrium, $n_{total} = (a - x) + (b - 3x) + 2x = a + b - 2x$

Let $P$ be the total pressure of the equilibrium mixture.
According to Dalton's Law of Partial Pressures, the partial pressure of a gas ($p_i$) is equal to its mole fraction ($X_i$) multiplied by the total pressure ($P$).
$$p_i = X_i \times P = \left(\frac{n_i}{n_{total}}\right) \times P$$

Therefore, the equilibrium partial pressures are:
*   $p_{N_2} = \left( \frac{a - x}{a + b - 2x} \right) P$
*   $p_{H_2} = \left( \frac{b - 3x}{a + b - 2x} \right) P$
*   $p_{NH_3} = \left( \frac{2x}{a + b - 2x} \right) P$

The equilibrium constant in terms of partial pressures ($K_p$) is given by the law of mass action:
$$K_p = \frac{(p_{NH_3})^2}{(p_{N_2})(p_{H_2})^3}$$

Substituting the partial pressure expressions into the equation:
$$K_p = \frac{\left( \frac{2x \cdot P}{a + b - 2x} \right)^2}{\left( \frac{(a - x) \cdot P}{a + b - 2x} \right) \left( \frac{(b - 3x) \cdot P}{a + b - 2x} \right)^3}$$

$$K_p = \frac{\frac{4x^2 \cdot P^2}{(a + b - 2x)^2}}{\frac{(a - x)(b - 3x)^3 \cdot P^4}{(a + b - 2x)^4}}$$

Simplifying the expression by canceling terms:
$$K_p = \frac{4x^2 (a + b - 2x)^2}{(a - x)(b - 3x)^3 P^2}$$

This is the exact general expression for $K_p$. 

*(Note: If the initial mixture is strictly stoichiometric, i.e., $a=1, b=3$, the equation simplifies further: $n_{total} = 4 - 2x$, and $K_p = \frac{16x^2 (2-x)^2}{27(1-x)^4 P^2}$).*

---

---

## 📄 Source: 2023 Exam

### Q.8(a) Apply your acquired knowledge from Le-chatelier-Braun principle to the production of ammonia by Haber process. (05)

**Answer:**

**Haber Process for the Production of Ammonia:**
The industrial synthesis of ammonia ($NH_3$) from nitrogen and hydrogen gases is a reversible, exothermic process accompanied by a decrease in volume:
$$N_2(g) + 3H_2(g) \rightleftharpoons 2NH_3(g); \quad \Delta H = -92.4 \text{ kJ/mol}$$
*(1 volume + 3 volumes $\rightleftharpoons$ 2 volumes)*

To maximize the yield of ammonia, we apply **Le Chatelier's Principle** to optimize the reaction conditions:

1.  **Effect of Temperature:** Since the forward reaction is exothermic (releases heat), Le Chatelier's principle states that lowering the temperature will shift the equilibrium to the right to counteract the cooling, favoring $NH_3$ production. However, at very low temperatures, the kinetic energy of molecules is too low, and the reaction becomes impractically slow. Therefore, a compromise **optimum temperature of about $450^\circ C$ to $500^\circ C$** is used to ensure a respectable yield at a fast rate.
2.  **Effect of Pressure:** The reaction proceeds with a decrease in the number of gaseous moles (from 4 moles of reactants to 2 moles of products), which means a decrease in volume. According to Le Chatelier's principle, applying high pressure will shift the equilibrium in the direction of smaller volume (forward direction) to relieve the pressure. Thus, a very **high pressure of $200$ to $250 \text{ atmospheres}$** is utilized to maximize the yield.
3.  **Effect of Concentration:** Increasing the concentration of the reactants will drive the system to consume them by shifting the equilibrium to the right. In the Haber process, the yield is enhanced by constantly pumping in excess $N_2$ and $H_2$. Furthermore, the product **$NH_3$ is continuously removed** from the system by liquefaction, preventing the backward reaction and forcing the forward reaction to proceed continuously.
4.  **Role of Catalyst:** To compensate for the "compromise" low temperature, a catalyst is essential to speed up the attainment of equilibrium. Finely divided **Iron (Fe)** is used as the catalyst, often promoted by **Molybdenum (Mo)** to increase its efficiency.

---

---

### Q.8(b) Mention law of mass action. (02)

**Answer:**

**Statement of the Law of Mass Action:**
The Law of Mass Action states that *"At a given constant temperature, the rate of a chemical reaction at any instant is directly proportional to the product of the active masses (molar concentrations or partial pressures) of the reacting substances, with each concentration term raised to a power equal to its stoichiometric coefficient in the balanced chemical equation."*

---

---

### Q.8(c) What are reversible and irreversible reactions? (03)

**Answer:**

**Reversible Reactions:**
These are chemical reactions that take place in both the forward and backward directions simultaneously under the same conditions. Reactants combine to form products, and those same products can react with each other to reform the original reactants. They are usually carried out in closed vessels and never go to 100% completion; instead, they eventually reach a state of dynamic equilibrium. 
*   *Example:* The synthesis of ammonia: $N_2(g) + 3H_2(g) \rightleftharpoons 2NH_3(g)$

**Irreversible Reactions:**
These are chemical reactions that proceed in only one direction (the forward direction) and continue until one of the reactants is completely exhausted. The products formed do not react back to produce the original reactants under the given conditions. They typically involve the formation of a precipitate or the escape of a gas in an open vessel.
*   *Example:* Thermal decomposition of potassium chlorate: $2KClO_3(s) \xrightarrow{\Delta} 2KCl(s) + 3O_2(g)\uparrow$

---

## 📄 Source: 2021 Exam

### Q.2(c) Apply Le Chatelier's principle to work out the optimum conditions for securing the maximum yield of ammonia in industrial process. (04)

**Answer:**

**Haber Process for the Production of Ammonia:**
$$N_2(g) + 3H_2(g) \rightleftharpoons 2NH_3(g); \quad \Delta H = -92.4 \text{ kJ/mol}$$
*(1 volume + 3 volumes $\rightleftharpoons$ 2 volumes)*

Applying **Le Chatelier's Principle** to maximize $NH_3$ yield:
1.  **Temperature:** The forward reaction is exothermic. According to Le Chatelier, lowering the temperature shifts the equilibrium to the right, favoring $NH_3$ production. However, at very low temperatures, the reaction is too slow. Thus, a compromise **optimum temperature of $450^\circ C - 500^\circ C$** is maintained.
2.  **Pressure:** The reaction proceeds with a decrease in volume (from 4 gaseous moles to 2). Applying high pressure shifts the equilibrium in the direction of smaller volume (forward direction). Thus, an **optimum high pressure of $200 - 250 \text{ atm}$** is utilized.
3.  **Concentration:** Continuously adding excess $N_2$ and $H_2$ drives the equilibrium forward. Furthermore, continuously **removing the product $NH_3$** (by liquefaction) prevents the backward reaction, ensuring maximum yield.
4.  **Catalyst:** Finely divided Iron (Fe) with a Molybdenum (Mo) promoter is used to quickly establish equilibrium at the compromised low temperature.

---

---

### Q.4(c) Define chemical equilibrium. Why chemical equilibrium is called a dynamic equilibrium? (04)

**Answer:**

**Chemical Equilibrium:**
Chemical equilibrium is the state of a reversible reaction in a closed system where the rate of the forward reaction becomes exactly equal to the rate of the backward (reverse) reaction. At this state, the concentrations of reactants and products remain constant over time, and macroscopic properties like pressure, color, and temperature stop changing.

**Why is it called a dynamic equilibrium?**
In some physical systems, equilibrium implies a static state where all motion has stopped. However, chemical equilibrium is termed "dynamic" because the chemical reactions have **not** ceased. 
At equilibrium, the reactant molecules are still continuously colliding to form products (forward reaction), and the product molecules are continuously colliding to reform reactants (backward reaction). Because these two opposing processes are occurring at exactly the same speed ($Rate_{forward} = Rate_{backward}$), their macroscopic effects perfectly cancel each other out. There is constant microscopic activity, but zero net change, hence it is a "dynamic" balance.

---

## SECTION-B

---

## 📄 Source: 2020 Exam

### Q.3(a) What is chemical equilibrium? State and explain law of mass action. (04)

**Answer:**

**Chemical Equilibrium:**
Chemical equilibrium is the dynamic state of a reversible reaction in a closed system where the rate of the forward reaction becomes exactly equal to the rate of the backward (reverse) reaction. At this state, there is no net change in the measurable macroscopic properties of the system, such as concentrations, pressure, or color, over time.

**Law of Mass Action:**
*   **Statement:** *"At a given constant temperature, the rate of a chemical reaction is directly proportional to the product of the active masses (molar concentrations or partial pressures) of the reacting substances, with each concentration term raised to a power equal to its stoichiometric coefficient in the balanced chemical equation."*
*   **Explanation:** For a general reversible reaction: $aA + bB \rightleftharpoons cC + dD$
    The rate of the forward reaction ($R_f$) is proportional to $[A]^a [B]^b \implies R_f = k_f [A]^a [B]^b$
    The rate of the backward reaction ($R_b$) is proportional to $[C]^c [D]^d \implies R_b = k_b [C]^c [D]^d$
    At equilibrium, $R_f = R_b$:
    $k_f [A]^a [B]^b = k_b [C]^c [D]^d$
    $\frac{k_f}{k_b} = \frac{[C]^c [D]^d}{[A]^a [B]^b} = K_c$ (Equilibrium Constant).

---

---

### Q.3(b) Discuss the application of La-Chatelier-Brown principle to industrial reactions. (05)

**Answer:**

Le Chatelier's Principle states that if a dynamic equilibrium is disturbed by changing conditions (temperature, pressure, or concentration), the position of equilibrium shifts to counteract the change. This is widely applied in chemical industries to maximize the yield of desired products.

**1. Application in the Haber Process (Synthesis of Ammonia):**
Reaction: $N_2(g) + 3H_2(g) \rightleftharpoons 2NH_3(g); \quad \Delta H = -92.4 \text{ kJ/mol}$
*   **Temperature:** The forward reaction is exothermic. Lower temperatures favor $NH_3$ formation. However, to maintain a fast reaction rate, an optimum compromise temperature of $\approx 450^\circ C$ is used.
*   **Pressure:** The reaction involves a volume decrease (4 moles $\rightarrow$ 2 moles). High pressure shifts the equilibrium forward. Thus, an optimum high pressure of $200-250 \text{ atm}$ is applied.
*   **Concentration:** Constantly removing $NH_3$ by liquefaction and pumping in excess $N_2$ and $H_2$ continuously drives the reaction forward.

**2. Application in the Contact Process (Synthesis of Sulfuric Acid):**
Reaction: $2SO_2(g) + O_2(g) \rightleftharpoons 2SO_3(g); \quad \Delta H = -196 \text{ kJ/mol}$
*   **Temperature:** Exothermic reaction. Again, a compromise temperature of $\approx 450^\circ C$ is maintained for optimal yield and rate.
*   **Pressure:** Volume decreases (3 moles $\rightarrow$ 2 moles). High pressure favors $SO_3$ formation. A pressure of $1-2 \text{ atm}$ is generally sufficient due to high catalyst efficiency.
*   **Concentration:** Adding an excess of $O_2$ (air) drives the equilibrium to the right, maximizing the conversion of $SO_2$ to $SO_3$.

---

---

### Q.3(c) What are reversible and irreversible reactions? Give examples. (03)

**Answer:**

**Reversible Reactions:**
These are reactions that take place in both the forward and backward directions simultaneously under the same conditions. Reactants combine to form products, and those same products can react to reform the original reactants. They are usually carried out in closed vessels and never go to 100% completion, establishing a dynamic equilibrium. 
*   *Example:* Synthesis of ammonia: $N_2(g) + 3H_2(g) \rightleftharpoons 2NH_3(g)$

**Irreversible Reactions:**
These are reactions that proceed in only one direction (the forward direction) and continue until the limiting reactant is completely exhausted. The products formed do not react back to produce the original reactants under the given conditions. They typically occur in open vessels where a gas escapes or a precipitate forms.
*   *Example:* Thermal decomposition of potassium chlorate in an open vessel: $2KClO_3(s) \xrightarrow{\Delta} 2KCl(s) + 3O_2(g)\uparrow$

---

---

## 📄 Source: 2019 Exam

### Q.4(a) Discuss the influence of temperature on equilibrium constant with mathematical expression. (08)

**Answer:**

**Influence of Temperature on Equilibrium:**
The equilibrium constant ($K_p$ or $K_c$) is independent of pressure, volume, and concentration, but it is strictly dependent on the temperature of the system. Changing the temperature fundamentally changes the value of the equilibrium constant. The direction of the shift is governed by Le Chatelier's Principle and depends on whether the forward reaction is exothermic or endothermic:

1.  **Exothermic Reactions ($\Delta H < 0$):**
    An increase in temperature supplies heat to the system. According to Le Chatelier, the system shifts to absorb this heat by favoring the backward (endothermic) direction. Consequently, the concentration of reactants increases, and the concentration of products decreases. Therefore, **for exothermic reactions, the equilibrium constant ($K$) decreases as temperature increases.**
2.  **Endothermic Reactions ($\Delta H > 0$):**
    An increase in temperature supplies heat. The system shifts to absorb it by favoring the forward (endothermic) direction. The concentration of products increases. Therefore, **for endothermic reactions, the equilibrium constant ($K$) increases as temperature increases.**

**Mathematical Expression (van 't Hoff Equation):**
The exact quantitative relationship between the equilibrium constant and absolute temperature is given by the van 't Hoff equation, derived from thermodynamics ($\Delta G^\circ = -RT \ln K$ and the Gibbs-Helmholtz equation):

The differential form of the van 't Hoff equation is:
$$\frac{d(\ln K_p)}{dT} = \frac{\Delta H^\circ}{RT^2}$$
*(Where $\Delta H^\circ$ is the standard enthalpy of reaction, $R$ is the gas constant, and $T$ is the absolute temperature).*

By integrating this equation between two temperatures, $T_1$ and $T_2$ (assuming $\Delta H^\circ$ remains constant over this temperature range), we obtain the integrated form:
$$\int_{K_{p1}}^{K_{p2}} d(\ln K_p) = \frac{\Delta H^\circ}{R} \int_{T_1}^{T_2} \frac{dT}{T^2}$$

$$\ln K_{p2} - \ln K_{p1} = \frac{\Delta H^\circ}{R} \left[ -\frac{1}{T} \right]_{T_1}^{T_2}$$

$$\ln \left( \frac{K_{p2}}{K_{p1}} \right) = \frac{\Delta H^\circ}{R} \left( \frac{1}{T_1} - \frac{1}{T_2} \right)$$
or, using common logarithms ($\log_{10}$):
$$\log \left( \frac{K_{p2}}{K_{p1}} \right) = \frac{\Delta H^\circ}{2.303 R} \left( \frac{T_2 - T_1}{T_1 T_2} \right)$$

This mathematical expression proves the qualitative statements above: If $\Delta H^\circ$ is positive (endothermic) and $T_2 > T_1$, the right side is positive, meaning $\log(K_{p2}/K_{p1}) > 0$, hence $K_{p2} > K_{p1}$.

---

---

### Q.4(b) Calculate the value of $K_p$ for a reaction which has $\Delta G^\circ$ value -20kcal/mole at $25^\circ C$. (04)

**Answer:**

**Given Data:**
*   Standard Gibbs Free Energy Change ($\Delta G^\circ$) = $-20 \text{ kcal/mole} = -20,000 \text{ cal/mole}$
*   Temperature ($T$) = $25^\circ C = 25 + 273.15 = 298.15 \text{ K}$
*   Universal gas constant ($R$) = $1.987 \text{ cal K}^{-1}\text{mole}^{-1}$

**Solution:**
The fundamental thermodynamic relationship between standard free energy change and the equilibrium constant ($K_p$) is:
$$\Delta G^\circ = -RT \ln K_p$$
or, using base 10 logarithms:
$$\Delta G^\circ = -2.303 RT \log K_p$$

Substitute the given values into the equation:
$$-20,000 = -2.303 \times 1.987 \times 298.15 \times \log K_p$$
$$-20,000 = -1364.3 \times \log K_p$$

Rearranging to solve for $\log K_p$:
$$\log K_p = \frac{-20,000}{-1364.3}$$
$$\log K_p = 14.659$$

Now, calculate $K_p$ by taking the antilog:
$$K_p = 10^{14.659}$$
$$K_p = 10^{0.659} \times 10^{14}$$
$$K_p = 4.56 \times 10^{14}$$

**Final Answer:** The value of the equilibrium constant $K_p$ is **$4.56 \times 10^{14}$**.

---

## SECTION-B

---

### Q.6(c) What is reversible reaction? (02)

**Answer:**

**Reversible Reaction:**
A reversible reaction is a chemical reaction that can take place in both the forward and backward directions simultaneously under the exact same conditions. In these reactions, the reactants combine to form products, and as soon as products are formed, they begin reacting with each other to reform the original reactants. They never go to absolute completion and eventually establish a state of dynamic chemical equilibrium.
*   *Example:* $H_2(g) + I_2(g) \rightleftharpoons 2HI(g)$

---

---

## 📄 Source: 2018 Exam

### Q3(a) For $aA + bB + \dots \rightleftharpoons mM + nN + \dots$ reaction, derive equations for $K_p$, $K_c$ and $K_x$ and also find relation among them. (06)

**Answer:**
For the general reversible gaseous reaction:
$$aA + bB \rightleftharpoons mM + nN$$

**1. Equation for $K_c$ (using Molar Concentration):**
Applying the Law of Mass Action, the equilibrium constant in terms of molar concentrations (denoted by square brackets $[ ]$ or $C$) is:
$$K_c = \frac{[M]^m [N]^n}{[A]^a [B]^b} = \frac{C_M^m C_N^n}{C_A^a C_B^b}$$

**2. Equation for $K_p$ (using Partial Pressure):**
For gases, partial pressure ($P$) is directly proportional to concentration. The equilibrium constant in terms of partial pressures is:
$$K_p = \frac{P_M^m P_N^n}{P_A^a P_B^b}$$

**3. Equation for $K_x$ (using Mole Fraction):**
The equilibrium constant in terms of mole fractions ($X$) is:
$$K_x = \frac{X_M^m X_N^n}{X_A^a X_B^b}$$

**Relationship among $K_p$, $K_c$, and $K_x$:**
**Relation between $K_p$ and $K_c$:**
Assuming ideal gas behavior, $PV = nRT \implies P = (n/V)RT = CRT$.
Therefore, the partial pressures are:
$P_A = C_A RT, \quad P_B = C_B RT, \quad P_M = C_M RT, \quad P_N = C_N RT$
Substituting these into the $K_p$ expression:
$$K_p = \frac{(C_M RT)^m (C_N RT)^n}{(C_A RT)^a (C_B RT)^b}$$
$$K_p = \frac{C_M^m C_N^n}{C_A^a C_B^b} \times \frac{(RT)^{m+n}}{(RT)^{a+b}}$$
$$K_p = K_c (RT)^{(m+n) - (a+b)}$$
Let $\Delta n = (m+n) - (a+b)$, which is the difference in the number of moles of gaseous products and gaseous reactants.
**$$K_p = K_c (RT)^{\Delta n}$$**

**Relation between $K_p$ and $K_x$:**
According to Dalton's Law of partial pressures, the partial pressure of a gas is its mole fraction multiplied by the total pressure ($P_{total}$ or simply $P$):
$P_A = X_A P, \quad P_B = X_B P, \quad P_M = X_M P, \quad P_N = X_N P$
Substituting these into the $K_p$ expression:
$$K_p = \frac{(X_M P)^m (X_N P)^n}{(X_A P)^a (X_B P)^b}$$
$$K_p = \frac{X_M^m X_N^n}{X_A^a X_B^b} \times \frac{P^{m+n}}{P^{a+b}}$$
**$$K_p = K_x P^{\Delta n}$$**

---

---

### Q3(b) For the following reaction $PCl_5 \rightleftharpoons PCl_3 + Cl_2$, derive equation for $K_p$ and $K_c$ and also find the effects of pressure and volume on it. (06)

**Answer:**
**Reaction:** $PCl_5(g) \rightleftharpoons PCl_3(g) + Cl_2(g)$
Let the initial number of moles of $PCl_5$ be $1$ in a closed vessel of volume $V$. Let $\alpha$ be the degree of dissociation at equilibrium.

| | $PCl_5$ | $\rightleftharpoons$ | $PCl_3$ | $+$ | $Cl_2$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Initial Moles | 1 | | 0 | | 0 |
| Moles at Eq. | $1 - \alpha$ | | $\alpha$ | | $\alpha$ |

Total number of moles at equilibrium = $(1 - \alpha) + \alpha + \alpha = 1 + \alpha$. Let total pressure be $P$.

**1. Derivation for $K_c$:**
Equilibrium molar concentrations:
$[PCl_5] = \frac{1-\alpha}{V}, \quad [PCl_3] = \frac{\alpha}{V}, \quad [Cl_2] = \frac{\alpha}{V}$
$$K_c = \frac{[PCl_3][Cl_2]}{[PCl_5]} = \frac{(\frac{\alpha}{V}) (\frac{\alpha}{V})}{\frac{1-\alpha}{V}}$$
**$$K_c = \frac{\alpha^2}{(1 - \alpha)V}$$**

**2. Derivation for $K_p$:**
Partial pressures = Mole fraction $\times$ Total Pressure ($P$):
$P_{PCl_5} = \frac{1-\alpha}{1+\alpha}P, \quad P_{PCl_3} = \frac{\alpha}{1+\alpha}P, \quad P_{Cl_2} = \frac{\alpha}{1+\alpha}P$
$$K_p = \frac{P_{PCl_3} \cdot P_{Cl_2}}{P_{PCl_5}} = \frac{ \left( \frac{\alpha}{1+\alpha}P \right) \left( \frac{\alpha}{1+\alpha}P \right) }{ \frac{1-\alpha}{1+\alpha}P }$$
**$$K_p = \frac{\alpha^2 P}{1 - \alpha^2}$$**

**Effects of Pressure and Volume (Le Chatelier's Principle):**
1.  **Effect of Pressure:** The forward reaction results in an increase in the number of gaseous moles (1 mole $\rightarrow$ 2 moles), implying an increase in volume. If external **pressure is increased**, the system will shift in the direction that produces fewer moles of gas to relieve the stress. Thus, it shifts backward, decreasing the dissociation of $PCl_5$ ($\alpha$ decreases).
2.  **Effect of Volume:** An increase in the volume of the vessel results in a decrease in pressure. The system will shift in the direction that produces more moles of gas to re-establish pressure. Thus, **increasing the volume** shifts the equilibrium in the forward direction, favoring the dissociation of $PCl_5$ ($\alpha$ increases).

---

---

### Q6(a) State and explain the law of mass action. (03)

**Answer:**
**Statement:** Formulated by Guldberg and Waage, the Law of Mass Action states that: "At a constant temperature, the rate of a chemical reaction is directly proportional to the product of the active masses (molar concentrations) of the reacting substances, with each concentration term raised to a power equal to its stoichiometric coefficient in the balanced chemical equation."

**Explanation:**
Consider a general reversible reaction:
$$aA + bB \rightleftharpoons cC + dD$$
According to the law of mass action:
*   Rate of the forward reaction ($R_f$) $\propto [A]^a [B]^b \implies R_f = k_f [A]^a [B]^b$
*   Rate of the backward reaction ($R_b$) $\propto [C]^c [D]^d \implies R_b = k_b [C]^c [D]^d$
(Where $[ ]$ denotes active mass or molar concentration, and $k_f, k_b$ are velocity constants).
At equilibrium, $R_f = R_b$, which leads to the derivation of the equilibrium constant $K_c = \frac{k_f}{k_b} = \frac{[C]^c [D]^d}{[A]^a [B]^b}$.

---

---

### Q6(b) Derive the expression $\Delta G^\circ = -2.303 RT \log K_p$ and comment on it. (05)

**Answer:**

**Derivation:**
From fundamental chemical thermodynamics, the relationship between the Free Energy change ($\Delta G$) of a system at any given moment and its Standard Free Energy change ($\Delta G^\circ$) is given by the reaction isotherm equation:
$$\Delta G = \Delta G^\circ + RT \ln Q$$
Where:
*   $Q$ is the reaction quotient (the ratio of partial pressures of products to reactants at any given moment).
*   $R$ is the universal gas constant.
*   $T$ is the absolute temperature.

When the chemical reaction eventually reaches **equilibrium**, the system's free energy is at a minimum, meaning it can do no more net work. Therefore, at equilibrium:
1.  **$\Delta G = 0$**
2.  The reaction quotient ($Q$) becomes exactly equal to the thermodynamic equilibrium constant (**$K_p$**).

Substituting these equilibrium conditions into the thermodynamic equation:
$$0 = \Delta G^\circ + RT \ln K_p$$
Rearranging the equation to solve for $\Delta G^\circ$:
$$\Delta G^\circ = -RT \ln K_p$$
To convert the natural logarithm ($\ln$, base $e$) to the common logarithm ($\log$, base $10$), we multiply by $2.303$:
**$$\Delta G^\circ = -2.303 RT \log K_p$$**

**Comment on the Expression:**
This is one of the most vitally important equations in physical chemistry because it bridges the gap between pure thermodynamics ($\Delta G^\circ$) and chemical kinetics/equilibrium ($K_p$). 
It allows us to mathematically predict the feasibility and extent of a chemical reaction before even performing it:
*   If **$\Delta G^\circ$ is highly negative**, the math dictates that $\log K_p$ must be a large positive number, meaning **$K_p \gg 1$**. The reaction is highly spontaneous and proceeds almost to completion (favoring products).
*   If **$\Delta G^\circ$ is highly positive**, $\log K_p$ is negative, so **$K_p \ll 1$**. The reaction is highly non-spontaneous and hardly proceeds at all (favoring reactants).

---

---

### Q6(c) Calculate the value of $K_p$ for a reaction which has $\Delta G^\circ$ value -20 Kcal/mole at $25^\circ C$. (04)

**Answer:**

**Given Data:**
*   Standard Gibbs Free Energy Change ($\Delta G^\circ$) = $-20 \text{ kcal/mole} = -20,000 \text{ cal/mole}$
*   Temperature ($T$) = $25^\circ C = 25 + 273.15 = 298.15 \text{ K}$
*   Universal gas constant ($R$) = $1.987 \text{ cal K}^{-1}\text{mole}^{-1}$

**Solution:**
Using the equation derived above:
$$\Delta G^\circ = -2.303 RT \log K_p$$
$$-20,000 = -2.303 \times 1.987 \times 298.15 \times \log K_p$$
$$-20,000 = -1364.3 \times \log K_p$$
$$\log K_p = \frac{-20,000}{-1364.3} = 14.659$$
$$K_p = 10^{14.659} = 10^{0.659} \times 10^{14} = 4.56 \times 10^{14}$$

**Final Answer:** The value of the equilibrium constant $K_p$ is **$4.56 \times 10^{14}$**.

---

---

## 📄 Source: 2017 Exam

### Q8(a) Define reversible reaction. Why chemical equilibrium is called a dynamic equilibrium? (04)

**Answer:**
**Reversible Reaction:** A chemical reaction that does not go to completion and can proceed simultaneously in both the forward direction (reactants to products) and the backward direction (products to reactants) under the exact same experimental conditions. Example: $N_2(g) + 3H_2(g) \rightleftharpoons 2NH_3(g)$.

**Why Equilibrium is "Dynamic":**
Chemical equilibrium is termed "dynamic" rather than "static" because, at the equilibrium point, the chemical reactions have absolutely not ceased. At the microscopic level, reactant molecules are constantly colliding to form products (forward reaction), and product molecules are constantly colliding to break back down into reactants (backward reaction).
However, equilibrium is reached when the *velocity* of the forward reaction perfectly equals the *velocity* of the backward reaction ($R_f = R_b$). Because these opposing processes are occurring at the exact same rate, there is zero net change in the macroscopic concentrations of any species. It outwardly *appears* as if the reaction has stopped (static), but it is actually a state of fierce, perfectly balanced continuous motion (dynamic).

---

---

### Q8(b) Derive the $K_c$ and $K_p$ expressions for the reaction $PCl_5(g) \rightleftharpoons PCl_3(g) + Cl_2(g)$ and explain the effect of pressure on the equilibrium. (04)

**Answer:**
*(Note: The full derivation was detailed in the 2018 Exam, Section A, Q3(b). For brevity, the final results are presented here as requested by the 4-mark weight).*

**Reaction:** $PCl_5(g) \rightleftharpoons PCl_3(g) + Cl_2(g)$
Let initial moles of $PCl_5$ be $1$, degree of dissociation be $\alpha$, total pressure be $P$, and volume be $V$.
At equilibrium, moles are: $PCl_5 = (1-\alpha)$, $PCl_3 = \alpha$, $Cl_2 = \alpha$. Total moles = $(1+\alpha)$.

**1. Expression for $K_c$ (Concentration):**
$$K_c = \frac{[PCl_3][Cl_2]}{[PCl_5]} = \frac{(\alpha/V)(\alpha/V)}{(1-\alpha)/V}$$
**$$K_c = \frac{\alpha^2}{(1 - \alpha)V}$$**

**2. Expression for $K_p$ (Partial Pressure):**
$$K_p = \frac{P_{PCl_3} \cdot P_{Cl_2}}{P_{PCl_5}} = \frac{ \left( \frac{\alpha}{1+\alpha}P \right) \left( \frac{\alpha}{1+\alpha}P \right) }{ \frac{1-\alpha}{1+\alpha}P }$$
**$$K_p = \frac{\alpha^2 P}{1 - \alpha^2}$$**

**Effect of Pressure on Equilibrium:**
According to Le Chatelier's Principle, increasing the pressure of a system forces it to shift in the direction that reduces the total pressure (the direction with fewer gaseous moles).
In this reaction: $1 \text{ mole} (PCl_5) \rightleftharpoons 2 \text{ moles} (PCl_3 + Cl_2)$.
The forward reaction produces more moles. Therefore, an **increase in pressure** will shift the equilibrium in the **backward direction**. This suppresses the dissociation of $PCl_5$, decreasing the value of $\alpha$.

---

---

### Q8(c) State and explain the characteristics of chemical equilibrium. (04)

**Answer:**
The state of chemical equilibrium possesses several distinct, fundamental characteristics:

1.  **Equality of Rates:** It is the exact point where the velocity of the forward reaction becomes absolutely equal to the velocity of the backward reaction.
2.  **Constancy of Observable Properties:** Once equilibrium is established, all macroscopic, measurable properties of the system (such as pressure, concentration, color intensity, and density) remain perfectly constant indefinitely, provided the temperature remains unchanged.
3.  **Dynamic Nature:** The equilibrium is not static. The opposing chemical reactions are continuously occurring at the molecular level, but their equal rates result in zero net macroscopic change.
4.  **Reversibility of Approach:** The exact same equilibrium state can be achieved regardless of the direction from which it is approached (i.e., whether you start with pure reactants or pure products).
5.  **Requirement of a Closed System:** True thermodynamic equilibrium can only be achieved and maintained in a completely closed vessel where no reactants or products can escape into the surroundings.
6.  **Effect of a Catalyst:** A positive catalyst alters the activation energy, speeding up *both* the forward and backward reactions by the exact same proportion. It helps the system attain equilibrium much faster, but it absolutely does not change the final equilibrium concentrations or the value of the equilibrium constant.

---
