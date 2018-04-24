print "Please enter your name:"
name = raw_input(">")

print "Welcome to Tradeshift %s!" % name

age = int(raw_input("Enter your age"))

while age < 5:
	print " Adding age"
	age = age + 1


total = 0
for num in range(101):
	total = total + num
print total


print "MY name is"
i = 0
while i <5:
	print 'Arief five times (' + str(i) + ').'
	i = i + 1

while True:
	print "Please enter your name:"
	name = raw_input(">")
	if name == "Your name":
		break
print "Thank you"
