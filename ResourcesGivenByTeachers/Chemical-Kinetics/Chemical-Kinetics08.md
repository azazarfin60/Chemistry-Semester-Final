[⬅ Chemical-Kinetics07](Chemical-Kinetics07.md) | [🏠 Index](00-index.md) | [Chemical-Kinetics09 ➡](Chemical-Kinetics09.md)

---

# Chemical Kinetics: Slides 036-040

## Slide 36

> 📷 **[Diagram]** Second Order Derivation - Part 2

### **Kinetics of Second Order Reaction**

Or, $$\frac{1}{a-b} \left[ \frac{1}{b-x} - \frac{1}{a-x} \right] dx = kdt$$

By integration,
$$\frac{1}{a-b} \int \left[ \frac{1}{b-x} - \frac{1}{a-x} \right] dx = \int kdt$$

$$\frac{1}{(a - b)} [-\ln (b - x) + \ln (a - x)] = kt + \text{constant}$$

$$\frac{1}{(a-b)} \ln \frac{a-x}{b-x} = kt + \text{constant} \quad \dots (ii)$$

When, $t = 0, x = 0$; from eq- (ii)

$$\text{Constant} = \frac{1}{(a-b)} \ln \frac{a}{b} \quad \dots (iii)$$

---

## Slide 37

> 📷 **[Diagram]** Second Order Derivation - Final Integrated Form

### **Kinetics of Second Order Reaction**

From eq- (ii) and (iii), we get,

$$kt = \frac{1}{(a-b)} \ln \frac{a-x}{b-x} - \frac{1}{(a-b)} \ln \frac{a}{b}$$

$$k = \frac{1}{t(a-b)} \ln \frac{b(a-x)}{a(b-x)} \quad \dots (iv)$$

This is the integrated rate expression for second order reaction.

---

## Slide 38

> 📷 **[Diagram]** Property 1: Half-life vs. Initial Concentration

### **Properties of Second Order Reaction**

**1. The time required to complete a given fraction of reaction is inversely proportional to the initial concentration of reactant.**

Suppose, the half life of reaction will be determined. In this case, $x = 0.5a$

We have,
$$t = \frac{1}{k} \times \frac{x}{a(a-x)}$$

$$t_{1/2} = \frac{1}{k} \times \frac{0.5 a}{a(a-0.5a)}$$

Or, $t_{1/2} = \frac{1}{k} \times \frac{1}{a}$

$$t_{1/2} \propto \frac{1}{a}$$

---

## Slide 39

> 📷 **[Diagram]** Property 2: Rate Constant Dependency on Units

### **Properties of Second Order Reaction**

**2. The value of rate constant will be changed if unit of concentration is changed.**

Suppose, the present unit of concentration is $m$ times of the previous unit.

$$k = \frac{1}{t} \times \frac{mx}{ma(a-x)m}$$

Or, $k = \frac{1}{t} \times \frac{x}{a(a-x)} \times \frac{1}{m}$

So, the new value of $k$ is $1/m$ times of previous value.

---

## Slide 40

> 📷 **[Diagram]** Property 3: Conversion to Pseudo-First Order

### **Properties of Second Order Reaction**

**3. The $2^{nd}$ order reaction is converted to the $1^{st}$ order when one of the reactants are present in large excess compared to other one.**

We have, $k = \frac{1}{t(a-b)} \ln \frac{b(a-x)}{a(b-x)}$

Let, $a \gg b$; then $a \gg x$

Therefore, $k = \frac{1}{ta} \ln \frac{ba}{a(b-x)}$

or, $k = \frac{1}{ta} \ln \frac{b}{(b-x)}$

At the time of reaction, $a$ is constant, so
$$k = \frac{1}{t} \ln \frac{b}{(b-x)}$$

This is the mathematical expression of $1^{st}$ order kinetics.


---

[⬅ Chemical-Kinetics07](Chemical-Kinetics07.md) | [🏠 Index](00-index.md) | [Chemical-Kinetics09 ➡](Chemical-Kinetics09.md)
