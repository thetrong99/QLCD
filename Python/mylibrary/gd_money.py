
class gd_money():
    def __init__(self,codegd,timegd,sl,ty_pr,rate_pr,mua_ban):
        self.codegd = codegd
        self.time = timegd
        self.sl = sl
        self.rate_pr = rate_pr
        self.ty_pr = ty_pr
        self.m_b  = mua_ban
        self.mua = ""
    def money(self):
        if self.m_b == 1:
            self.mua = "GD Mua"
            return float(self.sl * self.rate_pr)
        else:
            self.mua = "GD Ban"
            return float(self.sl * self.rate_pr*1.05)