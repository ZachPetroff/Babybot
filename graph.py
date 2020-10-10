import matplotlib.pyplot as plt
import numpy as np

def plot_movements(seperations, connection_changes, mins, ram_mean, lam_mean, rlm_mean, llm_mean):
    for seperation in range(len(seperations)):
        if seperation != 0:
            plt.plot(mins[seperations[seperation-1]:seperations[seperation]], ram_mean[seperations[seperation-1]:seperations[seperation]], 'red', label="Connected Limb Movements")
            plt.plot(mins[seperations[seperation-1]:seperations[seperation]], lam_mean[seperations[seperation-1]:seperations[seperation]], 'black', label="Disconnected Limb Movements")
            plt.plot(mins[seperations[seperation-1]:seperations[seperation]], rlm_mean[seperations[seperation-1]:seperations[seperation]], 'black')
            plt.plot(mins[seperations[seperation-1]:seperations[seperation]], llm_mean[seperations[seperation-1]:seperations[seperation]], 'black')
            plt.legend()

            for loc in list(connection_changes)+[len(mins)]:
                plt.axvline(loc, color='black', linestyle='dashed')
            plt.xlim(seperations[seperation-1], seperations[seperation])
            plt.ylim(0, None)
            plt.ylabel("Movements")
            plt.xlabel("Minutes")
            plt.title("Session {}".format(seperation) + "\n" + "Disconnected" + " "*15 + "Connected" + " "*15 + "Disconnected")
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
    
def plot_expectation(mins, reward, rae_mean, lae_mean, rle_mean, lle_mean):
    plt.plot(mins, rae_mean, 'red', label="Connected Limbs")
    plt.plot(mins, lae_mean, "black", label="Disconnected Limbs")
    plt.plot(mins, rle_mean, "black")
    plt.plot(mins, lle_mean, "black")
    plt.xlabel("Minutes")
    plt.ylabel("Expectation")
    plt.title("Expectation Over Time")
    plt.plot([0, 60], [reward, reward], "yellow", label="Reward")

    plt.legend()
    plt.show()