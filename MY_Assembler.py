def decimalToBinary(n):
    return "{0:b}".format(int(n))


def binToHexa(n):
    num = int(n, 2)
    hex_num = hex(num)[2:]
    return hex_num


# Here change your Opp Code Value
OPPCode={
    "nop":0, "jmp":1, "addi":2, "lw":3, "add":4, 
    "sw":5, "beq":6, "sub":7, "sll":8, "slt":9, "and":10,
}

# ins=input("Enter Your Instruction: ")
readable = open(r"C:\Users\Shahan Ahmed\Downloads\CSE 332\read.txt","r")
wrightable=open(r"C:\Users\Shahan Ahmed\Downloads\CSE 332\write.txt","w")
ins=readable.read()
print(ins)
insList=ins.split()
oppCode=insList[0].lower()
binary=OPPCode[oppCode]
FINALOPP=decimalToBinary(binary).zfill(6) #On my Design OPP Code is 6 Bit so zfill is (6)


# Remove all charecter
insList2=[]
for i in range (1,len(insList)):
    res = ''.join([i for i in insList[i] if i.isdigit()])
    insList2.append(res)
    
print(insList2)
length=len(insList2)
res=""
print(length)
for i in range(0,length):
    if length==3:    
        ret=decimalToBinary(int(insList2[i])).zfill(5) # On my code Rs Rt Rd Imidiate is 5 bit so, zfill (5)
        res=res+ret
    elif length==1:
        ret=decimalToBinary(int(insList2[i])).zfill(15) # On my code JUMP is 15 bit so, zfill (15)
        res=res+ret

MainBinary=FINALOPP+res
MainHex=binToHexa(MainBinary)
wrightable.write("v2.0 raw\n"+MainHex)