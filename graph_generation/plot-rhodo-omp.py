import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Read data-file using Pandas
df = pd.read_csv('rhodo_omp_scale.csv')
max_length = 10
T1 = 7019 

# Calculate new columns
df['pe_mpi_only'] = (1.0/df['nodes'].iloc[0:max_length]/40.0)*(T1/df['MPI-only'].iloc[0:max_length])*100
df['pe_1mpi_40t'] = (1.0/df['nodes'].iloc[0:max_length]/40.0)*(T1/df['1 MPI x 40 OpenMP'].iloc[0:max_length])*100
df['pe_2mpi_20t'] = (1.0/df['nodes'].iloc[0:max_length]/40.0)*(T1/df['2 MPI x 20 OpenMP'].iloc[0:max_length])*100
df['pe_4mpi_10t'] = (1.0/df['nodes'].iloc[0:max_length]/40.0)*(T1/df['4 MPI x 10 OpenMP'].iloc[0:max_length])*100
df['pe_5mpi_8t'] = (1.0/df['nodes'].iloc[0:max_length]/40.0)*(T1/df['5 MPI x 8 OpenMP'].iloc[0:max_length])*100
df['pe_8mpi_5t'] = (1.0/df['nodes'].iloc[0:max_length]/40.0)*(T1/df['8 MPI x 5 OpenMP'].iloc[0:max_length])*100
df['pe_10mpi_4t'] = (1.0/df['nodes'].iloc[0:max_length]/40.0)*(T1/df['10 MPI x 4 OpenMP'].iloc[0:max_length])*100
df['pe_20mpi_2t'] = (1.0/df['nodes'].iloc[0:max_length]/40.0)*(T1/df['20 MPI x 2 OpenMP'].iloc[0:max_length])*100
df['pe_40mpi_1t'] = (1.0/df['nodes'].iloc[0:max_length]/40.0)*(T1/df['40 MPI x 1 OpenMP'].iloc[0:max_length])*100

#print(df['pe_1mpi_40t'], df['pe_2mpi_20t'])
print(df['pe_40mpi_1t'])
"""
print(df['pe_1mpi_40t'])
print(df['pe_2mpi_20t'])
print(df['pe_4mpi_10t'])
print(df['pe_5mpi_8t'])
print(df['pe_8mpi_5t'])
print(df['pe_10mpi_4t'])
print(df['pe_20mpi_2t'])
print(df['pe_40mpi_1t'])
"""
fig, ax = plt.subplots()
ax.plot(df['nodes'], df['pe_mpi_only'],'h-', label='MPI-only (n nodes x 40 cores)',linewidth=3.0)
ax.plot(df['nodes'], df['pe_1mpi_40t'],'*-',label='1 MPI x 40 OpenMP')
ax.plot(df['nodes'], df['pe_2mpi_20t'],'+-', label='2 MPI x 20 OpenMP')
ax.plot(df['nodes'], df['pe_4mpi_10t'],'x-',label='4 MPI x 10 OpenMP')
ax.plot(df['nodes'], df['pe_5mpi_8t'],'s-',label='5 MPI x 8 OpenMP')
ax.plot(df['nodes'], df['pe_8mpi_5t'],'<-',label='8 MPI x 5 OpenMP')
ax.plot(df['nodes'], df['pe_10mpi_4t'],'>-',label='10 MPI x 4 OpenMP')
ax.plot(df['nodes'], df['pe_20mpi_2t'], 'o-',label='20 MPI x 2 OpenMP',linewidth=4.0)
ax.plot(df['nodes'], df['pe_40mpi_1t'], 'v-', label='40 MPI x 1 OpenMP',linewidth=4.0)

ax.grid()
plt.xlabel('Number of nodes', fontsize=14)
plt.ylabel('Parallel efficiency (%)', fontsize=14)
plt.title('Intel Xeon Gold 6148 (Skylake) processors with 2x20-core 2.4 GHz, 192 GiB of RAM\nRhodopsin system (32,000 atoms),lj/charmm/coul/long + PPPM\nwith USER-OMP (Intel compiler 2019u5, GCC 8.2.0)')

plt.legend()
fig.savefig("pe_omp_rhodopsin.png")


plt.show()
