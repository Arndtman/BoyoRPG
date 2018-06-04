import re

file1 = open("boyoTest.txt","r")
lines = file1.readlines()
print(lines)
file1.close()


with open('boyoTest.txt', 'r') as fp:
    read_lines = fp.readlines()
    read_lines = [line.rstrip('\n') for line in read_lines]
    print(read_lines)

for item in read_lines:
    var = 0
    if "*" in item:
        print(item)
    else:
        a = lambda x: int(filter(str.isdigit, x) or 0) #re.findall('\d+', x )
        b = re.findall('\d+', item )
        c = int(filter(str.isdigit, item) or 0)
        #print("else: ", item, a(item))
        #print(b)
        if "CLICK" in item:
            print item
            print(" I AM CLICKING NOW")
        elif "w" in item:
            print "w= ", c
            var = c
        elif "d" in item:
            print "d= ", c
            var = c
        elif "s" in item:
            print "s= ", c
            var = c 
        elif "a" in item:
            print "a= ", c
            var = c
        while var!= 0:
            if "CLICK" in item:
                print item
                print(" I AM CLICKING NOW")
            elif "w" in item:
                print "w"
            elif "d" in item:
                print "d"
            elif "s" in item:
                print "s"
            elif "a" in item:
                print "a"
            var -= 1
            
  

s = "1234"
i = int(s)
print i+1
