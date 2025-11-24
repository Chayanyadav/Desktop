 # filght booking program
import random

print(" domestic/international")
dist=(input())



def domestic():
 if dist=="domestic":
  print("Enter Starting Point:")
  start=input()
  print("Enter destination")
  dest=input()
  print("enter ticket/seat preference:")
  print("Economy class")
  print("Premium Economy class")
  print("Business class")
  pref=input()
  print("Enter trip preference")
  print("one way / round trip")
  trip=input()
  print("Enter Date")
  date=input()
  print("----------------------------------------------------")

  print("Your ticket is successfully booked. ")

  print("-----------------------------------------------------")
  print("From:" + " " + start + " " + "To:" +" " + dest) 
  print("Date")
  print(date)
  print("Seat number:")
  print(random.randint(1,100))
  print("Seat type:")
  print(pref)
  print("Price:INR")
  print(random.randint(2700,15000))
  print(trip)



domestic()



def international():
 if dist=="international":
  print("Enter Starting Point:")
  start=input()
  print("Enter destination:")
  dest=input()
  print("enter ticket/seat preference:")
  print("Economy class")
  print("Premium Economy class")
  print("Business class")
  pref=input()
  print("Enter trip preference:" )
  print("one way / round trip")
  trip=input()
  print("Enter Date:")
  date=input()
  print("----------------------------------------------------")

  print(" Your ticket is successfully booked. ")

  print("-----------------------------------------------------")
  print("From:" + " " + start + " " + "To:" + " "+ dest) 
  print("Date:")
  print(date)
  print("Seat number:")
  print(random.randint(1,100))
  print("Seat type:")
  print(pref)
  print("Price:INR")
  print(random.randint(65000,200000))
  print(trip)


international()




print("---------------------------------------")