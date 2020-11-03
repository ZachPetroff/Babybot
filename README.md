
# Mobile-Paradigm and Extinction Bursts
  
   The Mobile-Paradigm was originally introduced by Rovee & Rovee in 1969, as a way to measure the effects of conjugate reinforcement on infants.
 In the study, the limb movements of 10-week-old infants were recorded during three different periods: the baseline period, the connected period, and
 the disconnected period. During the baseline period, infants were sat in a crib, below a still mobile. The connected period then immediately followed,
 in which one limb was connected to the mobile, allowing the infant to move the mobile and recieve a visual reward if they moved the connected limb. 
 Lastly, the disconnected period, which was identical to the baseline period, immediately followed. For the most part, limb movements
 were as predicted. During the connected period, the movements of the connected limb quickly ascended while the disconnected limb movements stayed near the 
 baseline. However, unexpectedly, during the disconnected period, the limb movements of the previously connected limb continued to rise, even faster than 
 the increase observed during the connected period. 

   This unexpected phenomena is now known as an "extinction burst", and occurs whenever a vending machine eats your dollar without returning a snack or 
 your web page fails to open after the first click. Quickly, torrents of button-presses and mouse-clicks follow, in the absence of the contingent reward.
 The code within this repository attempts to explore how extinction bursts arise: the cognitive mechanisms, the physical systems, and the interplay 
 between the two.
 
 # [Violation of Expectancy and Frustration](https://github.com/ZachPetroff/Babybot/blob/master/examples/Expectation.ipynb)
  In many of the Mobile-Paradigm studies that followed the original, researchers reported frustration on the faces of the infants during
disconnect phase. This seems to be an appropriate response, if one expects a reward following a certain action and that reward is not given,
the most obvious reaction is that of frustration. Thus, one way we modeled extinction bursts is by modeling frustration in terms of 
violation of expectancy. Once the limb is connected and the infant begins to acquire a reward, they also begin to acquire an expectation 
for that reward. While the reward is still given, the expectation works against the reward, due to boredom or disinterest. However, when the 
reward is no longer given, feelings of frustration begin to bubble-up. We all have things in our life that we take forgranted, 
small rewards, that in their absence, fill us with a greater want than when they were attainable. This was the intuition behind this model
of the "babybot".
 
 # Mobile Dynamics
  The intuition behind this approach is that there are certain times during the connected phase when there is
  no additional reward for moving the connected limb; rather, there is a cost. The contingent reward for the connected
  limb is given once the mobile begins to move. However, the mobile continues to swing some time after the connected limb 
  moves. During this phase, moving the connected arm would provide no additional reward. If we assume that the infant, 
  in a sense, wants to be as "efficient" as possible, then movement during this window of time should be disencouraged.
