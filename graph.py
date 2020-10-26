# (C) 2020 Zachary Petroff, Indiana University Bloomington

import matplotlib.pyplot as plt
import numpy as np

def plot_movements(seperations, connection_changes, mins, ram_mean, lam_mean, rlm_mean, llm_mean, connected_limb_index=0):
    colors = []
    labels = []
    for limb in range(4):
        if connected_limb_index == limb:
            colors.append("red")
            labels.append("Connected Limb Movements")
        else:
            colors.append("black")
            labels.append("Disconnected Limb Movements")
    for seperation in range(len(seperations)):
        if seperation != 0:
            plt.plot(mins[seperations[seperation-1]:seperations[seperation]], ram_mean[seperations[seperation-1]:seperations[seperation]], colors[0], label=labels[0])
            plt.plot(mins[seperations[seperation-1]:seperations[seperation]], lam_mean[seperations[seperation-1]:seperations[seperation]], colors[1], label=labels[1])
            plt.plot(mins[seperations[seperation-1]:seperations[seperation]], rlm_mean[seperations[seperation-1]:seperations[seperation]], colors[2])
            plt.plot(mins[seperations[seperation-1]:seperations[seperation]], llm_mean[seperations[seperation-1]:seperations[seperation]], colors[3])
            plt.legend()

            for loc in list(connection_changes)+[len(mins)]:
                plt.axvline(loc, color='black', linestyle='dashed')
            plt.xlim(seperations[seperation-1], seperations[seperation])
            plt.ylabel("Movements")
            plt.xlabel("Minutes")
            plt.ylim(0,None)
            plt.title("Session {}".format(seperation) + "\n" + "Baseline" + " "*17 + "Connect" + " "*17 + "Disconnect")
            plt.show()

def plot_minute(minute, cms, mms, timestep):
    steps_per_min = 1 / timestep
    
    cms_slice = cms[int(minute * steps_per_min):int((minute * steps_per_min) + steps_per_min)]
    mms_slice = mms[int(minute * steps_per_min):int((minute * steps_per_min) + steps_per_min)]
    
    steps_per_min = np.arange(0, steps_per_min)
    
    plt.plot(steps_per_min, cms_slice, "red", label="Connected Limb Movements")
    plt.plot(steps_per_min, mms_slice, "black", label="Mobile Movements")
    plt.legend(bbox_to_anchor=(1.6, 1))
    plt.title("Minute {}".format(str(minute)))
    plt.show()
    
def plot_expectation(mins, reward, cost, rae_mean, lae_mean, rle_mean, lle_mean, connected_limb_index=0):
    colors = []
    labels = []
    for limb in range(4):
        if connected_limb_index == limb:
            colors.append("red")
            labels.append("Connected Limb Movements")
        else:
            colors.append("black")
            labels.append("Disconnected Limb Movements")
    plt.plot(mins, rae_mean, colors[0], label=labels[0])
    plt.plot(mins, lae_mean, colors[1], label=labels[1])
    plt.plot(mins, rle_mean, colors[2])
    plt.plot(mins, lle_mean, colors[3])
    plt.xlabel("Minutes")
    plt.ylabel("Expectation")
    plt.title("Expectation Over Time")
    plt.plot([0, len(mins)], [reward, reward], "black", label="Reward", linestyle="dashed")
    plt.plot([0, len(mins)], [cost, cost], "black", label="Cost", linestyle="dotted")

    plt.legend()
    plt.show()
    
def plot_rates(mins, norm_rates, moving_rates):
    plt.plot(mins, norm_rates, label="Rates Not Moving", color="red")
    plt.plot(mins, moving_rates, label="Rates Moving", color="black")
    plt.legend()
    plt.xlabel("Minutes")
    plt.ylabel("Rates")
    plt.title("Connected Limb Rates")
    plt.show()