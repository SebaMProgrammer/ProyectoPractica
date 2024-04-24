def simplifica(self):
    d=self.mcd(self.num,self.den)
    self.num=int(self.num/d)
    self.den=int(self.den/d)