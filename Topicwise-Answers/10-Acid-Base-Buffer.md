[⬅ 09-Periodic-Table](09-Periodic-Table.md) | [🏠 Index](index.md) | *(end)*

---

# Acid Base Buffer
**Priority:** 🟡 MEDIUM | **Frequency:** 7 sub-parts across 3/7 exams

> **Topics Covered:** Lewis acids/bases, buffer solution, buffer action, Henderson-Hasselbalch equation, precision/accuracy.

---

## 📄 Source: 2023 Exam

### Q.5(a) Define and Classify Buffer Solution with examples. (02)

**Answer:**

**Definition:**
A **Buffer Solution** is an aqueous solution that resists significant changes in its pH upon the addition of small amounts of either a strong acid or a strong base. It maintains a relatively constant hydrogen ion concentration.

**Classification:**
Buffer solutions are broadly classified into two types:
1.  **Acidic Buffer:** A solution containing a mixture of a weak acid and its salt with a strong base. It generally has a pH less than 7.
    *   *Example:* A mixture of Acetic Acid ($CH_3COOH$, a weak acid) and Sodium Acetate ($CH_3COONa$, its salt with a strong base $NaOH$).
2.  **Basic Buffer:** A solution containing a mixture of a weak base and its salt with a strong acid. It generally has a pH greater than 7.
    *   *Example:* A mixture of Ammonium Hydroxide ($NH_4OH$, a weak base) and Ammonium Chloride ($NH_4Cl$, its salt with a strong acid $HCl$).

---

---

### Q.5(b) Explain Buffer-action with examples. (03)

**Answer:**

**Buffer Action:**
The mechanism by which a buffer solution resists the change in pH upon the addition of an acid or a base is called buffer action. It works by having components that can neutralize any added $H^+$ or $OH^-$ ions.

**Explanation (Acidic Buffer Example):**
Consider an acidic buffer containing acetic acid ($CH_3COOH$) and sodium acetate ($CH_3COONa$). 
In solution, the salt is completely ionized, while the weak acid is only slightly ionized (and its ionization is further suppressed by the common $CH_3COO^-$ ion):
$CH_3COONa \rightarrow CH_3COO^- + Na^+$ (Complete ionization)
$CH_3COOH \rightleftharpoons CH_3COO^- + H^+$ (Weak ionization)

*   **Addition of Strong Acid (e.g., $HCl \rightarrow H^+ + Cl^-$):**
    When a small amount of strong acid is added, the extra $H^+$ ions combine with the large reserve of acetate ions ($CH_3COO^-$) provided by the salt to form weakly ionized acetic acid.
    $$CH_3COO^- + H^+ \rightarrow CH_3COOH$$
    Since the added $H^+$ is consumed to form a weak acid that doesn't easily dissociate, the pH of the solution remains almost unchanged.
*   **Addition of Strong Base (e.g., $NaOH \rightarrow Na^+ + OH^-$):**
    When a small amount of strong base is added, the extra $OH^-$ ions are neutralized by reacting with the undissociated weak acetic acid molecules to form water and acetate ions.
    $$CH_3COOH + OH^- \rightarrow CH_3COO^- + H_2O$$
    Since the added $OH^-$ is neutralized to form water, the pH of the solution again remains almost constant.

---

---

### Q.5(c) Deduce Henderson's equation of Buffer solution preparation. (05)

**Answer:**

**Derivation of the Henderson-Hasselbalch Equation for an Acidic Buffer:**

Consider an acidic buffer made of a weak acid ($HA$) and its salt ($BA$) with a strong base.
The weak acid dissociates partially in water:
$$HA \rightleftharpoons H^+ + A^-$$
The equilibrium constant (acid dissociation constant, $K_a$) for this reaction is:
$$K_a = \frac{[H^+][A^-]}{[HA]}$$

Rearranging this equation to solve for the hydrogen ion concentration $[H^+]$:
$$[H^+] = K_a \frac{[HA]}{[A^-]}$$

Taking the negative logarithm (base 10) on both sides:
$$-\log[H^+] = -\log \left( K_a \frac{[HA]}{[A^-]} \right)$$
$$-\log[H^+] = -\log K_a - \log \frac{[HA]}{[A^-]}$$

We know that $pH = -\log[H^+]$ and $pK_a = -\log K_a$. Substituting these into the equation:
$$pH = pK_a - \log \frac{[HA]}{[A^-]}$$

Inverting the ratio inside the logarithm changes the sign:
$$pH = pK_a + \log \frac{[A^-]}{[HA]}$$

**Approximation:**
1. Because $HA$ is a weak acid, it dissociates very little. Moreover, its dissociation is further suppressed by the presence of the common ion $A^-$ from the completely dissociated salt $BA$. Therefore, the equilibrium concentration of the un-ionized acid $[HA]$ can be taken as approximately equal to its initial concentration: $[HA] \approx [\text{Acid}]$.
2. Since the salt $BA$ is completely ionized ($BA \rightarrow B^+ + A^-$), almost all the $A^-$ ions in the solution come from the salt. Therefore, the equilibrium concentration of $A^-$ can be taken as approximately equal to the initial concentration of the salt: $[A^-] \approx [\text{Salt}]$.

Substituting these approximations into the equation gives the final **Henderson-Hasselbalch Equation**:
$$pH = pK_a + \log \frac{[\text{Salt}]}{[\text{Acid}]}$$

*(Note: Similarly, for a basic buffer composed of a weak base and its salt, the equation is $pOH = pK_b + \log \frac{[\text{Salt}]}{[\text{Base}]}$).*

---

---

## 📄 Source: 2019 Exam

### Q.3(a) State and explain the modern concept of acids and bases with examples. (04)

**Answer:**

The "modern" concepts of acids and bases transcend the limitation of aqueous solutions (Arrhenius). The two primary modern theories are:

**1. Brønsted-Lowry Concept (Proton Transfer Theory):**
*   **Acid:** Any substance (molecule or ion) that acts as a **proton ($H^+$) donor**.
*   **Base:** Any substance (molecule or ion) that acts as a **proton ($H^+$) acceptor**.
*   *Explanation:* Acid-base reactions are viewed simply as proton transfer reactions.
*   *Example:* $NH_3(aq) + H_2O(l) \rightleftharpoons NH_4^+(aq) + OH^-(aq)$
    Here, $H_2O$ is the acid (donates a proton), and $NH_3$ is the base (accepts the proton).

**2. Lewis Concept (Electron Pair Theory):**
*   **Acid:** Any substance that can **accept a pair of electrons** to form a coordinate covalent bond (an electrophile). Lewis acids are electron-deficient.
*   **Base:** Any substance that can **donate a pair of electrons** to form a coordinate covalent bond (a nucleophile). Lewis bases are electron-rich.
*   *Explanation:* This is the most comprehensive theory as it includes reactions without protons.
*   *Example:* $BF_3 + :NH_3 \rightarrow F_3B-NH_3$
    Here, $BF_3$ is a Lewis acid (it has an incomplete octet and accepts electrons), and $NH_3$ is a Lewis base (it has a lone pair of electrons to donate).

---

---

### Q.3(b) Define buffer solution. Explain the mechanism of buffer action of acidic buffer solution. (04)

**Answer:**

**Buffer Solution:**
A buffer solution is a solution that resists drastic changes in its pH value when small amounts of a strong acid or a strong base are added to it. It has a reserve acidity and reserve alkalinity.

**Mechanism of Buffer Action (Acidic Buffer):**
An acidic buffer consists of a weak acid and a salt of that weak acid with a strong base (e.g., Acetic acid, $CH_3COOH$, and Sodium acetate, $CH_3COONa$).

1.  **Composition in Solution:**
    The weak acid ionizes slightly: $CH_3COOH \rightleftharpoons CH_3COO^- + H^+$
    The salt ionizes completely: $CH_3COONa \rightarrow CH_3COO^- + Na^+$
    Because of the common ion effect from the massive amount of acetate ions ($CH_3COO^-$) from the salt, the ionization of the weak acid is further suppressed. The solution contains a large reserve of un-ionized $CH_3COOH$ and a large reserve of $CH_3COO^-$ ions.

2.  **Action on adding Strong Acid (e.g., $HCl \rightarrow H^+ + Cl^-$):**
    The added $H^+$ ions are highly reactive and would normally drop the pH drastically. However, they are immediately neutralized by the reserve basic acetate ions:
    $CH_3COO^- + H^+ \rightarrow CH_3COOH$
    The highly acidic free $H^+$ is converted into a very weakly acidic, un-ionized molecule ($CH_3COOH$), so the pH barely changes.

3.  **Action on adding Strong Base (e.g., $NaOH \rightarrow Na^+ + OH^-$):**
    The added $OH^-$ ions are neutralized by the small amount of existing $H^+$ ions to form water. As $H^+$ is consumed, Le Chatelier's principle causes the reserve un-ionized acetic acid to dissociate to replace the lost $H^+$:
    $CH_3COOH \rightleftharpoons CH_3COO^- + H^+$
    (Net reaction: $CH_3COOH + OH^- \rightarrow CH_3COO^- + H_2O$)
    The highly basic free $OH^-$ is neutralized, and the pH remains essentially constant.

---

---

### Q.3(c) Define and explain precision and accuracy. (04)

**Answer:**

In analytical chemistry and experimental measurements, accuracy and precision describe two entirely different aspects of data quality:

**1. Precision:**
*   **Definition:** Precision refers to the degree of agreement or reproducibility among a series of individual measurements of the exact same quantity, made under the same conditions.
*   **Explanation:** It describes the "scatter" of the data. If you measure the volume of a liquid five times and get $25.01 \text{ mL}$, $25.02 \text{ mL}$, and $25.01 \text{ mL}$, your measurements are highly precise because they are very close to each other. High precision implies that random errors are very small. *However, precise measurements are not necessarily accurate.*

**2. Accuracy:**
*   **Definition:** Accuracy refers to the degree of closeness or agreement between an experimentally measured value and the true, accepted, or theoretical value of that quantity.
*   **Explanation:** It describes the "correctness" of the data. If the true volume of the liquid is exactly $25.00 \text{ mL}$, and your measurement is $25.01 \text{ mL}$, your measurement is highly accurate. High accuracy implies that systematic errors (biases in the instrument or procedure) are very small.

*(Analogy: On a dartboard, hitting the bullseye is high accuracy. Hitting the same spot on the outer ring three times in a row is high precision, but low accuracy).*

---

---

## 📄 Source: 2018 Exam

### (c) Buffer solution and Buffer's action
A **Buffer Solution** is a specialized aqueous solution that stubbornly resists any drastic or sudden changes in its pH level upon the addition of small to moderate quantities of a strong acid or a strong base.
**Buffer's Action (Mechanism):** This resistance is achieved by having a "reserve" of both an acidic component and a basic component in the solution (usually a weak acid and its conjugate base salt, e.g., Acetic acid + Sodium acetate).
*   If a strong acid (like $HCl$) is added, the highly reactive $H^+$ ions are quickly "mopped up" and neutralized by the reserve conjugate base (acetate ions) to form more of the weak, un-ionized acid.
*   If a strong base (like $NaOH$) is added, the highly reactive $OH^-$ ions are neutralized by the reserve $H^+$ from the weak acid, forcing the weak acid to slightly dissociate to replace the lost protons. In both cases, the dangerous free $H^+$ or $OH^-$ is removed, keeping the pH stable.

---

## 📄 Source: 2018 Exam (Short Notes)

### (c) Buffer solution and Buffer's action
A **Buffer Solution** is a specialized aqueous solution that stubbornly resists any drastic or sudden changes in its pH level upon the addition of small to moderate quantities of a strong acid or a strong base.
**Buffer's Action (Mechanism):** This resistance is achieved by having a "reserve" of both an acidic component and a basic component in the solution (usually a weak acid and its conjugate base salt, e.g., Acetic acid + Sodium acetate).
*   If a strong acid (like $HCl$) is added, the highly reactive $H^+$ ions are quickly "mopped up" and neutralized by the reserve conjugate base (acetate ions) to form more of the weak, un-ionized acid.
*   If a strong base (like $NaOH$) is added, the highly reactive $OH^-$ ions are neutralized by the reserve $H^+$ from the weak acid, forcing the weak acid to slightly dissociate to replace the lost protons. In both cases, the dangerous free $H^+$ or $OH^-$ is removed, keeping the pH stable.

---

## 📄 Source: 2017 Exam (Short Notes)

### (c) Lewis concept of acids and bases.
**Answer:**

Proposed by G.N. Lewis (1923), this is the most comprehensive theory because it completely removes the necessity of hydrogen protons or aqueous solvents. It focuses entirely on electron pairs.
*   **Lewis Acid:** Any chemical species (molecule or ion) that can **accept a pair of electrons** to form a new coordinate covalent bond. Lewis acids are electron-deficient electrophiles. They include molecules with incomplete octets (like $BF_3$, $AlCl_3$) and simple cations (like $H^+$, $Ag^+$).
*   **Lewis Base:** Any chemical species that can **donate a pair of electrons** to form a coordinate covalent bond. Lewis bases are electron-rich nucleophiles. They must have at least one unshared "lone pair" of electrons (like $:NH_3$, $H_2\ddot{O}:$, or anions like $Cl^-$).
*   *Neutralization:* In the Lewis concept, a neutralization reaction is simply the donation of an electron pair from the base to the acid, resulting in the formation of a stable coordinate covalent bond (an adduct). Example: $BF_3 \text{ (Acid)} + :NH_3 \text{ (Base)} \rightarrow F_3B-NH_3 \text{ (Adduct)}$.

---



---

[⬅ 09-Periodic-Table](09-Periodic-Table.md) | [🏠 Index](index.md) | *(end)*
