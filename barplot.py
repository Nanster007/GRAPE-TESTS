import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json

datasets = ["naval", "power", "energy", "kin8nm", "yacht", "concrete", "housing"]
#datasets = ["energy", "concrete", "housing"]
algos = ["spectral_v1", "mean_v1", "knn_v1", "mice_v1", "svd_v1", "gnn_mdi_v1"]
#algos = ["spectral_v1", "mean_v1", "knn_v1", "mice_v1", "svd_v1"]

with open("data_dict.json", "r") as file:
    data_dict = json.load(file) 

iterator = 0
rmse_array = []
for i in algos:
    rmse_array.append([])
    for j in datasets:
        rmse_array[iterator].append(data_dict[j][i]["rmse"])
    iterator += 1

x = np.arange(len(datasets))  # the label locations
width = 0.10  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - 3*width, rmse_array[0], width, label="Spectral")
rects2 = ax.bar(x - 2*width, rmse_array[1], width, label="Mean")
rects3 = ax.bar(x - width, rmse_array[2], width, label="KNN")
rects4 = ax.bar(x, rmse_array[3], width, label="MICE")
rects5 = ax.bar(x + width, rmse_array[4], width, label="SVD")
rects6 = ax.bar(x + 2*width, rmse_array[5], width, label="GRAPE")


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('test_rmse')
ax.set_xlabel('Datasets')
ax.set_title('Feature Inputation at missing rate 0.3')
ax.set_xticks(x)
ax.set_xticklabels(datasets)
ax.legend()
fig.tight_layout()

plt.savefig('barplot.png')
