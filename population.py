"""
population
"""

import json
from linkedbst import LinkedBST

def parser(path):
    """
    reads json
    """
    with open(path, 'r', encoding='utf-8') as file:
        file = json.load(file)
        return file

def perc(dct:dict):
    """
    counts percentage of hr-k for specific year and town
    """
    sums = dct["акат."]+dct["жид."]+dct["вірм."]+\
        dct["лат."]+dct["гр-кат."]
    return dct["гр-кат."]/sums*100

def create_dict(all_info:list):
    """
    creates dictionary of year and percentage for every town
    """
    res = {"КутиСтарі":{}, "Брустури":{}, "Кути":{}}
    for i in all_info:
        res[i["населений пункт"]][perc(i)]=i["рік"]
    return res

def build_tree(dic_p_y):
    """
    builds search tree for every town
    """
    tree = LinkedBST()
    for i in dic_p_y:
        tree.add((i, dic_p_y[i]))
    tree.rebalance()
    return tree

def population_trees():
    """
    builds all trees
    """
    file = parser('./Kosiv_state.json')
    file=file["Косівщина"]
    file = create_dict(file)
    for i in file:
        done = build_tree(file[i])
        file[i] = done
    return file

def find(trees, start_perc):
    """
    prints the results
    """
    assert 0<=start_perc<=100, 'Percentage wrong'
    for i in trees:
        print(f'Years in {i} with more than {start_perc}%')
        print(trees[i].find_years(start_perc))


if __name__=="__main__":
    tre = population_trees()
    per = int(input('Input the percentage (0 to 100) '))
    find(tre, per)
