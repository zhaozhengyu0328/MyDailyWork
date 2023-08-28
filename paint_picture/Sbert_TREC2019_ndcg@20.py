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
Y_Cor19_Map = [0.330246,
0.359676,
0.378694,
0.409033,
0.438725,
0.467476,
0.492017,
0.520791,
0.544697,
0.565824,
0.581798,
0.597689,
0.611968,
0.62693,
0.640387,
0.645529,
0.656239,
0.665805,
0.667603,
0.667359,
0.659511,

]


plt.figure()

# Map的分布
plt.plot(X_cor19, Y_Cor19_Map, label="NDCG@20", color="#95C4BF", marker='o', linestyle="-",linewidth= 2)


# plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))   # 将横坐标的值全部显示出来
# X_labels = ['0.8','0.85','0.87','0.9','0.93','0.94','0.95','0.96','0.98']
# plt.xticks(X_Trec19,X_labels,rotation=0)
plt.legend()
plt.title("NDCG@20(TREC2019)",fontsize='xx-large',fontweight='heavy')
plt.xlabel("α",fontsize='xx-large')

plt.xticks(fontsize='xx-large',fontweight='heavy')
plt.yticks(fontsize='xx-large',fontweight='heavy')
plt.tick_params(labelsize='xx-large')
# plt.ylabel("Y")
plt.show()
