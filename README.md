# Discrete High-Fidelity Audio Amplifier 

**Author:** Mehrshad Arshad  

This repository contains the complete two-phase design and SPICE-level validation of a discrete high-fidelity audio amplifier, developed as my 4th-semester Electronics II final project at Sharif University of Technology. The project demonstrates the progression from a high-gain open-loop architecture to a highly linear, low-distortion closed-loop system capable of driving heavy $50\Omega$ loads.

## Technologies & Simulation Automation
* **Environment:** LTspice
* **Custom Device Modeling:** Configured specific forward current gains for discrete BJTs (`2N3904 bf=200`, `2N3906 bf=150`).
* **SPICE Automation:** Implemented custom `.meas` and `.FOUR` directives to automate the extraction of RMS power, efficiency, and Total Harmonic Distortion (THD) directly from the transient analysis.
* **Noise Injection:** Utilized mathematical white noise generation (`V=(white(2e6*time) / 4)`) in the bias network to stress-test Power Supply Rejection Ratio (PSRR) and closed-loop THD.

## Phase I: Open-Loop High-Gain Architecture
The initial objective was to maximize differential gain and Common-Mode Rejection Ratio (CMRR) while minimizing output resistance prior to feedback.
* **Design:** A BJT differential input pair loaded by a Folded-Cascode stage to maximize output impedance. A Class-A Darlington buffer was utilized to step down the output impedance. Biasing was distributed via a master current reference and Wilson current mirrors.
* **Extracted Metrics:**
  * **Differential Voltage Gain ($A_{vd}$):** 92.3 dB
  * **CMRR:** 118 dB
  * **Input Resistance ($R_{in}$):** 103 kΩ
  * **Output Resistance ($R_{out}$):** 3.9 kΩ
  * **Quiescent Power ($P_Q$):** 24 mW

## Phase II: Closed-Loop Power Amplification & Audio DSP
To drive a heavy **$50\Omega$** load without exceeding the $190\text{ mW}$ total power budget, the output stage was completely re-architected. 
* **Design Pivot:** The Class-A buffer was replaced with a Class-AB Push-Pull Sziklai pair. A $V_{BE}$ multiplier was introduced to precisely bias the output transistors and eliminate crossover distortion. Global negative feedback ($R_f = 200\text{ k}\Omega$, $R_g = 10\text{ k}\Omega$) was applied to linearize the response.
* **Extracted Metrics:**
  * **Closed-Loop Gain:** 21 V/V
  * **Output Swing:** 16 Vpp (Symmetrical, zero clipping)
  * **THD:** 0.0074% (Clean) / 0.039% (Under thermal noise injection)
  * **Output Stage Efficiency ($\eta_{out}$):** 69.57%
  * **PSRR:** 73.98 dB
  * **Output Resistance ($R_{out}$):** 0.28 Ω
* **Audio Validation:** Processed a 44.1 kHz, 16-bit `.wav` audio file through the transient SPICE model, proving the transient stability and linearity of the closed-loop design under complex load conditions.
