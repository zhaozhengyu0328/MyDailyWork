import matplotlib.pyplot as plt
X_Trec19 = [0.8,
0.83,
0.84,
0.85,
0.86,
0.87,
0.9,
0.93,
0.94,
0.95,
0.96,
0.98,
]
Y_Trec19_Map = [0.455608,
0.458768,
0.45976,
0.460725,
0.461514,
0.461705,
0.462915,
0.463374,
0.463094,
0.462528,
0.4622,
0.46024,
]


plt.figure()

# Map的分布
plt.plot(X_Trec19, Y_Trec19_Map, label="Map", color="#F8681A", marker='o', linestyle="-")


# plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))   # 将横坐标的值全部显示出来
# X_labels = ['0.8','0.85','0.87','0.9','0.93','0.94','0.95','0.96','0.98']
# plt.xticks(X_Trec19,X_labels,rotation=0)
plt.legend()
plt.title("Map(TREC2019)")
plt.xlabel("α")
# plt.ylabel("Y")
plt.show()
