print("============This is Our Room===========")
list=['sanaulla','madhu','mani','ravi','Prasad Rao']
print("we have to know how many members in the room")
print("-----------Monthly PAYABLE AMOUNT PER EACH MEMBER IN THE ROOM----------")
rent=int(input("enter amount for the room rent per momth:"))
rent_amount=float(rent/6)
curry=int(input("enter amount for the curries per month:"))
curry_amount=float(curry/6)
power=int(input("enter amountof power bill per month:"))
power_bill=float(power/6)
total=float(rent_amount+curry_amount+power_bill)
print("the rent amount is RS."+str(rent_amount)+"\n the curry amount is RS."+str(curry_amount)+"\nthe power bill is RS. "+str(power_bill))
print("total amount for each person"+" RS."+str(total)+"\n happy ENJOY....!")

