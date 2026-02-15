#Q4

monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

monday_class.add("Grace")

both_classes = monday_class & wednesday_class
either_class = monday_class | wednesday_class
only_monday = monday_class - wednesday_class
only_one_class = monday_class ^ wednesday_class

is_subset = monday_class <= either_class

print("Monday class:", monday_class)
print("Wednesday class:", wednesday_class)
print("Attended both classes:", both_classes)
print("Attended either class:", either_class)
print("Only Monday:", only_monday)
print("Only one class (not both):", only_one_class)
print("Is Monday subset of all students?", is_subset)
