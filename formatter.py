file  = open("data.txt","r",encoding = "utf-8")

for i in file.readlines():
    index_str = (i.find(":")) #finds ":" (without quotes) in string 
    a ="\"" + ((i[:index_str] + "\"" + i[index_str:])) #adds " to both start and end, and to content before ":"
    z = a[:index_str + 4] + "\"" + a[index_str + 4:] #adds " to content after ":"
    print(z.strip() + "\"" + ",") #prints the formatted text, add new code if you want output in file
