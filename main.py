import numpy as np

# ========== Matrix Input ==========
def get_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []
    for i in range(rows):
        row = input(f"Enter row {i+1} (numbers separated by space): ").split()
        row = [float(x) for x in row]
        matrix.append(row)

    return np.array(matrix)

# ========== Vector Input ==========
def get_vector(size):
    v = input(f"Enter a vector of size {size} (numbers separated by space): ").split()
    return np.array([float(x) for x in v])

# ========== Menu ==========
def show_menu():
    print("\n=== Matrix Operations Menu ===")
    print("1) Matrix × Vector")
    print("2) Row/Column Sum & Mean")
    print("3) Slicing (Row & Column)")
    print("4) Matrix Transpose")
    print("5) Matrix Reshape")
    print("6) Exit\n")

# ========== Program Start ==========
matrix = get_matrix()
print("\nYour Matrix:\n", matrix)

while True:
    show_menu()
    choice = input("Choose an option: ")

    # ===== 1) Matrix × Vector =====
    if choice == "1":
        vector = get_vector(matrix.shape[1])
        result = matrix.dot(vector)
        print("Result:", result)

    # ===== 2) Sum & Mean =====
    elif choice == "2":
        print("\nRow Sums:", matrix.sum(axis=1))
        print("Column Sums:", matrix.sum(axis=0))
        print("Row Means:", matrix.mean(axis=1))
        print("Column Means:", matrix.mean(axis=0))

    # ===== 3) Slicing =====
    elif choice == "3":
        r = int(input("Enter row index: "))
        c = int(input("Enter column index: "))
        print("Row:", matrix[r])
        print("Column:", matrix[:, c])

    # ===== 4) Transpose =====
    elif choice == "4":
        print("Transpose:\n", matrix.T)

    # ===== 5) Reshape =====
    elif choice == "5":
        rows = int(input("New number of rows: "))
        cols = int(input("New number of columns: "))
        try:
            print("Reshaped Matrix:\n", matrix.reshape(rows, cols))
        except:
            print("❌ Invalid reshape dimensions!")

    # ===== 6) Exit =====
    elif choice == "6":
        print("Goodbye ✌️")
        break

    else:
        print("Invalid option!")