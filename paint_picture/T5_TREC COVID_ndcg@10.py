import matplotlib.pyplot as plt
X_Trec19 = [0,
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
1,

]
Y_Trec19_P20 = [0.370163,
0.394985,
0.427395,
0.457754,
0.48152,
0.506279,
0.532947,
0.542976,
0.559581,
0.580056,
0.588123,
0.584809,
0.605908,
0.612601,
0.626841,
0.631958,
0.635945,
0.640127,
0.636816,
0.634705,
0.613111,


]

plt.figure()

# P_20的分布
plt.plot(X_Trec19, Y_Trec19_P20,label="NDCG@10",  color="#E7DAD2", marker='o', linestyle="-",linewidth = 2)

# plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))   # 将横坐标的值全部显示出来
# X_labels = ['0.8','0.85','0.87','0.9','0.93','0.94','0.95','0.96','0.98']
# plt.xticks(X_Trec19,X_labels,rotation=0)
plt.legend()
plt.title("NDCG@10(Corvid-19)",fontsize='xx-large',fontweight='heavy')

plt.xticks(fontsize='xx-large',fontweight='heavy')
plt.yticks(fontsize='xx-large',fontweight='heavy')
plt.tick_params(labelsize='xx-large')
plt.xlabel("α",fontsize='xx-large')
# plt.ylabel("Y")
plt.show()
