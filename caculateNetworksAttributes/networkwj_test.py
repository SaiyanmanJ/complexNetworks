# calculate some networks attributes such as Degree(度)，Modularity(模块度).....

#%%
import networkwj as nj
import networkx as nx
import matplotlib.pyplot as plt

Gx = nx.Graph()

path = "networksInfo/dolphins.txt"

with open(path, 'r') as f:
    for nodePair in f.readlines():
        nodePair = nodePair.strip() # delete '\n' 
        node_info = nodePair.split(' ') # split string by space and return list
        i = int(node_info[0]);j = int(node_info[1])
        Gx.add_edge(i, j)

Gj = nj.Graph()
# read data
Gj.read_Data("networksInfo/dolphins.txt") # return a 2-d list

# -------------------------------------------------------------上面没问题


# -------------------------------------------------------------测试正确性
eps = 1e-15  # 小数点后10位

# 对数器
def verification(Gx, Gj): # 验证函数

    '''

    # 1.节点数量验证
    print(f"节点数量验证 number_of_nodes() test: {Gx.number_of_nodes() == Gj.get_number_of_nodes()} 数量：{Gj.get_number_of_nodes()}\n")

    # 2.节点存在性验证
    gxn = list(Gx.nodes)
    gxn.sort()

    print(f"节点存在性验证 nodes test: {set(gxn) == Gj.nodes} \n")
    print(Gj.nodes)
    print()

    # 3.边数验证
    print(f"边的数量验证 number_of_edges_test: {Gx.number_of_edges() == Gj.get_number_of_edges()} 数量：{Gj.get_number_of_edges()}\n")

    # 4.边存在性验证
    edges_test = True
    # Gx的边都在Gj里
    
    for edge in Gx.edges:
        if edge not in Gj.edges and (edge[1], edge[0]) not in Gj.edges:
            edges_test = False
            break
    # Gj的边都在Gx里

    for edge in Gj.edges:
        if edge not in Gx.edges and (edge[1], edge[0]) not in Gx.edges:
            edges_test = False
            break

    print(f"边的存在性验证 edges test：{edges_test}\n")
    # print(gxe)
    print(Gj.edges)
    print()

    # 5.1节点的度验证
    gxd = list(Gx.degree)
    gxd.sort(key = lambda a: a[0])
    print(f"节点的度验证 degree test :{gxd == Gj.get_degree()}\n")
    print(Gj.get_degree())
    print()

    # 5.2 网络的度分布验证
    print(f"网络的度分布验证　degree histogram test:{nx.degree_histogram(Gx) == Gj.get_degree_histogram()}")
    # print(nx.degree_histogram(Gx))
    print(Gj.get_degree_histogram())

    # 6.网络密度验证
    print(f"网络密度验证 network density: {abs(nx.density(Gx) - Gj.get_density()) < eps}")
    # print(nx.density(Gx))
    print(Gj.get_density())
    print()

    # 7.1 节点聚类系数验证
    gxc = []
    temp = nx.clustering(Gx) # 返回字典
    for key in sorted(temp):# 字典的key排序之后，以元组形式插入list
        gxc.append((key, temp[key]))

    nodes_clustering_test = True
    for i in range(len(gxc)):
        if abs(gxc[i][1] - Gj.get_clustering()[i][1]) > eps: # 误差超过eps则报错
            # print(f"{gxc[i]}--{Gj.get_clustering()[i]}")
            nodes_clustering_test = False
            break

    print(f"节点聚类系数验证 nodes clustering test： {nodes_clustering_test}\n")
    #print(gxc)
    #print()
    print(Gj.get_clustering())
    print()

    # 7.2 网络聚类系数验证
    print(f"网路聚类系数验证 networks clustering test: {abs(nx.average_clustering(Gx) - Gj.get_average_clustering()) < eps}")
    # print(nx.average_clustering(Gx))
    print(Gj.get_average_clustering())

    # 8.1 平均最短路径长度验证
    nxavgPathLength = nx.average_shortest_path_length(Gx)
    print(f"平均最短路径长度验证 average_shortest_path_length() test:{abs(nxavgPathLength - Gj.get_average_shortest_path_length()) < eps}")
    print(Gj.get_average_shortest_path_length())

    # 8.2 两点之间最短路径序列
    
    nxpath = nx.shortest_path(Gx, source = 4, target = 5)
    njpath = Gj.get_shortest_path(source = 4, target = 5)
    flag = True
    flag = nxpath in njpath
    print(f"最短路径验证 shortest_path() test: {flag}")
    print(njpath)
    # print(nxpath)
    print()

    # 8.3 两点之间最短路径长度    
    nxPathLength = nx.shortest_path_length(Gx, source = 4, target = 5)
    njPathLength = Gj.get_shortest_path_length(source = 4, target = 5)

    print(f"最短路径长度验证 shortest_path_length() 4 和　5　test: {nxPathLength == njPathLength}")
    print(njPathLength)
   
    
    # 8.4 网络中所有节点之间的最短路径-----结果目测正确，嵌套太多先不写程序验证

    print(f"网络所有节点对之间的最短路径验证 shortest_path(G) test: {1}")
    with open("nx_all_shortest_path.txt", 'w') as f:
        f.write(str(nx.shortest_path(Gx)))  
    with open("nj_all_shortest_path.txt", 'w') as f:    
        f.write(str(Gj.get_all_shortest_path()))
    '''

    # 9. 节点介数验证 

    # print(nx.betweenness_centrality(Gx))
    print(Gj.get_betweenness_centrality())
    # 
    
# %%
verification(Gx, Gj)
# %%
