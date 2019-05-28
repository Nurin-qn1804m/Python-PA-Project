class CalUtils:
    def __init__(self):
        self.names = ""
        self.heights = 0
        self.totalStudentHeight = []
        self.totalStudentCount = []

    def calAvgHeight(self):
        print ("Total Average Height: ")
        with open("ListOfStudents.txt", "r")as f:
            lines = f.readlines()
            for line in lines:
                words = line.split("\t")
                self.totalStudentHeight.append(float(words[1]))
                avg = (sum(self.totalStudentHeight) / len(self.totalStudentHeight))

        print(avg)

        y = (input("Enter new student name: "))
        z = float(input("Enter student height: "))
        with open("ListOfStudents.txt", "a")as f:
            f.write("\n" + y + "\t" + str(z))

obj = CalUtils()
obj.calAvgHeight()






