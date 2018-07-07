# This is a simple program
name=(input("enter your name:"))
print("hello...."+" "+name+"  "+"\n please fill the fields")
salary=float(input("enter your salary:"))
bonus=float(salary/5)
total=(salary+bonus)
month=int(input("enter how many months:"))
get=float(total)*float(month)
print(name+"  "+"congratulations..!\n you get"+" "+str(get)+" "+"rupees for  "+str(month)+"months")
