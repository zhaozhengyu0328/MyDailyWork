import matplotlib.pyplot as plt
X_Robust04 =[0.25,
0.3,
0.35,
0.4,
0.45,
0.5,
0.55,
0.6,
0.65,
0.7,
0.75,
0.8,
0.85,
0.9,
0.95,
]
Y_Robust04_Map = [0.186259,
0.189597,
0.192434,
0.195058,
0.19684,
0.199019,
0.200069,
0.200158,
0.199449,
0.198237,
0.195825,
0.193144,
0.190589,
0.187048,
0.183535,

]


plt.figure()

# Map的分布
plt.plot(X_Robust04, Y_Robust04_Map, label="Map", color="#95C4BF", marker='o', linestyle="-")


# plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))   # 将横坐标的值全部显示出来
X_labels = ['0.8','0.85','0.87','0.9','0.93','0.94','0.95','0.96','0.98']
# plt.xticks(X_Trec19,X_labels,rotation=0)
plt.legend()
plt.title("Map(Robust04)")
plt.xlabel("α")
# plt.ylabel("Y")
plt.show()
