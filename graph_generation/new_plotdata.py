import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read data-file using Pandas
df = pd.read_csv('performance_gpu.csv')
max_length = 6
# Calculate new columns
df['norm_4k'] = df['4K atoms'].iloc[0:max_length]/df['4K atoms'].max()
print(df['norm_4k'], df['4K atoms'].iloc[0:max_length])
df['norm_256k'] = df['256K atoms'].iloc[0:max_length]/df['256K atoms'].max()
df['norm_11M'] = df['11M atoms'].iloc[0:max_length]/df['11M atoms'].max()

fig, ax = plt.subplots()
ax.plot(df['cores'], df['norm_4k'],'o-',label='4K atoms')
ax.plot(df['cores'], df['norm_256k'],'*-', label='256K atoms')
ax.plot(df['cores'], df['norm_11M'],'v-',label='11M atoms')

ax.grid()
plt.xlabel('Number of cores', fontsize=12)
plt.ylabel('Normalized Speed-up factor per node', fontsize=12)
plt.title('Lennard-Jones system in a Intel Xeon E5-2680 v3 Haswell CPU 2x12 Cores \n with four NVIDIA K80 GPUs per node and Mellanox EDR InfiniBand network\n LAMMPS version 3Mar20, Intel compiler and CUDA', fontsize=8)

plt.legend()
plt.show()

fig.savefig("gpu_mpi_counts.png")

