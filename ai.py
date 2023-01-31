file  = open("data.txt","r",encoding = "utf-8")

for i in file.readlines():
    index_str = (i.find(":"))
    a ="\"" + ((i[:index_str] + "\"" + i[index_str:]))
    z = a[:index_str + 4] + "\"" + a[index_str + 4:]
    print(z.strip() + "\"" + ",")