print("This is a freefall calculator")
height = float(input("At what height should i throw it from"))
g = float(input("With how much acceleration should we throw it, Earth's acceleration is 9.81"))
time = (2 * height / g) ** 0.5
print("It takes to fall ", time, "seconds")



