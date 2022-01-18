"""
    Greedy Algorithm of IM
    @author 梦否[baiyazi]
    2022-1-18 12:01:17
"""

import networkx as nx
from ic import IC


def Greedy(nx_G, numberOfSeed, p=0.5, iter=5):
    """
    Influence Maximization 贪心算法
    :param nx_G: networkx格式的图
    :param numberOfSeed: 待选定的种子节点数量
    :param p: 无权重独立级联模型传播概率
    :param iter: 每轮迭代次数
    :return: 种子节点集合
    """
    Seed = []
    nodes = list(nx_G.nodes)
    for i in range(numberOfSeed):
        best_Inf, best_Inf_node = 0, 0
        for v in set(nodes) - set(Seed):
            # 计算边际影响增益
            temp = IC.unWeightedIC(nx_G, Seed + [v], p=p, iter=iter)
            if temp > best_Inf:
                best_Inf, best_Inf_node = temp, v
        Seed.append(best_Inf_node)
    return Seed


if __name__ == '__main__':
    s = Greedy(nx.karate_club_graph(), 8)
    print(s)