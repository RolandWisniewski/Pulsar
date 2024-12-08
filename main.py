import h5py
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import AutoMinorLocator

# Load data
filename = "J0953+0755_602MHz_07Mar14_SP_I.hdf5"
with h5py.File(filename, 'r') as f:
    data = np.array(f.get('default'))

def stddev(data, row):
    """Compute standard deviation for a sliding window."""
    left_border = 0
    right_border = 100
    avg = 0
    std_list = []
    data_row = data[row]
    while right_border <= 1000:
        new_data = data_row[left_border:right_border]
        std_list.append(np.std(new_data))
        left_border += 50
        right_border += 50
    left_border = 50 * std_list.index(min(std_list))
    right_border = left_border + 100
    avg = sum(data_row[left_border:right_border]) / 100
    return data_row - avg
    
def format_axes(fig):
    """Format plot axes with minor ticks."""
    for i, ax in enumerate(fig.axes):
        ax.xaxis.set_minor_locator(AutoMinorLocator(2))
        ax.yaxis.set_minor_locator(AutoMinorLocator(2))
        ax.tick_params(which='major', direction='in', length=5, top=True, right=True)
        ax.tick_params(which='minor', direction='in', length=2, top=True, right=True)
        
def pulse_width_peak(x):
    """Calculate pulse width (W) and width-to-separation time (WST)."""
    ms = 0.256
    m = max(new_data2)
    f1 = [i for i, j in enumerate(new_data2) if j == m][0]
    f2 = [i for i, j in enumerate(new_data2) if j == m][0]
    while new_data2[f1] > x*m:
        f1 -= 1
    while new_data2[f2]-1 > x*m:
        f2 += 1
    W = round(((f2-f1)*ms), 2)
    WST = round(((W/1000*360)/0.71), 2)
    return W, WST

# Process data
row = 1245
r_min = row
r_max = 1309
new_data = []
total_energy = []

while row <= r_max-1:
    total_energy.append(np.sum(stddev(data, row)))
    new_data = np.append(new_data, stddev(data, row)[500:750])
    row += 1

new_data = new_data.reshape(r_max-r_min, 250)
new_data2 = np.apply_along_axis(np.mean, 0 , new_data)

# Normalize total energy
total_energy2 = []
for i in total_energy:
    total_energy2.append(i/max(total_energy))

# Plotting
fig = plt.figure(figsize=(6, 9))
gs0 = GridSpec(6, 10, figure=fig, wspace=0, hspace=0)
gs1 = GridSpec(6, 22, figure=fig, hspace=0)

# Fluctuation spectra
ax1 = fig.add_subplot(gs0[:5, 2:9])
img = ax1.imshow(new_data, cmap='hot', aspect='auto', origin='lower', vmin=0, vmax=600)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.text(75, r_max-r_min+0.5, "Fluctuation spectra")

# Total energy
ax2 = fig.add_subplot(gs0[:5, :2])
ax2.plot(total_energy2, [_ for _ in range(len(total_energy2))], 'indigo', drawstyle='steps-pre')
ax2.margins(0.1, 0)
ax2.set_ylabel("Pulse Number")
ax2.text(-0.07, len(total_energy2), "Total energy")

# Average profile
ax3 = fig.add_subplot(gs0[5, 2:9])
ax3.plot([(499+i)/3.6 for i in range(250)], new_data2/100, 'indigo')
ax3.margins(0, 0.1)
ax3.set_xlabel("Pulse Phase (°)")
ax3.set_ylabel("Intensity")
ax3.text(755/3.6, max(new_data2)/100, "Average profile", rotation=-90, rotation_mode="anchor")

# Colorbar
ax4 = fig.add_subplot(gs1[:5, 20])
plt.colorbar(img, cax=ax4)
ax4.set_ylabel("Flux (arbitrary units)")

# Add title and format
fig.suptitle("J0953+0755", x=0.56, y=0.96, size="xx-large", weight=800)
format_axes(fig)

# Pulse width metrics
print(f"W50 = {pulse_width_peak(0.5)[0]} ms")
print(f"W50 = {pulse_width_peak(0.5)[1]}°")
print(f"W10 = {pulse_width_peak(0.1)[0]} ms")
print(f"W10 = {pulse_width_peak(0.1)[1]}°")

# Show first plot
plt.show()

# Create new Figure with black background
fig = plt.figure(figsize=(8, 8), facecolor='black')

# Add a subplot with no frame
ax = plt.subplot(frameon=False)

# Plot each row of the data with dynamic scaling and line width
X = np.linspace(-1, 1, new_data.shape[-1])
G = 0.005
for i in range(len(new_data)-1, -1, -1):
    xscale = 1 - i / 200
    lw = 1.5 - i / 100
    x = xscale * X
    y = i + G * new_data[i]
    ax.fill_between(x, y, y+0.2, color="white", lw=lw)
    ax.fill_between(x, y, color="black", lw=lw)

# Set y limit (or first line is cropped because of thickness)
ax.set_ylim(-1, 70)

# No ticks
ax.set_xticks([])
ax.set_yticks([])

# 2 part titles to get different font weights
ax.text(0.5, 1.0, "PULSAR ", transform=ax.transAxes,
        ha="right", va="bottom", color="w",
        family="sans-serif", fontweight="bold", fontsize=16)
ax.text(0.5, 1.0, "J0953+0755", transform=ax.transAxes,
        ha="left", va="bottom", color="w",
        family="sans-serif", fontweight="light", fontsize=16)

# Show second plot
plt.show()
