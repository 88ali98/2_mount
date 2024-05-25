#1
# class Computer:
#     def __init__(self, cpu, memory):
#         self.__cpu = cpu
#         self.__memory = memory

#     @property
#     def cpu(self):
#         return self.__cpu
#     @property
#     def memory(self):
#         return self.__memory
#     def __make_computations(self):
#         print(f"""Резюльтат сложения {self.cpu+self.memory}
#                   Резюльтат вычисления {self.cpu-self.memory} 
#                   Резюльтат умнажение {self.cpu*self.memory}
#                   Резюльтат деления {self.cpu/self.memory}""")
        

#     @property
#     def make_computations(self):
#         return self.__make_computations
    

# computer = Computer(134112433, 140)
# computer.make_computations()

# class Laptop(Computer):#2
#     def __init__(self, cpu, memory, memory_card):
#         super().__init__(cpu, memory)
#         self.__memory_card = memory_card

#     @property
#     def memory_card(self):
#         return self.__memory_card
#     def info(self):
#         print(f"процессор - {self.cpu}, память - {self.memory}, карта памяти - {self.memory_card}")

# laptop = Laptop(124, 500, 75)
# laptop.info()

