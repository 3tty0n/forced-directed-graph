# coding=utf-8

import itertools
import json
import networkx as nx
from networkx.readwrite import json_graph
import numpy as np
import random


def random_walk(graph, start_node=None, size=-1, metropolized=False):
    """
    RWでサンプリングしたノード列を返す

    :param graph: グラフ
    :param start_node: 先頭ノード
    :param size: ノード列のサイズ
    :param metropolized: metropolis hasting random walk フラグ
    :return: サンプリングしたノード列
    """
    if start_node is None:
        start_node = random.choice(graph.nodes())

    v = start_node
    for c in itertools.count():
        if c == size:
            return
        if metropolized:
            candidate = random.choice(graph.neighbors(v))
            v = candidate if (random.random() < float(graph.degree(v)) / graph.degree(candidate)) else v
        else:
            v = random.choice(graph.neighbors(v))

        yield v


def create_json_from_file(file, size):
    """
    ファイルを読み込んでjsonを生成する
    :param file: ファイル名
    """
    G = nx.read_edgelist('data/' + file + '.txt')
    edges = list(random_walk(graph=G, size=size, metropolized=False))
    G1 = nx.Graph()
    G1.add_path(edges)
    for n in G1:
        G1.node[n]['name'] = n
    d = json_graph.node_link_data(G1)
    json.dump(d, open('static/' + file + '.json', 'w'))
    print('Wrote node-link JSON data to static/' + file + '.json')
