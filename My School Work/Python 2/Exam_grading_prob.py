# this is a input statement
mark = int(input("how many marks did you score\n"))
# if it meets a specific  condiition it will tell what grade you got and how many marks you need to go to the next grade


def grade(marks):
    if marks < 2:
        gradeU = 2-marks
        print("you got a grade U and need", gradeU,
              "marks to go to the next grade")
    elif marks >= 2 and marks < 4:
        grade1 = 4-marks
        print("you got a grade 1 and need", grade1,
              "marks to go to the next grade")
    elif marks >= 4 and marks < 13:
        grade2 = 13-marks
        print("you got a grade 2 and need", grade2,
              "marks to go to the next grade")
    elif marks >= 13 and marks < 22:
        grade3 = 22-marks
        print("you got a grade 3 and need ", grade3,
              "marks to go to the next grade")
    elif marks >= 22 and marks < 31:
        grade4 = 31-marks
        print("you got a grade 4 and need", grade4,
              "marks to go to the next grade")
    elif marks >= 31 and marks < 41:
        grade5 = 41-marks
        print("you got a grade 5 and need ", grade5,
              "marks to go to the next grade")
    elif marks >= 41 and marks < 54:
        grade6 = 54-marks
        print("you got a grade 6 and need ", grade6,
              "marks to go to the next grade")
    elif marks >= 54 and marks < 67:
        grade7 = 67-marks
        print("you got a grade 7 and need ", grade7,
              "marks to go to the next grade")
    elif marks >= 67 and marks < 80:
        grade8 = 80-marks
        print("you got a grade 8 and need", grade8,
              "marks to go to the next grade")
    elif marks >= 80 and marks <= 99:
        aced = 100 - marks
        print("you got a grade 9 and need", aced, " mark to ace the exam")
    elif marks == 100:
        print("you got a grade 9 and you also aced the exam")


grade(mark)
