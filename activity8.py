import csv



class Customer:

    def __init__(self,ID,firstName,lastName,company,address,city,state,zip,cust_list):
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def getAddress(self):
        return self.address



def display_title():
    print("Customer Viewer")


def csv_reader():
      cust_list = []
      with open("customers.csv", newline="") as file:
          reader = csv.reader(file)
          for row in reader:
            cust_list.append(row)
      return cust_list


def find_customer(cust_id,cust_list):
      for row in cust_list:
        if row[0] == cust_id:
            print(row[1]+" "+ row[2])
            print(row[4])
            print(row[5] + "," +row[6] + " "+ row[7])
            return cust_id



def main():
    display_title()
    cust_list = csv_reader()
    cust_id = str(input("Enter Customer ID:"))
    find_customer(cust_id, cust_list)

    while True:
        choice = input("Continue?y/n: ")
        if choice.lower() == "y":
           cust_id = str(input("Enter Customer ID:"))
           id = find_customer(cust_id,cust_list)
           if id == None:
               print("No customer with that specified ID.")
        else:
           break
    print("Bye!")



if __name__ == '__main__':
    main()




