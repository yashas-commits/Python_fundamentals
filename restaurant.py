# 1. Ask for the Total Bill Amount
# We use float() because bills usually have decimals (e.g., 55.75)
total_bill = float(input("Enter the total bill amount: $"))

# 2. Ask for the Number of People
# Since you can't have half a person, we use int()
people_count = int(input("How many people are splitting the bill? "))

# 3. Calculate the Share per Person
# Division (/) in Python always returns a float
share = total_bill / people_count

# 4. Output the result
print(f"Total Bill: ${total_bill}. Each person pays: ${share}")

# --- BONUS: Verifying Data Types ---
print("-" * 30)
print("Data Type Verification:")
print(f"Total Bill type: {type(total_bill)}")
print(f"People Count type: {type(people_count)}")
print(f"Share type: {type(share)}")