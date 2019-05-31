class CalUtils:
    def __init__(self):
        self.names = ""
        self.heights = 0
        self.totalStudentHeight = []
        self.totalStudentCount = []

    def calAvgHeight(self):
        print ("Student average height is ")
        with open("ListOfStudents.txt", "r")as f:
            lines = f.readlines()
            for line in lines:
                words = line.split("\t")
                self.totalStudentHeight.append(float(words[1]))
                avg = (sum(self.totalStudentHeight) / len(self.totalStudentHeight))
                x = round( avg , 2)
        print(x)
        print("in metres")
        


        y = (input("Enter new student name: "))
        z = float(input("Enter student height: "))
        with open("ListOfStudents.txt", "a")as f:
            f.write("\n" + y + "\t" + str(z))
            self.totalStudentHeight.append(float(words[1]))
            avg = (sum(self.totalStudentHeight) / len(self.totalStudentHeight))
            x = round( avg , 2)
            self.totalStudentCount.append(float(words[1]))


        print("Students average height is")
        print(x)
        print ("in metres")








obj = CalUtils()
obj.calAvgHeight()












