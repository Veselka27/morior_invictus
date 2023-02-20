stock = 700
jeans_sold = 600
target = 500

target_hit = jeans_sold >= target
print("Hit jeans sales target: ")
print(target_hit)

current_stock = stock - jeans_sold
in_stock = current_stock != 0
print("Jeans in stock: ")
print(in_stock)
