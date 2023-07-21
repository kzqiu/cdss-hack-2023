# Pity Me: _A Statistical Analysis of Wish Pity in Genshin Impact_
## Columbia University Data Science Society 2023 Hackathon

The Gamma distribution that we propose makes sense, as we are modeling the number of steps needed at any given pity level to reach the succeeding pity level. While this is not a concrete metric, it provides a measure that is proportional to the probability of the average number of pulls needed to acquire a legendary at a certain number of pulls subtracted from 1.

From the data, we notice that the exponential distributions of going from one to a subsequent step in the pity ladder is roughly equal. Additionally, the number of successes for pulling a legendary at a certain pity level after a certain amount of time given some frequency is distributed as a poisson distribution. This ultimately allows us to model the process of opening wishes as a Poisson process, consisting of independent Poisson processes over distinct and equal intervals of time in which the time to the first or nth success can be modeled as an exponential distribution for each time interval. This ultimately results in the gamma distribution which allows us to find the time to first success (number of pulls needed for legendary) over whichever interval we choose. Then, given any pity level, we can then find the probability of finding a legendary in any given k pulls.


By Anupam Bhakta, Kevin Qiu, Oliver Smirnov
