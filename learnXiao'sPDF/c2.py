#2.1 


# 1.基本绘图流程

#%%
# 导入包
import networkx as nx
import matplotlib.pyplot as plt
G = nx.generators.random_graphs.barabasi_albert_graph(20, 1) # 生成BA无标度网络
nx.draw(G) # 绘制网络G

# matplotlib 输出方式
plt.savefig("ba.png") # 将图像存为png格式的图片文件
plt.show() # 在窗口中显示绘制的图像


# 2.networkx网络样式及参数 设置
# %%
import networkx as nx
import matplotlib.pyplot as plt
G = nx.generators.random_graphs.barabasi_albert_graph(20, 1)

# 参数设置， 大部分属性看名字就知道意思了， 特：width 是边的宽度 ，该处不是重点随便看看
nx.draw(G, node_size = 300, node_color = 'r', node_shape = 's', alpha = 0.8, width = 3, edge_color = 'r', style = 'dashed', with_labels = True, font_size = 20, font_color = 'k')

# 3.节点布局
# %%
import networkx as nx
import matplotlib.pyplot as plt

G = nx.generators.random_graphs.barabasi_albert_graph(20, 1)

# circular_layout 节点在一个圆环上均匀分布
pos = nx.circular_layout(G)
nx.draw(G, pos)
plt.show()

# random_layout 节点随机分布
pos = nx.random_layout(G)
nx.draw(G, pos)
plt.show()

# shell_layout 节点在同心圆上分布
pos = nx.shell_layout(G)
nx.draw(G, pos)
plt.show()

# spring_layout
pos = nx.spring_layout(G)
nx.draw(G, pos)
plt.show()

# spectral_layout
pos = nx.spectral_layout(G)
nx.draw(G, pos)
plt.show()

# 绘图时直接指定布局
nx.draw(G, pos = nx.circular_layout(G))
plt.show()
# %%

