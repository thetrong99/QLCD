from mylibrary.gd_gold import * 
from mylibrary.gd_money import * 
gold = []
money = []
def inp():
    codegd = input("Nhap ma giao dich : ")
    time = input("Nhap ngay giao dich: ")
    sl = input("Nhap so luong: ")
    chose_gd = int(input("chon loai giao dich: (1-Vang  2-Tien): "))
    
    if chose_gd == 1:
        ty_pri = input("chon loai 18k / 24k / 9999: ")
        ord_pr = input("Nhap don gia: ")
        
        a = gd_gold(codegd,time,int(sl),ty_pri,int(ord_pr))
        gold.append(a)
        sumg = 0
        for i in gold:
            print("%s - %s - %s - %d -%d - Thanh tien: %d "\
                %(i.codegd,i.time,i.ty_pri,i.sl,i.ord_pr,i.gold()))
            sumg += i.gold()
        print("Tong so tien: "+ str(sumg))

    else:
        ty_pr = input("Chon loai USD / EUR / AUD: ")
        rate_pr = int(input("Nhap ty gia: "))
        mua_ban = int(input("Ban mua hay ban? (1-mua 0-ban): "))
        b = gd_money(codegd,time,int(sl),ty_pr,rate_pr,mua_ban)
        money.append(b)
        summ = 0
        for i in money:
            print(i.mua + ": %s - %s - %s - %d -%d - Thanh tien: %.3f "\
                %(i.codegd,i.time,i.ty_pr,i.sl,i.rate_pr,i.money()))
            summ += i.money()
        print("Tong so tien: " + str(summ))

def main():
    print("Quan ly giao dich : ")
    inp()
    while True:
        t = int(input("tiep tuc nhap (1-co 0-khong): "))
        if t == 1 :
            inp()
        else:
            break;
if __name__ == '__main__':
    main()
