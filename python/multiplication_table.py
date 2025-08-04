print("   ", end="")
for i in range(1, 21):
    print(f"{i:4}", end="")
print("\n" + "==" * 42)

for i in range(1, 21):
    print(f"{i:2} ||", end="")
    for j in range(1, 21):
        print(f"{i*j:4}", end="")
    print()
