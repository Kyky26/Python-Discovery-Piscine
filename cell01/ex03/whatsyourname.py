first = input("Hey, what's your first name? : ")
last = input("And your last name? : ")

first_cleaned = first.strip()
last_cleaned = last.strip()

print(f"Well, pleased to meet you, {first_cleaned} {last_cleaned}.")