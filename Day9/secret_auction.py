def info():

    def key(dic,count):
        for k,v in dic.items():
            if v == count:
                return k

    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidders.append(name)
    bids.append(bid)
    if name in dic:
        dic[name].append(bid)
    else:
        dic[name] = bid
    
    again = input("Are there any other bidders? Type 'Y' or 'N':  ").lower()
    

    if again == 'y':
        info()
    else:
        count = 0
        for i in dic.values():
            if i > count:
                count = i
        print(f"The winner is {key(dic,count)} of ${count}.")

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         |_________|
                         `'-------'`
                       .-------------.
                       |______________|

'''

print(logo)
print("Welcome to Secret Auction Program")
bidders = []
bids = []
dic = {}
info()



