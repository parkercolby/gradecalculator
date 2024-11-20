import matplotlib.pyplot as plt
import os
import math

def main():
    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")

    choice = int(input("Enter your selections: "))
    if choice == 1:
        name = input("What is the student's name: ")
        file = open("data/students.txt", "r")
        code = -1
        gradecount=0
        grade=0
        for line in file:
            if name in line:
                code = line[0:3]
                break
        file.close()
        if code == -1:
            print("Student not found")
        else:
            for f in os.listdir("data/submissions"):
                check = open("data/submissions/" + str(f),"r")
                line = check.readline()
                if line[len(line)-3]=='|' and line[0:3]==code:
                    grade += float(line[len(line)-2:len(line)])
                    gradecount+=1
                elif line[len(line)-2]=='|' and line[0:3]==code:
                    gradecount+=1
                    grade += float(line[len(line)-1:len(line)])
                elif line[0:3]==code:
                    gradecount+=1
                    grade += float(line[len(line)-3:len(line)])
            print(f"{math.floor(grade/gradecount)}%")
    elif choice == 2:
        assignment = input("What is the assignment name: ")
        f = open("data/assignments.txt", "r")
        token=False
        min,max,avg,count = 100,0,0,0
        code=-1
        for line in f.readlines():
            if token:
                code = str(line)
                break
            if assignment in line:
                token = True
        if not token:
            print("Assignment not found")
        else:
            for i in os.listdir("data/submissions"):
                check = open("data/submissions/" + str(i), "r")
                line = check.readline()
                val = float(line[len(line)-2:])
                print(val)
                avg+=val
                count += 1
                if val<min:
                    min=val
                elif val>max:
                    max=val
            print(f"Min: {min}%")
            print(f"Avg: {math.floor(avg/count)}%")
            print(f"Max: {max}%")
    else:
        pass

if __name__ == '__main__':
    main()
