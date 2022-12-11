"""Solution of Advent of Code 2022."""

class Solutions(object):
    """One funciton per day."""
    def __init__(self, data):
        """Initialize."""
        self.dict_function = {}
        self.dict_function['day_1'] = self.day_1(data)


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
         


if __name__ == "__main__":
    nday = input('Day :')
    with open(f'day{nday}','r') as file:
        data = file.read()
    s = Solutions(data)
    s.dict_function[f'day_{nday}']
