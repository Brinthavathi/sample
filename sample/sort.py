week=['sunday','monday','tuesday','wednesday','thursday','friday']
month=['jan','feb','mar','apr','may','june','july','aug','sep','act','nov','des']
adding=week+month
adding.sort()
print(adding)
adding.reverse()
print(adding)
adding.sort(reverse=True)
print(adding)
remove=adding[0:3]
del adding[0:3]
print(adding)
lastAdd=adding+remove
print(lastAdd)

