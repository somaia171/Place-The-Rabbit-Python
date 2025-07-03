farm = [["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"]]

print("Welcome to place the rabbit.\n")
print(f"{farm[0]}\n{farm[1]}\n{farm[2]}\n")
print("Where should the rabbit go? 🐇")
colomn = int(input("\nPlease choose colomn number: "))
if colomn == 1 or colomn == 2 or colomn == 3:
    raw = int(input("Please choose raw number: "))
    if raw == 1 or raw == 2 or raw == 3:
        farm[raw-1][colomn-1] = "🐇"
        print(f"\nSuccess...\n\n{farm[0]}\n{farm[1]}\n{farm[2]}")
    else:
        print("\nInvalid Choice! Please enter valid raw number")
else:
        print("\nInvalid Choice! Please enter valid colomn number")
