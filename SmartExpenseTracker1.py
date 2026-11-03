#Project Title: Smart Expense Tracker 💰

print("==============================")
print("    SMART EXPENSE TRACKER     ")
print("==============================")

print("\nCreate your profile")

name = input("\nEnter your name: ").strip().title()
user_id = input("Enter your User Id: ")
budget = float(input("Enter your monthly Budget: "))

if name != "":
    print("\nPROFILE CREATED SUCCESSFULLY! ✅")
    
    print("\nName: ",name)

    unmasked1 = user_id[0:4]
    unmasked2 = user_id[-4:]
    
    masked = "*" * (len(user_id) - 4)
    result = unmasked1 + masked + unmasked2    
    
    print("User Id: ",result)
    
    if budget > 0:
        print(f"Monthly Budget: ₹{budget}")
    else:
        print("\n⚠️ Budget cannot be zero or negative")    
        
else:
    print("\n⚠️ Name cannot be empty. Please try again.")
    
expenses = []

while True:
    
    print("\n")
    print("==============================")
    print("           MAIN MUNE          ")
    print("==============================")

    print("\n1. Create Profile")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Expense Summary")
    print("5. Search by Category")
    print("6. Exit")

    choice = int(input("\nEnter your choice: "))
    
    match choice:
        case 1:
            name = input("\nEnter your full name: ").strip().title()
            user_id = input("Enter youe userId: ")
            budget = int(input("Enter your monthly Budget: "))
            
            if name != "":
                print("\nPROFILE CREATED SUCCESSFULLY! ✅")
    
                print("\nName: ",name)

                unmasked1 = user_id[0:4]
                unmasked2 = user_id[-4:]
    
                masked = "*" * (len(user_id) -4)
                result = unmasked1 + masked + unmasked2    
                
                print("User Id: ",result)
            
                if budget > 0:    
                    print(f"Monthly Budget: ₹{budget}")
                else:
                    print("\n⚠️ Budget cannot be zero or negative") 
                    
            else:
                print("\n⚠️ Name cannot be empty. Please try again.")
                
        case 2:
            
            print("\n---------- ADD EXPENSES ----------")
            
            expense_name = input("\nExpense Name: ").capitalize()
            category = input("Category: ").capitalize()
            date = input("Date (DD-MM-YYYY): ").strip()
            
            if expense_name == "" or category == "" or date == "":
                print("⚠️ Expense name, category, and date cannot be empty!")
                
            else:
                
                try:
                    amount = float(input("Amount: ₹"))
                
                    if amount > 0:
                        new_expenses = {
                            "Expense": expense_name,
                            "Amount": amount,
                            "Category": category,
                            "Date": date
                        }    
                
                        expenses.append(new_expenses)
                        print("\nExpense added successfully! ✅")
                    
                    else:
                        print("⚠️ Amount must be greater than zero!")                
                
                except ValueError:
                    print("⚠️ Invalid amount! Please enter a number.")
            
        case 3:
            total_expenses = 0
            
            print("==============================")
            print("          ALL EXPENSES        ")
            print("==============================")

            print(f"{'Expense':<15}{'Category':<15}{'Amount':<15}{'Date':<10}")
            
            for item in expenses:
                print(f"{item['Expense']:<15}{item['Category']:<15}₹{item['Amount']:<14.2f}{item['Date']:<10}")
                
                total_expenses += item['Amount']
                
            print(f"\nTotal Expenses: ₹{total_expenses:.2f}")
            
        case 4:
            highest = expenses[0]
            
            print("==============================")
            print("        EXPENSE SUMMARY       ")
            print("==============================")
            
            if len(expenses) == 0:
                print("\nNo expenses recorded yet")
            
            else:    
                total = 0
                
                for expense in expenses: 
                    total += expense['Amount']
            
                avg_expense = total / len(expenses)
                
                for expense in expenses:
                    if expense['Amount'] > highest['Amount']:
                        highest = expense
                    
                remaining = budget - total
            
                print("\n")   
                print(f"Total Expenses: ₹{total:.2f}")
                print(f"Average Expense: ₹{avg_expense:.2f}")
                print(f"Highest Expense: {highest['Expense']} (₹{highest['Amount']:.2f})")
                print(f"\nMonthly Budget: ₹{budget:.2f}")
                print(f"Remaining Budget: ₹{remaining:.2f}")
                
            if total > budget:
                print("\nStatus: 🚨 Budget exceeded!")
                
            elif (total >= budget * 0.8):
                print("\nStatus: ⚠️ You are approaching your budget limit")
                
            else:
                print("\nStatus: 👍 Budget under control")
                
        case 5:
            print("==============================")
            print("       SEARCH BY CATEGORY     ")
            print("==============================")
            
            search = input("\nEnter category: ").capitalize()
            
            if search == "":
                print("\nCategory cannot be empty!!")
            
            else:
                found = False
                category_total = 0
                
                print(f"\n========== EXPENSES IN {search.upper()} ==========")
                
                for expense in expenses:   
                     
                    if expense["Category"].capitalize() == search:
                        print(f"\n{expense['Expense']:<15} - {expense['Amount']:<15.2f}")
                        
                        category_total += expense["Amount"]
                        found = True
                        
                        continue
                
                if found:
                        print("------------------------------")
                        print(f"Category Total: ₹{category_total:.2f}")
                else:
                    print("\nNo expenses found in this category.")
                    
        case 6:
            print("\nThank you for using Smart Expense Tracker!")
            print("Goodbye 👋")  
            break
          
        case _:
            print("\nEnter valid choice")