import random
class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50
    def get_home(self):
        self.home = Home()
    def get_home(self):
        self.home = Home()
    def get_car(self):
        self.car = Auto(brands_of_car)
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = job(job_list)
        def eat(self):
         if self.home.food <=0:
            self.shopping("food")
         else:
             self.satiety >=100
             self.satiety = 100
             return
         self.satilety += 5
         self.satilety -= 5
def work(self):
    if self.car.drive():
        pass
    else:
        if self.car.fuel < 20:
            self.shopping("fuel")
            return
        else:
            self.to_repair()
            return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satilety -= 4
    def to_repair(self):
        pass
    def chill(self):
        pass
    def clean_home(self):
        pass
def day_indexes(self,day):
    dav = f"Today the {day} ot {self.name} s life"
    print(f"{day:=^50}", "/n")
    human_indexes = self.name + "s indexes"
    print(f"{human_indexes:^50}", "/n")
    print(f"Money + {self.money}")
    print(f"Satiety - {self.satiety}")
    print(f"Gladness - {self.gladness}")
    print(f"{"Home indexes"}:^50", "/n")
    print(f"Food - {self.home.food}")
    print(f"Mess {self.home.mess}")
    car_indexes = f"{self.car.brand} car indexes"
    print(f"{car_indexes:^50}", "/n")
    print(f"Fue {self.car.fuel}")
    print(f"Strenght - {self.car.strenght}")
    def is_alive(self):
        if self.gladness <0:
           print("Depression")
           return False
        if self.satiety <0:
            print("Dead")
        return False
    if self.money <-500:
        print("Bankrupt")
        return False
    def live(self,day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get.car()
            print(f"I dont have a job, I m going to get a job{self.job.job} with Salary {self.days_indexes(day)}")
dice = random.randint(1,4)
if self.satiety <20:
    if self.home.mess > 15:
        print("I wanna chill, but i have to clean the house")
    else:
        print("Let s chill")
        self.chill()
    elif self.money < 0:
       print("Started to work!")
       self.to_repair()
elif dice == 2:
    print("time to work")
    self.work()
elif dice == 3
    print("Cleaning time")
    self.clean_home()
elif dice == 4
    print("Time for shopping")
    self.shopping(manage= "delicates")
    class Auto:
        pass
    class House:
        pass
    class job:
        pass
    job_list = {
        "Java developer": {"salary": 50, "gladness_less": 10},
        "C++ developer": {"Salary": 70, "gladness_less": 20},
        "Python developer": {"salary": 40, "gladness_less": 50},
        "Rust developer" :{"salary": 60, "gladness_less": 40}
    }
    brands_of_car = {
        "BMW": {"fuel": 100, "strenght": 100, "consumption": 8},
        "LADA": {"fuel": 80, "strenght": 40, "consumption": 12},
        "VOLVO": {"fuel": 60, "strenght": 150, "consumption": 6},
        "FORD": {"fuel": 50, "strenght": 120, "consumption": 9},
    }
    nick =Human("Nick")
    for day in range(1,8):
        if nick.live(day) == False:
            break