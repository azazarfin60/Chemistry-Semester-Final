*(start)* | [🏠 Index](index.md) | [02-Chemical-Equilibrium ➡](02-Chemical-Equilibrium.md)

---

# Chemical Kinetics
**Priority:** 🔴 CRITICAL | **Frequency:** 25 sub-parts across 7/7 exams + CT03

> **Topics Covered:** Rate of reaction, rate law, order, molecularity, 1st/2nd order derivations, half-life, pseudo-order, Arrhenius equation, activated complex theory.

---

## 📄 Source: 2024 Exam

### Q.5(a) Differentiate between order and molecularity. (03)

**Answer:**

| Feature | Order of Reaction | Molecularity of Reaction |
| :--- | :--- | :--- |
| **Definition** | It is the sum of the powers of the concentration terms of the reacting species in the experimentally determined rate equation. | It is the total number of reacting species (molecules, atoms, or ions) that collide simultaneously to bring about a chemical change in an elementary step. |
| **Nature of Value** | It can be a whole number, zero, or even a fractional value. | It is always a whole number (1, 2, or 3). It cannot be zero or fractional. |
| **Derivation** | It is a purely experimental quantity and cannot be deduced simply from the balanced chemical equation. | It is a theoretical concept that can be determined simply by looking at the reaction mechanism's elementary steps. |
| **Applicability** | It is meant for the overall reaction and represents the true dependence of rate on concentration. | It is meaningful only for simple (elementary) reactions or individual steps of a complex reaction, not for the overall complex reaction. |

---

---

### Q.5(b) Derive the mathematical expression $K = \frac{2.303}{t_2 - t_1} \log \frac{a-x_1}{a-x_2}$ for a first order reaction. (04)

**Answer:**

**Derivation:**
Consider a general first-order reaction:
$A \rightarrow \text{Products}$

Let the initial concentration of reactant A at time $t = 0$ be $a \text{ mol/L}$.
Let the amount of A reacted at time $t_1$ be $x_1$. Then the concentration of A remaining at time $t_1$ is $(a - x_1)$.
Let the amount of A reacted at time $t_2$ be $x_2$. Then the concentration of A remaining at time $t_2$ is $(a - x_2)$.

According to the rate law for a first-order reaction, the rate of reaction is directly proportional to the concentration of the reactant:
$$-\frac{d[A]}{dt} = K[A]$$
where $K$ is the first-order rate constant.

Replacing $[A]$ with $(a-x)$ and $-d[A]$ with $dx$:
$$\frac{dx}{dt} = K(a-x)$$
$$\frac{dx}{a-x} = K dt$$

Integrating both sides within the time limits $t_1$ to $t_2$, and corresponding concentration limits $x_1$ to $x_2$:
$$\int_{x_1}^{x_2} \frac{dx}{a-x} = K \int_{t_1}^{t_2} dt$$

$$[-\ln(a-x)]_{x_1}^{x_2} = K [t]_{t_1}^{t_2}$$

$$- [\ln(a-x_2) - \ln(a-x_1)] = K (t_2 - t_1)$$

$$\ln(a-x_1) - \ln(a-x_2) = K (t_2 - t_1)$$

$$\ln \left( \frac{a-x_1}{a-x_2} \right) = K (t_2 - t_1)$$

Converting the natural logarithm ($\ln$) to base-10 logarithm ($\log$) by multiplying by 2.303:
$$2.303 \log \left( \frac{a-x_1}{a-x_2} \right) = K (t_2 - t_1)$$

Rearranging for the rate constant $K$:
$$K = \frac{2.303}{t_2 - t_1} \log \frac{a-x_1}{a-x_2}$$
*(This expression represents the rate constant evaluated between any two time intervals during the reaction).*

---

---

### Q.5(c) The half life of a first order reaction is 100 seconds. What is the time required to complete 75% of the reaction? (03)

**Answer:**

**Given Data:**
*   Half-life of the first-order reaction, $t_{1/2} = 100 \text{ s}$
*   Target completion percentage = 75%

**To Find:**
*   Time required, $t_{75\%}$

**Solution:**
**Step 1: Calculate the rate constant ($k$)**
For a first-order reaction, the half-life is independent of the initial concentration:
$$t_{1/2} = \frac{0.693}{k}$$
$$k = \frac{0.693}{100 \text{ s}} = 0.00693 \text{ s}^{-1}$$

**Step 2: Calculate the time for 75% completion**
Let the initial concentration be $a = 100$.
For 75% completion, the amount reacted $x = 75$.
The remaining concentration is $(a - x) = 100 - 75 = 25$.

The integrated rate equation for a first-order reaction is:
$$t = \frac{2.303}{k} \log \left( \frac{a}{a - x} \right)$$
$$t_{75\%} = \frac{2.303}{0.00693 \text{ s}^{-1}} \log \left( \frac{100}{25} \right)$$
$$t_{75\%} = 332.32 \times \log(4)$$
$$t_{75\%} = 332.32 \times 0.6020$$
$$t_{75\%} = 200 \text{ seconds}$$

*(Alternative logical method: 75% completion means exactly 2 half-lives have passed. After 1st half-life (100s), 50% remains. After 2nd half-life (another 100s), 25% remains, meaning 75% is completed. Total time = 100 + 100 = 200s).*

**Final Answer:** The time required to complete 75% of the reaction is **200 seconds**.

---

---

## 📄 Source: 2023 Exam

### Q.7(a) Define rate constant. Derive an expression for the rate constant of a first order reaction. (06)

**Answer:**

**Rate Constant ($k$):**
The rate constant (or specific reaction rate) is a proportionality constant in the rate law equation. It is numerically equal to the rate of the reaction when the molar concentrations of all the reacting species are strictly unity (1 mol/L). It is independent of concentration but depends heavily on temperature and the presence of a catalyst.

**Derivation for a First-Order Reaction:**
Consider a general first-order reaction where reactant A converts to products:
$A \rightarrow \text{Products}$

Let the initial concentration of reactant A at time $t = 0$ be $a \text{ mol/L}$.
Let $x \text{ mol/L}$ be the amount of A that has reacted after a time interval $t$.
Therefore, the concentration of A remaining at time $t$ is $(a - x) \text{ mol/L}$.

According to the law of mass action and the definition of a first-order reaction, the rate of reaction ($\frac{dx}{dt}$) at any instant $t$ is directly proportional to the remaining concentration of the reactant:
$$\frac{dx}{dt} \propto (a-x)$$
$$\frac{dx}{dt} = k(a-x)$$
where $k$ is the first-order rate constant.

Rearranging the variables to group $x$ on one side and $t$ on the other:
$$\frac{dx}{a-x} = k dt$$

Integrating both sides:
$$\int \frac{dx}{a-x} = k \int dt$$
$$-\ln(a-x) = kt + C \quad \dots \text{(Equation 1)}$$
where $C$ is the integration constant.

To find the value of $C$, we apply the initial boundary conditions:
At $t = 0$, $x = 0$ (no reaction has occurred yet).
Substituting these into Equation 1:
$$-\ln(a-0) = k(0) + C \implies C = -\ln(a)$$

Substitute the value of $C$ back into Equation 1:
$$-\ln(a-x) = kt - \ln(a)$$
$$kt = \ln(a) - \ln(a-x)$$
$$kt = \ln \left(\frac{a}{a-x}\right)$$
$$k = \frac{1}{t} \ln \left(\frac{a}{a-x}\right)$$

Converting the natural logarithm ($\ln$, base $e$) to the common logarithm ($\log$, base 10) by multiplying by 2.303:
$$k = \frac{2.303}{t} \log \left(\frac{a}{a-x}\right)$$

This is the standard integrated rate equation for a first-order reaction.

---

---

### Q.7(b) Why does the reaction rate keep on changing as it proceeds? (02.5)

**Answer:**

The rate of a chemical reaction keeps changing (specifically, decreasing) as it proceeds because the rate is directly proportional to the active mass (concentration) of the reactants. 
As the reaction progresses over time, the reactant molecules are continuously consumed to form products. Therefore, the concentration of the reactants continuously drops. According to collision theory, fewer reactant molecules mean fewer effective collisions occur per unit of time. As the frequency of these successful collisions decreases, the overall rate of the reaction decreases simultaneously. The rate is at its absolute maximum precisely at $t=0$ and asymptotically approaches zero as the reaction nears completion.

---

---

### Q.7(c) Define molecularity. (01.5)

**Answer:**

**Molecularity:**
Molecularity is defined as the total number of reacting species (which can be molecules, atoms, or ions) that must collide simultaneously in a single, elementary step of a chemical reaction to bring about the chemical change. It is a strictly theoretical concept deduced from the reaction mechanism, and it is always a positive whole number (typically 1, 2, or rarely 3). It can never be zero, fractional, or negative.

---

---

## 📄 Source: 2021 Exam

### Q.2(a) Distinguish between order and molecularity of a reaction. (04)

**Answer:**

| Feature | Order of Reaction | Molecularity of Reaction |
| :--- | :--- | :--- |
| **Definition** | It is the sum of the powers of the concentration terms of the reacting species in the experimentally determined rate equation. | It is the total number of reacting species (molecules, atoms, or ions) that collide simultaneously to bring about a chemical change in an elementary step. |
| **Nature of Value** | It can be a whole number, zero, or even a fractional value. | It is always a positive whole number (1, 2, or 3). It cannot be zero or fractional. |
| **Derivation** | It is a purely experimental quantity and cannot be deduced simply from the balanced chemical equation. | It is a theoretical concept that can be determined simply by looking at the reaction mechanism's elementary steps. |
| **Applicability** | It is meant for the overall complex reaction and represents the true dependence of rate on concentration. | It is meaningful only for simple (elementary) reactions or individual steps of a complex reaction, not for the overall complex reaction. |

---

---

### Q.2(b) Prove that, if one of the reactants is present in large excess, the second order reaction shows the first order kinetics. (04)

**Answer:**

**Proof of Pseudo-First Order Kinetics:**
Consider a second-order reaction involving two reactants A and B:
$$A + B \rightarrow \text{Products}$$
Let the initial concentration of A be '$a$' and B be '$b$'. Let '$x$' amount react after time '$t$'.
The integrated rate equation for a general second-order reaction is:
$$k = \frac{1}{t(a-b)} \ln \frac{b(a-x)}{a(b-x)}$$

Now, suppose reactant A is present in a very **large excess** compared to reactant B.
Mathematically, this means: $a \gg b$
Because the maximum amount that can react ($x$) is limited by the limiting reagent B, $x$ cannot be larger than $b$. Since $a$ is much larger than $b$, it is also much larger than $x$:
$$a \gg x$$

Applying these approximations:
*   The term $(a - b)$ approximately equals $a$ (since subtracting a tiny amount $b$ from a massive amount $a$ barely changes it).
*   The term $(a - x)$ approximately equals $a$ (since $x$ is very small compared to $a$).

Substituting these approximations back into the rate equation:
$$k = \frac{1}{t(a)} \ln \frac{b(a)}{a(b-x)}$$

Canceling '$a$' from the numerator and denominator inside the natural logarithm:
$$k = \frac{1}{t \cdot a} \ln \frac{b}{(b-x)}$$

Since the initial concentration '$a$' is present in such a large excess, its concentration remains virtually unchanged throughout the reaction. Thus, '$a$' is essentially a constant. We can group the constants together ($k \cdot a = k'$):
$$k' = \frac{1}{t} \ln \frac{b}{(b-x)}$$

This final equation is exactly the mathematical expression for the integrated rate law of a **first-order reaction**. Therefore, a second-order reaction behaves like a first-order reaction (pseudo-first order) when one reactant is in large excess.

---

---

## 📄 Source: 2020 Exam

### Q.4(a) Define the rate, rate law, order and molecularity of a reaction. (04)

**Answer:**

1.  **Rate of Reaction:** It is the change in the concentration of any one of the reactants or products per unit time. It indicates how fast or slow a chemical reaction is taking place.
2.  **Rate Law:** It is the experimentally determined mathematical expression that relates the rate of a reaction to the molar concentrations of the reactants, with each concentration term raised to some power. (e.g., $Rate = k[A]^x[B]^y$).
3.  **Order of Reaction:** It is the sum of the powers (exponents) of the concentration terms of the reacting species present in the experimentally determined rate law. (e.g., Order = $x + y$). It can be zero, fractional, or an integer.
4.  **Molecularity:** It is defined as the total number of reacting species (molecules, atoms, or ions) that must collide simultaneously in a single, elementary step of a chemical reaction to bring about a chemical change. It is always a positive whole number (1, 2, or 3).

---

---

### Q.4(b) Derive an expression for the rate constant of a second order reaction with two different reactants. (04)

**Answer:**

**Derivation:**
Consider a second-order reaction involving two different reactants:
$$A + B \rightarrow \text{Products}$$

Suppose the initial concentration of A is $a \text{ mol/L}$ and of B is $b \text{ mol/L}$. Let $x \text{ mol/L}$ of both react in time $t$.
Remaining concentrations at time $t$:
$[A] = (a - x)$
$[B] = (b - x)$

The rate of the reaction is proportional to the product of their remaining concentrations:
$$\frac{dx}{dt} = k(a-x)(b-x)$$
where $k$ is the second-order rate constant.

Rearranging the variables:
$$\frac{dx}{(a-x)(b-x)} = k dt$$

Using the method of partial fractions, the left side can be split:
$$\frac{1}{a-b} \left[ \frac{1}{b-x} - \frac{1}{a-x} \right] dx = k dt$$

Integrating both sides:
$$\frac{1}{a-b} \int \left[ \frac{1}{b-x} - \frac{1}{a-x} \right] dx = \int k dt$$
$$\frac{1}{a-b} \left[ -\ln(b-x) - (-\ln(a-x)) \right] = kt + C$$
$$\frac{1}{a-b} \ln \left( \frac{a-x}{b-x} \right) = kt + C \quad \dots \text{(Equation 1)}$$

To find the integration constant $C$, apply initial conditions: at $t = 0, x = 0$.
$$C = \frac{1}{a-b} \ln \left( \frac{a}{b} \right)$$

Substituting $C$ back into Equation 1:
$$\frac{1}{a-b} \ln \left( \frac{a-x}{b-x} \right) = kt + \frac{1}{a-b} \ln \left( \frac{a}{b} \right)$$
$$kt = \frac{1}{a-b} \ln \left( \frac{a-x}{b-x} \right) - \frac{1}{a-b} \ln \left( \frac{a}{b} \right)$$
$$kt = \frac{1}{a-b} \left[ \ln \left( \frac{a-x}{b-x} \right) - \ln \left( \frac{a}{b} \right) \right]$$
$$k = \frac{1}{t(a-b)} \ln \frac{b(a-x)}{a(b-x)}$$

This is the exact integrated rate expression for a second-order reaction with two different initial reactant concentrations.

---

---

### Q.4(c) On what condition, a second order reaction becomes a first order reaction. Explain. (04)

**Answer:**

**Condition:** A second-order reaction becomes a first-order reaction (specifically, a **pseudo-first order reaction**) when one of the reactants is present in a very large excess compared to the other.

**Explanation:**
Consider the second-order rate equation derived above:
$$k = \frac{1}{t(a-b)} \ln \frac{b(a-x)}{a(b-x)}$$

Assume reactant A is present in massive excess, so $a \gg b$.
Because B is the limiting reagent, the maximum amount that can react ($x$) is small. Therefore, $a \gg x$.
Since $a$ is overwhelmingly large, subtracting $b$ or $x$ from it makes virtually no difference:
$(a - b) \approx a$
$(a - x) \approx a$

Substituting these approximations into the rate equation:
$$k = \frac{1}{t \cdot a} \ln \frac{b \cdot a}{a(b-x)}$$
$$k = \frac{1}{t \cdot a} \ln \frac{b}{(b-x)}$$
$$k \cdot a = \frac{1}{t} \ln \frac{b}{(b-x)}$$

Since '$a$' is present in large excess, its concentration remains practically constant throughout the reaction. Thus, $k \cdot a$ is a new constant, $k'$:
$$k' = \frac{1}{t} \ln \frac{b}{(b-x)}$$

This final equation is identical to the integrated rate law for a first-order reaction. The reaction rate now depends only on the concentration of the limiting reactant B. This explains how the condition of a large excess of one reactant causes a second-order reaction to exhibit first-order kinetics.

---

## SECTION-B

---

## 📄 Source: 2019 Exam

### Q.6(a) Define order and molecularity. Derive an expression for the rate constant of a second order reaction. (07)

**Answer:**

**Order of Reaction:** It is the sum of the powers of the concentration terms of the reacting species present in the experimentally determined rate law equation.
**Molecularity:** It is the total number of reacting species (molecules, atoms, or ions) that must collide simultaneously in an elementary step to bring about a chemical reaction.

**Derivation of Rate Constant for a Second Order Reaction:**
Consider a simple second-order reaction involving a single reactant type:
$$2A \rightarrow \text{Products}$$

Let the initial concentration of reactant $A$ be '$a$' mol/L.
After time '$t$', let '$x$' mol/L of $A$ react to form products.
The remaining concentration of $A$ at time $t$ is $(a - x)$ mol/L.

According to the rate law for a second-order reaction, the rate is proportional to the square of the reactant concentration:
$$\frac{dx}{dt} = k(a - x)^2$$
*(where $k$ is the second-order rate constant)*

Rearranging the variables:
$$\frac{dx}{(a - x)^2} = k dt$$

Integrating both sides:
$$\int \frac{dx}{(a - x)^2} = \int k dt$$
$$\frac{1}{a - x} = kt + C \quad \dots \text{(Equation 1)}$$
*(where C is the integration constant)*

To find $C$, we apply the initial conditions: at time $t = 0$, the amount reacted $x = 0$.
Substituting these into Equation 1:
$$\frac{1}{a - 0} = k(0) + C \implies C = \frac{1}{a}$$

Substitute the value of $C$ back into Equation 1:
$$\frac{1}{a - x} = kt + \frac{1}{a}$$
$$kt = \frac{1}{a - x} - \frac{1}{a}$$
$$kt = \frac{a - (a - x)}{a(a - x)}$$
$$kt = \frac{x}{a(a - x)}$$

$$k = \frac{1}{t} \left[ \frac{x}{a(a - x)} \right]$$
This is the integrated rate expression for a second-order reaction involving a single reactant.

---

---

### Q.6(b) Show that a first order reaction is never completed. (03)

**Answer:**

The integrated rate equation for a first-order reaction is:
$$t = \frac{2.303}{k} \log \left( \frac{a}{a-x} \right)$$
Where '$a$' is the initial concentration and '$a-x$' is the concentration remaining at time '$t$'.

If a reaction were to be 100% completed, all of the reactant would be consumed, meaning the amount reacted '$x$' would exactly equal the initial amount '$a$'.
Substituting $x = a$ into the equation to find the time required for completion:
$$t = \frac{2.303}{k} \log \left( \frac{a}{a - a} \right)$$
$$t = \frac{2.303}{k} \log \left( \frac{a}{0} \right)$$
$$t = \frac{2.303}{k} \log (\infty)$$
Since $\log(\infty) = \infty$, then:
$$t = \infty$$
Mathematically, it would take an infinite amount of time for the concentration of the reactant to reach absolute zero. Therefore, a true first-order reaction is never theoretically 100% completed.

---

---

## 📄 Source: 2018 Exam

### Q4(a) Derive equation for $2^{nd}$ order reaction for both type $2A \rightarrow \text{product}$ and $A+B \rightarrow \text{product}$. Also find the properties of a $2^{nd}$ order reaction mathematically. (08)

**Answer:**

**1. Derivation for Type: $2A \rightarrow \text{Products}$**
Let initial concentration of A be $a$ mol/L. After time $t$, $x$ mol/L reacts. Remaining concentration is $(a - x)$.
The rate law is: $\frac{dx}{dt} = k(a - x)^2$
Rearranging and integrating: $\int \frac{dx}{(a - x)^2} = \int k dt$
$\frac{1}{a - x} = kt + C$
At $t = 0, x = 0 \implies C = \frac{1}{a}$
Substituting C: $\frac{1}{a - x} = kt + \frac{1}{a} \implies kt = \frac{1}{a - x} - \frac{1}{a} = \frac{x}{a(a - x)}$
**Integrated equation:** **$k = \frac{1}{t} \left[ \frac{x}{a(a - x)} \right]$**

**2. Derivation for Type: $A + B \rightarrow \text{Products}$ (where $a \neq b$)**
Let initial concentrations of A and B be $a$ and $b$ mol/L. After time $t$, $x$ mol/L of both react.
Rate law: $\frac{dx}{dt} = k(a - x)(b - x)$
Rearranging: $\frac{dx}{(a - x)(b - x)} = k dt$
Using partial fractions: $\frac{1}{a-b} \left[ \frac{1}{b-x} - \frac{1}{a-x} \right] dx = k dt$
Integrating: $\frac{1}{a-b} [-\ln(b-x) + \ln(a-x)] = kt + C \implies \frac{1}{a-b} \ln \left(\frac{a-x}{b-x}\right) = kt + C$
At $t = 0, x = 0 \implies C = \frac{1}{a-b} \ln \left(\frac{a}{b}\right)$
Substituting C and rearranging:
**Integrated equation:** **$k = \frac{1}{t(a-b)} \ln \frac{b(a-x)}{a(b-x)}$**

**Mathematical Properties of a $2^{nd}$ Order Reaction:**
1.  **Half-Life Dependency:** The half-life ($t_{1/2}$) is the time when $x = a/2$.
    Using the $2A \rightarrow P$ formula: $t_{1/2} = \frac{1}{k} \frac{a/2}{a(a - a/2)} = \frac{1}{k} \frac{a/2}{a(a/2)} = \frac{1}{k \cdot a}$
    *Property:* The half-life is **inversely proportional** to the initial concentration of the reactant ($t_{1/2} \propto 1/a$).
2.  **Unit of Rate Constant:** The unit depends on concentration.
    $k = \frac{\text{concentration}}{\text{time} \cdot (\text{concentration})^2} = \text{concentration}^{-1} \text{ time}^{-1}$ (e.g., $L \text{ mol}^{-1} s^{-1}$).
    *Property:* If the unit of concentration is increased $m$ times, the numerical value of $k$ decreases to $1/m$ of its original value.
3.  **Pseudo-First Order Conversion:** In the $A + B$ reaction, if reactant A is in large excess ($a \gg b$), then $a \gg x$, so $(a-b) \approx a$ and $(a-x) \approx a$.
    The equation becomes $k \cdot a = \frac{1}{t} \ln \frac{b}{b-x}$. Since $a$ is constant, let $k \cdot a = k'$.
    $k' = \frac{1}{t} \ln \frac{b}{b-x}$ (which is the exact mathematical expression for a $1^{st}$ order reaction).

---

---

### Q4(b) State and explain activated-complex theory with graphical representation. (04)

**Answer:**

**Activated-Complex Theory (Transition State Theory):**
Formulated by Eyring and Polanyi, this theory provides a detailed microscopic view of reaction kinetics.
*   **Postulate:** A chemical reaction does not occur instantaneously upon collision of reactant molecules. Instead, the colliding reactant molecules must first acquire a specific minimum threshold energy to merge and form a highly energetic, unstable, and temporary intermediate structure called the **Activated Complex** (or Transition State).
*   **Energy Barrier:** The activated complex represents the absolute peak of the potential energy barrier separating reactants from products. The extra energy required by the reactants to reach this peak is called the **Activation Energy ($E_a$)**.
*   **Decomposition:** Once the activated complex is formed at the peak of the barrier, it has two highly probable paths: it can either decompose forward to form the final, more stable products, or decompose backward to reform the original reactants. The rate of the overall reaction is directly proportional to the concentration of the activated complex at the peak of the barrier.

**Graphical Representation (Potential Energy Diagram):**
Imagine a 2D graph mapping the energy path of a reaction.
1.  **Axes:** The Y-axis represents Potential Energy, and the X-axis represents the Reaction Coordinate (the progress of the reaction from start to finish).
2.  **The Curve:** The curve starts at a specific energy level representing the ground state energy of the **Reactants ($E_R$)**. As the reaction progresses, the curve slopes steeply upward, representing the energy input (Activation Energy, $E_a$) required to break initial bonds.
3.  **The Peak:** The highest point of the curve is the **Transition State**, where the short-lived **Activated Complex** exists at its maximum potential energy.
4.  **The Drop:** From the peak, the curve slopes downwards as new bonds form, releasing energy. It settles at a final energy level representing the ground state energy of the **Products ($E_P$)**.
5.  **Enthalpy Change:** The vertical difference between the starting Reactant energy ($E_R$) and final Product energy ($E_P$) is the overall heat of reaction ($\Delta H$). If $E_P < E_R$, the reaction is exothermic.

---

---

### Q5(a) Define the rate of reaction, rate law, order of reaction and molecularity of reaction. (04)

**Answer:**
1.  **Rate of Reaction:** It is defined as the change in the molar concentration of any one of the reactants or products per unit of time. (Rate = $\pm \frac{dC}{dt}$).
2.  **Rate Law:** It is an experimentally determined mathematical equation that expresses the exact dependence of the reaction rate on the molar concentrations of the reacting species. For $aA+bB \rightarrow P$, Rate $= k[A]^x[B]^y$, where $x$ and $y$ are experimentally found.
3.  **Order of Reaction:** It is the sum of the powers (exponents) to which the concentration terms are raised in the experimentally determined rate law equation. From the above, Order $= x + y$.
4.  **Molecularity of Reaction:** It is the total number of reacting species (atoms, molecules, or ions) that must collide together simultaneously in a single, elementary step to result in a chemical reaction.

---

---

### Q5(b) Differentiate between order of reaction and molecularity of reaction. (04)

**Answer:**

| Feature | Order of Reaction | Molecularity of Reaction |
| :--- | :--- | :--- |
| **Origin** | It is an **experimental** quantity derived entirely from the observed rate law. | It is a **theoretical** concept based on the proposed reaction mechanism. |
| **Values** | It can be a whole number, zero, a fraction, or even negative. | It is always a **positive whole number** (1, 2, 3). It can never be zero or a fraction. |
| **Applicability** | It applies to the overall, complete reaction (whether simple or complex). | It applies only to a single, elementary step of a complex reaction mechanism. It has no meaning for a complex overall reaction. |
| **Condition Dependence** | The order can change if experimental conditions (like pressure or concentration) are drastically changed (e.g., pseudo-order). | Molecularity is fixed for a specific elementary step and does not change with external conditions. |

---

---

### Q5(c) The half-life of a $1^{st}$ order reaction is 3400 min. Calculate the value of rate constant. What is the time required to complete 99% of the reaction? (04)

**Answer:**

**Given Data:**
*   Half-life ($t_{1/2}$) = $3400 \text{ min}$

**1. Calculate the value of the rate constant ($k$):**
For a first-order reaction, the relationship between half-life and the rate constant is:
$$k = \frac{0.693}{t_{1/2}}$$
$$k = \frac{0.693}{3400 \text{ min}}$$
$$k = 2.038 \times 10^{-4} \text{ min}^{-1}$$
**(Answer Part 1: Rate constant $k = 2.038 \times 10^{-4} \text{ min}^{-1}$)**

**2. Calculate the time required for 99% completion ($t_{99\%}$):**
Let the initial concentration '$a$' = 100.
For 99% completion, the amount reacted '$x$' = 99.
The remaining concentration '$(a - x)$' = $100 - 99 = 1$.

The integrated rate equation for a first-order reaction is:
$$t = \frac{2.303}{k} \log \left( \frac{a}{a-x} \right)$$
Substitute the values:
$$t_{99\%} = \frac{2.303}{2.038 \times 10^{-4}} \log \left( \frac{100}{1} \right)$$
$$t_{99\%} = \frac{2.303}{2.038 \times 10^{-4}} \times \log(10^2)$$
$$t_{99\%} = \frac{2.303 \times 2}{2.038 \times 10^{-4}}$$
$$t_{99\%} = \frac{4.606}{2.038 \times 10^{-4}}$$
$$t_{99\%} = 22600.58 \text{ min}$$
**(Answer Part 2: Time required for 99% completion is $22600.58 \text{ min}$)**

---

---

## 📄 Source: 2017 Exam

### Q5(a) Deduce an expression for the rate constant of a chemical reaction in which concentrations of two reactants are not identical. (04)

**Answer:**
This is a second-order reaction of the type: $A + B \rightarrow \text{Products}$
Let the initial concentration of reactant $A$ be '$a$' mol/L, and the initial concentration of reactant $B$ be '$b$' mol/L, where **$a \neq b$**.
After time '$t$', let '$x$' mol/L of both $A$ and $B$ react.
The remaining concentration of $A$ is $(a - x)$, and $B$ is $(b - x)$.

The rate of the reaction is given by:
$$\frac{dx}{dt} = k(a - x)(b - x)$$
Rearranging the variables:
$$\frac{dx}{(a - x)(b - x)} = k dt$$
To integrate this, we use the method of partial fractions:
$$\frac{1}{a - b} \left[ \frac{1}{b - x} - \frac{1}{a - x} \right] dx = k dt$$
Integrating both sides:
$$\frac{1}{a - b} \int \left( \frac{1}{b - x} - \frac{1}{a - x} \right) dx = \int k dt$$
$$\frac{1}{a - b} [-\ln(b - x) + \ln(a - x)] = kt + C$$
$$\frac{1}{a - b} \ln \left( \frac{a - x}{b - x} \right) = kt + C \quad \dots \text{(Equation 1)}$$
*(where C is the integration constant)*

To find $C$, apply the initial condition: at $t = 0, x = 0$.
$$\frac{1}{a - b} \ln \left( \frac{a}{b} \right) = k(0) + C \implies C = \frac{1}{a - b} \ln \left( \frac{a}{b} \right)$$
Substitute $C$ back into Equation 1:
$$\frac{1}{a - b} \ln \left( \frac{a - x}{b - x} \right) = kt + \frac{1}{a - b} \ln \left( \frac{a}{b} \right)$$
$$kt = \frac{1}{a - b} \left[ \ln \left( \frac{a - x}{b - x} \right) - \ln \left( \frac{a}{b} \right) \right]$$
$$kt = \frac{1}{a - b} \ln \left[ \frac{b(a - x)}{a(b - x)} \right]$$
**$$k = \frac{1}{t(a - b)} \ln \left[ \frac{b(a - x)}{a(b - x)} \right]$$**
This is the required integrated rate equation.

---

---

### Q5(b) Define pseudo-order reaction. The following reaction shows the $1^{\text{st}}$ order kinetics-explain why.

---

### Q5(c) Discuss the temperature effect on reaction rate. (04)

**Answer:**
It is a general rule that the rate of almost all chemical reactions (whether exothermic or endothermic) increases significantly with an increase in temperature.

**1. Temperature Coefficient:**
For many homogeneous reactions, a mere $10^\circ C$ rise in temperature causes the reaction rate to double or even triple. The ratio of the rate constants measured at two temperatures differing by $10^\circ C$ is called the Temperature Coefficient (usually $k_{t+10} / k_t \approx 2$ to $3$).

**2. Collision Theory Explanation:**
An increase in temperature does not significantly increase the total number of collisions. Instead, it dramatically alters the energy distribution among the molecules (Maxwell-Boltzmann distribution). As temperature rises, the curve flattens and shifts to higher energies. This massively increases the specific *fraction* of molecules that possess kinetic energy greater than or equal to the required **Activation Energy ($E_a$)**. With vastly more molecules capable of undergoing "effective collisions," the reaction rate surges.

**3. Arrhenius Equation:**
The exact mathematical relationship between the rate constant ($k$) and absolute temperature ($T$) is given by Svante Arrhenius:
**$$k = A e^{-E_a / RT}$$**
Where $A$ is the pre-exponential factor, $E_a$ is the activation energy, and $R$ is the gas constant. This equation proves that $k$ (and thus the rate) increases exponentially with $T$.

---

---

## 📄 Source: ClassTests Exam

### Q.1 Define rate of reaction. Discuss briefly how rate of reaction depends on temperature and reactant concentration. (7)
**Answer:**
**Rate of Reaction:** It is defined as the change in the molar concentration of any one of the reactants or products per unit of time. (Rate = $\pm \frac{dC}{dt}$).

**Dependence on Temperature:**
The rate of almost all reactions increases exponentially with an increase in temperature. According to the **Collision Theory**, increasing the temperature shifts the Maxwell-Boltzmann distribution curve of molecular energies, massively increasing the specific fraction of molecules that possess kinetic energy equal to or greater than the Activation Energy ($E_a$). With vastly more molecules capable of "effective collisions," the rate surges. (Governed by the Arrhenius equation: $k = A e^{-E_a/RT}$).

**Dependence on Reactant Concentration:**
The rate of a reaction is generally directly proportional to the concentration of the reactants. According to the **Law of Mass Action**, a higher concentration means there are more reactant molecules crowded into a given volume. This crowding drastically increases the frequency of random collisions between molecules. More total collisions lead to a proportionally higher number of effective collisions per unit time, thereby increasing the overall reaction rate.

---

### Q.2 Distinguish between order and molecularity. (5)
**Answer:**
*(Note: See the detailed table provided in the 2018 Exam, Section B, Q5(b) for the complete distinction. In short: Order is experimental, can be fractional/zero, and applies to the overall reaction. Molecularity is theoretical, always a whole integer, and applies only to a single elementary step).*

---

### Q.3 Derive an expression for the rate constant of a first order reaction. (5)
**Answer:**
Consider a first-order reaction: $A \rightarrow \text{Products}$.
Let the initial concentration of $A$ at time $t = 0$ be '$a$' mol/L.
After time $t$, let '$x$' mol/L of $A$ react. The remaining concentration is $(a - x)$.
The rate of reaction is directly proportional to the first power of the remaining concentration:
$$\frac{dx}{dt} \propto (a - x)^1$$
$$\frac{dx}{dt} = k(a - x)$$
Rearranging variables:
$$\frac{dx}{a - x} = k dt$$
Integrating both sides:
$$\int \frac{dx}{a - x} = \int k dt$$
$$-\ln(a - x) = kt + C \quad \dots \text{(Equation 1)}$$
Apply initial conditions to find $C$: At $t = 0$, $x = 0$.
$$-\ln(a - 0) = k(0) + C \implies C = -\ln a$$
Substitute $C$ back into Equation 1:
$$-\ln(a - x) = kt - \ln a$$
$$kt = \ln a - \ln(a - x) = \ln \left( \frac{a}{a - x} \right)$$
Converting natural log ($\ln$) to base-10 log ($\log$):
$$kt = 2.303 \log \left( \frac{a}{a - x} \right)$$
**$$k = \frac{2.303}{t} \log \left( \frac{a}{a - x} \right)$$**
This is the required integrated rate equation for a 1st order reaction.

---

### Q.4 Show that the time required to complete a given fraction of reaction is independent of initial concentration of reactant. (3)
**Answer:**
Using the first-order integrated rate equation derived above:
$$t = \frac{1}{k} \ln \left( \frac{a}{a - x} \right)$$
Let the "given fraction" of the reaction completed be denoted by '$f$'. Therefore, the amount reacted '$x$' is equal to that fraction of the initial concentration: $x = f \cdot a$.
Substitute this into the equation:
$$t = \frac{1}{k} \ln \left( \frac{a}{a - fa} \right)$$
Factor out '$a$' in the denominator:
$$t = \frac{1}{k} \ln \left( \frac{a}{a(1 - f)} \right)$$
The initial concentration '$a$' cancels out completely:
**$$t = \frac{1}{k} \ln \left( \frac{1}{1 - f} \right)$$**
Because the rate constant ($k$) is a constant at a given temperature, and the fraction ($f$) is a chosen constant value, the calculated time ($t$) depends purely on constants. This proves mathematically that the time required to complete any specific fraction of a first-order reaction is completely independent of the starting concentration '$a$'.

---

---


---

*(start)* | [🏠 Index](index.md) | [02-Chemical-Equilibrium ➡](02-Chemical-Equilibrium.md)
