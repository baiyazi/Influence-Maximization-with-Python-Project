"""
    Independent Cascade
    算法过程：
    - 激活节点$v$会试图去激活他的邻居节点$w$，成功激活的概率为$p_{v, w}$；
    - $p_{v, w}$ 概率类似翻硬币，可以推断概率值大于$0$小于$1$；
    - 对每次激活的邻居对$(v, w)$，都会存储其结果并一直保存，也就是对每个节点只会尝试激活一次；
    - 直到图$G$中所有邻居对完成这个过程；
    @author 梦否[baiyazi]
    2022-1-17 20:42:19
"""
import networkx as nx
from copy import deepcopy
import random
import tqdm


def unWeightedIC(nx_G, Seed, p=0.5, iter=5):
    """
    无权重IC模型
    :param nx_G: networkx的图
    :param Seed: 激活节点或者激活节点集合
    :param p: 独立级联激活概率值
    :param iter: 迭代次数
    :return: 被激活节点平均个数
    """
    assert type(nx_G) == nx.Graph
    assert type(Seed) == list

    count = 0
    for i in range(iter):
        UsedNodes = deepcopy(Seed)
        ActivatedNodes = deepcopy(Seed)
        tempSeed = deepcopy(Seed)
        CurrentActivatedNodes = []
        while tempSeed:
            for v in tempSeed:
                for w in nx.neighbors(nx_G, v):
                    if w not in UsedNodes:
                        if random.random() < p:
                            CurrentActivatedNodes.append(w)
                        UsedNodes.append(w)
            tempSeed = CurrentActivatedNodes
            ActivatedNodes.extend(CurrentActivatedNodes)
            CurrentActivatedNodes = []
        count += len(ActivatedNodes)

    return count / iter


if __name__ == '__main__':
    print(unWeightedIC(nx.karate_club_graph(), [2]))