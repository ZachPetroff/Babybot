import numpy as np
import main

def simulate(num_infants=100, num_sessions=1, timestep=1/120, 
             baseline_time=10, aquisition_time=30, extinction_time=20, rates=[20,20,20,20], 
             reward=.06, cost=.0075, expectation_growth=1e-4, expectation_decay=3e-4, mobile_on=False):
    
    connection = np.array([False]*baseline_time+[True]*aquisition_time+[False]*extinction_time)  # connection for each minute
    for session in range(num_sessions-1):
        connection = np.append(connection, connection[:baseline_time+aquisition_time+extinction_time])
    n_minutes = len(connection)
    
    connection_labels = []
    prev_connection = False
    counter = 0
    for c in range(len(connection)):
        if prev_connection == connection[c]:
            counter += 1
        else:
            if len(connection_labels) < 1:
                connection_labels.append(counter/2)
            else:
                connection_labels.append(counter/2 + connection_labels[-1]*2)
            counter = 0
            prev_connection = connection[c]
    
    # limb movements
    ram_mean = np.zeros((n_minutes,))
    lam_mean = np.zeros((n_minutes,))
    rlm_mean = np.zeros((n_minutes,))
    llm_mean = np.zeros((n_minutes,))
    
    # limb expectations
    rae_mean = np.zeros((n_minutes,))
    lae_mean = np.zeros((n_minutes,))
    rle_mean = np.zeros((n_minutes,))
    lle_mean = np.zeros((n_minutes,))
    
    # rates
    norm_rates = np.zeros((n_minutes,))
    moving_rates = np.zeros((n_minutes,))
    
    for infant in range(num_infants):
        babybot = main.Babybot(rates=rates,reward=reward,cost=cost,expectation_growth=expectation_growth,expectation_decay=expectation_decay, timestep=timestep, mobile_on=mobile_on)
        
        ram, lam, rlm, llm, rae, lae, rle, lle, mins, cms, mms, nr, mr = babybot.one_cycle(n_minutes, connection)
        ram_mean += ram
        lam_mean += lam
        rlm_mean += rlm
        llm_mean += llm

        rae_mean += rae
        lae_mean += lae
        rle_mean += rle
        lle_mean += lle
        
        norm_rates += nr
        moving_rates += mr

        
    ram_mean = ram_mean / num_infants
    lam_mean = lam_mean / num_infants
    rlm_mean = rlm_mean / num_infants
    llm_mean = llm_mean / num_infants

    rae_mean = rae_mean / num_infants
    lae_mean = lae_mean / num_infants
    rle_mean = rle_mean / num_infants
    lle_mean = lle_mean / num_infants
    
    norm_rates = norm_rates / num_infants
    moving_rates = moving_rates / num_infants

    connection_changes = np.where(connection[1:]^connection[:-1])[0]

    seperations = [0]

    if len(connection_changes) > 2:
        for change in range(len(connection_changes)):
            if change % 2 == 0 and change != 0:
                seperations.append(int(connection_changes[change] - ((connection_changes[change] - connection_changes[change-1])/2)))
    
    seperations.append(len(connection))
    
    return seperations, connection_changes, mins, ram_mean, lam_mean, rlm_mean, llm_mean, reward, rae_mean, lae_mean, rle_mean, lle_mean, norm_rates, moving_rates, cms, mms, timestep

simulate()