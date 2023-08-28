import matplotlib.pyplot as plt
X_Cor19 = [0.8,
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
0.98
]
Y_Cor19_P20 = [0.647,
0.641,
0.636,
0.631,
0.625,
0.628,
0.634,
0.638,
0.639,
0.634,
0.635,
0.622

]

plt.figure()

# P_20的分布
plt.plot(X_Cor19, Y_Cor19_P20,label="P@20",  color="#269120", marker='o', linestyle="-")

# plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))   # 将横坐标的值全部显示出来
# X_labels = ['0.8','0.85','0.87','0.9','0.93','0.94','0.95','0.96','0.98']
# plt.xticks(X_Trec19,X_labels,rotation=0)
plt.legend()
plt.title("P@20(TREC2019)")
plt.xlabel("α")
# plt.ylabel("Y")
plt.show()
