import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read data-file using Pandas
df = pd.read_csv('timing_data.csv')
max_length = 15
# Calculate new columns
df['sp_pair'] = df['Pair'].iloc[0]/df['Pair'].iloc[0:max_length]
df['sp_bond'] = df['Bond'].iloc[0]/df['Bond'].iloc[0:max_length]
df['sp_kspace'] = df['Kspace'].iloc[0]/df['Kspace'].iloc[0:max_length]
df['sp_neigh'] = df['Neigh'].iloc[0]/df['Neigh'].iloc[0:max_length]
df['sp_comm'] = df['Comm'].iloc[0]/df['Comm'].iloc[0:max_length]
df['sp_wtime'] = df['walltime'].iloc[0]/df['walltime'].iloc[0:max_length]
#df['sp_perform'] = df['Performance']/df['Performance'].iloc[0]

fig, ax = plt.subplots()
ax.plot(df['cores'], df['sp_pair'], label='Pair')
ax.plot(df['cores'], df['sp_bond'], label='Bond')
ax.plot(df['cores'], df['sp_kspace'], label='Kspace')
ax.plot(df['cores'], df['sp_neigh'], label='Neigh')
ax.plot(df['cores'], df['sp_comm'], label='Comm')
ax.plot(df['cores'], df['sp_wtime'], 'o-', label='Walltime')
#ax.plot(df['cores'], df['sp_perform'], '.-', label='Performance')
ax.set(xlabel='Number of cores', ylabel='Speed-up factor',
       title='Speed-up for Rhodopsin system (32,000 atoms) \nInputs taken from LAMMPS bench directory')
ax.grid()
plt.legend()
fig.savefig("scaling_rhodopsin.png")


plt.show()
