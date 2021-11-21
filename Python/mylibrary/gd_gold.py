
class gd_gold():
    def __init__(self,codegd,timegd,sl,ty_pri,ord_pr):
        self.codegd = codegd
        self.time = timegd
        self.sl = sl
        self.ord_pr = ord_pr
        self.ty_pri = ty_pri
    def gold(self):
        return self.sl * self.ord_pr