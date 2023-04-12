import random


class Pass():
    def __init__(self, numbers, symbols, caps, lower):
        self.letters_caps = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K',
                             'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
        self.letters_lower = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k',
                              'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
        self.numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        self.symbols_list = ['!', '#', '$', '%', '&', '?', '*', '+', '_', '-', '@']
        self.new_pass = []
        self.numbers = numbers
        self.symbols = symbols
        self.caps = caps
        self.lower = lower

    def generate_N(self):
        for x in range(int(self.numbers)):
            num = random.choice(self.numbers_list)
            self.new_pass.append(num)
        for y in range(int(self.symbols)):
            sym = random.choice(self.symbols_list)
            self.new_pass.append(sym)
        for i in range(int(self.caps)):
            let = random.choice(self.letters_caps)
            self.new_pass.append(let)
        for p in range(int(self.lower)):
            low = random.choice(self.letters_lower)
            self.new_pass.append(low)
        random.shuffle(self.new_pass)
        np = ''.join(self.new_pass)
        return np
