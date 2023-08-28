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
Y_Trec19_P20 = [0.375,
0.404,
0.431,
0.458,
0.481,
0.498,
0.525,
0.544,
0.565,
0.583,
0.599,
0.607,
0.62,
0.625,
0.63,
0.638,
0.647,
0.631,
0.634,
0.634,
0.615,



]

plt.figure()

# P_20的分布
plt.plot(X_Trec19, Y_Trec19_P20,label="P@20",  color="#269120", marker='o', linestyle="-",linewidth = 2)

# plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))   # 将横坐标的值全部显示出来
# X_labels = ['0.8','0.85','0.87','0.9','0.93','0.94','0.95','0.96','0.98']
# plt.xticks(X_Trec19,X_labels,rotation=0)
plt.legend()
plt.title("P@20(Corvid-19)",fontsize='xx-large',fontweight='heavy')
plt.xlabel("α",fontsize='xx-large')
plt.xticks(fontsize='xx-large',fontweight='heavy')
plt.yticks(fontsize='xx-large',fontweight='heavy')
plt.tick_params(labelsize='xx-large') 
# plt.ylabel("Y")
plt.show()
