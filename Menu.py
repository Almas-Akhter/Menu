n=int(input("How many customers list you want to:"))

cust={}

for i in range(n):

    print("Enter details of", i+1," customer:")

    name=input("Enter name of customer:")

    cname=name.lower()

    pn=int(input("Enter Phone number:"))

    cust [cname]=pn

c=0

while True:

    print('''

    1. Show record

    2. Add new customer

    3. Delete a customer

    4. Search record

    5. Update record

    6. Exit

    ''')

    c=int (input("Enter your choice:"))

    if c==1:

        for i in cust:

           print (i, ":", cust[i])

        elif c==2:

           print("Enter details of new customer:")

           cname=input("Enter name:")

           pn=int(input("Enter phone number: "))

           cust[cname] = pn

       elif c==3:

           n=input("Enter name to be deleted:")

           nm=n.lower()

           f=cust.pop (nm,-1)
          if f!==1:

               print (f, " is deleted successfully.")

          else:

               print (f, "not found.")

      elif c==4:

          n=input("Enter Customer Name:")

          name=n.lower()

          if name in cust:

               print (name, "found in the record.")

          else:

              print (name, "not found in the record.")

     elif c==5:

          cname=input("Enter Customer Name:")

          pn=int(input("Enter phone number to modify:"))

          cust [cname] =pn

     elif c==6:

          print("Goodbye") 
          break
