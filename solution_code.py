"""Solution of Advent of Code 2022."""
import math
from copy import deepcopy
import sys
from collections import deque
#from sympy import sympify, solve, Symbol

class Solutions(object):
    """One funciton per day."""
    def __init__(self):
        """Initialize."""

    def day_1(self, data):
        """Solution of day1."""
        
        data = data.split('\n\n')
        data = [linha.split() for linha in data]
        max = soma = 0
        top3 = [0, 0, 0]
        for linha in data:
            for value in linha:
                soma += int(value)
            if soma > max:
                max = soma
            if soma > min(top3):
                top3[top3.index(min(top3))] = soma
            soma = 0
        print(f'Max Calories: {max}')
        print(f'Top3 Calories: {sum(top3)}')

    def day_2(self, data):
        """Solution of day2."""
        score = {
            'A X': 3,
            'A Y': 6,
            'A Z': 0,
            'B X': 0,
            'B Y': 3,
            'B Z': 6,
            'C X': 6,
            'C Y': 0,
            'C Z': 3}
        bonus = {
            'X': 1,
            'Y': 2,
            'Z': 3}
        sum_score = 0
        turns = data.split('\n')
        for turn in turns:
            sum_score += score[turn] + bonus[turn[2]]
        print(f'Total Score1: {sum_score}')

        score2 = {
            'A': {0: 'Z',3: 'X',6: 'Y'},
            'B': {0: 'X',3: 'Y',6: 'Z'},
            'C': {0: 'Y',3: 'Z',6: 'X'}}

        result_value = {
            'X': 0,
            'Y': 3,
            'Z': 6}

        sum_score = 0
        for turn in turns:
            sum_score += result_value[turn[2]] + bonus[score2[turn[0]][result_value[turn[2]]]]
            print(sum_score)
        print(f'Total Score1: {sum_score}')   

    def day_3(self, data):
        """Solution of day3."""
        rucksack = data.split('\n')
        element = []
        for nruck in rucksack:
            a = nruck[:int(len(nruck)/2)]
            b = nruck[int(len(nruck)/2):]
            dup = []
            for el_a in a:
                if b.count(el_a):
                    dup.append(el_a)
            set_dup = set(dup)
            dict_dup = {}
            for el_dup in set_dup:
                dict_dup[el_dup] = a.count(el_dup) + b.count(el_dup)

            element.append(max(dict_dup, key=dict_dup.get))
        s_prio = 0
        for el in element:
            if ord(el) > 96:
                s_prio += ord(el) - 96
            else:
                s_prio += ord(el) - 64 + 26
        print(s_prio)
        """Two Stars"""
        element = []
        for idx in range(0, len(rucksack), 3):
            a = rucksack[idx]
            b = rucksack[idx+1]
            c = rucksack[idx+2]
            dup = []
            for el_a in a:
                if b.count(el_a) and c.count(el_a):
                    dup.append(el_a)
            set_dup = set(dup)
            dict_dup = {}
            for el_dup in set_dup:
                dict_dup[el_dup] = a.count(el_dup) + b.count(el_dup)

            element.append(max(dict_dup, key=dict_dup.get))
        s_prio = 0
        for el in element:
            if ord(el) > 96:
                s_prio += ord(el) - 96
            else:
                s_prio += ord(el) - 64 + 26
        print(s_prio)

    def day_4(self, data):
        """Solution of day4."""
        spaces = data.split('\n')
        spaces = [elf.split(',') for elf in spaces]
        soma = 0
        for space in spaces:
            a = [int(value) for value in space[0].split('-')]
            b = [int(value) for value in space[1].split('-')]
            if (((a[0] <= b[0]) and (a[1] >= b[1]))
                or ((a[0] >= b[0]) and (a[1] <= b[1]))):
                #self.day_4_printspaces(a[0],a[1])
                #self.day_4_printspaces(b[0],b[1])
                soma += 1
            
        print(f'Total Conflit: {soma}')
        soma = 0
        """
        for space in spaces:
            a = [int(value) for value in space[0].split('-')]
            b = [int(value) for value in space[1].split('-')]
            if (((b[0] <= a[1]) and (a[1] <= b[1]))) or (((a[0] <= b[1]) and (b[1] <= a[1]))):
                print(f'{space} {b[0] <= a[1]} {a[1] <= b[1]} {a[0] <= b[1]} {b[1] <= a[1]}')
                self.day_4_printspaces(a[0],a[1])
                self.day_4_printspaces(b[0],b[1])
                soma += 1
         */   
        print(f'Total Overlap: {soma}')"""

    def day_4_printspaces(self, st, end):
        """Print line of elv spaces."""
        for idx in range(100):
            if (idx >= int(st)) and (idx <= int(end)):
                print('#', end='')
            else:
                print('-', end='')
        print()

    def day_5(self, data):
        """Solution of day5."""
        [maps, cmds] = data.split('\n\n')
        cmds = cmds.splitlines()
        cmds = [pos.split() for pos in cmds]
        qnt = 1
        from_s = 3
        to_s = 5

        max_stack = int(maps.splitlines()[-1].split()[-1])
        maps = maps.splitlines()[-2::-1]
        stacks = ['']*max_stack
        for idx in range(max_stack):
            for line in maps:
                stacks[idx] += line[idx*4+1]
            stacks[idx] = list(stacks[idx].replace(' ',''))


        """
        #one star
        for cmd in cmds:
            for el in range(int(cmd[qnt])):
                stacks[int(cmd[to_s])-1].append(stacks[int(cmd[from_s])-1].pop())
        
        """
        
        #two star
        for cmd in cmds:
            n_el = len(stacks[int(cmd[from_s])-1])-int(cmd[qnt])
            for el in range(int(cmd[qnt])):
                stacks[int(cmd[to_s])-1].append(stacks[int(cmd[from_s])-1].pop(n_el))

        top = ''
        for st in stacks:
            top += st[-1]
        print(top)

    def day_6(self, data):
        """Solution of day6."""
        msg = list(data)
        l_msg = len(msg)
        for idx in range(0, l_msg-4):
            if len(set(msg[idx:idx+4])) == 4:
                print(f'Star: {idx+4}')
                break

        for idx in range(0, l_msg-14):
            chrs = set(msg[idx:idx+14])
            if len(chrs) == 14:
                print(f'Start of msg: {idx+14}')
                break

    def day_7(self, data):
        """Solution of day7."""
        filesys = data.split("$ ")
        filesys = [line.splitlines() for line in filesys]
        self.root_files = {}
        path = ['root']
        for cmdline in filesys[1:]:
            cmd = cmdline[0].split()[0]
            arg = ''
            if cmd == 'cd':
                arg = cmdline[0].split()[1]
                if arg == '/':
                    path = ['root']
                elif arg == '..':
                    path.pop()
                else:
                    path.append(arg)
            elif cmd == 'ls':
                files = cmdline[1:]
                dict_path = '/'.join(path)
                if dict_path not in self.root_files.keys():
                    self.root_files[dict_path] = {}
                    name_dir = []
                    size = 0
                    for item in files:
                        if item.split()[0] == 'dir':
                            name_dir.append(item.split()[-1])
                        else:
                            size += int(item.split()[0])
                    self.root_files[dict_path]['n_dir'] = name_dir
                    self.root_files[dict_path]['files_size'] = size
        dir_sum = 0
        for folder in self.root_files:
            total_size = self.day_7_folder_size_calc(folder)
            self.root_files[folder]['total'] = total_size
            if total_size < 100000:
                dir_sum += total_size

        
        total = 70000000
        need =  30000000
        used = self.root_files['root']['total']
        free = total - used
        print(f'Livre {free}')

        min_folder = 70000000
        dir_choose = ''

        for folder in self.root_files:
            dir_space = self.root_files[folder]['total']
            if (free + dir_space) > need:
                if min_folder > (free + dir_space):
                    min_folder = (free + dir_space)
                    dir_choose = folder

        print(f'Folder {dir_choose} -- {min_folder} -- {self.root_files[dir_choose]["total"]}')

    def day_7_folder_size_calc(self, path):
        """Calculate size file total."""

        size = 0
        if len(self.root_files[path]['n_dir']):
            size += self.root_files[path]['files_size']
            for folders in self.root_files[path]['n_dir']:
                size += self.day_7_folder_size_calc(path+'/'+folders)
        else:
            return self.root_files[path]['files_size']
        return size

    def day_8(self, data):
        """Solution of day8."""
        treemap = data.splitlines()
        treemap = [list(line) for line in treemap]

        x,y = len(treemap),len(treemap[0])

        ext_tree = 2*len(treemap)+2*len(treemap[0])-4
        int_tree = 0
        max_scenario = 0
        for idx in range(1,x-1):
            for idy in range(1,y-1):
                tree = treemap[idy][idx]
                down = [el[idx] for el in treemap[idy+1:]]
                up = [el[idx] for el in treemap[:idy]]
                left = treemap[idy][:idx]
                right = treemap[idy][idx+1:]
                print(f'Tree {tree} -- ', end='')
                """
                if ((max(down) < tree)
                    or (max(up) < tree)
                    or (max(left) < tree)
                    or (max(right) < tree)):
                        int_tree += 1
                        print(f'visible -- ', end='')
                else:
                    print(f'not visible -- ', end='')
                """
                view_u = view_d = view_r = view_l = 0
                if right[0] >= tree:
                    view_r = 1
                else:
                    for t_r in right:
                        view_r += 1
                        if t_r >= tree:
                            break
                if down[0] >= tree:
                    view_d = 1
                else:
                    for t_d in down:
                        view_d += 1
                        if t_d >= tree:
                            break

                if left[-1] >= tree:
                    view_l = 1
                else:
                    for t_l in left[::-1]:
                        view_l += 1
                        if t_l >= tree:
                            break
                if up[-1] >= tree:
                    view_u = 1
                else:
                    for t_u in up[::-1]:
                        view_u += 1
                        if t_u >= tree:
                            break

                scenario = view_u*view_d*view_l*view_r
                if scenario > max_scenario:
                    max_scenario = scenario
                print(f'Scenario :{view_u*view_d*view_l*view_r}')


        print(f'External {ext_tree}')
        print(f'Internal {int_tree}')
        print(f'Max Scenario {max_scenario}')
        print(f'Total {int_tree+ext_tree}')

    def day_9(self, data):
        """Solution of day9."""
        cmd = data.splitlines()
        cmd = [line.split() for line in cmd]

        x = y = 0
        xmax = xmin = ymax = ymin = 0

        for line in cmd:
            if line[0] == 'R':
                x += int(line[1])
            if line[0] == 'L':
                x -= int(line[1])
            if line[0] == 'D':
                y -= int(line[1])
            if line[0] == 'U':
                y += int(line[1])

            if x > xmax:
                xmax = x
            if x < xmin:
                xmin = x
            if y > ymax:
                ymax = y
            if y < ymin:
                ymin = y

        lx = xmax-xmin+1
        ly = ymax-ymin+1
        
        H = (-xmin,-ymin) 
        T = [(-xmin,-ymin)]*9 
        vt = vh = (0,0)
        x = -xmin
        y = -ymin
        steps = 0

        for line in cmd:
            for idx in range(int(line[1])):
                if line[0] == 'R':
                    x += 1
                    vh = (1,0)
                if line[0] == 'L':
                    x -= 1
                    vh = (-1,0)
                if line[0] == 'D':
                    y -= 1
                    vh = (0,-1)
                if line[0] == 'U':
                    y += 1
                    vh = (0,1)
                H = (x,y)
                for iT in range(0, steps+1):
                    if iT == 0:
                        d = (H[0] - T[0][0],H[1] - T[0][1])
                        d_abs = math.sqrt(d[0]**2 + d[1]**2)
                        if d_abs >= 2:
                            vt = (-vh[0]+d[0],-vh[1]+d[1])
                        else:
                            vt = (0,0)
                    else:
                        d = (T[iT-1][0] - T[iT][0],T[iT-1][1] - T[iT][1])
                        d_abs = math.sqrt(d[0]**2 + d[1]**2)
                    if d_abs >= 2:
                        T[iT] = (T[iT][0]+vt[0],T[iT][1]+vt[1])
                
                count = self.day_9_map_print(lx,ly,H,T,steps)

                


                print(f'{vh} -- {H} -- {d} -- {vt} -- {T} -- {count}')
                if steps <= 7:
                    steps += 1
        print(f'Tail count -- {count}')

    def day_9_map_print(self, lx, ly, H, T, steps):

        maps = [['.']*(lx) for idx in range(ly)]
        maps[H[1]][H[0]] = 'H'
        for idxT in range(steps+1):
            maps[T[idxT][1]][T[idxT][0]] = idxT
        
        tc = 0
        for line in maps:
            for row in line:
                print(row, end='')
                if row == 8:
                    tc += 1
            print()
        print('#'*40)
        return tc

    def day_10(self, data):
        """Solution for day10."""
        ciclo = 0
        ist = 0
        X = 1
        cmds = [line.split() for line in data.splitlines()]
        total = 0
        ctr = '#'
        for cmd in cmds:

            if cmd[0] == 'noop':
                ist = 1
                pay_X = 0
            elif cmd [0] == 'addx':
                ist = 2
                pay_X = int(cmd[1])

            for idx in range(ist):
                ciclo += 1
                
                if (ciclo%40) == 20:
                    
                    if ciclo <= 220:
                        total += X*ciclo
                if (ciclo%40) == 0:
                    print(f'Ciclo: {ciclo:03d} -- {ctr} -- {X} -- {X*ciclo}')
                    ctr = ''
                if (idx % 2):
                    X += pay_X
                if (ciclo%40) in range(X-1,X+2):
                    ctr += '#'
                else:
                    ctr += '.'
        ciclo += 1
        print(f'total: {total}')    

    def day_11(self, data):
        """Solution day11."""
        data = data.split('\n\n')
        monkies = {}
        for monkie_data in data:
            monkie_data = monkie_data.splitlines()
            monkie = monkie_data[0].replace(':','').split()[-1]
            itens = [int(item) for item in monkie_data[1].replace(',','').split()[2:]]

            opp = monkie_data[2].split('=')[1]

            if opp == ' old * old':
                math_opp = self.day_11_pow
                payload = 2
            elif opp.split()[1] == '+':
                math_opp = self.day_11_add
                payload = int(opp.split()[2])
            elif opp.split()[1] == '-':
                math_opp = self.day_11_sub
                payload = int(opp.split()[2])
            elif opp.split()[1] == '/':
                math_opp = self.day_11_div
                payload = int(opp.split()[2])
            elif opp.split()[1] == '*':
                math_opp = self.day_11_mult
                payload = int(opp.split()[2])

            test = int(monkie_data[3].split()[-1])
            t_true = monkie_data[4].split()[-1]
            t_false = monkie_data[5].split()[-1]


            monkies[monkie] = {}
            monkies[monkie]['list'] = itens
            monkies[monkie]['newlist'] = []
            monkies[monkie]['opp'] = math_opp
            monkies[monkie]['payload'] = payload
            monkies[monkie]['test'] = test
            monkies[monkie]['result'] = {}
            monkies[monkie]['result'][True] = t_true
            monkies[monkie]['result'][False] = t_false
            monkies[monkie]['testes'] = 0
        monkies_k = monkies.keys()
        lcm = 1
        for monkie in monkies_k:
            lcm *= monkies[monkie]['test']
        for r in range(10000):
            if r == 19 or r%100 == 0:
                print(f'Round {r}')
            for monkie in monkies_k:
                itens = monkies[monkie]['list']
                for idx in range(len(itens)):
                    opp = (monkies[monkie]['opp'](itens[0], monkies[monkie]['payload'])% lcm)
                    test = (opp % monkies[monkie]['test']) == 0
                    if test:
                        monkies[monkies[monkie]['result'][True]]['list'].append(opp)
                    else:
                        monkies[monkies[monkie]['result'][False]]['list'].append(opp)
                    monkies[monkie]['list'].pop(0)
                    monkies[monkie]['testes'] += 1

                if r == 19 or r%100 == 0:
                    print(f'\tMonkey {monkie} -- {monkies[monkie]["testes"]}')

        test_c = []
        for monkie in monkies.keys():
            test_c.append(monkies[monkie]['testes'])

        test_c = sorted(test_c)[-2:]
        print(f'{test_c[0] * test_c[1]}')

    def day_11_add(self, old, payload):
        """add function day11."""
        return (old + payload)
    def day_11_sub(self, old, payload):
        """add function day11."""
        return (old - payload)
    def day_11_mult(self, old, payload):
        """add function day11."""
        return (old * payload)
    def day_11_div(self, old, payload):
        """add function day11."""
        return (old / payload)
    def day_11_pow(self, old, payload):
        """add function day11."""
        return old**payload

    def day_12(self, data):
        """Solution day12."""
        data = data.splitlines()



        x = 1
        y = 0
        map = []
        for row in range(len(data)):
            map.append([])
            for col in range(len(data[row])):
                level = data[row][col]
                if level == 'S':
                    start = (row,col)
                    data[row][col].replace('S','a')
                    level = 'a'  
                elif level == 'E':
                    end = (row,col)
                    data[row][col].replace('E','z')
                    level = 'z'        
                map[row].append(level)
        nrows = len(map)
        ncols = len(map[0])
        map_print = [['.']*(ncols) for idx in range(nrows)]
        map_graph = [[[]*1]*(ncols) for idx in range(nrows)]
        
        for part in [0,1]:
            grafo = {}
            for row in range(nrows):
                #print(f'Row: {row}\n\tCol: ', end ='')
                for col in range(ncols):
                    direction = []
                    #print(f' {col}:', end = '')
                    if row == 0:
                        if ((ord(map[row+1][col]) == ord(map[row][col])) or
                        (ord(map[row+1][col]) == (ord(map[row][col])+1)) or
                        (ord(map[row+1][col]) < ord(map[row][col])) or
                        (ord(map[row+1][col]) == ord(map[row][col]) - part)):
                            direction.append(f'{row+1}_{col}')
                            #print('v', end='')
                            
                    elif row == (nrows-1):
                        if ((ord(map[row-1][col]) == ord(map[row][col])) or
                        (ord(map[row-1][col]) == (ord(map[row][col])+1)) or
                        (ord(map[row-1][col]) == (ord(map[row][col]) - part)) or
                        (ord(map[row-1][col]) < ord(map[row][col]))):
                            direction.append(f'{row-1}_{col}')
                            #print('^', end='')
                    else:
                        if ((ord(map[row-1][col]) == ord(map[row][col])) or
                        (ord(map[row-1][col]) == (ord(map[row][col])+1)) or
                        (ord(map[row-1][col]) == (ord(map[row][col]) - part)) or
                        (ord(map[row-1][col]) < ord(map[row][col]))):
                            direction.append(f'{row-1}_{col}')
                            #print('^', end='')
                        if ((ord(map[row+1][col]) == ord(map[row][col])) or
                        (ord(map[row+1][col]) == (ord(map[row][col])+1)) or
                        (ord(map[row+1][col]) == (ord(map[row][col])- part)) or
                        (ord(map[row+1][col]) < ord(map[row][col]))):
                            direction.append(f'{row+1}_{col}')
                            #print('v', end='')


                    if col == 0:
                        if ((ord(map[row][col+1]) == ord(map[row][col])) or
                        (ord(map[row][col+1]) == (ord(map[row][col])+1)) or
                        (ord(map[row][col+1]) == (ord(map[row][col]) - part)) or
                        (ord(map[row][col+1]) < ord(map[row][col]))):
                            direction.append(f'{row}_{col+1}')
                            #print('>', end='')
                    elif col == (ncols-1):
                        if ((ord(map[row][col-1]) == ord(map[row][col])) or
                        (ord(map[row][col-1]) == (ord(map[row][col])+1)) or
                        (ord(map[row][col-1]) == (ord(map[row][col]) - part)) or
                        (ord(map[row][col-1]) < ord(map[row][col]))):
                            direction.append(f'{row}_{col-1}')
                            #print('<', end='')
                    else:
                        if ((ord(map[row][col-1]) == ord(map[row][col])) or
                        (ord(map[row][col-1]) == (ord(map[row][col])+1)) or
                        (ord(map[row][col-1]) == (ord(map[row][col]) - part)) or
                        (ord(map[row][col-1]) < ord(map[row][col]))):
                            direction.append(f'{row}_{col-1}')
                            #print('<', end='')
                        if ((ord(map[row][col+1]) == ord(map[row][col])) or
                        (ord(map[row][col+1]) == (ord(map[row][col])+1)) or
                        (ord(map[row][col+1]) == (ord(map[row][col]) - part)) or
                        (ord(map[row][col+1]) < ord(map[row][col]))):
                            direction.append(f'{row}_{col+1}')
                            #print('>', end='')

                    grafo[f'{row}_{col}'] = direction

                    map_graph[row][col] = direction


            grafo_dist = {}
            grafo_vist = {}

            for no in grafo.keys():
                grafo_dist[no] = int(1e9)
                grafo_vist[no] = False

            no = f'{start[0]}_{start[1]}'
            no_fim = f'{end[0]}_{end[1]}'
            grafo_dist[no] = 0
            grafo_vist[no] = True

            Q = deque()

            
            dist = 0
            caminho = []
            Q.append([no,dist])
            while Q:
                state = Q.popleft()
                no, dist = state

                if no == no_fim:
                    print(dist)
                    break


                for vizinho in grafo[no]:
                    if [vizinho,dist + 1] not in Q:
                        Q.append([vizinho,dist + 1])

            print(f'part{part+1}: {dist}')

    def day_13(self, data):
        """Solution day13."""
        packets = [pck.split('\n') for pck in data.split('\n\n')]
        l=0
        order = []
        idx = 0
        for p1, p2 in packets:
            idx += 1
            a = self.day_13_comp(eval(p1), eval(p2),l)
            if a:
                order.append(idx)
        print(f'part1 :{sum(order)}')


        #to high 1561824
        #to high 33408
        data = data.replace('\n\n','\n')
        packets = data.split('\n')
        """
        packets = [p.replace('[]','0') for p in packets]
        packets = [p.replace('[','').replace(']','').replace(',','') for p in packets]
        packets.append('2')
        packets.append('6')
        """



        idx2 = 1
        idx6 = 2
        total = 1
        for p in packets:
            if self.day_13_comp(eval(p), [[2]],l):
                idx2 += 1
            if self.day_13_comp(eval(p), [[6]],l):
                idx6 += 1
        print(idx2*idx6)

    def day_13_comp(self, pck1, pck2, level):
        """Function for comparation day13."""
        idx = 0
        if isinstance(pck1, int) and isinstance(pck2, int):
            if pck1 < pck2:
                return 1
            elif pck1 > pck2:
                return 0
            else:
                return -1
        elif isinstance(pck1, list) and isinstance(pck2, list):
            for left, right in zip(pck1,pck2):
                c = self.day_13_comp(left, right, level+1)
                if c != -1:
                    return c
                
                idx += 1
    
            if idx < len(pck1) and idx == len(pck2):
                return 0
            elif idx == len(pck1) and idx < len(pck2):
                return 1
            else:
                return -1
        elif isinstance(pck1, list) and isinstance(pck2, int):
            return self.day_13_comp(pck1, [pck2], level+1)
        elif isinstance(pck1, int) and isinstance(pck2, list):
            return self.day_13_comp([pck1], pck2, level+1)

    def day_13_comp2(self, pck1, pck2):
        """Function for comparation day13."""
        idx = 0
        if isinstance(pck1, int) and isinstance(pck2, int):
            if pck1 < pck2:
                return -1
            elif pck1 > pck2:
                return 1
            else:
                return 0
        elif isinstance(pck1, list) and isinstance(pck2, list):
            for left, right in zip(pck1,pck2):
                c = self.day_13_comp(left, right)
                if c != 0:
                    return c
                
                idx += 1
    
            if idx < len(pck1) and idx == len(pck2):
                return -1
            elif idx == len(pck1) and idx < len(pck2):
                return 1
            else:
                return 0
        elif isinstance(pck1, list) and isinstance(pck2, int):
            return self.day_13_comp(pck1, [pck2])
        elif isinstance(pck1, int) and isinstance(pck2, list):
            return self.day_13_comp([pck1], pck2)   

    def day_14(self, data):
        """day14."""
        rocks = data.splitlines()
        rocks = [rock.split(' -> ') for rock in rocks]
        rocks_coord = []

        #separacao das coordenadas
        for idx, r in enumerate(rocks):
            rocks_coord.append([])
            for kdx,coord in enumerate(r):
                x = int(coord.split(',')[0])
                y = int(coord.split(',')[1])
                rocks_coord[idx].append([x,y])
        
        #limites x e y
        xmin = 10e10
        ymin = 10e10
        ymax = 0
        xmax = 0
        for rock in rocks_coord:
            for coord in rock:
                if coord[0] > xmax:
                    xmax = coord[0]
                elif coord[0] < xmin:
                    xmin = coord[0]

                if coord[1] > ymax:
                    ymax = coord[1]
                elif coord[1] < ymin:
                    ymin = coord[1]
        
        #mapeamento rochas
        xdim = xmax-xmin+1
        padding = xdim*4
        ydim = ymax+1
        maps = [['.']*(xdim+4*padding) for _ in range(ydim+2)]
        for rock in rocks_coord:
            for icoord in range(len(rock)-1):
                if rock[icoord][0] == rock[icoord+1][0]:
                    x = rock[icoord][0]-xmin
                    y1 = rock[icoord][1]
                    y2 = rock[icoord+1][1]
                    if y2 > y1:
                        for i in range(y1,y2+1):
                            maps[i][x+padding] = '#'
                    else:
                      for i in range(y2,y1+1):
                            maps[i][x+padding] = '#'
                elif rock[icoord][1] == rock[icoord+1][1]:
                    y = rock[icoord][1]
                    x1 = rock[icoord][0]-xmin
                    x2 = rock[icoord+1][0]-xmin
                    if x2 > x1:
                        for i in range(x1,x2+1):
                            maps[y][i+padding] = '#'
                    else:
                        for i in range(x2,x1+1):
                            maps[y][i+padding] = '#'

        maps2 = deepcopy(maps)

        # areia
        xareia = 500
        count = 0
        while(y<=ymax):
            xareia = 500
            y = 0
            while(True):
                if y == ymax+1:
                    maps[y][xareia-xmin+padding] = 'o'
                    break
                if (maps[y+1][xareia-xmin+padding] == '.'):
                    y += 1
                elif maps[y+1][xareia-xmin+padding] != '.':
                    if maps[y+1][xareia-xmin-1+padding] == '.':
                         y += 1
                         xareia -= 1
                    elif maps[y+1][xareia-xmin+1+padding] == '.':
                        y += 1
                        xareia += 1
                    else:
                        maps[y][xareia-xmin+padding] = 'o'
                        break
            count += 1

        #self.day_14_print_map(maps)
        #print(f'Part 1: {count-1}')

        
        for idx,_ in enumerate(maps2[ymax+1]):
            maps2[ymax+2][idx] = '#'

        xareia = 500
        count = 0
        y = 0
        while(maps2[0][xareia-xmin+padding] != 'o'):
            xareia = 500
            y = 0
            while(1):
                if (maps2[y+1][xareia-xmin+padding] == '.'):
                    y += 1
                elif maps2[y+1][xareia-xmin+padding] != '.':
                    if maps2[y+1][xareia-xmin-1+padding] == '.':
                         y += 1
                         xareia -= 1
                    elif maps2[y+1][xareia-xmin+1+padding] == '.':
                        y += 1
                        xareia += 1
                    else:
                        maps2[y][xareia-xmin+padding] = 'o'
                        break
            count += 1
        self.day_14_print_map(maps2)
        print(f'Part2: {count}')
    
    def day_14_print_map(self, map):

        for y,line in enumerate(map):
            print(f'{y}\t',end='')
            for row in line:
                print(row, end='')
            print()

    def day_15(self, data):
        """day15 solution."""
        data = data.splitlines()
        data = [line.replace(',','') for line in data]
        data = [line.split(':') for line in data]
        #sensores e beacons
        sensors = []
        beacons = []
        for s,b in data:
            sensors.append([int(s.split('=')[1].replace(' y','')),int(s.split('=')[2])])
            beacons.append([int(b.split('=')[1].replace(' y','')),int(b.split('=')[2])])
        radius = []
        print('Parsing sensores e beacons')
        for idx,_ in enumerate(sensors):
            xr = abs(sensors[idx][0]-beacons[idx][0])
            yr = abs(sensors[idx][1]-beacons[idx][1])
            radius.append(xr+yr)
            

        y=2000000
        marks_lim = [1e9,-1e9]
        count = 0
        for idx,s in enumerate(sensors):
            r = radius[idx]+1
            l = y - s[1]
            c = r-abs(l)
            if c > 0:
                if (-c+1 + s[0]) < marks_lim[0]:
                    marks_lim[0] = -c+1 + s[0]
                if (c + s[0]) > marks_lim[1]:
                    marks_lim[1] = c + s[0]

        beacons_y = []
        for b in beacons:
            if b[1] == y and b not in beacons_y:
                beacons_y.append(b)
          
        print(f'Part1 : {marks_lim[1]-marks_lim[0] - len(beacons_y)}')

        #part2
        s_par = []
        for idS1, s1 in enumerate(sensors):
            for idS2, s2 in enumerate(sensors):
                deltaX = abs(sensors[idS1][0]-sensors[idS2][0])
                deltaY = abs(sensors[idS1][1]-sensors[idS2][1])
                if (deltaX + deltaY - radius[idS1] - radius[idS2]) == 2:
                    if len(s_par) < 2:
                        s_par.append([[sensors[idS1],sensors[idS2]],[radius[idS1],radius[idS2]]])
        eq = []        
        for reta, sensores in enumerate(s_par):
            print(f'Reta: {reta} -- {sensores}')
            x1, y1 = sensores[0][0]
            x2, y2 = sensores[0][1]
            r1 = sensores[1][0]
            r2 = sensores[1][1]
            
            if y2 < y1:
                eq.append([[x1,y1 - r1 - 1],[x2, y2 + r2 + 1]])
            else:
                eq.append([[x2,y2 - r2 - 1],[x1, y1 + r1 + 1]])
        
        




    def day_18(self, data):
        """Solution of day18."""
        blocks = data.splitlines()
        blocks = [block.split(',') for block in blocks]
        faces = {}
        for block in blocks:
            faces['_'.join(block)] = 6
        
        adj_face = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
        xmin = ymin = zmin = 1e10
        xmax = ymax = zmax = 0
        for block in blocks:
            x,y,z = int(block[0]),int(block[1]),int(block[2])
            if x > xmax:
                xmax = x
            if y > ymax:
                ymax = y
            if z > zmax:
                zmax = z
            if x < xmin:
                xmin = x
            if y < ymin:
                ymin = y
            if z < zmin:
                zmin = z
            
            block_test = '_'.join(block)
            for adj in adj_face:
                adj_test = f'{x+adj[0]}_{y+adj[1]}_{z+adj[2]}'
                if adj_test in faces:
                    faces[block_test] -= 1
        total1 = 0
        for face in faces:
            total1 += faces[face]
        print('Part1', total1)
        blank = {}
        in_out = {}
        for x in range(xmin-1,xmax+1):
            for y in range(ymin-1,ymax+1):
                for z in range(zmin-1,zmax+1):
                    coor = f'{x}_{y}_{z}'
                    
                    if coor not in faces:
                        limits = 0
                        for xtest in range(x,xmax+1):
                            coortest = f'{xtest}_{y}_{z}'
                            if coortest in faces:
                                limits += 1
                                break
                        
                        for xtest in range(x,xmin-1,-1):
                            coortest = f'{xtest}_{y}_{z}'
                            if coortest in faces:
                                limits += 1
                                break

                        for ytest in range(y,ymax+1):
                            coortest = f'{x}_{ytest}_{z}'
                            if coortest in faces:
                                limits += 1
                                break
                        
                        for ytest in range(y,ymin-1,-1):
                            coortest = f'{x}_{ytest}_{z}'
                            if coortest in faces:
                                limits += 1
                                break
                        for ztest in range(z,zmax+1):
                            coortest = f'{x}_{y}_{ztest}'
                            if coortest in faces:
                                limits += 1
                                break
                        
                        for ztest in range(z,zmin-1,-1):
                            coortest = f'{x}_{y}_{ztest}'
                            if coortest in faces:
                                limits += 1
                                break
                        if limits == 6:
                            blank[coor] = limits

        for coord in blank:
            block = coord.split('_')
            x,y,z = int(block[0]),int(block[1]),int(block[2])
            
            block_test = '_'.join(block)
            for adj in adj_face:
                adj_test = f'{x+adj[0]}_{y+adj[1]}_{z+adj[2]}'
                if adj_test in blank:
                    blank[block_test] -= 1
        
        total2 = 0
        for face in blank:
            adj_count = 0
            block = face.split('_')
            x,y,z = int(block[0]),int(block[1]),int(block[2])
            block_test = '_'.join(block)
            for adj in adj_face:
                adj_test = f'{x+adj[0]}_{y+adj[1]}_{z+adj[2]}'
                if adj_test in faces:
                    adj_count += 1

            
            if blank[face] == adj_count:
                total2 += blank[face]
        print('Part2', total1-total2)

    def day_19(self, data):
        """Solution of day19."""
        data = data.splitlines()
        data = [bprint.split('.') for bprint in data]
        
        blueprints = []
        for bprint in data:
            cost = {}
            cost['ore'] = [int(bprint[0].split()[-2]),0,0,0]
            cost['clay'] = [int(bprint[1].split()[-2]),0,0,0]
            cost['obsidian'] = [int(bprint[2].split()[-5]),int(bprint[2].split()[-2]),0,0]
            cost['geode'] = [int(bprint[3].split()[-5]),0,int(bprint[3].split()[-2]),0]
            blueprints.append(cost)
        
        robots = ['ore','clay','obsidian','geode']
        q = []
        for irobot,blueprint in enumerate(blueprints):
            t = 32
            carteira = []
            print(blueprint)
            for robot in robots:
                carteira.append(0)
            inventario = []
            for robot in robots:
                inventario.append(0)
            inventario[0] = 1
            
            fila = deque([carteira + inventario +[t]])
            print(f'{irobot}')
            print(f'{irobot}', end='')

            maxOreCost = max([custo[0] for _,custo in blueprint.items()])
            maxClayCost = max([custo[1] for _,custo in blueprint.items()])
            maxObsCost = max([custo[2] for _,custo in blueprint.items()])
            maxCost = [maxOreCost, maxOreCost, maxObsCost, 999]
            caminho = set()
            maxGeode = 0
            it = 0
            dup = 0
            while fila:
                a = fila.popleft()
                cartOre, cartClay, cartObsidian, cartGeode = a[0:4] 
                rOre, rClay, rObsidian, rGeode = a[4:8]
                tAtual = a[8]
                it += 1
                    
                
                maxGeode = max(cartGeode, maxGeode)

                if tAtual == 0:
                    continue
                pulaCompra = [0,0,0,0]
                if rOre > maxOreCost:
                    rOre = maxOreCost
                    pulaCompra[0] = 1
                if rClay > maxClayCost:
                    rClay = maxClayCost
                    pulaCompra[1] = 1
                if rObsidian > maxObsCost:
                    rObsidian = maxObsCost
                    pulaCompra[2] = 1

                if cartOre >= tAtual*maxOreCost-rOre*(tAtual-1):
                    cartOre = tAtual*maxOreCost - rOre*(tAtual-1)
                if cartClay >= tAtual*maxClayCost - rClay*(tAtual-1):
                    cartClay = tAtual*maxClayCost - rClay*(tAtual-1)
                if cartObsidian >= tAtual*maxObsCost - rObsidian*(tAtual-1):
                    cartObsidian =  tAtual*maxObsCost - rObsidian*(tAtual-1)
                #atualiza lista de inventario atual
                invAtual = [rOre, rClay, rObsidian, rGeode]

                #if not it%100000:
                #    print(len(fila), maxGeode, tAtual)

                if (cartOre, cartClay, cartObsidian, cartGeode, rOre, rClay, rObsidian, rGeode, tAtual) in caminho:
                    dup += 1
                    continue
                caminho.add((cartOre, cartClay, cartObsidian, cartGeode, rOre, rClay, rObsidian, rGeode, tAtual))

                #sem compra
                novaCart = [cartOre + rOre,
                            cartClay + rClay,
                            cartObsidian + rObsidian,
                            cartGeode + rGeode]
                fila.append(novaCart + invAtual + [tAtual-1])
                #comprando
                for id, robot in enumerate(robots):
                    if (cartOre >= blueprint[robot][0]
                        and cartClay  >= blueprint[robot][1] 
                        and cartObsidian>= blueprint[robot][2] 
                        and cartGeode >= blueprint[robot][3]):
                        #Carteira pos compra
                        cartPosCompa = [cartOre - blueprint[robot][0],
                                        cartClay - blueprint[robot][1],
                                        cartObsidian - blueprint[robot][2],
                                        cartGeode - blueprint[robot][3]]
                        #coleta do inventario anterior a compra
                        novaCart = [cart+inv for cart,inv in zip(cartPosCompa,invAtual)]                        
                        novoIvent = [inv+1 if id == idInv else inv for idInv,inv in enumerate(invAtual)]
                        fila.append(novaCart + novoIvent +[tAtual-1])
            qualidade = maxGeode * (irobot+1)
            q.append(qualidade)
            print(f'| Qualidade: {qualidade}', end='')
            print(f'| GEODE: {maxGeode}')
    
    def day_20(self, data):
        """Solution for day20."""
        pt = 2
        key = 811589153

        order = [[id,int(n) * (key if pt==2 else 1),False] for id, n in enumerate(data.splitlines())] 
        out = deepcopy(order)
        size = len(order)
        for r in range(10 if pt==2 else 1):
            for id, el, _ in order:

                if el==0:                
                    continue

                idxNow = out.index([id,el,False])
                next = el + idxNow

                if next >= 0:
                    out.pop(idxNow)
                    idxFut = next % (size-1)
                elif next < 0:
                    out.pop(idxNow)
                    idxFut = (next + size - 1) % (size-1)
                
                out.insert(idxFut, [id,el, False])
                """
                print(el, end='\t\t')
                print(idxNow, end=' -> ')
                print(idxFut, end='\t\t')   
                out = [[i,e,False] for i,e,visit in out if not visit]
                for i,e,_ in out:
                    print(f'{e}', end='\t')
                print()
                """

            #for id, el, _ in out:
            #    print(r, el, end=' ')
            #print()

        for idx, el in enumerate(out):
            if el[1] == 0:
                zero_id = idx
                break
                
        


        with open('out20','w') as f:
            for el in out:
                print(el, file=f)

        print(zero_id)
        print(f'{out[(1000+zero_id)%size][1]} {out[(2000+zero_id)%size][1]} {out[(3000+zero_id)%size][1]}')
        print(f'{out[(1000+zero_id)%size][1] + out[(2000+zero_id)%size][1]+ out[(3000+zero_id)%size][1]}')

    def day_21(self, data):
        """Solution for AoC2022 day21."""

        find_monk = 'root'

        equations = data.splitlines()
        equations = [eq.replace(':','').split() for eq in equations]
        numbers = {eq[0] : int(eq[1]) for eq in equations if eq[1].isnumeric() and eq[0] != 'humn'}


        expressoes = {eq[0] : ' '.join(eq[1:]) for eq in equations if not eq[1].isnumeric()}

        root_vars = [expressoes['root'].split()[0],expressoes['root'].split()[2]]

        print(expressoes['root'])

        humn_exp = ''
        num_exp = ''
        for var_root in root_vars:
            exp_root = var_root
            f_var = []
            f_var.append(var_root)
            while(f_var):

                for var,exp in expressoes.items():
                    if var == 'root':
                        continue
                    if len(f_var):
                        if  f_var[0] not in expressoes.keys():
                            if f_var[0] != 'humn':
                                exp_root = exp_root.replace(f_var[0], f'{numbers[f_var[0]]}')

                            f_var.pop(0)
                        elif f_var[0] == var:
                            
                            var1 = exp.split()[0]
                            var2 = exp.split()[2]
                            exp_root = exp_root.replace(f_var[0], f'({exp})')
                            f_var.append(var1)
                            f_var.append(var2)
                            f_var.pop(0)

            if 'humn' in exp_root:
                humn_exp = exp_root
            else:    
                num_exp = str(eval(exp_root))

        humn = Symbol("humn")
        print(solve(sympify(f'{humn_exp} - {num_exp}', evaluate=True)))
        

        """
        #pt 1
        while(len(numbers) < len(equations)):
            for line in equations:
                if line[0] in numbers.keys():
                    continue
                else:
                    if line[1] in numbers.keys() and line[3] in numbers.keys():
                        a = numbers[line[1]]
                        op = line[2]
                        b = numbers[line[3]]
                        numbers[line[0]] = eval(f'int({a}{op}{b})')
        """       
        #print(numbers[find_monk])

    def day_22(self, data):
        """Solution for AoC2022 day22."""
        comandos_line = data.splitlines()[-1]
        mapa = data.splitlines()[:-2]
        mapa1 = [list(line) for line in mapa]
        cubo = deepcopy(mapa)
        max_cols = max(len(line) for line in mapa1)
        mapa = []
        for line in mapa1:
            if len(line) < max_cols:
                mapa.append(line + [' ']*(max_cols - len(line)))
            else:
                mapa.append(line)

        mapa = [line + ['*'] for line in mapa]

        mapa.append(len(mapa[-1]) * ['*'])
        mapa_desenho = deepcopy(mapa)
        


        comandos = []
        cmd = ''
        for chr in comandos_line:
            if chr not in ['R','L']:
                cmd += chr
            else:
                comandos.append(cmd)
                comandos.append(chr)
                cmd = ''

        #marcar inicio
        #sistema de coordenadas Y(linhas),X(col) -- > [Y][X]
        for x,row in enumerate(mapa[1]):
            if row == '.':
                p = [0,x]
                break
        # mapa[p[0]][p[1]] = 's'
        # inicia +X(direita)
        dict_versor = {0: [0,1], 1: [1,0], 2: [0,-1], 3: [-1,0]}
        dict_versor_chr = {0: '>', 1: 'v', 2: '<', 3: '^'}
        versor = 0
        for cmd in comandos:
            if cmd == 'R':
                if versor < 3:
                    versor += 1
                else:
                    versor = 0
            elif cmd == 'L':
                if versor > 0:
                    versor -= 1
                else:
                    versor = 3
            else:
                steps = int(cmd)
                trajeto = ''
                #direita
                p_fut = p
                
                for _ in range(steps):
                    p_fut = [p+v for p,v in zip(p_fut,dict_versor[versor])]

                    if (p_fut[0] < 0 or p_fut[1] < 0 or
                        mapa[p_fut[0]][p_fut[1]] == '*' or
                        mapa[p_fut[0]][p_fut[1]] == ' '):
                        p_fut = self.day_22_rotacao(mapa, p_fut, versor, dict_versor)
                        mapa_desenho[p_fut[0]][p_fut[1]] = dict_versor_chr[versor]

                    elif mapa[p_fut[0]][p_fut[1]] == '.':
                        mapa_desenho[p_fut[0]][p_fut[1]] = dict_versor_chr[versor]
                        
                    elif mapa[p_fut[0]][p_fut[1]] == '#':
                        p_fut = [p-v for p,v in zip(p_fut,dict_versor[versor])]
                        mapa_desenho[p_fut[0]][p_fut[1]] = dict_versor_chr[versor]
                        break

                #print(p, p_fut, dict_versor_chr[versor])
                p = p_fut
        #for i,line in enumerate(mapa_desenho):
        #    print(f'{i}\t', end ='')
        #    for ch in line:
        #        print(ch, end='')
        #    print()
        print(f'day22.1 :{(p[0]+1)*1000 + (p[1]+1)*4 + versor}')

        LADO = 4
        parsing = [['1'],['2','3','4'],['5','6']]

        

        faces = {}
        cubo = [line.replace(' ','') for line in cubo]
        for idx, line in enumerate(cubo):
            parsing_pag = int(idx/4)
            for ncols,face in enumerate(parsing[parsing_pag]):
                if face not in faces.keys():
                    faces[face] = []
                faces[face].append(line[ncols*LADO:(ncols+1)*LADO])


        cubo_completo = {}
        for face_id, face in faces.items():
            for row, line in enumerate(face):
                for col, ch in enumerate(line):
                    chave = f'F{face_id}:{row}:{col}'
                    if ((row > 0 and row < (LADO-1)) and
                        (col > 0 and col < (LADO-1))):
                         vetor_t = [face_id]*4
                    else:
                        vetor_t = [0]*4
                    cubo_completo[chave] = [ch,vetor_t]

        print(cubo_completo)

        # for i,line in enumerate(cubo):
        #     print(f'{i}\t', end ='')
        #     for ch in line:
        #         print(ch, end='')
        #     print()
    
    def day_22_rotacao(self, mapa, p, versor, dict_versor):
        """Realiza a rotacao(ultrapassou limite) no mapa conforme a line/coluna."""
        
        if (versor % 2) == 0:  #linha
            linha = mapa[p[0]]

            if dict_versor[versor][1] == 1:

                for idx in range(len(linha)):
                    if linha[idx] == '#':
                        return [p-v for p,v in zip(p,dict_versor[versor])]
                    if linha[idx] == '.':
                        return [p[0], idx]
            else:
                for idx in range(len(linha)-1,0,-1):
                    print(idx)
                    if linha[idx] == '#':
                        return [p-v for p,v in zip(p,dict_versor[versor])]
                    if linha[idx] == '.':
                        return [p[0], idx]

        else:
            col = [linha[p[1]] for linha in mapa]
            if dict_versor[versor][0] == 1:
                for idx in range(len(col)):
                    
                    if col[idx] == '#':
                        return [p-v for p,v in zip(p,dict_versor[versor])]
                    if col[idx] == '.':
                        return [idx, p[1]]
            else:
                for idx in range(len(col)-1,0,-1):
                    
                    if col[idx] == '#':
                        return [p-v for p,v in zip(p,dict_versor[versor])]
                    if col[idx] == '.':
                        return [idx, p[1]]
        return p
                
    def day_23(self, data):
        """Solution day23 od AoC2022."""
        data = data.splitlines()
        mapa = [list(line) for line in data]
        pad = len(mapa)

        mapa = [['.']*pad + line + ['.']*pad for line in mapa]

        line = ['.'] * pad * 3
        for _ in range(pad):
            mapa.insert(0,line)
            mapa.append(line)

        self.day_23_desenha_mapa(mapa)

        dl = len(mapa)
        dr = len(mapa[0])

        dict_regioes = {'N': [[-1,-1],[-1, 0],[-1, 1]],
                        'S': [[+1,-1],[+1, 0],[+1, 1]],
                        'W': [[-1,-1],[ 0,-1],[+1,-1]],
                        'E': [[-1,+1],[ 0,+1],[+1,+1]]}
        seq = ['N','S','W','E']
        for part in [1,2]:
            elfos = {}
            for l,line in enumerate(mapa):
                for r,ch in enumerate(line):
                    if ch == '#':
                        elfos[f'e_{l}_{r}'] = {}
                        elfos[f'e_{l}_{r}']['p'] = [l,r]
                        elfos[f'e_{l}_{r}']['n'] = [0,0]

            for round in range(10 if part==1 else 10000):
                next = {}



                
                lista_p_elfos = [elfo['p'] for elfo in elfos.values()]

                lmax = max(p[0] for p in lista_p_elfos)
                lmin = min(p[0] for p in lista_p_elfos)
                rmax = max(p[1] for p in lista_p_elfos)
                rmin = min(p[1] for p in lista_p_elfos)
                print(f'Round {round} {lmin}:{lmax} -- {rmin}:{rmax}')
                parados = True
                for elfo,info_elfo in elfos.items():
                    elfo_l, elfo_r = info_elfo['p']
                    info_elfo['n'] = info_elfo['p']
                    #ve se está sozinho
                    vizinhos = -1
                    for l in [1,0,-1]:
                        for r in [1,0,-1]:
                            if [elfo_l+l, elfo_r+r] in lista_p_elfos:
                                vizinhos += 1
                    if vizinhos:
                        for tent in range(4):
                            regiao = dict_regioes[seq[(round+tent)%4]] 
                            livres = 0
                            for l,r in regiao:
                                if [elfo_l+l, elfo_r+r] not in lista_p_elfos:
                                    livres += 1
                            
                            if livres == 3:
                                l,r = regiao[1]
                                info_elfo['n'] = [l + elfo_l, r + elfo_r]
                                next_p = f'{l + elfo_l}_{r + elfo_r}'
                                if next_p not in next.keys():
                                    next[next_p] = 0
                                next[next_p] += 1
                                parados = False
                                break
                for elfo,info_elfo in elfos.items():

                    l,r = info_elfo['n']
                    if info_elfo['p'] != info_elfo['n']:
                        if next[f'{l}_{r}'] == 1:
                            elfos[elfo]['p'] = [l,r]
                            elfos[elfo]['n'] = [0,0]
                        else:
                            elfos[elfo]['n'] = [0,0]

                #print(round)
                #self.day_23_desenha_mapa(self.day_23_marca_mapa(elfos, dl, dr))
                if parados and part==2:
                    break
            #enquadramento
            lista_p_elfos = [elfo['p'] for elfo in elfos.values()]
            lmax = max(p[0] for p in lista_p_elfos)
            lmin = min(p[0] for p in lista_p_elfos)
            rmax = max(p[1] for p in lista_p_elfos)
            rmin = min(p[1] for p in lista_p_elfos)
            quadro = []
            for line in self.day_23_marca_mapa(elfos, dl, dr)[lmin:lmax+1]:
                quadro.append(line[rmin:rmax+1])
            
            self.day_23_desenha_mapa(quadro)
            print(f'day23.{part}: round{round} {(lmax-lmin+1)*(rmax-rmin+1) - len(lista_p_elfos)}')

    def day_23_marca_mapa(self, dict_elfos, l, r):
        """Gera o mapa com os elfos."""
        line = ['.'] * r
        mapa = []
        for il in range(l):
            mapa.append([])
            for ir in range(r):
                mapa[il].append('.')

        for elfo in dict_elfos.values():
            l,r = elfo['p']
            mapa[l][r] = '#'
        return mapa

    def day_23_desenha_mapa(self, mapa):
        """Print no mapa."""
        print('#\t', end='')
        for i in range(len(mapa[0])):
            print(f'{i%10}',end='')
        print()
        for i,line in enumerate(mapa):
            print(f'{i}\t', end ='')
            for ch in line:
                print(ch, end='')
            print()

    def day_24(self, data):
        """Solution of day24 AoC2022."""
        data = data.splitlines()
        mapa = [list(line) for line in data]
        
        nevascas = {}
        n = 0
        lTotal = len(mapa)
        rTotal = len(mapa[0])
        dict_mov = {'^': [-1,0], 'v':[1,0], '<': [0,-1], '>': [0,1], 'X': [0,0]}
        limite = {'^': lTotal-2, 'v':lTotal-2, '<': rTotal-2, '>': rTotal-2}
        for l,line in enumerate(mapa):
            for r,ch in enumerate(line):
                if ch in ['^', 'v', '<', '>']:
                    nevascas[f'n{n}'] = {}
                    nevascas[f'n{n}']['t0'] = [l,r]
                    nevascas[f'n{n}']['ch'] = ch
                    nevascas[f'n{n}']['m'] = dict_mov[ch]
                    nevascas[f'n{n}']['lim'] = limite[ch]
                    n += 1

        inicial = [0,1]
        final = [lTotal-1, rTotal-2]
        
        neve = []
        print(f'Neve em 0')
        for n in nevascas.values():
            neve.append([n['ch'],self.day_24_f_desc(n,0)])
        self.day_24_desenha_mapa(lTotal, rTotal, neve, [])
        posicoes_validas = []
        posicoes_validas.append(inicial)
        posicoes_validas.append(final)
        for l in range(1,lTotal-1):
            for r in range(1,rTotal-1):
                posicoes_validas.append([l,r])

        t0 = 0
        for entrada, saida in [[inicial,final],[final,inicial],[inicial,final]]:
            rota = deque([entrada])
            for t in range(t0, t0+1000):
                neve = []
                for n in nevascas.values():
                    neve.append([n['ch'],self.day_24_f_desc(n,t+1)])
                neve_pos = [pos for _, pos in neve]

                novas_pos = []
                while rota:
                    pos = rota.popleft()
                    for mov in dict_mov.values():
                        lElfo, rElfo = [e + m for e,m in zip(pos, mov)]
                        pElfo = [lElfo, rElfo]
                        if pElfo in posicoes_validas:
                            if not (pElfo in neve_pos or pElfo in novas_pos):
                                novas_pos.append(pElfo)
                rota.clear()
                
                error = False
                for pos in novas_pos:
                    if pos not in rota:
                        rota.append(pos)
                for p in rota:
                    if p in neve_pos:
                        error = True
                        print(p)

                if t%20 == 0:
                    print(f'day24: {t+1}: {entrada} --> {saida}')
                    self.day_24_desenha_mapa(lTotal, rTotal, neve, rota)

                if saida in rota:
                    print('cheguei')
                    #self.day_24_desenha_mapa(lTotal, rTotal, neve, rota)
                    t0 = t
                    break
            print(f'day24: {t+1}: {entrada} --> {saida}')

    def day_24_desenha_mapa(self, lT, rT, nevascas, elfos):
        """Print no mapa."""

        mapa = []
        for l in range(lT):
            mapa.append([])
            for r in range(rT): 
                if l == 0 or l==(lT-1):
                    mapa[l].append('#')
                elif r == 0 or r==(rT-1):
                    mapa[l].append('#')
                else:
                    mapa[l].append('.')
        mapa[0][1] = '.'
        mapa[-1][-2] = '.'

        for sentido, ponto in nevascas:
            if mapa[ponto[0]][ponto[1]] == '.':
                mapa[ponto[0]][ponto[1]] = sentido
            elif mapa[ponto[0]][ponto[1]] in ['^', 'v', '<', '>']:
                mapa[ponto[0]][ponto[1]] = 2
            else:
                mapa[ponto[0]][ponto[1]] += 1


        for lElfo, rElfo in elfos:
            mapa[lElfo][rElfo] = 'E'

        print('#\t', end='')
        for i in range(rT):
            print(f'{i%10}',end='')
        print()


        for i,line in enumerate(mapa):
            print(f'{i}\t', end ='')
            for ch in line:
                print(ch, end='')
            print()

    def day_24_f_desc(self, nevasca, t):
        """Retorna a posicao da nevasca em t."""
        l0,r0 = nevasca['t0']
        lMov,rMov = nevasca['m']
        lim = nevasca['lim']
        if nevasca['ch'] in ['^', 'v']:
            return [(lMov*t + l0 - 1)%(lim) + 1,r0]
        if nevasca['ch'] in ['<', '>']:
            return [l0,(rMov*t + r0 - 1)%(lim) + 1]

    def day_25(self, data):
        """Solution of day25 Aoc2022."""
        list_SNAFU_in = data.splitlines()
        simb_SNAFU = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
        simb_SNAFU_back = {-2: '=', -1: '-', 0: '0', 1: '1', 2: '2'}
        sum_dec = 0
        for n_SNAFU in list_SNAFU_in:
            SNAFU_to_dec = 0
            for p, dSNAFU in enumerate(n_SNAFU[::-1]):
                
                SNAFU_to_dec += simb_SNAFU[dSNAFU]*5**(p)
            sum_dec += SNAFU_to_dec
        print(sum_dec)
        resto = sum_dec % 5
        quociente = int(sum_dec//5)
        dec_to_SNAFU = []
        while quociente:
            resto = sum_dec % 5
            quociente = int(sum_dec//5)
            if resto > 2:
                quociente += 1
                resto -= 5
            dec_to_SNAFU.append(resto)
            #print(f'{sum_dec}: q:{quociente} r:{resto}')
            sum_dec = quociente
        print(''.join([simb_SNAFU_back[d] for d in dec_to_SNAFU[::-1]]))



if __name__ == "__main__":
    nday = int(input('Day :'))
    with open(f'.\data\day{nday}','r') as file:
        data = file.read()

    print(f'####### DAY {nday} #######')
    s = Solutions()
    func = f's.day_{nday}(data)'
    eval(func)
