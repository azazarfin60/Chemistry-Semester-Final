[⬅ Chemical-Kinetics08](Chemical-Kinetics08.md) | [🏠 Index](00-index.md) | [Chemical-Kinetics10 ➡](Chemical-Kinetics10.md)

---

# Chemical Kinetics: Slides 041-045

## Slide 41

> 📷 **[Diagram]** Numerical Problem: Hydrolysis of Ethyl Acetate

### **Numerical Problem**

**Hydrolysis of ethyl acetate by NaOH using equal concentration of the reactants, was studied by titrating 25 ml of the reaction mixture at different time intervals against standard acid. From the data given below, establish that this is a $2^{nd}$ order reaction.**

| $T$ (min) | 0 | 5 | 15 | 25 |
| :--- | :--- | :--- | :--- | :--- |
| ml of acid used | 16 | 10.24 | 6.13 | 4.32 |

We know, the $2^{nd}$ order integrated rate equation:
$$K = \frac{1}{t} \times \frac{x}{a(a-x)} \quad \dots (i)$$

The volume of acid used at any time is a measure of concentration of the unreacted substances at that time. Therefore, $a = 16$.

*   After 5 min, $(a - x) = 10.24$ and $x = 5.76$
*   After 15 min, $(a - x) = 6.13$ and $x = 9.85$
*   After 25 min, $(a - x) = 4.32$ and $x = 11.68$

From eq- (i):
$$K = \frac{1}{16 \times 5} \times \frac{5.76}{10.24} = 0.0070$$

---

## Slide 42

> 📷 **[Diagram]** Numerical Problem Solution (Contd.)

### **Numerical Problem (Continued)**

$$K = \frac{1}{16 \times 15} \times \frac{9.85}{6.13} = 0.0067$$

$$K = \frac{1}{16 \times 25} \times \frac{11.68}{4.32} = 0.00675 \quad \text{[Correction: Slide typo shows 6.13 in denominator]}$$

The value of $k$ being fairly constant, this reaction is of $2^{nd}$ order.

---

## Slide 43

> 📷 **[Diagram]** Kinetics of Third Order Reaction - Derivation

### **Kinetics of Third Order Reaction**

Suppose, **$3 A \rightarrow \text{Product}$**

Initial concentration of A is "a" mole/liter, at $t$ time its concentration will be $(a - x)$,

$$\frac{dx}{dt} = k(a - x)^3 \quad \dots (i)$$

By integration,
$$\frac{1}{2(a - x)^2} = kt + \text{constant} \quad \dots (ii)$$

When $t = 0, x = 0$, then $\text{Constant} = \frac{1}{2a^2}$

Therefore,
$$kt = \frac{1}{2(a - x)^2} - \frac{1}{2a^2}$$

$$k = \frac{1}{t} \times \frac{x(2a - x)}{2a^2(a - x)^2} \quad \dots (iii)$$

This is the mathematical expression for rate constant of $3^{rd}$ order kinetics.

---

## Slide 44

> 📷 **[Diagram]** Property 1: Half-life vs. Initial Concentration

### **Properties of $3^{rd}$ Order Reaction**

**1. The time required for completion of a given fraction of a $3^{rd}$ order reaction is inversely proportional to square of initial concentration.**

Suppose, for $t_{1/2}$, $x = 0.5 a$

We have,
$$t_{1/2} = \frac{1}{k} \times \frac{x(2a - x)}{2a^2(a - x)^2}$$

Or, $$t_{1/2} = \frac{1}{k} \times \frac{0.5a(2a - 0.5a)}{2a^2(a - 0.5a)^2}$$

Or, $t_{1/2} = \frac{1.5}{k} \times \frac{1}{a^2}$

$$t_{1/2} \propto \frac{1}{a^2}$$

---

## Slide 45

> 📷 **[Diagram]** Property 2: Rate Constant Dependency on Units

### **Properties of $3^{rd}$ Order Reaction**

**2. The value of rate constant of $3^{rd}$ order reaction depends on unit of concentration.**

We have,
$$k = \frac{1}{t} \times \frac{x(2a - x)}{2a^2(a - x)^2}$$

Suppose, the present unit is $n$ times of the previous one.

$$k = \frac{1}{t} \times \frac{nx(2an - nx)}{2(an)^2(an - nx)^2}$$

Or, $k = \frac{1}{t} \times \frac{x(2a - x)}{2a^2(a - x)^2} \times \frac{1}{n^2}$

So, the value of $k$ is $1/n^2$ times of previous one.


---

[⬅ Chemical-Kinetics08](Chemical-Kinetics08.md) | [🏠 Index](00-index.md) | [Chemical-Kinetics10 ➡](Chemical-Kinetics10.md)
