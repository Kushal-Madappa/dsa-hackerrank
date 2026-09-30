# HackerRank: Day 12: Inheritance
# https://www.hackerrank.com/challenges/30-inheritance/problem
class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        avg = sum(self.scores) / len(self.scores)
        if avg >= 90:
            return 'O'
        if avg >= 80:
            return 'E'
        if avg >= 70:
            return 'A'
        if avg >= 55:
            return 'P'
        if avg >= 40:
            return 'D'
        return 'T'


line = input().split()
firstName, lastName, idNum = line[0], line[1], line[2]
numScores = int(input())
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
