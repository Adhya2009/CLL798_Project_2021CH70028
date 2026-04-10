# Name: Adhya Makkar
# Entry number: 2021CH70028

import numpy as np
import matplotlib.pyplot as plt

# --- Parameters ---
L = 50          # Grid size (L x L)
P_GROWTH = 0.05 # Probability of a tree growing (p)
P_LIGHTNING = 0.001 # Probability of a lightning strike (f)
STEPS = 500     # Number of generations

# States
EMPTY, TREE, FIRE = 0, 1, 2

def run_simulation():
    grid = np.zeros((L, L))
    history_sizes = []

    for _ in range(STEPS):
        new_grid = grid.copy()
        avalanche_count = 0
        
        for r in range(L):
            for c in range(L):
                # 1. Fire spreads to neighbors
                if grid[r, c] == TREE:
                    # Check 4 neighbors for fire
                    has_fire_neighbor = False
                    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                        nr, nc = (r + dr) % L, (c + dc) % L # Periodic boundaries
                        if grid[nr, nc] == FIRE:
                            has_fire_neighbor = True
                            break
                    
                    if has_fire_neighbor or np.random.rand() < P_LIGHTNING:
                        new_grid[r, c] = FIRE
                        avalanche_count += 1
                
                # 2. Growth
                elif grid[r, c] == EMPTY:
                    if np.random.rand() < P_GROWTH:
                        new_grid[r, c] = TREE
                
                # 3. Fire dies out
                elif grid[r, c] == FIRE:
                    new_grid[r, c] = EMPTY
        
        if avalanche_count > 0:
            history_sizes.append(avalanche_count)
        grid = new_grid

    return history_sizes

# --- Plotting the 'Avalanche' Distribution ---
sizes = run_simulation()
plt.figure(figsize=(10, 5))

# Log-Log plot for SOC analysis
counts, bins = np.histogram(sizes, bins=20)
plt.loglog(bins[:-1], counts, 'bo-', label='Avalanche Size Distribution')
plt.title("Frequency Distribution of Avalanches (Log-Log)")
plt.xlabel("Avalanche Size (S)")
plt.ylabel("Frequency N(S)")
plt.grid(True, which="both", ls="-")
plt.show()
