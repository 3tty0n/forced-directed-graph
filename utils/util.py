# coding=utf-8

import itertools
import json
import networkx as nx
from networkx.readwrite import json_graph
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


def create_json_from_file_random(filename, size):
    """
    ファイルを読み込んでjsonを生成する。
    :param filename: ファイル名
    :param size: サイズ
    :return:
    """
    file = open('../data/' + filename + '.txt')
    lines = file.readlines()
    file.close()
    sample = random.sample(lines, size)
    G = nx.parse_edgelist(sample, nodetype=int)
    for n in G:
        G.node[n]['name'] = n
    d = json_graph.node_link_data(G)
    json.dump(d, open('../static/' + filename + '.json', 'w'))
    print('Wrote node-link JSON data to static/' + filename + '.json')


create_json_from_file_random('twitter_combined', 100)
create_json_from_file_random('BA10000', 5000)