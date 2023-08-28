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
Y_Trec19_P20 = [0.345788,
0.373918,
0.402454,
0.428576,
0.446775,
0.465093,
0.493,
0.507032,
0.525727,
0.543593,
0.55779,
0.561575,
0.572923,
0.579724,
0.585983,
0.592134,
0.595864,
0.588286,
0.58869,
0.591954,
0.575436,

]

plt.figure()

# P_20的分布
plt.plot(X_Trec19, Y_Trec19_P20,label="NDCG@20",  color="#F8681A", marker='o', linestyle="-",linewidth = 2)

# plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))   # 将横坐标的值全部显示出来
# X_labels = ['0.8','0.85','0.87','0.9','0.93','0.94','0.95','0.96','0.98']
# plt.xticks(X_Trec19,X_labels,rotation=0)
plt.legend()
plt.title("NDCG@20(Corvid-19)",fontsize='xx-large',fontweight='heavy')
plt.xlabel("α",fontsize='xx-large')

plt.xticks(fontsize='xx-large',fontweight='heavy')
plt.yticks(fontsize='xx-large',fontweight='heavy')
plt.tick_params(labelsize='xx-large')
# plt.ylabel("Y")
plt.show()
