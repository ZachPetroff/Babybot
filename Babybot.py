# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np

class Babybot:
  def __init__(self, ranges=[.33, .33, .33, .33], reward=.001, punishment=.001, expectation_growth=1e-10, expectation_decay=.025, connected=False, connected_limb="right arm"):
    self.ranges = ranges # probabilities of each limb moving
    self.reward = reward 
    self.punishment = punishment
    self.expectation = [0, 0, 0, 0]
    self.expectation_growth = expectation_growth
    self.expectation_decay = expectation_decay
    self.connected = False
    self.limbs = ['right arm', 'left arm', 'right leg', 'left leg']
    self.connected_limb = self.limbs.index(connected_limb)
    self.move_counter = [0, 0, 0, 0]

  def update_ranges(self, moves):
    # if the limb is connected, a reward is given and expectation for a reward grows
    if self.connected == True and moves[self.connected_limb] == True: # reward state
      # possible extension: logistic curve  
      for limb in range(len(self.limbs)):
        if moves[limb] == True:
          self.expectation[limb] += self.expectation_growth
          # creates the peaking effect shown in data, the movements peak around 35 and then decrease to around 30 (fatigue, boredom)
          self.ranges[limb] += self.reward - self.expectation[limb]

    elif self.connected == False: # disconnected

      # the expectation for a reward will increase movement when reward is not given (frustration)
      for limb in range(len(self.limbs)):
        if moves[limb] == True:
          self.ranges[limb] += self.expectation[limb] - self.punishment # - reward
          if self.expectation[limb] > 0:  # keeps movement from going down during base
            self.expectation[limb] -= self.expectation_decay # creates decrease in movement at the end of the disconnected state

  def move(self):
    rand_dist = np.random.uniform(0,1,4)
    moves = [] # contains which limbs should be updated 
    for limb in range(len(self.limbs)):
      if rand_dist[limb] < self.ranges[limb]:
        move = True
        moves.append(move)
      else:
        move = False
        moves.append(move)
    self.update_ranges(moves)
    return moves

  def one_cycle(self, bin_size=25, steps_per_bin=30):
    r_arm_moves = []
    l_arm_moves = []
    r_leg_moves = []
    l_leg_moves = []

    r_arm_expectations = []
    l_arm_expectations = []
    r_leg_expectations = []
    l_leg_expectations = []

    bins = []
    for bin in range(bin_size):
      self.move_counter = [0, 0, 0, 0]
      if 4 < bin < 20:
        self.connected = True
      else:
        self.connected = False
      for step in range(steps_per_bin):
        moves = self.move()
        for move in range(len(moves)):
          if moves[move] == True:
            self.move_counter[move] += 1
      bins.append(bin)
      r_arm_moves.append(self.move_counter[0])
      l_arm_moves.append(self.move_counter[1])
      r_leg_moves.append(self.move_counter[2])
      l_leg_moves.append(self.move_counter[3])

      r_arm_expectations.append(self.expectation[0])
      l_arm_expectations.append(self.expectation[1])
      r_leg_expectations.append(self.expectation[2])
      l_leg_expectations.append(self.expectation[3])

    return r_arm_moves, l_arm_moves, r_leg_moves, l_leg_moves, r_arm_expectations, l_arm_expectations, r_leg_expectations, l_leg_expectations, bins

num_infants = 100
bin_size = 27

reward = 2.5e-3 #@param 
# 2.5e-3
punishment=7e-4 #@param
# 7e-4
expectation_growth=9e-6 #@param
#9e-6
expectation_decay=2.5e-5 #@param
#2.5e-5

# limb movements
ram_mean = np.zeros((bin_size,))
lam_mean = np.zeros((bin_size,))
rlm_mean = np.zeros((bin_size,))
llm_mean = np.zeros((bin_size,))

# limb expectations
rae_mean = np.zeros((bin_size,))
lae_mean = np.zeros((bin_size,))
rle_mean = np.zeros((bin_size,))
lle_mean = np.zeros((bin_size,))

babybot = Babybot(ranges=[.25, .25, .25, .25],reward=reward,punishment=punishment,expectation_growth=expectation_growth,expectation_decay=expectation_decay)

for infant in range(num_infants):
      ram, lam, rlm, llm, rae, lae, rle, lle, bins = babybot.one_cycle(bin_size, 60)
      ram_mean += ram
      lam_mean += lam
      rlm_mean += rlm
      llm_mean += llm

      rae_mean += rae
      lae_mean += lae
      rle_mean += rle
      lle_mean += lle

      babybot = Babybot(ranges=[.25, .25, .25, .25],reward=reward,punishment=punishment,expectation_growth=expectation_growth,expectation_decay=expectation_decay)

ram_mean = ram_mean / num_infants
lam_mean = lam_mean / num_infants
rlm_mean = rlm_mean / num_infants
llm_mean = llm_mean / num_infants

rae_mean = rae_mean / num_infants
lae_mean = lae_mean / num_infants
rle_mean = rle_mean / num_infants
lle_mean = lle_mean / num_infants

max_connected = max(ram_mean[:19])
max_disconnected = max(ram_mean)

print("Maximum movements while connected: ", max_connected)
print("Maximum movements while disconnected: ", max_disconnected)

# plot max values
plt.plot([0, bin_size], [max_connected, max_connected], "black", linestyle=(0,(1,10)))
plt.plot([0, bin_size], [max_disconnected, max_disconnected], "black", linestyle=(0,(1,10)))

# plot list of mean movements of each limb
plt.plot(bins, ram_mean, 'red')
plt.plot(bins, lam_mean)
plt.plot(bins, rlm_mean)
plt.plot(bins, llm_mean)

# visualize base, connected, and disconnected
plt.plot([5,5], [0,60], 'black', linestyle='dashed')
plt.plot([19,19], [0,60], 'black', linestyle='dashed')
plt.annotate("Base", (1, 60))
plt.annotate("Connected", (9.5, 60))
plt.annotate("Disconnected", (20.5, 60))

plt.show()

# plot expectations
plt.plot(bins, rae_mean, 'red')
plt.plot(bins, lae_mean)
plt.plot(bins, rle_mean)
plt.plot(bins, lle_mean)