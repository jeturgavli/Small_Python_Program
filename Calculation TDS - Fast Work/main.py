from prettytable import PrettyTable

def say_amount(amount):
    return round(amount)

while True:
    print("Type 'exit' to exit ")
    user_input = input("Enter Amount : ")
    if user_input.lower() == 'exit':
        print("Program exited.")
        break
    
    amount = int(user_input)

    tds = round(amount * 0.01)
    sgst_cgst = tds * 2
    netcheck_amount = amount - tds - sgst_cgst
    say_netcheck_amount = say_amount(netcheck_amount)

    table = PrettyTable()
    table.field_names = ["Description", "Amount"]
    table.add_row(["TDS", tds])
    table.add_row(["SGST 1% + CGST 1%", sgst_cgst])
    table.add_row(["Netcheck Amount", netcheck_amount])
    table.add_row(["SAY", say_netcheck_amount])

    print(table)
