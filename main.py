import matplotlib.patches as mpatches
import numpy as np
import matplotlib.pyplot as plt
math_scores = np.array([[3, 5, 6], [8, 9, 7]])

print(math_scores[1][1])
# age = np.array([18, 22, 25, 29, 32, 35, 40, 44, 50])
# experience = np.array([1, 2, 4, 6, 8, 10, 12, 15, 20])
age = [18, 22, 25, 29, 32, 35, 40, 44, 50]
experience = [1, 2, 4, 6, 8, 10, 12, 15, 20]

plott = np.array([]).reshape(0, 2)
for items in range(len(age)):
    item = [age[items], experience[items]]
    plott = np.append(plott, [item], axis=0)

print(plott)

plt.style.use('seaborn-v0_8-whitegrid')
fig, graph = plt.subplots()
graph.scatter(plott[:, 0], plott[:, 1])

graph.set_title("Age vs Work Experience", fontsize=24)
graph.set_xlabel("Age", fontsize=16)
graph.set_ylabel("Experience", fontsize=16)

line_up, = plt.plot([1,2,3], label='Line 2')
line_down, = plt.plot([3,2,1], label='Line 1')
plt.legend(handles=[line_up, line_down])

plt.show()
