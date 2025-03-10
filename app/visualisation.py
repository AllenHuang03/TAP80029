import matplotlib.pyplot as plt
import numpy as np

def plot_light_curve():
    time = np.linspace(0, 10, 100)
    flux = np.sin(time) + np.random.normal(0, 0.1, len(time))

    plt.figure(figsize=(8, 4))
    plt.plot(time, flux, marker="o", linestyle="-", color="b", label="Pulsar Light Curve")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Flux Intensity")
    plt.title("Pulsar Light Curve")
    plt.legend()
    plt.grid()
    plt.savefig("frontend/static/light_curve.png")  # Save image for UI
