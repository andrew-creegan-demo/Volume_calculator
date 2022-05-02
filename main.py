import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate, signal
import json
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Define settings
config_filename = "conf.json"
with open(config_filename, "r") as file:
    conf = json.load(file)

# Select data file
Tk().withdraw()
data_filename = askopenfilename(title="Select data file", initialdir=".")
Tk().destroy()

# Read data
flow = np.genfromtxt(data_filename)

# Calculate volume
flow_filtered = signal.savgol_filter(flow, conf["filter_window_length"], conf["filter_order"])
volume = integrate.cumulative_trapezoid(flow_filtered, dx=conf["dx"], initial=conf["initial"])
max_volume = volume[np.argmax(volume)]
print(f"max volume: {max_volume}")

# Plot results
plt.plot(flow, label="Flow")
plt.plot(volume, label="Volume")
plt.legend()
plt.show()
