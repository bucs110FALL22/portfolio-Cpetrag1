print(10*5)
print(10**2)
print(15/10)
print(15//10)
print(-15//10)
print(15%10)
print(10%15)
print(10%10)
print(0%10)
print(10/15)
# Would have been better written as 2/3

#Money exchange
rate = float(input("What is the current exchange rate from Euros to the US? Dollar"))
amt = float(input("How many Euros would you like to exchange?"))
total = rate*amt
result = round(total - 3, 2)
print("You will receive " + str(result) + " dollars")
