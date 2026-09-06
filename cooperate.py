class Employee:
    count=0
    def __init__(self,work,salary):
        self.work=work
        self.salary=salary
        Employee.count += 1
    def get_work(self):
        print(f"My work is {self.work}")
    def get_salary(self):
        print(f"My salary is {self.salary}")
    def bonus(self):
        return  self.salary*0.1

class Manager(Employee):
    def __init__(self,work,salary,team_size):
        super().__init__(work,salary)
        self.team_size=team_size
    def get_team_size(self):
        print(f"My team size is {self.team_size}")  #capacity of team
        print(f"Total employees created so far: {Employee.count}") # actual number of employees created so far
    def bonus(self):
        return super().bonus()*2

class Ceo(Manager):
    def __init__(self, work, salary, team_size):
        super().__init__(work, salary, team_size)
    def bonus(self):
        return super().bonus()*3

e1=Employee("Software Development", 50000)
e2=Employee("Data Analysis", 60000)
e3=Employee("Project Management", 70000)
e4=Employee("Quality Assurance", 55000)

m1=Manager("Team Management", 80000, 10)
c1=Ceo("Executive Leadership", 100000, 10)

e1.get_work()
e2.get_work()
e3.get_salary()

m1.get_work()
m1.get_team_size()
print(m1.bonus())

c1.get_work()
print(c1.bonus())

c1.get_team_size()

