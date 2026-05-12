# Chemical Kinetics: Slides 026-030

## Slide 26

![Half-life of First Order Reaction](file:///home/azaz/Downloads/Documents/Chemical-Kinetics/Chemical-Kinetics-026.png)

### **Half-life Period of First Order Reaction**

The half-time of a reaction is defined as the time required to reduce the concentration of the reactant to half of its initial value. It is denoted by the symbol $t_{1/2}$. Thus,

For first order reaction, we know that
$$k = \frac{1}{t} \ln \frac{[A]_0}{[A]}$$

at half life of reaction,
$t = t_{1/2}$ & $[A] = [A]_0/2$

So
$$k = \frac{1}{t_{1/2}} \ln \frac{[A]_0}{[A]_0/2}$$
$$\Rightarrow t_{1/2} = \frac{0.693}{k}$$

* Since $k$ is a constant for a given reaction at a given temperature

**Diagram Analysis:**
The slide features an illustration of a student emphasizing a critical point:
> **"Half-time of a 1st order reaction is a constant independent of initial concentration of reactant."**

---

## Slide 27

![Property 1: Reaction Never Completes](file:///home/azaz/Downloads/Documents/Chemical-Kinetics/Chemical-Kinetics-027.png)

### **Properties of First Order Reaction**

**1. First order reaction is never completed.**

We have, $\ln \frac{c_0}{c} = kt$

Or, $\frac{c_0}{c} = e^{kt}$

Or, $c = c_0 e^{-kt}$

If reaction is completed, then, $c = 0$

Here, $0 = c_0 e^{-kt}$

$e^{kt} = \frac{c_0}{0} = \infty$

Hence, $k \neq 0$, So, $t = \infty$

---

## Slide 28

![Property 2: Fraction Completion Independence](file:///home/azaz/Downloads/Documents/Chemical-Kinetics/Chemical-Kinetics-028.png)

### **Properties of First Order Reaction**

**2. The time required to complete a given fraction of reaction is independent of initial concentration of reactant.**

Suppose, the half life of reaction will be determined. In this case, $x = 0.5a$

We have, $$t_{1/2} = \frac{2.303}{k} \log \frac{a}{a - 0.5a}$$

Or, $$t_{1/2} = \frac{2.303}{k} \log 2$$

$$t_{1/2} = \frac{0.693}{k}$$

---

## Slide 29

![Property 3: Rate Constant Independence of Units](file:///home/azaz/Downloads/Documents/Chemical-Kinetics/Chemical-Kinetics-029.png)

### **Properties of First Order Reaction**

**3. The value of rate constant is independent of unit of concentration.**

We have, $k = \frac{2.303}{t} \log \frac{a}{a-x} \quad \dots (i)$

Suppose, the present unit of concentration is $n$ times of the previous unit.

$$k = \frac{2.303}{t} \log \frac{na}{n(a-x)}$$

Or, $k = \frac{2.303}{t} \log \frac{a}{a-x} \quad \dots (ii)$

The above two equations are same, so the value of rate constant remains unchanged.

---

## Slide 30

![Numerical Problem Example](file:///home/azaz/Downloads/Documents/Chemical-Kinetics/Chemical-Kinetics-030.png)

### **Numerical Problem**

**50% of a first order reaction is completed in 23 min. Calculate the time required to complete 90% of the reaction.**

We have, $t_{1/2} = \frac{0.693}{k}$

$$k = \frac{0.693}{23} = 0.030130 \text{ min}^{-1}$$

Again, $t(90\%) = \frac{2.303}{k} \log \frac{a}{a - 0.9a} \quad [x = 0.9a]$

$$t(90\%) = \frac{2.303}{0.030130} \log \frac{1}{1 - 0.9} \quad [x = 0.9a]$$

$$t(90\%) = \frac{2.303}{0.030130} = 76.4 \text{ min}$$
