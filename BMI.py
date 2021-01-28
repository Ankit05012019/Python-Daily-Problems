## BMI claculator

class MassHeight:

    def __init__(self,height,mass):

       self.height=height
       self.mass=mass

    def __str__(self):

        return f"Your height is {self.height} and weight is {self.mass}"

    def bmi(self):

        ans=self.mass/(self.height*self.height)
        return ans


if __name__== "__main__" :

    checking = "yes"
    while True:

        ht=input("Enter you height in meters ")
        mass=input("Enter your height in kg  ")

        obj=MassHeight(float(ht),float(mass))
        print(obj)
        BMI=obj.bmi()

        print(f"you BMI is {BMI}")

        while True:
           checking=input("do you want to try again(yes/y/no/) ")
           if checking.lower() == "yes" or checking.lower() == "y":
               continue
           elif checking.lower() == "no" or checking.lower() == "n":
               print ("Thank You!!")
               break
           else:
                print("please provide a valid input")
