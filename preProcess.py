def prePorcess():
    print "Ten minutes later...."
    return [1,2,3,4,5]

def myFunction(x):
    return  [ y**2 for y in x]
    


x =  prePorcess()
print myFunction(x)