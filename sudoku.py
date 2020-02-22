import numpy as np
import timeit

board = np.array([
    [8, 1, 4, 0, 0, 0, 0, 0, 0],
    [0, 2, 5, 0, 0, 0, 0, 0, 0],
    [7, 3, 6, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 0]    
])

def runner(array):
    for item in array:
        if type(item) is not np.int64:
            runner(item)
        else:
            print(item)

runner(board)

def checker(table, coord_y, coord_x, search):
    if search == "column":
        #assign the coordinates' values in order to analyse a column 
        #(constant value at the y axis and all values of the x axis)
        x_a, x_b, x_c, x_d, x_e, x_f, x_g, x_h, x_i = range(9)
        y_a, y_b, y_c, y_d, y_e, y_f, y_g, y_h, y_i = coord_y
    elif search == "line":
        x_a, x_b, x_c, x_d, x_e, x_f, x_g, x_h, x_i = coord_x 
        y_a, y_b, y_c, y_d, y_e, y_f, y_g, y_h, y_i = range(9)
    else:
        x_discriminator = coord_x//3 * 3
        y_discriminator = coord_y//3 * 3
        x_a, x_b, x_c, x_d, x_e, x_f, x_g, x_h, x_i = [x_discriminator + item for item in range(3)]*3
        y_a, y_b, y_c, y_d, y_e, y_f, y_g, y_h, y_i = [y_discriminator]*3 + [y_discriminator+1]*3 + [y_discriminator+2]*3
    checker_list = np.array([
                            table[y_a][x_a], table[y_b][x_b], table[y_c][x_c], 
                            table[y_d][x_d], table[y_e][x_e], table[y_f][x_f], 
                            table[y_g][x_g], table[y_h][x_h], table[y_i][x_i]
                             ])
    can_be = [(coord_y, coord_x)]+[num for num in range(1,10) if num not in checker_list]
    print(can_be)

    checker(board, 1, 0, "block")
    #a = bool(table[x_a][y_a] > 0)
    #b = bool(table[x_b][y_b] > 0)
    #c = bool(table[x_c][y_c] > 0)
    #d = bool(table[x_d][y_d] > 0)
    #e = bool(table[x_e][y_e] > 0)
    #f = bool(table[x_f][y_f] > 0)
    #g = bool(table[x_g][y_g] > 0)
    #h = bool(table[x_h][y_h] > 0)
    #i = bool(table[x_i][y_i] > 0)
    #result = (not a and b and c and d and e and f and g and h and i) \
    #or (a and not b and c and d and e and f and g and h and i) \
    #or (a and b and not c and d and e and f and g and h and i) \
    #or (a and b and c and not d and e and f and g and h and i) \
    #or (a and b and c and d and not e and f and g and h and i) \
    #or (a and b and c and d and e and not f and g and h and i) \
    #or (a and b and c and d and e and f and not g and h and i) \
    #or (a and b and c and d and e and f and g and not h and i) \
    #or (a and b and c and d and e and f and g and h and not i)
     
