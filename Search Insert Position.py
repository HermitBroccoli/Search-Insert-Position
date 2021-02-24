l = [1,3,5,6]
target = int(input())

def y(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i

        else:
            for y in range(len(l)):
                if l[y] == target:
                    q = 1
                else:
                    q = 0    

            if q == 0:
                l.append(target)
            else:
                l = sorted(l)

            l = sorted(l)
            for j in range(len(l)):
                if l[j] == target:
                    return j   

print(y(l, target))