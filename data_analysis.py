import os
import matplotlib.pyplot as plt
import numpy as np

weigthed_average = False # Performance weighted average (True) or only time (False)
num_trials = 16 # Select number of trials

w_t = 1 # Weight for time
w_s = 1 # Weight for score

time_with = []
time_without = []
weighted_average_with = []
weighted_average_without = []
max_velocity_with = []
max_velocity_without = []
distance_with = []
distance_without = []

for trial in range(1, num_trials + 1):
    for filename in os.listdir("trials/with_haptics/" + str(trial)):
       with open(os.path.join("trials/with_haptics/" + str(trial), filename)) as f:
           weighted_average = 0
           for lines in f:
               if 'TIME_ALIVE' in lines:
                   time = round(float(lines.split(",")[-1].strip()), 2)
                   time_with.append(time)
                   weighted_average += time * w_t
               if 'SCORE' in lines:
                   score = int(lines.split(",")[-1].strip())
                   score_per_second = score / time
                   weighted_average += score_per_second * w_s
               if 'MAX_VELOCITY' in lines:
                   velocity = round(float(lines.split(",")[-1].strip()), 2)
                   max_velocity_with.append(velocity)
               if 'DISTANCE_TRAVELLED' in lines:
                   distance = round(float(lines.split(",")[-1].strip()), 2)
                   distance_with.append(distance)
           weighted_average_with.append(weighted_average)

time_with = np.array(time_with)
weighted_average_with = np.array(weighted_average_with)

for trial in range(1, num_trials + 1):
    for filename in os.listdir("trials/without_haptics/" + str(trial)):
       with open(os.path.join("trials/without_haptics/" + str(trial), filename)) as f:
           weighted_average = 0
           for lines in f:
               if 'TIME_ALIVE' in lines:
                   time = round(float(lines.split(",")[-1].strip()), 2)
                   time_without.append(time)
                   weighted_average += time * w_t
               if 'SCORE' in lines:
                   score = int(lines.split(",")[-1].strip())
                   score_per_second = score / time
                   weighted_average += score_per_second * w_s
               if 'MAX_VELOCITY' in lines:
                   velocity = round(float(lines.split(",")[-1].strip()), 2)
                   max_velocity_without.append(velocity)
               if 'DISTANCE_TRAVELLED' in lines:
                   distance = round(float(lines.split(",")[-1].strip()), 2)
                   distance_without.append(distance)
           weighted_average_without.append(weighted_average)

time_without = np.array(time_without)
weighted_average_without = np.array(weighted_average_without)

if weigthed_average == True:
    performance_with = weighted_average_with
    performance_without = weighted_average_without
    title_str = "Performance weighted average"
else:
    performance_with = time_with
    performance_without = time_without
    title_str = "Time [s]"

# Figure 1 - Box plot performance, without haptics vs. with haptics
fig1, ax1 = plt.subplots()

ax1.boxplot([performance_without, performance_with])

ax1.set_title("Performance - without and with haptics")
ax1.set_ylabel(title_str)
ax1.set_xticks([1, 2], ['Without haptics', 'With haptics'])

# Figure 2 - Box plot performance per trial
fig2, ax2 = plt.subplots()

ax2.boxplot([performance_without[::3], performance_without[1::3], performance_without[2::3], performance_with[::3],
             performance_with[1::3], performance_with[2::3]])
ax2.set_title("Performance - without and with haptics")
ax2.set_ylabel(title_str)
ax2.set_xticks([1, 2, 3, 4, 5, 6], ['Trial 1 - without haptics', 'Trial 2 - without haptics', 'Trial 3 - without haptics',
                    'Trial 1 - with haptics', 'Trial 2 - with haptics', 'Trial 3 - with haptics'])

# Figure 3 - Learning curve, Performance
fig3, (ax3, ax4) = plt.subplots(1, 2, sharey='row')

trials = np.array([1, 2, 3])
mean_y_with = np.array([np.mean(performance_with[0::3]), np.mean(performance_with[1::3]), np.mean(performance_with[2::3])])
mean_y_without = np.array([np.mean(performance_without[0::3]), np.mean(performance_without[1::3]), np.mean(performance_without[2::3])])

for i in trials:
    ax3.scatter(np.full(num_trials, i).astype(str), performance_without[i-1::3])
ax3.plot(np.arange(0,3), mean_y_without, color='red')

for i in trials:
    ax4.scatter(np.full(num_trials, i).astype(str), performance_with[i-1::3])
ax4.plot(np.arange(0,3), mean_y_with, color='red')

ax3.set_ylabel(title_str)
ax3.spines['right'].set_visible(False)
ax3.margins(x=0.26)

ax4.spines['left'].set_visible(False)
ax4.yaxis.set_visible(False)
ax4.margins(x=0.26)

fig3.suptitle('Learning curve - Performance')
fig3.text(0.5, 0.05, 'Trial number', ha='center', va='center')

plt.subplots_adjust(wspace=0, hspace=0)

# Figure 4 - Max velocity vs. time alive
fig4, ax5 = plt.subplots()

ax5.scatter(max_velocity_with, performance_with, color='blue')
ax5.scatter(max_velocity_without, performance_without, color='green')
ax5.set_ylabel(title_str)
ax5.set_xlabel('Velocity')
ax5.set_title("Max. velocity vs. Time alive")
ax5.legend(['With haptics', 'Without haptics'])


# Figure 5 - Travelled distance vs. time alive
fig5, ax6 = plt.subplots()

ax6.set_title("Travelled distance vs. Time alive")
ax6.scatter(distance_with, performance_with, color='blue')
ax6.scatter(distance_without, performance_without, color='green')
ax6.set_ylabel(title_str)
ax6.set_xlabel('Travelled distance')
ax6.legend(['With haptics', 'Without haptics'])

plt.show()