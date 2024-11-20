import matplotlib.pyplot as plt

def main():
    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")

    choice = int(input("Enter your selections: "))
    if choice == 1:
        name = input("What is the student's name: ")
        file = open("students.txt", "r")
        code = -1
        for line in file:
            if name in line:
                code = line[0:3]
                break
        file.close()
        if code == -1:
            print("Student not found")
        else:

        file = open("submissions")
    elif choice == 2:
        pass
    else:
        pass

if __name__ == '__main__':
    main()
