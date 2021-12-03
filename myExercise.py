import sys
student = {}
file = open(sys.argv[1], "r", encoding="utf-8")

for i in file:
    name = i.split(":")[0]
    student[name] = i.split(":")[1].split(",")

try:
    for j in sys.argv[2].split(","):
        a = student[j][0]
        b = student[j][1]
        print("Name:"+str(j)+"\nUniversity:"+str(a)+"\nDepartment:"+str(b))

except KeyError:
    print("\nNo record of '{}' was found".format(j))
except IndexError:
    print("\nCould not find {}'s university or department".format(j))