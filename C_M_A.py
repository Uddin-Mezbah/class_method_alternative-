class Employee:
    no_of_leavs = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The name is {self.name} salary is {self.salary} and role is{self.role}"

    @classmethod
    def change_leaves(cls,newleavs):
        cls.no_of_leavs = newleavs

    @classmethod
    def from_str(cls,string):
       # parms = string.split("-")
       # print(parms)
       # return cls(parms[0],parms[1],parms[2])

        return cls(*string.split("-"))





davide = Employee("davide",400,"Instructor")
harry = Employee("harry",500,"student")
wasim = Employee.from_str("wasim-490-student")

print(wasim.salary)
harry.change_leaves(34)

#Employee.no_of_leavs = 89
print(harry.no_of_leavs)
