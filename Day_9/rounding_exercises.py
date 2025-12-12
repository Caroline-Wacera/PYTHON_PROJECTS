#1️⃣ Basic Rounding
#Round the number 7.68 to the nearest whole number.
number = 7.68
print(round(number))


#2️⃣ Decimal Places
#Round 12.34567 to 2 decimal places.
number = 12.34567
print(round(number,2))


#3️⃣ More Decimal Places
#Round 98.123456 to 4 decimal places.
number = 98.123456
print(round(number,4))


#4️⃣ Always Round Down
#Use floor rounding to round 9.999 down.
import math
x = 9.999
print(math.floor(x))


#5️⃣ Always Round Up
#Use ceil rounding to round 6.0001 up.
import math
x = 6.0001
print(math.ceil(x))


#6️⃣ Convert to Money Format
#Format 4500.5 to exactly 2 decimal places (like currency)
x = 4500.5
print(f"{x:.2f}")


#Remove Decimals Completely
#Convert 89.765 to an integer (no decimals).
x = 89.765
print(int(x))


#8️⃣ Combined Rounding
#Round 3.5555 to 2 decimal places → what do you get?
x = 3.5555
print(round(x, 2))


#9️⃣ Real-world: Shopping VAT
#A product costs 254.789 Ksh.
#Round the price to 2 decimal places.
price = 254.789
rounded_price = round(price, 2)
print(f"The price of the product costs {rounded_price} Kshs")


#🔟 Real-world: Taxi App
#A distance recorded is 12.0001 km.
#Round it up to charge the customer correctly.
import math
distance = 12.0001
rounded_up = math.ceil(distance)
print(f"The rounded up distance is {rounded_up} Km")

