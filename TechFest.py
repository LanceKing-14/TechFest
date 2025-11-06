print(" Welcome to SMIT TechFest ")
print(" Event organized by Lance King of APPDAET BTCS2")

number = (int(input("\nHow many participants will register: ")))

if number <= 0:
    print("\033[31mInvalid number of participants\033[0m")
    exit()

else:
    participants = []

for i in range(number):
    name = input("\nWhat is your name? ")
    track = input("What is your track? ")
    participants.append({"name": name, "track":track})

    print("\nRegistered participants:")
    for i, p in enumerate(participants, 1):
        print(f"{i}. {p['name']} - {p['track']}")