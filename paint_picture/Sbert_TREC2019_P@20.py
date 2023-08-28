import matplotlib.pyplot as plt
X_cor19 =[0,
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
Y_Cor19_P20 = [0.403488,
0.432558,
0.452326,
0.486047,
0.517442,
0.543023,
0.566279,
0.590698,
0.615116,
0.631395,
0.644186,
0.659302,
0.67093,
0.676744,
0.688372,
0.687209,
0.693023,
0.696512,
0.695349,
0.689535,
0.681395,
]


plt.figure()

# Map的分布
plt.plot(X_cor19, Y_Cor19_P20, label="P@20", color="#EECF9F", marker='o', linestyle="-")


# plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))   # 将横坐标的值全部显示出来
X_labels = ['0.8','0.85','0.87','0.9','0.93','0.94','0.95','0.96','0.98']
# plt.xticks(X_Trec19,X_labels,rotation=0)
plt.legend()
plt.title("P@20(TREC2019)",fontsize='xx-large',fontweight='heavy')
plt.xlabel("α",fontsize='xx-large')

plt.xticks(fontsize='xx-large',fontweight='heavy')
plt.yticks(fontsize='xx-large',fontweight='heavy')
plt.tick_params(labelsize='xx-large')
# plt.ylabel("Y")
plt.show()
