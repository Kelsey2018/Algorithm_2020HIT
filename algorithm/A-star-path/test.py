def trans(list):
    translist = []
    for item in list:

        translist.append((item[0]-1,item[1]-1))
    return translist

list = [(35,2),(34,3),(33,4),(34,5),(34,6),(35,6),(34,7),(35,7),(34,8),(35,8),(36,8),(33,9),(34,9),(35,9),(36,9),
        (33,10),(34,10),(35,10),(33,11),(34,11),(36,11),(37,11),(33,12),(35,12),(36,12),(34,13),(35,13),
        (33,14),(34,14),(35,14),(33,15),(34,15),(35,15),(32,16),(33,16),(34,16),
        (32,17),(33,17),(34,17),(31,18),(32,18),(33,18),(30,19),(31,19),(32,19),
        (29,20),(30,20),(31,20)
        ]
print(trans(list))