def add_element(data_structure,element):
    data_structure.append(element)
    return data_structure

def remove_element(datastructure,element):
    if element in datastructure:
        datastructure.remove(element)
    else :
        print(f"{element} not found in the datastructure")

my_list =[]
add_element(my_list, 10)
print(my_list)

remove_element(my_list,3)


x = 1 
x =x>5
print(x)