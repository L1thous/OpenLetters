#所需调用函数
def output(a,st=[]):#覆盖题目函数
    b=list(str(a))
    c=[]
    for i in b:
        if i==" ":
            c.append(" ")
        elif i in st:
            c.append(i)
        else:
            c.append("*")
    return c
def gs(st,inp):#大小写转换函数
    st.append(inp)
    if inp.isalpha():
        a=chr(ord(inp)-32)
        b=chr(ord(inp)+32)
        if a.isalpha():
            st.append(a)
        elif b.isalpha():
            st.append(b)
def sum(s):#求和用函数
    n=0
    for i in s:
        n+=i
    return n
def e_n(i_s,char):#检测输入用函数
    if i_s.startswith(char):
        return i_s[1:]
    return None
#初始化
Song=[]#曲库
st=[]#已开
showst=[]#已开显示
#导入题库
cho=int(input("输入1手动导入,输入2自动导入:"))
if cho==1:
    npr=int(input("输入题目数："))
    intro=input("输入简介：")
    print("依次输入题目：")
    for i in range(npr):
        k=input()
        Song.append(k)
elif cho==2:
    fil=input("输入txt文件名,无需txt后缀:")
    with open(f"{fil}.txt","r",encoding="utf-8") as f:
        intr=f.readline()
        intro=intr.strip("\n")
    with open(f"{fil}.txt","r",encoding="utf-8") as f:
        al=list(f.readlines())
        npr=len(al)-1
        for i in range(1,npr+1):
            le=al[i]
            k=le.strip("\n")
            Song.append(k)
sg=[0]*npr
#开字母区
print("guessed:",end="")
for i in showst:
    print(i,end="")
print()
print(intro)
for i in range(1,npr+1):
    print(i,end="")
    print(".",end="")
    m=output(Song[i-1],st)
    for f in m:
        print(f,end="")
    print()
while sum(sg)<npr:
    print("进行操作：",end="")
    ans=input()
    if len(ans)==1:
        gs(st,ans)
        showst.append(ans)
    elif str(ans)==str("rev"):
        Songtem=[0]*npr
        sgtem=[0]*npr
        print("开始重置......")
        for i in range(npr):
            print("第",i+1,"题新序号：",end="")
            s=int(input(""))
            Songtem[s-1]=Song[i]
            sgtem[s-1]=sg[i]
        Song=Songtem
        sg=sgtem
    else:
        result_1=e_n(ans,"@")
        result_2=e_n(ans,"!")
        if result_1 is not None:
            sg[int(result_1)-1]=1
        elif result_2 is not None:
            k=int(input("插入位置序号："))
            Song.insert(k-1,result_2)
            sg.insert(k-1,0)
            npr+=1
        else:
            jud=0
            for i in range(npr):
                if Song[i]==ans:
                    sg[i]=1
                    jud+=1
            if jud==0:
                print("Wrong!")
    print()
    print("guessed:",end="")
    for i in showst:
        print(i,end="")
    print()
    print(intro)
    for i in range(1,npr+1):
        print(i,end="")
        print(".",end="")
        m=output(Song[i-1],st)
        num=0
        for j in m:
            if j=="*":
                num+=1
        if num==0:
            sg[i-1]=1
            print(Song[i-1],end="")
        elif sg[i-1]==1:
            print(Song[i-1],end="")
        else:
            for f in m:
                print(f,end="")
        print()
input("恭喜完成！")
