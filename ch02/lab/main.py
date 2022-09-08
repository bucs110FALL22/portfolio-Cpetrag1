import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 2
cost_per_class = cost_per_week/classes_per_week
print("This is how much each class costs: " + str(cost_per_class))

#Part B
list = [1,2,3,4,5]
print("random choice: " + str(random.choice(list)))