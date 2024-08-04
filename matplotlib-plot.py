import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Grab Data
    np_exp_data = np.loadtxt("np_exp.csv", delimiter=',', dtype=int)
    pd_exp_data = pd.read_csv("pd_exp.csv", index_col=0)
    
    # Line Plot
    plt.figure()
    plt.plot(np_exp_data[:, 0], np_exp_data[:, 1])
    plt.plot(pd_exp_data)

    # We must apply our features to our plot before showing for them to show up on our plot. 

    # Lets add a title
    plt.title("A comparison of x^2 and x^3")

    # Lets add axis labels
    plt.xlabel("x")
    plt.ylabel("f(x)")

    # Lets add a legend
    plt.legend(["x^3", "x^2"]) # Note that you must put the legend in a list format

    plt.show()
