'''
def func(item, my_list):
    my_list.remove(item)
    return my_list

l = ["umair", "ali", "khan", "ahmed", "sarah"]
print(func("ali", l))'''

def rem(l,word):
    for item in l:
        l.remove(word)
        return l

l = ["umair", "ali", "khan", "ahmed", "sarah"]
rem(l,"ali")