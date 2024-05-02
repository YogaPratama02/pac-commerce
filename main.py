from tabulate import tabulate
from math import sqrt



class Membership:
    # inisialisasi data
    data = {
        "Belle": "Platinum",
        "Ana": "Gold",
        "Cahya": "Platinum"
    }

    def __init__(self, username: str) -> None:
        self.username = username
    
    def show_benefit(self) -> None:
        headers = ["Membership", "Discount", "Another Benefit"]
        table_data = [
            ["Platinum" , "15%", "Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%"],
            ["Gold" , "10%", "Benefit Silver + Voucher Ojek Online"],
            ["Silver" , "8%", "Voucher Makanan"],
        ]

        table = tabulate(table_data, headers, tablefmt='github')
        print("Benefit PacCommerce Memberships")
        print("")
        print(table)
        print("")
    
    def show_requirements(self) -> None:
        headers = ["Membership", "Monthly Expense (juta)", "Monthly Income (juta)"]
        table_data_requirement = [
            ["Platinum" , "8", "15"],
            ["Gold" , "6", "10"],
            ["Silver" , "5", "7"],
        ]

        table = tabulate(table_data_requirement, headers, tablefmt='github')
        print("Requirements PacCommerce Memberships")
        print("")
        print(table)
    
    def predict_membership(self, username: str, monthly_expense: float, monthly_income: float) -> None:
        parameter_data = [[8, 15], [6, 10], [5, 7]]
        
        result_tmp = []
        
        for idx, _ in enumerate(parameter_data):
            if monthly_expense < monthly_income:
                # implement euclidean distance
                euclidean_dist = round(sqrt((monthly_expense - parameter_data[idx][0])**2 + \
                                            (monthly_income - parameter_data[idx][1])**2), 2)
                
                result_tmp.append(euclidean_dist)

            else:
                raise Exception("Income must be greater than expenses")
            
        # store the euclidean distance values to dictionary
        dict_result = {
            "Platinum": result_tmp[0],
            "Gold": result_tmp[1],
            "Silver": result_tmp[2]
        }
        
        print(f"The results of calculating the Euclidean Distance from user{username} are {dict_result}")
        
        # get minimum values from result list
        get_min_distance = min(result_tmp)
        
        # iterate to dictionary data
        for key, value in dict_result.items():
            # compare with minimum data
            if value == get_min_distance:
                print(key)
                
                # insert predicted data to dict data
                self.data[username] = key
    
    def calculate_price(self, username: str, list_harga: list) -> float:
        if username in self.data:
            # get membership
            membership = self.data.get(username)
            
            # create branching for each membership to get discount
            if membership == "Platinum":
                total_price = sum(list_harga) - (sum(list_harga) * 0.15)
                
                return total_price
            
            elif membership == "Gold":
                total_price = sum(list_harga) - (sum(list_harga) * 0.10)
                
                return total_price
            
            elif membership == "Silver":
                total_price = sum(list_harga) - (sum(list_harga) * 0.08)
                
                return total_price
            
            else:
                raise Exception("Membership has not yet been implemented")
                
        else:
            raise Exception("The member is still not in the database")

    
user = Membership(username = "Shandy")
user.show_benefit()
user.show_requirements()
user.predict_membership(username = "Shandy", monthly_expense = 7, monthly_income = 12)
user.calculate_price(username = "Shandy", list_harga=[300000, 500000, 1250000])
