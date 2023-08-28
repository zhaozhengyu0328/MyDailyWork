import matplotlib.pyplot as plt
X_Robust04 = [
0,
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
Y_Robust04 = [0.253414,
0.276506,
0.291566,
0.3,
0.307631,
0.317871,
0.322088,
0.327309,
0.332731,
0.336345,
0.340161,
0.339357,
0.340361,
0.339157,
0.337952,
0.33494,
0.332932,
0.331526,
0.326506,
0.320281,
0.314659,


]

plt.figure()

# P_20的分布
plt.plot(X_Robust04, Y_Robust04,label="P@20",  color="#FA7F6F", marker='o', linestyle="-",linewidth = 2)

# plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))   # 将横坐标的值全部显示出来
# X_labels = ['0.8','0.85','0.87','0.9','0.93','0.94','0.95','0.96','0.98']
# plt.xticks(X_Trec19,X_labels,rotation=0)
plt.legend()
plt.title("P@20(Robust04)",fontsize='xx-large',fontweight='heavy')
plt.xlabel("α",fontsize='xx-large')

plt.xticks(fontsize='xx-large',fontweight='heavy')
plt.yticks(fontsize='xx-large',fontweight='heavy')
plt.tick_params(labelsize='xx-large')
# plt.ylabel("Y")
plt.show()
