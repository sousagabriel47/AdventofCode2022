"""Solution of Advent of Code 2022."""

class Solutions(object):
    """One funciton per day."""
    def __init__(self, data):
        """Initialize."""
        self.dict_function = {
            'day_1': self.day_1(data),
            'day_2': self.day_2(data)}


    def day_1(init, data):
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

    def day_2(init, data):
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
        turns = data.split()
        for turn in turns:
            sum_score += score[turn] + bonus[turn[2]]

        print(f'Total Score: {sum_score}')

if __name__ == "__main__":
    nday = int(input('Day :'))
    with open(f'day{nday}','r') as file:
        data = file.read()

    print(f'####### DAY {nday} #######')
    s = Solutions(data)
    s.dict_function[f'day_{nday}']
