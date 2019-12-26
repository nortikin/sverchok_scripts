"""
in verts_list v
in edge_list  s .=[[]]   n=0
in pol_list   s .=[[]]   n=0
out verts_out v
out edges_out s
out pols_out s
"""
from sverchok.data_structure import match_long_repeat as mlr
import numpy as np

def remove_doubles_numpy(vertices, edgs, pols):
    """Removes doubled verts and updates edges and pols indexes"""
    np_verts = np.array(vertices)
    v_out, idx = np.unique(np_verts, axis=0, return_inverse=True)

    e_out = []
    for e in edgs:
        e_out.append([idx[e[0]], idx[e[1]]])

    p_out = []
    for p in pols:
        p_new = []
        for c in p:
            p_new.append(idx[c])
        p_out.append(p_new)

    return v_out.tolist(), e_out, p_out

verts_out, edges_out, pols_out = [], [], []

for params in zip(*mlr([verts_list, edge_list, pol_list])):
    result = remove_doubles_numpy(*params)
    verts_out.append(result[0])
    edges_out.append(result[1])
    pols_out.append(result[2])
