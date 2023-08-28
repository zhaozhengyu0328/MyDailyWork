import matplotlib.pyplot as plt
X_cor19 = [0.8,
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
Y_Cor19_Map = [0.1592,
0.161357,
0.162037,
0.162701,
0.16351,
0.164282,
0.166497,
0.168068,
0.168295,
0.168216,
0.167701,
0.165952,

]


plt.figure()

# Map的分布
plt.plot(X_cor19, Y_Cor19_Map, label="Map", color="#F8681A", marker='o', linestyle="-")


# plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))   # 将横坐标的值全部显示出来
X_labels = ['0.8','0.85','0.87','0.9','0.93','0.94','0.95','0.96','0.98']
# plt.xticks(X_Trec19,X_labels,rotation=0)
plt.legend()
plt.title("Map(TREC COVID)")
plt.xlabel("α")
# plt.ylabel("Y")
plt.show()
