[⬅ 04-Colligative-Properties](04-Colligative-Properties.md) | [🏠 Index](00-index.md) | [06-Thermochemistry ➡](06-Thermochemistry.md)

---

# Atomic Structure
**Priority:** 🟠 HIGH | **Frequency:** 14 sub-parts across 5/7 exams

> **Topics Covered:** Bohr's model, quantum numbers, Schrödinger equation, Hund's rule, (n+l) rule, orbit vs orbital, emission/absorption spectra, de Broglie equation.

---

## 📄 Source: 2023 Exam

### Q.1(a) Discuss the postulates of Bohr's atomic model. (04.5)

**Answer:**

**Postulates of Bohr's Atomic Model:**
Niels Bohr proposed his atomic model in 1913 to overcome the limitations of Rutherford's model and to explain the line spectrum of hydrogen. The main postulates are:

1.  **Stationary Circular Orbits:** Electrons revolve around the nucleus in specific, closed circular paths called orbits or shells. These orbits have a fixed radius and energy. As long as an electron remains in a particular orbit, it does not radiate or lose energy. These are called "stationary states."
2.  **Quantization of Angular Momentum:** An electron can only revolve in those orbits for which its orbital angular momentum ($mvr$) is an integral multiple of $h/2\pi$.
    $$mvr = \frac{nh}{2\pi}$$
    Where:
    *   $m$ = mass of the electron
    *   $v$ = velocity of the electron
    *   $r$ = radius of the orbit
    *   $h$ = Planck's constant
    *   $n$ = an integer (1, 2, 3...) called the principal quantum number.
3.  **Energy Levels (Shells):** The stationary orbits are designated as K, L, M, N... shells, corresponding to $n = 1, 2, 3, 4...$ respectively. The energy of an orbit increases as its distance from the nucleus increases.
4.  **Emission and Absorption of Energy:**
    *   Energy is absorbed when an electron jumps from a lower energy orbit to a higher energy orbit (excitation).
    *   Energy is emitted (radiated) in the form of a photon when an electron jumps from a higher energy orbit ($E_2$) back to a lower energy orbit ($E_1$).
    *   The frequency ($\nu$) of the emitted radiation is given by Planck's equation:
        $$\Delta E = E_2 - E_1 = h\nu$$

---

---

### Q.1(b) Distinguish between orbit and orbital. (04)

**Answer:**

| Feature | Orbit | Orbital |
| :--- | :--- | :--- |
| **Definition** | It is a well-defined circular path around the nucleus in which an electron revolves (Bohr's concept). | It is a 3D region in space around the nucleus where the probability of finding an electron is maximum (Quantum mechanical concept). |
| **Shape** | Orbits are strictly circular or elliptical (2D planar motion). | Orbitals have complex 3D shapes (e.g., s-orbital is spherical, p-orbital is dumbbell-shaped). |
| **Directional Characteristic**| Orbits are non-directional as they simply represent a planar path. | Except for the s-orbital, all other orbitals (p, d, f) have directional characteristics. |
| **Heisenberg's Principle** | It violates Heisenberg's Uncertainty Principle because it implies the exact position and momentum of an electron are known simultaneously. | It conforms to Heisenberg's Uncertainty Principle, representing only a "probability cloud" rather than a fixed path. |
| **Maximum Electrons** | The maximum number of electrons an orbit can accommodate is $2n^2$ (where $n$ is the orbit number). | An orbital can accommodate a maximum of only 2 electrons (with opposite spins). |

---

---

### Q.1(c) What is emission spectrum? (01.5)

**Answer:**

**Emission Spectrum:**
An emission spectrum is the spectrum of frequencies (or wavelengths) of electromagnetic radiation emitted by an atom's electrons when they transition from a higher energy state (excited state) down to a lower energy state. It typically appears as a series of distinct, bright, colored lines against a dark background. Because each element has a unique set of quantized energy levels, its emission spectrum serves as a unique "fingerprint" identifying that element.

---

---

### Q.2(a) Define Magnetic quantum number. (02)

**Answer:**

**Magnetic Quantum Number ($m_l$):**
The magnetic quantum number determines the spatial orientation of an orbital relative to the standard coordinate axes when the atom is placed in an external magnetic field.
It describes how the electron cloud is oriented in 3D space. For a given azimuthal quantum number ($l$), $m_l$ can take integral values ranging from $-l$ through $0$ to $+l$. The total number of possible $m_l$ values for a given subshell is $(2l + 1)$, which corresponds to the total number of orbitals in that subshell.

---

---

### Q.2(b) Find the all quantum number for n=4. (02)

**Answer:**

For the principal quantum number $n = 4$ (the N shell), the possible values for the other quantum numbers are:

1.  **Azimuthal Quantum Number ($l$):** Takes values from $0$ to $(n-1)$.
    $l = 0, 1, 2, 3$ (corresponding to s, p, d, and f subshells).
2.  **Magnetic Quantum Number ($m_l$):** Takes values from $-l$ to $+l$.
    *   For $l = 0$ (4s): $m_l = 0$ (1 orbital)
    *   For $l = 1$ (4p): $m_l = -1, 0, +1$ (3 orbitals)
    *   For $l = 2$ (4d): $m_l = -2, -1, 0, +1, +2$ (5 orbitals)
    *   For $l = 3$ (4f): $m_l = -3, -2, -1, 0, +1, +2, +3$ (7 orbitals)
    *(Total number of orbitals = $1+3+5+7 = 16 = n^2$)*
3.  **Spin Quantum Number ($m_s$):**
    For every single value of $m_l$ (i.e., inside each of the 16 orbitals), the electron can have two possible spin states:
    $m_s = +\frac{1}{2}$ (spin up) or $-\frac{1}{2}$ (spin down).
    *(Total maximum electrons in n=4 shell = $16 \times 2 = 32 = 2n^2$)*.

---

---

## 📄 Source: 2021 Exam

### Q.5(a) Distinguish between emission spectrum and absorption spectrum. (04)

**Answer:**

| Feature | Emission Spectrum | Absorption Spectrum |
| :--- | :--- | :--- |
| **Formation** | Formed when atoms in an excited state return to a lower energy state by emitting radiation. | Formed when a continuous white light passes through a cool gas/substance, and atoms absorb specific wavelengths to jump to higher energy states. |
| **Appearance** | Consists of bright, colored lines against a completely dark background. | Consists of dark lines (missing wavelengths) against a continuous bright, colored background. |
| **Source** | Produced directly by heating a substance or passing an electric discharge through a gas. | Produced by transmitting light from an external source through a transparent absorbing medium. |
| **Wavelengths** | The wavelengths of the emitted bright lines are characteristic of the emitting element. | The wavelengths of the dark absorption lines exactly match the bright lines the element would emit. |

---

---

### Q.5(b) Explain quantum numbers and their significances in characterizing an electron in an atom. (04)

**Answer:**

Quantum numbers are a set of four numerical values that provide a complete quantum mechanical description of an electron in an atom, specifying its energy, location, and spin.

1.  **Principal Quantum Number ($n$):**
    *   **Values:** $1, 2, 3, \dots$
    *   **Significance:** It designates the main energy shell (K, L, M, N...) the electron belongs to. It primarily determines the average distance of the electron from the nucleus (size of the orbital) and the total energy of the electron.
2.  **Azimuthal (or Angular Momentum) Quantum Number ($l$):**
    *   **Values:** $0$ to $(n-1)$.
    *   **Significance:** It designates the specific subshell (s, p, d, f) within the main shell. It defines the three-dimensional shape of the orbital (e.g., $l=0$ is spherical, $l=1$ is dumbbell-shaped) and the orbital angular momentum of the electron.
3.  **Magnetic Quantum Number ($m_l$):**
    *   **Values:** $-l$ through $0$ to $+l$.
    *   **Significance:** It determines the spatial orientation of the orbital relative to an external magnetic field. It dictates how many specific orbitals exist within a given subshell (e.g., three p-orbitals: $p_x, p_y, p_z$).
4.  **Spin Quantum Number ($m_s$):**
    *   **Values:** $+1/2$ or $-1/2$.
    *   **Significance:** It describes the intrinsic angular momentum (spin) of the electron about its own axis (spin-up or spin-down). It is responsible for the magnetic properties of the atom.

---

---

### Q.5(c) Derive de-Broglie's equation for a particle of mass 'm' and moving with a velocity of 'v'. (04)

**Answer:**

**Derivation of de-Broglie's Equation:**
Louis de Broglie proposed that just as light exhibits wave-particle duality, all moving material particles also possess wave-like characteristics. He derived the relationship between the momentum of a particle and the wavelength of its associated wave (matter wave).

According to Planck's quantum theory, the energy ($E$) of a photon of light acting as a wave is given by:
$$E = h\nu \quad \dots \text{(Equation 1)}$$
Where $h$ is Planck's constant and $\nu$ is the frequency of the wave.
Since $\nu = c/\lambda$ (where $c$ is the speed of light and $\lambda$ is the wavelength),
$$E = \frac{hc}{\lambda} \quad \dots \text{(Equation 2)}$$

According to Einstein's mass-energy equivalence principle, if the photon is considered a particle of mass $m$, its energy is:
$$E = mc^2 \quad \dots \text{(Equation 3)}$$

Equating the energy from Equation 2 and Equation 3:
$$mc^2 = \frac{hc}{\lambda}$$

Rearranging to solve for the wavelength ($\lambda$):
$$\lambda = \frac{hc}{mc^2}$$
$$\lambda = \frac{h}{mc}$$

de Broglie suggested that this equation, derived for a photon, also applies to material particles. For a material particle of mass $m$ moving with a velocity $v$ (instead of the speed of light $c$), the equation becomes:
$$\lambda = \frac{h}{mv}$$

Since mass $\times$ velocity = momentum ($p$), the equation can be written as:
$$\lambda = \frac{h}{p}$$

This is the de-Broglie equation, which beautifully links the wave nature ($\lambda$) and particle nature ($p$ or $mv$) of matter.

---

---

## 📄 Source: 2020 Exam

### Q.6(a) Write the postulates and limitations of Bohr's Atomic Model. (06)

**Answer:**

**Postulates of Bohr's Atomic Model:**
1.  **Stationary Orbits:** Electrons revolve around the positively charged nucleus in specific, closed, circular paths called orbits or stationary states (K, L, M, N...). While in these orbits, electrons do not radiate or lose energy.
2.  **Quantization of Angular Momentum:** An electron can only revolve in those specific orbits where its angular momentum ($mvr$) is an integral multiple of $h/2\pi$.
    $mvr = n \frac{h}{2\pi}$ (where $n = 1, 2, 3 \dots$)
3.  **Energy Transition:** Energy is only absorbed or emitted when an electron jumps from one stationary orbit to another.
    *   Jumping from a lower to a higher orbit absorbs energy.
    *   Jumping from a higher to a lower orbit emits energy as a photon.
4.  **Frequency of Emitted Radiation:** The energy of the emitted or absorbed photon is exactly equal to the energy difference between the two orbits.
    $\Delta E = E_{higher} - E_{lower} = h\nu$

**Limitations of Bohr's Atomic Model:**
1.  **Multi-electron Atoms:** It successfully explains the spectrum of single-electron species (like H, $He^+$, $Li^{2+}$) but completely fails to explain the spectra of multi-electron atoms.
2.  **Fine Structure:** It cannot explain the fine structure of spectral lines (the splitting of a single line into closely spaced multiple lines when observed under high-resolution spectrometers).
3.  **Zeeman and Stark Effects:** It fails to explain the splitting of spectral lines under the influence of an external magnetic field (Zeeman effect) or an external electric field (Stark effect).
4.  **Heisenberg's Uncertainty Principle:** Bohr assumes electrons have a known radius and known velocity simultaneously, which violates the Heisenberg Uncertainty Principle.
5.  **Wave Nature of Electron:** It treats the electron purely as a particle revolving in a 2D planar orbit, completely ignoring the wave nature of the electron proposed by de Broglie and the 3D probability model of orbitals.

---

---

### Q.6(b) Define spectrum and classify them. (04)

**Answer:**

**Spectrum:**
When a beam of electromagnetic radiation (like white light) is passed through a dispersing medium such as a prism or a diffraction grating, it splits into its constituent wavelengths or frequencies. The resulting ordered arrangement or pattern of these distinct lines, bands, or colors is called a spectrum.

**Classification of Spectra:**
Spectra are broadly classified into two main types based on how they are produced:

1.  **Emission Spectrum:** Produced when radiation emitted directly from a source (like a heated gas or an electric discharge) is analyzed. It appears as bright lines or bands on a dark background. It is further divided into:
    *   *Continuous Spectrum:* Contains unbroken bands of all wavelengths (e.g., rainbow, incandescent bulb).
    *   *Line Spectrum:* Contains sharp, distinct, separated bright lines (characteristic of atoms, e.g., Hydrogen spectrum).
    *   *Band Spectrum:* Contains groups of closely spaced lines appearing as fluted bands (characteristic of molecules).
2.  **Absorption Spectrum:** Produced when continuous white light is first passed through an absorbing sample (like a cool gas) before passing through the prism. The sample absorbs specific wavelengths to excite its electrons. This results in dark gaps or dark lines appearing on the otherwise continuous bright background.

---

---

### Q.6(c) Atomic spectrum is the finger point for the concerned atom. Explain it. (02)

**Answer:**

An atomic spectrum (specifically the line emission spectrum) consists of distinct, sharply defined bright lines of specific wavelengths. These wavelengths correspond exactly to the discrete energy differences between the quantized energy levels within that specific atom.
Because the atomic structure, the number of protons, and the specific spacing of energy levels are uniquely different for every chemical element, no two elements can ever produce the exact same pattern of spectral lines. Just as a human fingerprint uniquely identifies a person, the exact pattern and frequencies of an atomic spectrum uniquely identify the element producing it, making it the "fingerprint" of the atom.

---

---

## 📄 Source: 2019 Exam

### Q.1(a) Explain the origin of band spectrum and line spectrum. (04)

**Answer:**

**Origin of Line Spectrum:**
A line spectrum originates from **atoms** (atomic spectrum). When isolated gaseous atoms are excited (by heating or electric discharge), their electrons absorb energy and jump to higher, unstable energy levels. When these electrons transition back down to lower, more stable energy levels, they emit energy in the form of photons. Because the energy levels in an atom are strictly quantized (discrete), the energy differences between them are also quantized ($\Delta E = h\nu$). This results in the emission of electromagnetic radiation of very specific, discrete frequencies, which appear as sharp, distinctly separated bright lines on the spectrum.

**Origin of Band Spectrum:**
A band spectrum originates from **molecules** (molecular spectrum). Unlike atoms, molecules have vibrational and rotational energy levels in addition to electronic energy levels. For every electronic energy level, there are many closely spaced vibrational levels, and for every vibrational level, there are many closely spaced rotational levels. When a molecule is excited and transitions between electronic states, it can simultaneously undergo numerous vibrational and rotational transitions. Because these sub-levels are packed so closely together, the resulting emitted frequencies are incredibly close to one another. Instead of appearing as isolated sharp lines, thousands of these closely spaced lines merge together, appearing as continuous, fluted bands of color.

---

---

### Q.1(b) Describe the postulates of Bohr's atomic model. Mention its limitations. (08)

**Answer:**

**Postulates of Bohr's Atomic Model:**
1.  **Stationary Orbits:** Electrons revolve around the positively charged nucleus in specific, closed, circular paths called orbits or stationary states (K, L, M, N...). While in these orbits, the centrifugal force perfectly balances the electrostatic attraction, and electrons do not radiate or lose energy.
2.  **Quantization of Angular Momentum:** An electron can only revolve in those specific orbits where its angular momentum ($mvr$) is an integral multiple of $h/2\pi$.
    $mvr = n \frac{h}{2\pi}$ (where $n = 1, 2, 3 \dots$)
3.  **Energy Transition:** Energy is only absorbed or emitted when an electron jumps from one stationary orbit to another.
    *   Jumping from a lower to a higher orbit absorbs energy.
    *   Jumping from a higher to a lower orbit emits energy as a photon.
4.  **Frequency of Emitted Radiation:** The energy of the emitted or absorbed photon is exactly equal to the energy difference between the two orbits.
    $\Delta E = E_{higher} - E_{lower} = h\nu$

**Limitations of Bohr's Atomic Model:**
1.  **Multi-electron Atoms:** It successfully explains the spectrum of single-electron species (like H, $He^+$, $Li^{2+}$) but completely fails to explain the spectra of multi-electron atoms.
2.  **Fine Structure:** It cannot explain the fine structure of spectral lines (the splitting of a single line into closely spaced multiple lines when observed under high-resolution spectrometers).
3.  **Zeeman and Stark Effects:** It fails to explain the splitting of spectral lines under the influence of an external magnetic field (Zeeman effect) or an external electric field (Stark effect).
4.  **Heisenberg's Uncertainty Principle:** Bohr assumes electrons have a known radius and known velocity simultaneously, which violates the Heisenberg Uncertainty Principle.
5.  **Wave Nature of Electron:** It treats the electron purely as a particle revolving in a 2D planar orbit, completely ignoring the wave nature of the electron proposed by de Broglie.

---

---

## 📄 Source: 2018 Exam

### Q1 Short note: (12)
### (a) Schrodinger's wave equation
**Answer:**
The Schrödinger wave equation is the fundamental mathematical equation of wave mechanics (quantum mechanics) that describes the wave-like behavior of an electron in an atom. Proposed by Erwin Schrödinger in 1926, it relates the energy of an electron to its wave function ($\psi$).
For an electron of mass $m$ and potential energy $V$ moving in three-dimensional space ($x, y, z$), the time-independent Schrödinger wave equation is:
$$\frac{\partial^2\psi}{\partial x^2} + \frac{\partial^2\psi}{\partial y^2} + \frac{\partial^2\psi}{\partial z^2} + \frac{8\pi^2m}{h^2}(E - V)\psi = 0$$
Where:
*   $\psi$ (psi) = wave function (amplitude of the electron wave)
*   $E$ = Total energy of the electron
*   $h$ = Planck's constant
Solving this differential equation yields quantized energy levels (eigenvalues) and specific wave functions (orbitals). The square of the wave function, $|\psi|^2$, gives the probability of finding the electron at a specific point in space.

---

### (b) Magnetic quantum number
**Answer:**
The magnetic quantum number ($m_l$) is the third quantum number derived from the Schrödinger wave equation.
*   **Significance:** It specifies the spatial orientation of an orbital within a particular subshell under the influence of an external magnetic field. It dictates exactly how many specific orbitals exist within that subshell.
*   **Values:** For any given azimuthal quantum number ($l$), $m_l$ can take integral values ranging from $-l$ through $0$ to $+l$. This results in exactly $(2l + 1)$ values.
*   *Example:* If $l=1$ (a p-subshell), $m_l$ can be $-1, 0, +1$, indicating there are three p-orbitals oriented differently in space ($p_x, p_y, p_z$).

---

### (c) Hund's principle and (n+l) rules
**Answer:**
**Hund's Rule of Maximum Multiplicity:** This rule governs the filling of electrons in degenerate orbitals (orbitals with identical energy, such as the three p-orbitals or five d-orbitals). It states that electron pairing will not occur in degenerate orbitals until each orbital of that given subshell is singly occupied with an electron, and all these single electrons must have parallel spins. This arrangement minimizes inter-electronic repulsion and maximizes stability.

**(n+l) Rule (Madelung's Rule):** This rule is used to determine the relative energy order of different atomic orbitals, deciding the sequence in which they are filled according to the Aufbau principle.
1.  Orbitals with a lower sum of $(n+l)$ have lower potential energy and are filled with electrons first. (e.g., $4s$: $n+l = 4+0=4$; $3d$: $n+l = 3+2=5$. Thus, $4s$ is filled before $3d$).
2.  If two distinct orbitals happen to have the exact same $(n+l)$ value, the orbital with the lower principal quantum number '$n$' has the lower energy and is filled first. (e.g., $3p$: $3+1=4$; $4s$: $4+0=4$. The $3p$ orbital is filled first because $3 < 4$).

---


---

[⬅ 04-Colligative-Properties](04-Colligative-Properties.md) | [🏠 Index](00-index.md) | [06-Thermochemistry ➡](06-Thermochemistry.md)
