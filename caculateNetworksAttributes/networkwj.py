# achieve some function of undirected graph

#%%
import copy
import sys
MAX_INT = sys.maxsize

class Graph:
    """only support undirected and unweighted graph, and can't change info of graph
        仅支持 无向无权图；存储方式为邻接矩阵存储；读入数据不能更改。
    """
    def __init__(self, type='undirected'):
        self.type = type # type of graph
        self.number_of_nodes = 0 # 节点数量
        self.number_of_edges = 0 # 边的数量
        self.adjacency_matrix = [] # 邻接矩阵存储
        self.adjacency_table = [] # 邻接表存储
        self.nodes = set([]) # 存储节点
        self.edges = [] # 存储边
        self.degree = [] # 每个节点的度
        self.average_degree = float("-inf") # 代表最小值
        self.density = float("-inf")

        self.clustering_of_nodes = [] # 节点聚类系数
        self.average_clustering_of_network = float("-inf") # 网络的聚类系数
        self.betweenness_of_nodes = {} # 节点的介数
        self.degree_histogram = [] # 度分布
        self.max_degree = -1 # 节点最大度
        self.average_shortest_path_length = float("-inf")
        self.all_shortest_path = {} # 网路中全部节点的最短路径
        self.shortest_path_amount_through_node = {} # 存储经过节点i的最短路径条数


    def read_Data(self, path):
        "read node pair from txt and store Adjacency matrix"
        # create a  2-d list as a Adjacency matrix
        
        # read data as a str list
        with open(path, 'r') as f:
            for nodePair in f.readlines():
                nodePair = nodePair.strip() # delete '\n' 
                node_info = nodePair.split(' ') # split string by space and return list
                
                i = int(node_info[0]);j = int(node_info[1])
                self.nodes.add(i);self.nodes.add(j) # add node in set()   
                self.edges.append((i, j)) # p--顺序不与输入相同，

        # 存储在邻接矩阵
        self.adjacency_matrix = [ [MAX_INT for j in range(self.get_number_of_nodes())] for i in range(self.get_number_of_nodes())]
        for node_pair in self.edges:
            self.adjacency_matrix[node_pair[0]][node_pair[1]] = 1 
            self.adjacency_matrix[node_pair[1]][node_pair[0]] = 1

        # 存储在邻接表
        self.adjacency_table = [[] for i in range(self.get_number_of_nodes())] # 二维列表
        for tp in self.edges: # 添加边
            self.adjacency_table[tp[0]].append(tp[1])
            self.adjacency_table[tp[1]].append(tp[0])

    def get_number_of_nodes(self):
        if self.number_of_nodes == 0:
            self.number_of_nodes = len(self.nodes) # nodes set集合的个数就是节点数量   

        return self.number_of_nodes

    def get_number_of_edges(self):
        "return total number of edges"
        if self.number_of_edges == 0: # 如果没计算过
            self.number_of_edges = len(self.edges) # edges set集合的个数就是节点数量   

        return self.number_of_edges

    # node's degree
    def get_degree(self):
        "get node degree and return list of degree"
        if len(self.degree) == 0:
            for i in range(self.get_number_of_nodes()):
                sum = self.get_number_of_nodes() - self.adjacency_matrix[i].count(MAX_INT)
                if self.max_degree < sum:
                    self.max_degree = sum   
                self.degree.append((i, sum)) # 元组格式加入
              
        return self.degree


    # average degree 平均度----------------------
    def get_average_degree(self):
        if self.average_degree == float("-inf"): # 如果没计算就计算一下，否则返回
            self.get_degree() # 调用一下 防止没计算
            self.average_degree = 0
            
            sum = 0
            for d in self.degree: # 节点度的和
                sum += d
            self.average_degree = sum/self.get_number_of_nodes() # 平均度公式

        return self.average_degree


    # denisty 密度
    def get_density(self):
        if self.density == float("-inf"): # 如果没计算就计算，否则返回
            # 密度公式
            self.density = 2 * self.get_number_of_edges() / self.get_number_of_nodes() / (self.get_number_of_nodes() - 1)  

        return self.density
    
    # clustering coefficient(聚类系数) of each node -----------------------------------------------bug 结果全为2.0  
    def get_clustering(self):
        if len(self.clustering_of_nodes) == 0: # 元素个数为0代表没计算过，需要计算
            for i in range(len(self.adjacency_table)): # 取出邻接点
                if len(self.adjacency_table[i]) <= 1: # 0个或者1个邻接点
                    self.clustering_of_nodes.append((i, 0))
                else:
                    neighbor_edges_sum = 0
                    for j in range(len(self.adjacency_table[i])): # 取出邻接点的 一个节点 i
                        remaining_neighbor_of_node = self.adjacency_table[i][0:j] + self.adjacency_table[i][j + 1:] # 除了节点i的邻接点
                        temp1 = set(self.adjacency_table[self.adjacency_table[i][j]])
                        temp2 = set(remaining_neighbor_of_node) # 节点 i 与 剩余节点的交集即i与它邻接点的边书 多算了节点
                        temp = temp1 & temp2
                        neighbor_edges_sum += len(temp)
                    if neighbor_edges_sum == 0:
                        self.clustering_of_nodes.append((i, 0))
                    else:
                        nnlen = len(self.adjacency_table[i]) # 节点的邻居个数
                        self.clustering_of_nodes.append((i, neighbor_edges_sum / nnlen / (nnlen - 1)))
        return self.clustering_of_nodes
    
    # clustering coefficient of network   网络的聚类系数
    def get_average_clustering(self):
        if self.average_clustering_of_network == float("-inf"):
            cn_sum = 0
            for cn in self.get_clustering(): #统计节点的聚类系数
                cn_sum += cn[1]
            self.average_clustering_of_network = cn_sum / self.get_number_of_nodes() # 网络的聚类系数公式
        
        return self.average_clustering_of_network
    
    # degree histogram 节点度分布 即节点的度值出现的次数
    def get_degree_histogram(self):
        if len(self.degree_histogram) == 0:
            self.get_degree() # 得到节点的度，以及最大度
            self.degree_histogram = [0 for i in range(self.max_degree + 1)]
            for i, degree in self.get_degree(): # 遍历节点的度值
                self.degree_histogram[degree] += 1                
        return self.degree_histogram
    

    # average path length 平均最短路径长度--------------------------------
    def get_average_shortest_path_length(self):
        if self.average_shortest_path_length == float("-inf"):
            # 求节点路径长度
            path  = self.get_all_shortest_path()
            index = range(self.get_number_of_nodes())
            sum = 0
            for i in index:
                for j in index[i + 1:]:
                    sum += len(path[j][i]) - 1
            self.average_shortest_path_length = 2 * sum / self.get_number_of_nodes() / (self.get_number_of_nodes() - 1)
        return self.average_shortest_path_length

    
    # 返回两个节点之间最短路径序列
    def get_shortest_path(self,source = -1, target = -1): # 单源最短路径
        if source > -1 and target > -1:
            path = self.dijkstra(source=source, target=target)
        return path[target]

    # 返回两个节点之间最短路径长度
    def get_shortest_path_length(self, source = -1, target = -1):
        if source > -1 and target > -1:
            path = self.get_shortest_path(source = source,target = target) # 求最短路径
            return len(path) - 1
    # 所有节点的最短路径序列
    def get_all_shortest_path(self):
        # 求节点ｉ到　节点 i + 1 ---> n 的最短路径长度
        if len(self.all_shortest_path) == 0:
            for i in self.nodes:
                for j in self.nodes:
                    self.all_shortest_path[i] = self.dijkstra(i, j)
        return self.all_shortest_path

    # 节点介数验证
    # 问题： 
    # 1.多个最短路径如何存储->改造dijkstra,存储多个最短路径
    # 2.经过节点i的最短路径数量如何计算->节点i在全部路径序列中出现的次数
    # 3.归一化->公式即可
    # 4.
    def get_betweenness_centrality(self): 
        if len(self.betweenness_of_nodes) == 0:
            self.betweenness_centrality = 0
            self.get_all_shortest_path()

            # 初始化 self.shortest_path_amount_through_node
            for i in self.nodes:
                self.shortest_path_amount_through_node[i] = 0
                self.betweenness_of_nodes[i] = 0
            # 计算每个节点的所经最短路径数量，但是数量多算了一倍 从i 到 j 和从 j 到 i是一样的路径，最后要除以2
            for s in self.all_shortest_path:
                for t in self.all_shortest_path[s]:
                    sti = {} # 临时存储 当前s和t 之间的的n条最短路径中 i 出现的次数
                    st_amount = len(self.all_shortest_path[s][t]) # 得到 从 s 到 t的最短路径条数
                    for l in self.all_shortest_path[s][t]:
                        if s <= t: # 起点 编号 小于 终点编号，否则会重复计算
                            for i in l[1:len(l) - 1]: # 去除起点和终点
                                # self.shortest_path_amount_through_node[i] += 1
                                if i not in sti:
                                    sti[i] = 1
                                else:
                                    sti[i] += 1
                    for key in sti:    
                        self.betweenness_of_nodes[key] += sti[key] / st_amount  
                    
            

            # 归一化
            for i in self.nodes:
                self.betweenness_of_nodes[i] /= (self.get_number_of_nodes() - 1) * (self.get_number_of_nodes() - 2)* 1/2
        return self.betweenness_of_nodes
        
        #return self.shortest_path_amount_through_node



    # dijkstra        
    def dijkstra(self, source=-1, target=-1):
        # 存储从source 到 target的多条最短路径

        # 初始化path
        path = {}
        for i in range(self.get_number_of_nodes()):
            path[i] = [[source]]

        dis = [MAX_INT for i in self.nodes] # 源节点与各节点的最短路径长度，先置为最大值
        dis[source] = 0 # 存储source节点到其他节点的距离，source到source距离为0
        v = [False for i in self.nodes] # 最短路径已经被确定的节点置为True

        for i in self.nodes: # 循环n次
            # 从未确定最短路径的点中,寻找距离最小的点，用ｔ存储
            t = -1 
            for j in self.nodes:
                if not v[j] and (t == -1 or dis[j] < dis[t]):
                    t = j
            #　用ｔ更新source节点到其它节点的距离
            for j in self.nodes:
                if dis[j] >= dis[t] + self.adjacency_matrix[t][j]:
                    tempPath = copy.deepcopy(path[t]) # tempPath是一个二维列表
                    for l in tempPath: # 为每个序列添加当前节点
                        l.append(j)

                    if dis[j] > dis[t] + self.adjacency_matrix[t][j]: # 原来的最短路径序列不合格了
                        path[j] = tempPath
                    else: # 最短路径相等的时候，原来的最短路径也合格，只需要把当前的最短路径添加进去
                        for l in tempPath:
                            path[j].append(l)

                dis[j] = min(dis[j], dis[t] + self.adjacency_matrix[t][j]) # 更新最短路径长度                
            # 标记ｔ节点为确定的最短路径点
            v[t] = True
        return path
# %%
