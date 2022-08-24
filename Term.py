class Term:
    def __init__(self, coeff, exp):
        self.coeff = coeff
        self.exp = exp

    
    def __add__(self, other):
        if self.exp == other.exp:
            return Term(self.coeff + other.coeff, self.exp)
        else:
            return None

    
    def __mul__(self, other):
        return Term(self.coeff * other.coeff, self.exp + other.exp)
    

    def __sub__(self, other):
        if self.exp == other.exp:
            return Term(self.coeff - other.coeff, self.exp)
        else:
            return None
    

    def __truediv__(self, other):
        return Term(self.coeff / other.coeff, self.exp - other.exp)


    def __eq__(self, other):
        return self.coeff == other.coeff and self.exp == other.exp


    def __ne__(self, other):
        return not self == other


    def plugin(self, number):
        return self.coeff * number ** self.exp


    def __str__(self):
        return f"{self.coeff}x^{self.exp}"