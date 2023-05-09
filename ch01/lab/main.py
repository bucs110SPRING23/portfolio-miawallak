import random 
#Part A
weeks = 16
print(weeks, "weeks")
classes = 5
print(classes, "classes")
tuition = 6000
print(tuition, "tuition")
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 4
print(classes_per_week, "classes_per_week")
cost_per_class = (cost_per_week / classes_per_week)
print("Cost per class:", cost_per_class)

#Part B
mycolors = ["Green", "Purple", "Yellow", "Blue", "Red"]
myvar = random.choice(mycolors) 
print(myvar)
