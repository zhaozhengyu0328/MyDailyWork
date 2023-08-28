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
Y_Trec19_P20 = [0.408,
0.428,
0.46,
0.498,
0.53,
0.556,
0.572,
0.59,
0.61,
0.628,
0.638,
0.638,
0.662,
0.67,
0.688,
0.696,
0.704,
0.71,
0.702,
0.688,
0.662,




]

plt.figure()

# P_20的分布
plt.plot(X_Trec19, Y_Trec19_P20, label="P@10",  color="#BEB8DC", marker='o', linestyle="-",linewidth = 2)


# plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))   # 将横坐标的值全部显示出来
# X_labels = ['0.8','0.85','0.87','0.9','0.93','0.94','0.95','0.96','0.98']
# plt.xticks(X_Trec19,X_labels,rotation=0)
plt.legend()
plt.title("P@10(Corvid-19)",fontsize='xx-large',fontweight='heavy')

plt.xticks(fontsize='xx-large',fontweight='heavy')
plt.yticks(fontsize='xx-large',fontweight='heavy')
plt.tick_params(labelsize='xx-large')
plt.xlabel("α",fontsize='xx-large')
# plt.ylabel("Y")
plt.show()
