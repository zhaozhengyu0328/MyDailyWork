import matplotlib.pyplot as plt
X_Robust04 =[0,
0.05,
0.1,
0.15,
0.2,
0.25,
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
1
]
Y_Robust04_Map = [0.297854,
0.321512,
0.339039,
0.348808,
0.359745,
0.372475,
0.378478,
0.384538,
0.390822,
0.394828,
0.39957,
0.400413,
0.400965,
0.399019,
0.396962,
0.394509,
0.39174,
0.389747,
0.383405,
0.377458,
0.371389,


]


plt.figure()

# Map的分布
plt.plot(X_Robust04, Y_Robust04_Map, label="NDCG@20", color="#82B0D2", marker='o', linestyle="-",linewidth = 2)


# plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))   # 将横坐标的值全部显示出来
X_labels = ['0.8','0.85','0.87','0.9','0.93','0.94','0.95','0.96','0.98']
# plt.xticks(X_Trec19,X_labels,rotation=0)
plt.legend()
plt.title("NDCG@20(Robust04)",fontsize='xx-large',fontweight='heavy')
plt.xlabel("α",fontsize='xx-large')
plt.xticks(fontsize='xx-large',fontweight='heavy')
plt.yticks(fontsize='xx-large',fontweight='heavy')
plt.tick_params(labelsize='xx-large')
# plt.ylabel("Y")
plt.show()
