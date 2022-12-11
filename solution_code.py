"""Solution of Advent of Code 2022."""

class Solutions(object):
    """One funciton per day."""
    def __init__(self, data):
        """Initialize."""
        self.dict_function = {
            'day_1': self.day_1,
            'day_2': self.day_2,
            'day_3': self.day_3}


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


if __name__ == "__main__":
    nday = int(input('Day :'))
    with open(f'day{nday}','r') as file:
        data = file.read()

    print(f'####### DAY {nday} #######')
    s = Solutions(data)
    s.dict_function[f'day_{nday}'](data)
