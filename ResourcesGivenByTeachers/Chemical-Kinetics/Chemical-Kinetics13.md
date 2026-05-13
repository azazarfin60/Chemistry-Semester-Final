[⬅ Chemical-Kinetics12](Chemical-Kinetics12.md) | [🏠 Index](00-index.md) | *(end)*

---

# Chemical Kinetics: Slides 061-063 (Final)

## Slide 61

> 📷 **[Diagram]** Numerical Problem: Arrhenius Equation Application

### **Numerical Problem**

**Example: 9**
The time required for 10% completion of first order reaction at 298 K is equal to that required for its 25% completion at 308 K. If the preexponential factor for the reaction is $3.56 \times 10^9 s^{-1}$, calculate the energy of activation.

**Solution:**
For first order reactions:
$$t = \frac{2.303}{K} \log \frac{N_0}{N_1}$$

*   At 298 K: $t = \frac{2.303}{K_{298}} \log \frac{100}{90}$
*   At 308 K: $t = \frac{2.303}{K_{308}} \log \frac{100}{75}$

Since time is the same:
$$\frac{2.303}{K_{298}} \log \frac{100}{90} = \frac{2.303}{K_{308}} \log \frac{100}{75}$$
$$\text{or } \frac{0.0458}{K_{298}} = \frac{0.1249}{K_{308}} \implies \frac{K_{308}}{K_{298}} = \frac{0.1249}{0.0458} = 2.73$$

According to Arrhenius equation:
$$2.303 \log \frac{K_{308}}{K_{298}} = \frac{E_a}{8.314} \left[ \frac{1}{298} - \frac{1}{308} \right]$$
$$2.303 \log 2.73 = \frac{E_a}{8.314} \left[ \frac{10}{298 \times 308} \right]$$
**$E_a = 76.65 \, \text{kJ}$**

---

## Slide 62

> 📷 **[Diagram]** Numerical Problem: Activation Energy and Rate Constants

### **Numerical Problem**

**Question: 10**
At 380°C, the half-life period for the first order decomposition of $H_2O_2$ is 360 min. The energy of activation of the reaction is $200 \, \text{kJ mol}^{-1}$. Calculate the time required for 75% decomposition at 450°C.

**Solution:**
For first order reaction, $K = \frac{0.693}{t_{1/2}}$
$K_{653} = \frac{0.693}{360} = 1.925 \times 10^{-3} \, \text{min}^{-1}$

$\log K_{723} - \log K_{653} = \frac{E_a}{2.303R} \left[ \frac{T_2 - T_1}{T_1 T_2} \right]$
$\log K_{723} - \log(1.925 \times 10^{-3}) = \left( \frac{200 \times 10^3}{2.303 \times 8.314} \right) \times \left[ \frac{723 - 653}{723 \times 653} \right]$
$\log K_{723} - (-2.7156) = 1.55 \implies \log K_{723} = -1.1656$
$K_{723} = 6.82 \times 10^{-2} \, \text{min}^{-1}$

For first order reaction at 450°C (723 K):
$$t = \frac{2.303}{K} \log \frac{a}{a-x} = \frac{2.303}{6.82 \times 10^{-2}} \log \frac{100}{100 - 75}$$
$t = 33.768 \times \log 4 = 33.768 \times 0.602 = \mathbf{20.33 \, \text{min}}$

---

## Slide 63

> 📷 **[Diagram]** Numerical Problem: Activation Energy Calculation

### **Numerical Problem**

**Example 2**
At a temperature of 600 K, the rate constant of a chemical reaction is $2.75 \times 10^{-8} M^{-1}s^{-1}$. When the temperature is increased to 800 K, the rate constant for the same reaction is $1.95 \times 10^{-7} M^{-1}s^{-1}$. What is the activation energy of this reaction?

**Given:** $T_1 = 600 \, \text{K}$, $k_1 = 2.75 \times 10^{-8} \, \text{M}^{-1}\text{s}^{-1}$, $T_2 = 800 \, \text{K}$, $k_2 = 1.95 \times 10^{-7} \, \text{M}^{-1}\text{s}^{-1}$

When the A factor is eliminated from the Arrhenius equation, the following equation is obtained:
$$\ln \frac{k_1}{k_2} = \left( -\frac{E_a}{R} \right) \left( \frac{1}{T_1} - \frac{1}{T_2} \right)$$

Substituting the given values:
$$\ln \left( \frac{2.75 \times 10^{-8}}{1.95 \times 10^{-7}} \right) = \left( -\frac{E_a}{8.314} \right) \times (0.00041)$$
$\ln(0.141) = E_a \times (-0.0000493) \implies -1.958 = E_a \times (-0.0000493)$
**$E_a = 39716 \, \text{J mol}^{-1} \approx 39.72 \, \text{kJ mol}^{-1}$**

The activation energy of the reaction is approximately $39716 \, \text{J mol}^{-1}$.


---

[⬅ Chemical-Kinetics12](Chemical-Kinetics12.md) | [🏠 Index](00-index.md) | *(end)*
