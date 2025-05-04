def hello ():
    print ("Hello AkiraChix")

# hello()

def say_hello(name):
    print(f"Hello {name}")

def great (name,age):
    year = 2025 - age
    print(f"Hello {name}, born in {year}")

def greatings(names):
    for name in names:
        print(f"Hello {name}")

def year_of_birth(name,age):
    year = 2025 - age
    print(f"Hello {name}, born in {year}")


def my_country(name ="Uganda"):
    print(f"I Love my country {name}")

def welcome_student(**kwarys):
    print(kwarys)

def create_sentense(**words):
    sentense = " "
    for word in words.values():
        sentense+=word
        sentense += " "
    return sentense

def exam_result(*args,**kwargs):
    name = kwargs.get("name")
    course = kwargs.get("course")

    if not name:
        name = "student" 
    if not args:
        print(f"Hello {name}, we don't have your results for {course}")
    else: 
         sum = 0
         for number in args:
                            sum+=number
                            average = sum / len(args)
         return f"Hello {name}, your average score for {course} is {average}"
  

# exam_result(60,70,80, name = "Jane", course = "Backend")
# exam_result(50, course = "Backend")
# exam_result(name = "Jane", course = "Mobile")