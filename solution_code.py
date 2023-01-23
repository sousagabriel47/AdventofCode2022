"""Solution of Advent of Code 2022."""
import math
from copy import deepcopy
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
        grafo = {}
        for row in range(nrows):
            print(f'Row: {row}\n\tCol: ', end ='')
            for col in range(ncols):
                direction = []
                print(f' {col}:', end = '')
                if row == 0:
                    if ((ord(map[row+1][col]) == ord(map[row][col])) or
                       (ord(map[row+1][col]) == (ord(map[row][col])+1)) or
                       (ord(map[row+1][col]) < ord(map[row][col]))):
                        direction.append(f'{row+1}_{col}')
                        print('v', end='')
                        
                elif row == (nrows-1):
                    if ((ord(map[row-1][col]) == ord(map[row][col])) or
                       (ord(map[row-1][col]) == (ord(map[row][col])+1)) or
                       (ord(map[row-1][col]) < ord(map[row][col]))):
                        direction.append(f'{row-1}_{col}')
                        print('^', end='')
                else:
                    if ((ord(map[row-1][col]) == ord(map[row][col])) or
                       (ord(map[row-1][col]) == (ord(map[row][col])+1)) or
                       (ord(map[row-1][col]) < ord(map[row][col]))):
                        direction.append(f'{row-1}_{col}')
                        print('^', end='')
                    if ((ord(map[row+1][col]) == ord(map[row][col])) or
                       (ord(map[row+1][col]) == (ord(map[row][col])+1)) or
                       (ord(map[row+1][col]) < ord(map[row][col]))):
                        direction.append(f'{row+1}_{col}')
                        print('v', end='')


                if col == 0:
                    if ((ord(map[row][col+1]) == ord(map[row][col])) or
                       (ord(map[row][col+1]) == (ord(map[row][col])+1)) or
                       (ord(map[row][col+1]) < ord(map[row][col]))):
                        direction.append(f'{row}_{col+1}')
                        print('>', end='')
                elif col == (ncols-1):
                    if ((ord(map[row][col-1]) == ord(map[row][col])) or
                       (ord(map[row][col-1]) == (ord(map[row][col])+1)) or
                       (ord(map[row][col-1]) < ord(map[row][col]))):
                        direction.append(f'{row}_{col-1}')
                        print('<', end='')
                else:
                    if ((ord(map[row][col-1]) == ord(map[row][col])) or
                       (ord(map[row][col-1]) == (ord(map[row][col])+1)) or
                       (ord(map[row][col-1]) < ord(map[row][col]))):
                        direction.append(f'{row}_{col-1}')
                        print('<', end='')
                    if ((ord(map[row][col+1]) == ord(map[row][col])) or
                       (ord(map[row][col+1]) == (ord(map[row][col])+1)) or
                       (ord(map[row][col+1]) < ord(map[row][col]))):
                        direction.append(f'{row}_{col+1}')
                        print('>', end='')

                grafo[f'{row}_{col}'] = direction

                map_graph[row][col] = direction
            print()


        grafo_dist = {}
        grafo_vist = {}

        for no in grafo.keys():
            grafo_dist[no] = int(1e9)
            grafo_vist[no] = False

        no = f'{start[0]}_{start[1]}'
        
        grafo_dist[no] = 0
        grafo_vist[no] = True

        Q = []

        Q.append(no)
        dist = 0
        while Q:
            s = Q.pop(0)
            print(s)
            for vizinhos in grafo[s]:
                if not grafo_vist[vizinhos]:
                    grafo_vist[vizinhos] = True
                    Q.append(vizinhos)

        print(dist)

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
        xmin = 0
        xmax = 0
        ymin = 0
        ymax = 0
        for idx,_ in enumerate(sensors):

            xr = abs(sensors[idx][0]-beacons[idx][0])
            yr = abs(sensors[idx][1]-beacons[idx][1])
            radius.append(xr+yr)
            
            if xmin > (sensors[idx][0]-radius[idx]):
                xmin = sensors[idx][0]-radius[idx]
            if xmax < (sensors[idx][0]+radius[idx]):
                xmax = sensors[idx][0]+radius[idx]
            if ymin > (sensors[idx][1]-radius[idx]):
                ymin = sensors[idx][1]-radius[idx]
            if ymax < (sensors[idx][1]+radius[idx]):
                ymax = sensors[idx][1]+radius[idx]
            
            if xmin > (beacons[idx][0]):
                xmin = beacons[idx][0]
            if xmax < (beacons[idx][0]):
                xmax = beacons[idx][0]
            if ymin > (beacons[idx][1]):
                ymin = beacons[idx][1]
            if ymax < (beacons[idx][1]):
                ymax = beacons[idx][1]

        
        xdim = xmax-xmin+1
        ydim = ymax-ymin+1
        maps = [['.']*(xdim) for _ in range(ydim)]

        for s,b in zip(sensors,beacons):
            maps[s[1]-ymin][s[0]-xmin] = 'S'
            maps[b[1]-ymin][b[0]-xmin] = 'B'

        self.day_14_print_map(maps)



if __name__ == "__main__":
    nday = int(input('Day :'))
    with open(f'.\data\day{nday}','r') as file:
        data = file.read()

    print(f'####### DAY {nday} #######')
    s = Solutions()
    func = f's.day_{nday}(data)'
    eval(func)
