# Chemical Kinetics: Slides 056-060

## Slide 56

![Arrhenius Equation: Integrated Form and Graph](file:///home/azaz/Downloads/Documents/Chemical-Kinetics/Chemical-Kinetics-056.png)

### **Arrhenius Equation**

If the rate constants of reaction are $k_1$ and $k_2$ at $T_1$ and $T_2$ respectively, then, by integration of eq- (iii):
$$\ln \frac{k_2}{k_1} = -\frac{E}{R} \left[ \frac{1}{T_2} - \frac{1}{T_1} \right]$$

$$\log \frac{k_2}{k_1} = \frac{E}{2.303 R} \left[ \frac{T_2 - T_1}{T_1 T_2} \right] \quad \dots (vi)$$

From the eq – (v), energy of activation can be calculated.

**The following graph can be drawn using the eq- (iv):**

![ln k vs 1/T Graph](file:///home/azaz/Downloads/Documents/Chemical-Kinetics/Chemical-Kinetics-056.png)
*   **$y$-axis:** $\ln k$
*   **$x$-axis:** $1/T$
*   **Intercept:** $\ln A$
*   **Slope:** $-E_a / R$

---

## Slide 57

![Concept of Activation Energy and Maxwell-Boltzmann Distribution](file:///home/azaz/Downloads/Documents/Chemical-Kinetics/Chemical-Kinetics-057.png)

### **Energy of Activation**

It is **defined** as the least possible amount of **energy** (minimum) which is required to start a reaction or the amount of **energy** available in a chemical system for a reaction to take place.

**Diagram Analysis:**
The graph shows the distribution of kinetic energies among molecules at two different temperatures ($T_1$ and $T_2$, where $T_2 > T_1$).
*   The $x$-axis represents Energy, and the $y$-axis represents the number of molecules.
*   **Threshold Energy ($E_a$):** Only molecules with energy greater than $E_a$ (the shaded area) can react.
*   At higher temperatures ($T_2$), the curve flattens and shifts to the right, significantly increasing the fraction of molecules that possess energy $\geq E_a$.
*   Since the probability of a molecule reacting increases, the rate increases.

---

## Slide 58

![Temperature Dependence and Energy Distribution Curves](file:///home/azaz/Downloads/Documents/Chemical-Kinetics/Chemical-Kinetics-058.png)

### **Temperature Dependence of Rate of Reaction**

**Fig. 4.8: Distribution curve showing energies among gaseous molecules**
This Maxwell-Boltzmann distribution shows that most molecules have a "most probable kinetic energy," while very few have extremely low or high energies.

**Fig. 4.9: Distribution curve showing temperature dependence of rate of a reaction**
This graph illustrates the effect of a 10°C temperature rise (from $t$ to $t+10$).
*   The shaded area under the curve beyond the "Energy of Activation" line represents the fraction of molecules capable of reacting.
*   The darker shaded area shows the **additional** molecules that gain enough energy to react when the temperature is increased by 10°. This effectively doubles the area for many reactions, explaining the "Temperature Coefficient" rule.

---

## Slide 59

![Numerical Problems on Arrhenius Equation](file:///home/azaz/Downloads/Documents/Chemical-Kinetics/Chemical-Kinetics-059.png)

### **Numerical Problem**

**Example 4.10:** The rate constants of a reaction at 500K and 700K are $0.02s^{-1}$ and $0.07s^{-1}$ respectively. Calculate the values of $E_a$ and $A$.

**Solution:**
$$\log \frac{k_2}{k_1} = \frac{E_a}{2.303 R} \left[ \frac{T_2 - T_1}{T_1 T_2} \right]$$
$$\log \frac{0.07}{0.02} = \left( \frac{E_a}{2.303 \times 8.314 \, \text{J K}^{-1} \text{mol}^{-1}} \right) \left[ \frac{700 - 500}{700 \times 500} \right]$$
$$0.544 = E_a \times 5.714 \times 10^{-4} / 19.15 \implies E_a = 18230.8 \, \text{J}$$
Since $k = A e^{-E_a/RT}$:
$$0.02 = A e^{-18230.8 / (8.314 \times 500)} \implies A = 1.61$$

**Example 4.11:** The first order rate constant for the decomposition of ethyl iodide by the reaction $C_2H_5I(g) \rightarrow C_2H_4(g) + HI(g)$ at 600K is $1.60 \times 10^{-5} s^{-1}$. Its energy of activation is $209 \, \text{kJ/mol}$. Calculate the rate constant of the reaction at 700K.

**Solution:**
$$\log k_2 = \log k_1 + \frac{E_a}{2.303 R} \left[ \frac{1}{T_1} - \frac{1}{T_2} \right]$$
$$= \log(1.60 \times 10^{-5}) + \frac{209000}{2.303 \times 8.314} \left[ \frac{1}{600} - \frac{1}{700} \right]$$
$$\log k_2 = -4.796 + 2.599 = -2.197 \implies k_2 = 6.36 \times 10^{-3} s^{-1}$$

---

## Slide 60

![Numerical Problem: Zero Activation Energy](file:///home/azaz/Downloads/Documents/Chemical-Kinetics/Chemical-Kinetics-060.png)

### **Numerical Problem**

**Example : 8**
For a reaction, the energy of activation is zero. What is the value of rate constant at 300 K if $k = 1.6 \times 10^6 s^{-1}$ at 280 K?

**Solution:**
We know,
$$\log \frac{k_{300}}{k_{280}} = \frac{E_a}{2.303 R} \left[ \frac{T_2 - T_1}{T_2 T_1} \right]$$

Given: $E_a = 0$
$$\therefore \frac{E_a}{2.303 R} \left[ \frac{T_2 - T_1}{T_2 T_1} \right] = 0$$
$$\log \frac{k_{300}}{k_{280}} = 0 \implies \frac{k_{300}}{k_{280}} = 1$$
Hence, $k_{300} = k_{280} = 1.6 \times 10^6 s^{-1}$
