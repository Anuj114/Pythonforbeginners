# with open(r"C:\Users\HP\PycharmProjects\pythonforbeginners\myfile.txt","a+") as file:
#     line_num = 1
#     for line in file.readlines():
#         print(f'{line_num}. {line.rstrip()}')
#         line_num += 1
#     file.write("\nI am adding 4th line as well")
#     file.seek(0)
#     print(file.read())

animals_list = []
with open(r"C:\Users\HP\PycharmProjects\pythonforbeginners\animals.txt") as file:
    for animal in file.readlines():
        print(animal.rstrip())
        animals_list.append(animal.rstrip())
with open(r"C:\Users\HP\PycharmProjects\pythonforbeginners\sorted_animals.txt","w") as sorted_file:
    for animal in sorted(animals_list):
        sorted_file.write(animal+"\n")