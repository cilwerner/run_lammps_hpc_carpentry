import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read data-file using Pandas
df = pd.read_csv('CPUvsGPU.csv')
max_length = 8
# Calculate new columns
df['pf_cpu'] = df['CPU']
df['pf_gpu'] = df['GPU']
df['pf_kkgpu'] = df['Kokkos/GPU']
df['sp_factor_gpu'] = df['pf_gpu']/df['pf_cpu']
df['sp_factor_kkgpu'] = df['pf_kkgpu']/df['pf_cpu']

fig, ax1 = plt.subplots()
ax1.plot(df['nodes'], df['pf_cpu'],'o-',label='CPU')
ax1.plot(df['nodes'], df['pf_gpu'],'*-', label='GPU Package')
ax1.plot(df['nodes'], df['pf_kkgpu'],'v-',label='Kokkos GPU package')
#ax1.legend()


ax1.grid()
plt.xlabel('Number of nodes', fontsize=12)
plt.ylabel('Performance (timesteps/second)', fontsize=12)
plt.title('Lennard-Jones system with ~11 million atoms \n Intel Xeon E5-2680 v3 Haswell CPU 2x12 Cores \n with four K80 GPUs per node and Mellanox EDR InfiniBand network \n GPU settings: "-sf gpu -pk gpu 4 neigh yes newton off split 1.0" with 6 MPI ranks/GPU\n LAMMPS version: 3Mar20, Intel Compiler and CUDA', fontsize=8)


ax2 = ax1.twinx()
color = 'red'
ax2.set_ylabel('speed-up factor', color=color, fontsize=12)  # we already handled the x-label with ax1
ax2.set_ylim([1,10])
ax2.plot(df['nodes'],df['sp_factor_gpu'],'*--', color='tab:orange',label='speed-up for GPU package')
ax2.plot(df['nodes'],df['sp_factor_kkgpu'],'v:', color='tab:green',label='speed-up for Kokkos/GPU package')
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()  # otherwise the right y-label is slightly clipped


h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1+h2, l1+l2, loc=2)


fig.savefig("CPUvsGPUvsKKGPU.png")
plt.show()
