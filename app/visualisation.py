import matplotlib.pyplot as plt

def plot_lightcurve(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df["time"], df["flux"], label="Light Curve")
    plt.xlabel("Time")
    plt.ylabel("Flux")
    plt.legend()
    plt.show()
