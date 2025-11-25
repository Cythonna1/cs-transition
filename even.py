nums=list(range(1,31))
evens=[]
odds=[]


for n in nums:
   if n % 2 == 0:
    evens.append(n)

   else:
    odds.append(n)


print ("Evens: ", evens)
print ("Odds: ", odds)