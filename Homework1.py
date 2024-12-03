import datetime

def get_current_datetime():
    current_datetime=datetime.datetime.now()
    formatted_datetime=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return  formatted_datetime
print("Current Date and Time: ", get_current_datetime())
      
try:
    divied=int(input("Enter a divied:"))
    divisor=int(input("enter a diviosr:"))
    result=divied/divisor 
    print(result)
except:
    print("error occur")
finally:
    print("Program executed successfully!!!")






