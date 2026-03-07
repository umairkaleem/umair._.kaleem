def tables(n):
    table = ""
    for i in range (1,11):
       table += f"{n} x {i} = {n*i}\n"
    with open("tables/table_of_{n}.txt") as f:
        f.write(table)
        

for i in range (2,6):
    tables(i)