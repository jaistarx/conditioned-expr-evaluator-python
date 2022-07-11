import re

def sec_split(f_arr):
    for i in f_arr:
        s_arr=re.split(" |=",i)
        if(s_arr[0]=="MyInteger"):
            globals()[s_arr[1]] = int(s_arr[2])
        elif(s_arr[0]=="MyString"):
            globals()[s_arr[1]] = s_arr[2]
                
def fir_split(line):
    f_arr=line.split(";")
    sec_split(f_arr)

def main():
    num=1
    while(1):
        line=input("\nEnter line "+ str(num) +" : ")
        check_line=line.split(" ")
        if(check_line[0]=="MyInteger" or check_line[0]=="MyString"):
            fir_split(line)
        else:
            try:
                result=str(eval(line))
                result=result.replace('"','')
                print(result)
            except Exception as e: print(e)
        num=num+1
    
main()