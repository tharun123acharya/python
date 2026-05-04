count = 1

while True:
    ch = input("Enter a character: ")

    if ch == 'L':
        print("Letter L entered. Stopping...")
        break

    print(f"Character {count}: {ch}")
    count += 1