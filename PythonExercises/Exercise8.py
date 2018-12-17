print("Exercise 8 \n")

a = [5, 10, 15, 20, 25]
print("(a)", a, "Created a list")

print("(b) Set b = a" )
b = a

print("(c) Set b[1]")
b[1] = 88

print("(d)", a, "Changes made in list b are also made in list a")

print("(e) Set c = a[:]")
c = a[:]

print("(f) Set c[2]")
c[2] = 77

print("(g)", a, "Nothing has happened to a after changes in list c")

def set_first_elem_to_zero(list):
    list[0] = 0
    return 1

set_first_elem_to_zero(a)
print("After running set_first_elem_to_zero on list a the first element changes to 0")
