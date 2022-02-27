def get_users_amount(string):
    # this is where i ask the user the amount they are willing to pay
    while True:
        # validation and we round the users input to 2 decimal place
        try:
            amount = round(float(input(string)), 2)
            return amount
        except ValueError:
            print("The amount should be a number")
            continue


def main_executer():
    total_budget = 0
    numbers_used_for_priority_list = []
    shop_names = []
    product_names = []
    has_items_been_bought = []
    amount_willing_to_pay_for_items = []
    quantity_needed_for_each_item = []
    priority_of_each_item = []
    repeat = True
    while repeat:
        shop_name = input("Enter the shops name\n")
        shop_names.append(shop_name)
        product_name = input("Enter the products name\n")
        product_names.append(product_name)
        has_item_been_bought = False
        while not has_item_been_bought:
            is_item_bought = input(
                "Have you bought the product, YES or NO\n").upper()
            if is_item_bought == "YES" or is_item_bought == "NO":
                has_item_been_bought = True
                has_items_been_bought.append(is_item_bought)
                amount_willing_to_pay_for_item = get_users_amount(
                    "Enter the amount you are willing to pay for the item\n")
                amount_willing_to_pay_for_items.append(
                    amount_willing_to_pay_for_item)
                valid_quantity_input = False
                while not valid_quantity_input:
                    quantity_needed = input("How many do you want\n")
                    if quantity_needed.isnumeric() and int(quantity_needed) >= 1:
                        valid_quantity_input = True
                        quantity_needed_for_each_item.append(
                            int(quantity_needed))
                        valid_priority_input = False
                        while not valid_priority_input:
                            priority_of_item = input(
                                "What is the priority of this item\n")
                            if priority_of_item.isnumeric() and priority_of_item not in numbers_used_for_priority_list and int(priority_of_item) >= 1:
                                valid_priority_input = True
                                priority_of_each_item.append(priority_of_item)
                                numbers_used_for_priority_list.append(
                                    priority_of_item)
                                valid_choice = False
                                while not valid_choice:
                                    print(
                                        "Press 1 if you want to continue writing your shopping list")
                                    print(
                                        "Press 2 if you want to stop and see your shopping list")
                                    users_choice = input(
                                        "Which number do you choose\n")
                                    if users_choice == "1":
                                        valid_choice = True
                                        continue
                                    elif users_choice == "2":
                                        valid_choice = True
                                        repeat = False
                                        for index in range(0, len(amount_willing_to_pay_for_items)):
                                            if has_items_been_bought[index] == "YES":
                                                continue
                                            else:
                                                total_budget += (
                                                    amount_willing_to_pay_for_items[index] * quantity_needed_for_each_item[index])
                                                continue
                                        print(total_budget)
                                        for index in range(0, len(amount_willing_to_pay_for_items)):
                                            print("Shops name:", shop_names[index], product_names[index], has_items_been_bought[index],
                                                  amount_willing_to_pay_for_items[index], quantity_needed_for_each_item[index], priority_of_each_item[index])
                                            pass
                            else:
                                print(
                                    "Invalid input it has to be a number that you have not used")
                    else:
                        print("Invalid input")
            else:
                print("Either type 'YES' or 'NO'")


main_executer()
