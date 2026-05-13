[⬅ Chemical-Kinetics06](Chemical-Kinetics06.md) | [🏠 Index](index.md) | [Chemical-Kinetics08 ➡](Chemical-Kinetics08.md)

---

# Chemical Kinetics: Slides 031-035

## Slide 31

![Practice Problems for First Order Reactions](file:///home/azaz/Downloads/Documents/Chemical-Kinetics/Chemical-Kinetics-031.png)

### **Solve Problem**

1. The $t_{1/2}$ of a substance in a 1st order reaction is 15 min. Calculate the rate constant.

2. For certain 1st order reaction, $t_{1/2}$ is 100 sec. How long will it take for the reaction to be completed 75 %

3. A 1st order reaction is one-fifth completed in 40 min. Calculate the time required for its 100 % completion.

---

## Slide 32

![Numerical Problems and Solutions](file:///home/azaz/Downloads/Documents/Chemical-Kinetics/Chemical-Kinetics-032.png)

### **Numerical Problem**

**Example 4.7:** A first order reaction is found to have a rate constant, $k = 5.5 \times 10^{-14} \text{ s}^{-1}$. Find the half-life of the reaction.

**Solution:**
$$t_{1/2} = \frac{0.693}{k}$$
$$t_{1/2} = \frac{0.693}{5.5 \times 10^{-14} \text{ s}^{-1}} = 1.26 \times 10^{13} \text{ s}$$

**Example 4.8:** Show that in a first order reaction, time required for completion of 99.9% is 10 times of half-life ($t_{1/2}$) of the reaction.

**Solution:**
When reaction is completed 99.9%, $[R]_n = [R]_0 - 0.999[R]_0$
$$k = \frac{2.303}{t} \log \frac{[R]_0}{[R]}$$
$$= \frac{2.303}{t} \log \frac{[R]_0}{[R]_0 - 0.999[R]_0} = \frac{2.303}{t} \log 10^3$$
$$t = \frac{6.909}{k}$$

For half-life of the reaction:
$$t_{1/2} = 0.693/k$$
$$\frac{t}{t_{1/2}} = \frac{6.909}{k} \times \frac{k}{0.693} = 10$$

---

## Slide 33

![Kinetics of Second Order Reactions - Introduction](file:///home/azaz/Downloads/Documents/Chemical-Kinetics/Chemical-Kinetics-033.png)

### **Kinetics of Second Order Reaction**

A **second-order reaction** rate is proportional to the square of the concentration of a reactant or the product of the concentration of two reactants.

**Examples:**

* $2 HI \rightarrow I_2 + H_2$
  Hydrogen Iodide decomposes into iodine gas and hydrogen gas.
* $O + O_3 \rightarrow O_2 + O_2$
  During combustion, oxygen atoms and ozone can form oxygen molecules.
* $O_2 + C \rightarrow O + CO$
  Oxygen molecules react with carbon to form oxygen atoms and carbon monoxide.
* $O_2 + CO \rightarrow O + CO_2$
  Oxygen molecules react with carbon monoxide to form carbon dioxide and oxygen atoms.
* $O + H_2O \rightarrow 2 OH$
  Water can react with loose oxygen atoms to form hydroxides.
* $2 NOBr \rightarrow 2 NO + Br_2$
  In the gas phase, nitrosyl bromide decomposes into nitrogen oxide and bromine gas.
* $NH_4CNO \rightarrow H_2NCONH_2$
  Ammonium cyanate in water isomerizes into urea.
* $CH_3COOC_2H_5 + NaOH \rightarrow CH_3COONa + C_2H_5OH$
  Hydrolysis of an ester (ethyl acetate) in the presence of a base (sodium hydroxide).

---

## Slide 34

![Second Order Derivation - Type 1](file:///home/azaz/Downloads/Documents/Chemical-Kinetics/Chemical-Kinetics-034.png)

### **Kinetics of Second Order Reaction**

**1. $2A \rightarrow \text{Product}$**

Suppose, the initial concentration of A is "a" mole/liter and after time $t$, $x$ mole/liter of A is converted to product.

Therefore,
$$\frac{dx}{dt} = k (a - x)^2 \quad \dots (i)$$

Or, $$\int \frac{dx}{(a-x)^2} = \int kdt$$

By integration,
$$\frac{1}{a-x} = kt + \text{constant} \quad \dots (ii)$$

When, $t = 0$, then $x = 0$, From eq-(ii), $\text{Constant} = \frac{1}{a}$

---

## Slide 35

![Second Order Derivation - Type 2](file:///home/azaz/Downloads/Documents/Chemical-Kinetics/Chemical-Kinetics-035.png)

### **Kinetics of Second Order Reaction**

Hence, $$\frac{1}{a-x} = kt + \frac{1}{a}$$

$$k = \frac{1}{t} \times \frac{x}{a(a-x)} \quad \dots (iii)$$

This is the integrated rate expression for second order reaction.

**2. $A + B \rightarrow \text{Products}$**

Suppose, the initial concentration of A is "a" mole/liter and of B is "b" mole/liter, then

$$\frac{dx}{dt} = k(a-x)(b-x) \quad \dots (i)$$

Or, $$\frac{dx}{(a-x)(b-x)} = kdt$$


---

[⬅ Chemical-Kinetics06](Chemical-Kinetics06.md) | [🏠 Index](index.md) | [Chemical-Kinetics08 ➡](Chemical-Kinetics08.md)
