from mylibrary.lib_qlcd import *
out = []
lst = {'sumpr': 0 }
def pr():
    ncd = input("Nhap ten CD : ")
    nsg = input("nhap ten ca sy: ")
    num = input("nhap so bai hat: ")
    pr = input ("nhap gia thanh : ")
    a = lib_qlcd(ncd,nsg,num,pr)
    out.append(a)
    lst["sumpr"] += int(pr)
    print("--- danh sach CD ---")
    for i in out:
        print("# %s - %s - %s - %d"%(str(i.ncd),str(i.nsg),str(i.num),int(i.pr)))
    print("Tong gia thanh: " + str(lst["sumpr"]))
        
def main():
    print("thong tin CD: ")
    pr()
    while True:
        tt = int(input("tiep tuc nhap (1-co 0-khong): "))
        if tt == 1:
            pr()
        else:
            break;
        
if __name__=='__main__':
    main()

    
