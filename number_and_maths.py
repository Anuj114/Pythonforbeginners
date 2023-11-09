# hosting_charges_per_hour = 0.51
# per_day = hosting_charges_per_hour * 24
# per_month = per_day * 30
# print("charges per day", str(per_day))
# print("charges per month", str(per_month))
#
# savings = 918
#
# twenty_servers_per_day = per_day * 20
# twenty_servers_per_month = per_month * 20
# days_in_savings = savings/per_day
#
# print(twenty_servers_per_day)
# print(twenty_servers_per_month)
# print(days_in_savings)

# distance = int(input("How far you want to travel in miles: "))
# if distance < 3 :
#     print("I suggest walk to your destination")
# elif distance >= 3 and distance <= 300:
#     print("I suggest drive to your destination")
# else:
#     print("I suggest fly to your destination")

# tasks_list = []
#
# task = input("Enter a task you want to add in your to-do list. Press Enter when done: ")
# while len(task) != 0:
#     tasks_list.append(task)
#     print("Task added successfully")
#     task = input("Enter a task you want to add in your to-do list. Press Enter when done: ")
# print(tasks_list)

# fact_dict = {}
# fact_dict["jeff"] = "fear of clown"
# fact_dict["David"] = "can make food"
# fact_dict["Jason"] = "can fly aeroplane"
#
# print(fact_dict)
#
# fact_dict["jeff"] = "fear of heightd"
# fact_dict["David"] = "can swim"
# fact_dict["Jason"] = "can sing"
# fact_dict["Anuj"] = "a musician"
#
# print(fact_dict)

# airport_list = [("O’Hare International Airport" , "ORD"),
#                 ("Los Angeles International Airport", "LAX"),
#                 ("Dallas/Fort Worth International Airport", "DFW"),
#                 ("Denver International Airport", "DEN")]
#
# for name, code in airport_list:
#     print(f'the code for {name} is {code}')

name = "Anuj Bhardwaj"
for i in range(len(name)-1, -1, -1):
    print(name[i])
