#  Self-Organized Criticality in the Forest Fire Model

Author:Adhya Makkar  
Entry Number: 2021CH70028  
Course: CLL 798: Complexity Science in Chemical Industry  

---

# 1. Introduction to the System

This project explores **Self-Organized Criticality (SOC)** through a 2D Forest Fire Model.  

SOC is a property of certain dynamical systems where they naturally evolve toward a *critical point* without external fine-tuning. In this state, even a minor event (like a single spark) can lead to a massive event (such as a forest-wide fire).

### Why this is a Complex System

- **Non-linearity:**  
  The spread of fire depends on the specific arrangement of trees.

- **Emergence:**  
  Large-scale patterns (avalanches) emerge from simple, local interaction rules.

- **Scale Invariance:**  
  The system exhibits similar behavior across different scales, characterized by a power-law distribution of fire sizes.

---

## 2. Model Description

The simulation is a **Cellular Automaton** governed by three primary factors:

- **Noise:**  
  Represented by the random growth of trees (`p`) and occasional lightning strikes (`f`).

- **Connectivity:**  
  Trees are "connected" if they are neighbors on the `L × L` grid. Fire spreads only between connected trees.

- **Avalanches:**  
  A fire that starts at one point and propagates through a connected cluster.  
  The size of an avalanche is the total number of trees burned in a single time step.

---

## 3. How the Code Works

The Python script executes the following steps at each generation:

- **Fire Propagation:**  
  Any tree adjacent to a burning cell catches fire.

- **Spontaneous Ignition:**  
  A tree may catch fire via lightning with probability `f`.

- **Growth:**  
  Empty cells grow trees with probability `p`.

- **Extinction:**  
  Burning cells become empty in the next step.

- **Periodic Boundaries:**  
  The grid is treated as a torus (edges wrap around), ensuring uniform connectivity across the system.

---

## 4. Analysis & Results

The simulation generates a **log-log plot** of avalanche size vs frequency.

- The plot shows a **linear trend on a log-log scale**, indicating a power-law distribution:

  N(S) ∝ S^(-τ)

- This confirms that the system reaches a **self-organized critical state**.

### Key Insight

The system naturally evolves to the **edge of chaos**, balancing:
- Tree growth
- Fire spread

This results in:
- Frequent small fires  
- Rare but large-scale events  

---

## ▶️ How to Run

python forest_fire.py

---

## 📊 Output

- Log-log plot of avalanche size distribution  
- Visualization of SOC behavior  
