# 🌌 Pulsar Data Visualization

This project visualizes pulsar data for J0953+0755, focusing on pulse intensity and pulse phase fluctuations. The analysis includes standard deviation filtering, total energy computation, and a detailed visualization of the pulsar's fluctuation spectra, average profile, and total energy. The code also computes and displays pulse width metrics such as $W_{50}$ and $W_{10}$.

## 🌟 Features

### 1. Standard Deviation Filtering
Applies a sliding window filter to the data, centering it by subtracting the local mean intensity over a selected window.

### 2. Pulse Width Calculation
Determines key metrics:
* $W_{50}$: Pulse width at 50% of the peak intensity.
* $W_{10}$: Pulse width at 10% of the peak intensity.
Both metrics are expressed in milliseconds ($ms$) and degrees (°) of pulse phase.

### 3. Total Energy Computation
Calculates the total energy of each pulse, normalized to show relative differences between pulses.

### 4. Data Visualization
* Fluctuation Spectra: Displays intensity variations over multiple pulses.
* Average Profile: Highlights the mean intensity profile across the pulse phase.
* Total Energy: Plots normalized pulse energy to emphasize variability.

### 5. Artistic Pulsar Rendering
Generates a unique, stylized visualization of pulse data with a black background, simulating dynamic pulse scaling.

## 📁 Data Overview

### Dataset:
* File: `J0953+0755_602MHz_07Mar14_SP_I.hdf5`
* Format: HDF5
* Key: `default` (contains pulse intensity data)

### Dimensions:
* Rows: Represent individual pulses.
* Columns: Represent data points within each pulse.

## 🔧 How to Run

###Prerequisites
* Python 3.x
* Required libraries:
```bash
pip install h5py numpy matplotlib
```

###Run the Code
1. Ensure the dataset is in the same directory as the script.
2. Execute the script:
```bash
python pulsar_analysis.py
```

## 🪐 Example Output

1. Pulse Width Metrics
```bash
W50 = 8.96 ms
W50 = 4.54°
W10 = 19.71 ms
W10 = 9.99°
```
2. Plots

<p align="center">
 <img src="https://github.com/user-attachments/assets/5ce3de23-eb20-48a4-9cbd-24f609cb814f">
 <img src="https://github.com/user-attachments/assets/a55755c8-2fcb-4e3d-b585-8d1aa4119414">
</p>

## 🤝 Contribution

Contributions are welcome! If you have ideas for optimization or new features, feel free to fork the repository and submit a pull request.

## 👤 Author
* Created by [RolandWisniewski](https://github.com/RolandWisniewski)

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
