class IIR2Filter:
    def __init__(self, b, _a, len_b, len_a):
        self.a = list(_a)
        self.b = list(b)
        self.len_a = len_a - 1
        self.len_b = len_b

        self.x = list()
        self.y = list()

        self.coeff_b = list()
        self.coeff_a = list()

        self.a0 = self.a[0]
        self._a = self.a[1:]
        for i in range(2 * self.len_b):
            self.coeff_b.append(self.b[(2 * self.len_b - 1 - i) % self.len_b] / self.a0)
        for i in range(2 * self.len_a):
            self.coeff_a.append(self._a[(2 * self.len_a - 2 - i) % self.len_a] / self.a0)

        self.i_b = 0
        self.i_a = 0

    def filter(self, x):
        self.x[self.i_b] = x
        b_terms = 0
        b_shift = self.coeff_b[(self.len_b - self.i_b - 1):]
        for i in range(self.len_b):
            b_terms += self.x[i] * b_shift[i]

        a_terms = 0
        a_shift = self.coeff_a[(self.len_a - self.i_a - 1):]
        for i in range(self.len_a):
            a_terms += self.y[i] * a_shift[i]

        filtered = b_terms - a_terms
        self.y[self.i_a] = filtered
        self.i_b += 1
        if self.i_b == self.len_b:
            self.i_b = 0
        self.i_a += 1
        if self.i_a == self.len_a:
            self.i_a = 0

        return filtered
