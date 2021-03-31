largest = None
smallest = None
nlist = list()

while True:
    num = raw_input("Enter a number: ")
    if num == "done":
        break
    try:
        numi = float(num)
        nlist.append(numi)
    except:
        print('Invalid input')
        continue

largest = max(nlist)
smallest = min(nlist)

print("Maximum", largest)
print("Minimum", smallest)
