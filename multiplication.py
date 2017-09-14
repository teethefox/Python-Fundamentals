print_me = [str(x) for x in range(1,13)]
print("x\t" + "\t".join(print_me))

a = 1

for y in range(1,13):
    this_row = []
    for a in range (1,13):
        this_row.append(a * y)
        a += 1

    print_row = [str(z) for z in this_row]
    print (str(y) + "\t" + "\t".join(print_row))