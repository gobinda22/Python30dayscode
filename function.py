def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

l1 = [1,2,3,4,5]
flist = list(filter(lambda x: (x%2!=0),l1))#filter with lamda function
print(flist)


