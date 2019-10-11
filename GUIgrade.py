import sys
import fileinput
import matplotlib.pyplot as plt
from tkinter import ttk
from Student import Student
from Student121 import Student121
from Student122 import Student122
from decimal import Decimal
import tkinter as tk
import tkinter.scrolledtext as tkst
import matplotlib.pyplot as plt

"""  
Main Code here
"""

class GUIgrade:

    student121DL=[]   #121 Data List
    student122DL=[]   #122 Data List
    
    def __init__(self, root, datafile):

        self.datafile = datafile
        self.root = root
        self.root.title("Grade Processing System")  #GUI title
        self.nb = ttk.Notebook(root)  #define tab in nb
        
        self.page0 = ttk.Frame(self.nb)  #sub the tab into the frame on top
        self.page1 = ttk.Frame(self.nb)  #tab2
        self.page2 = ttk.Frame(self.nb)  #tab3
        self.page3 = ttk.Frame(self.nb)  #tab4
        self.page4 = ttk.Frame(self.nb)  #tab5

        self.nb.add(self.page0, text='Data file')     #tab label 1
        self.nb.add(self.page1, text='121 Grade')     #tab label 2
        self.nb.add(self.page2, text='122 Grade')     #tab label 3
        self.nb.add(self.page3, text='Distribution')  #tab label 4
        self.nb.add(self.page4, text='Help')

        self.nb.pack(expand=1, fill="both")

        self.labelStat = tk.Label(self.root)  # Stat label
        self.labelStat.pack(anchor='w')

        self.labelAvgMark = tk.Label(self.root)  #Average mark label
        self.labelAvgMark.pack(anchor='w')

        self.labelMaxMark = tk.Label(self.root) #Max mark label
        self.labelMaxMark.pack(anchor='w')

        self.labelMinMark = tk.Label(self.root)  # Min mark label
        self.labelMinMark.pack(anchor='w')

        self.labelMedian = tk.Label(self.root)  # Median mark label
        self.labelMedian.pack(anchor='w')

        self.editArea0 = tkst.ScrolledText(self.page0,height=15)  #Layout of datafile scrolledtext
        self.editArea0.pack(expand=1, fill="both")  #Layout properities

        self.editArea1 = tkst.ScrolledText(self.page1, height=15)  #Layout of 121 scrolledtext
        self.editArea1.pack(expand=1, fill="both")  # Layout properities

        self.editArea2 = tkst.ScrolledText(self.page2, height=15)  #Layout of 122 scrolledtext
        self.editArea2.pack(expand=1, fill="both")  # Layout properities

        self.label121 = tk.Label(self.root)
        self.label121.pack()
        self.button = tk.Button(self.page3, text='121COM Grade Distribution')   #121 Distribution button
        self.button.bind('<Button-1>', self.event121)
        self.button.pack()

        self.label122 = tk.Label(self.root)
        self.label122.pack()
        self.button = tk.Button(self.page3, text='122COM Grade Distribution')  # 122 Distribution button
        self.button.bind('<Button-1>', self.event122)
        self.button.pack()

        self.editArea4 = tkst.ScrolledText(self.page4, height=15)  # Layout of help scrolledtext
        self.editArea4.pack(expand=1, fill="both")  # Layout properities


        self.readFile(self.datafile)
        #self.displayFile()
        self.displayFile('pass')  # display lines of the text files
        self.displayHelp()  # display help content


        """
        Lower GUI Part of the app 
        """

        self.menuChoice0 = tk.IntVar()   #Radio menu of Data File
        self.menuChoice0.set(0)
        self.menuItems0 = [('Display contents of input data file',0),  #Radio menu content
                    ('Display all valid input data for 121COM module',1),
                    ('Display all valid input data for 122COM module',2)]


        for (val, item) in enumerate(self.menuItems0):  #Show Data File Radio Button
            tk.Radiobutton(self.page0,
                           text=item[0],
                           variable=self.menuChoice0,
                           command=self.showChoice0,
                           value=val).pack(anchor=tk.W)





        self.menuChoice1 = tk.IntVar()   #Radio menu of 121 Grade
        self.menuChoice1.set(0)
        self.menuItems1 = [('Display all valid input data for 121COM module',0),  #Radio menu content
                    ('Display all students overall mark for 121COM module',1),
                    ('Display all students whose mark less than 40 for 121COM module',2)]


        for (val, item) in enumerate(self.menuItems1):  #Show 121 Radio Button
            tk.Radiobutton(self.page1,
                           text=item[0],
                           variable=self.menuChoice1,
                           command=self.showChoice1,    #Pending modification
                           value=val).pack(anchor=tk.W)


        self.menuChoice2 = tk.IntVar()  # Radio menu of 122 Grade
        self.menuChoice2.set(0)
        self.menuItems2 = [('Display all valid input data for 122COM module', 0),  # Radio menu content
                           ('Display all students overall mark for 122COM module', 1),
                           ('Display all students whose mark less than 40 for 122COM module', 2)]

        for (val, item) in enumerate(self.menuItems2):  # Show 122 Radio Button
            tk.Radiobutton(self.page2,
                           text=item[0],
                           variable=self.menuChoice2,
                           command=self.showChoice2,  # Pending modification
                           value=val).pack(anchor=tk.W)


    def event121(self, event):
        self.label122.config(text='              ')
        self.label121.config(text = 'Showing 121 Grade Chart')
        self.grade_distribute121()


    def event122(self, event):
        self.label121.config(text='              ')
        self.label122.config(text = 'Showing 122 Grade Chart')
        self.grade_distribute122()



    def grade_distribute121(self):
        print("Grade distributing ...")
        print("BackEnd display")
        print(' ')
        studentDL = []
        gradeFeq = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}
        self.readFile(self.datafile)
        print('%-15s%-20s%-10s%-17s%-20s' % ('Student', 'Name', 'CW Mark', 'Exam Mark', 'Overall'))
        print('=====================================================================')

        '''
        line = fileIn.readline()
    
        if not line:
            Analysis.exception_handle(self, 1)
            Analysis.analysis_menu(self)
        

        while line != '':
            studentRec = line.split('_')
            studentDL.append(Student(int(studentRec[0]), studentRec[1],
                                    float(studentRec[2]), float(studentRec[3])))
            line = fileIn.readline()

        fileIn.close()
        '''

        '''
        for e in GUIgrade.student121DL:
            self.editArea0.insert(tk.INSERT, ('%-10s%-10s%-15s%10.2f%10.2f%10.2f%10.2f\n' % (
                '121COM', e.getStudID(), e.getName(), e.getIAsgmt(), e.getTest(),
                e.getGAsgmt(), e.getExam())))
        '''

        for i in range(len(studentDL) - 1):  # swap
            for j in range(len(studentDL) - 1, i, -1):
                if studentDL[j - 1].getName() > studentDL[j].getName():
                    studentDL[j - 1], studentDL[j] = studentDL[j], studentDL[j - 1]

        num = 0
        sum = 0
        avg = 0
        a_count = 0
        b_count = 0
        c_count = 0
        d_count = 0
        f_count = 0
        #for e in studentDL:
        for e in GUIgrade.student121DL:
            #CWGet = studentDL[num].getCoursework()
            CWGet = e.getCoursework()
            #ExamGet = studentDL[num].getExam()
            ExamGet = e.getExam()
            #IDGet = studentDL[num].getStudID()
            #IDStr = str(IDGet)

            '''
            if CWGet < 0 or ExamGet < 0:
                Error_Flag = 1
                Data.exception_handle(self, 3)
                break

            if CWGet > 100 or ExamGet > 100:
                Error_Flag = 1
                Data.exception_handle(self, 3)
                break

            if len(IDStr) != 8:
                Error_Flag = 1
                Data.exception_handle(self, 2)
                break

            # print(e)
            
            '''
            total = round(e.overall(), 2)

            if total > 0 and total < 40:
                # overall = float(studentRec[2])*0.4 + float(studentRec[3])*0.6
                print(e, '          ', total, ' F')
                f_count += 1
                num += 1
                sum += total
            if total > 40 and total < 50:
                print(e, '          ', total, ' D')
                num += 1
                d_count += 1
                sum += total
            if total > 50 and total < 65:
                print(e, '          ', total, ' C')
                num += 1
                c_count += 1
                sum += total
            if total > 65 and total < 75:
                print(e, '          ', total, ' B')
                num += 1
                b_count += 1
                sum += total
            if total > 75 and total <= 100:
                print(e, '          ', total, ' A')
                num += 1
                a_count += 1
                sum += total

        print('Total number of records displayed: ', num)
        print("Grade A total: ", a_count)
        print("Grade B total: ", b_count)
        print("Grade C total: ", c_count)
        print("Grade D total: ", d_count)
        print("Grade F total: ", f_count)
        print("Total mark: ", sum)

        gradeFeq['A'] = a_count
        gradeFeq['B'] = b_count
        gradeFeq['C'] = c_count
        gradeFeq['D'] = d_count
        gradeFeq['F'] = f_count

        fig = plt.figure(figsize=(8, 6))  # width x height in inches
        ax1 = fig.add_subplot(111)  # 1 row 1 columns, column 1
        ax1.bar(['A', 'B', 'C', 'D', 'F'],
                [gradeFeq['A'], gradeFeq['B'], gradeFeq['C'],
                 gradeFeq['D'], gradeFeq['F']])  # vertical bar charts
        plt.title('121COM Grade Distribution')
        plt.ylabel('Student Numbers')
        plt.show()


    def grade_distribute122(self):
        print("Grade distributing ...")
        print("BackEnd display")
        print(' ')
        studentDL = []
        gradeFeq = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}
        self.readFile(self.datafile)
        print('%-15s%-20s%-10s%-17s%-20s' % ('Student', 'Name', 'CW Mark', 'Exam Mark', 'Overall'))
        print('=====================================================================')

        '''
        line = fileIn.readline()

        if not line:
            Analysis.exception_handle(self, 1)
            Analysis.analysis_menu(self)


        while line != '':
            studentRec = line.split('_')
            studentDL.append(Student(int(studentRec[0]), studentRec[1],
                                    float(studentRec[2]), float(studentRec[3])))
            line = fileIn.readline()

        fileIn.close()
        '''

        '''
        for e in GUIgrade.student121DL:
            self.editArea0.insert(tk.INSERT, ('%-10s%-10s%-15s%10.2f%10.2f%10.2f%10.2f\n' % (
                '121COM', e.getStudID(), e.getName(), e.getIAsgmt(), e.getTest(),
                e.getGAsgmt(), e.getExam())))
        '''

        for i in range(len(studentDL) - 1):  # swap
            for j in range(len(studentDL) - 1, i, -1):
                if studentDL[j - 1].getName() > studentDL[j].getName():
                    studentDL[j - 1], studentDL[j] = studentDL[j], studentDL[j - 1]

        num = 0
        sum = 0
        avg = 0
        a_count = 0
        b_count = 0
        c_count = 0
        d_count = 0
        f_count = 0
        # for e in studentDL:
        for e in GUIgrade.student122DL:
            # CWGet = studentDL[num].getCoursework()
            CWGet = e.getCoursework()
            # ExamGet = studentDL[num].getExam()
            OverallGet = e.overall()
            # IDGet = studentDL[num].getStudID()
            # IDStr = str(IDGet)

            '''
            if CWGet < 0 or ExamGet < 0:
                Error_Flag = 1
                Data.exception_handle(self, 3)
                break

            if CWGet > 100 or ExamGet > 100:
                Error_Flag = 1
                Data.exception_handle(self, 3)
                break

            if len(IDStr) != 8:
                Error_Flag = 1
                Data.exception_handle(self, 2)
                break

            # print(e)

            '''
            total = round(e.overall(), 2)

            if total > 0 and total < 40:
                # overall = float(studentRec[2])*0.4 + float(studentRec[3])*0.6
                print(e, '          ', total, ' F')
                f_count += 1
                num += 1
                sum += total
            if total > 40 and total < 50:
                print(e, '          ', total, ' D')
                num += 1
                d_count += 1
                sum += total
            if total > 50 and total < 65:
                print(e, '          ', total, ' C')
                num += 1
                c_count += 1
                sum += total
            if total > 65 and total < 75:
                print(e, '          ', total, ' B')
                num += 1
                b_count += 1
                sum += total
            if total > 75 and total <= 100:
                print(e, '          ', total, ' A')
                num += 1
                a_count += 1
                sum += total

        print('Total number of records displayed: ', num)
        print("Grade A total: ", a_count)
        print("Grade B total: ", b_count)
        print("Grade C total: ", c_count)
        print("Grade D total: ", d_count)
        print("Grade F total: ", f_count)
        print("Total mark: ", sum)

        gradeFeq['A'] = a_count
        gradeFeq['B'] = b_count
        gradeFeq['C'] = c_count
        gradeFeq['D'] = d_count
        gradeFeq['F'] = f_count

        fig = plt.figure(figsize=(8, 6))  # width x height in inches
        ax1 = fig.add_subplot(111)  # 1 row 1 columns, column 1
        ax1.bar(['A', 'B', 'C', 'D', 'F'],
                [gradeFeq['A'], gradeFeq['B'], gradeFeq['C'],
                 gradeFeq['D'], gradeFeq['F']])  # vertical bar charts
        plt.title('122COM Grade Distribution')
        plt.ylabel('Student Numbers')
        plt.show()


    def showChoice0(self):

        if self.menuChoice0.get() == 0:
            self.displayFile('data')
        elif self.menuChoice0.get() == 1:
            self.displayValidData('121', 'data')
        elif self.menuChoice0.get() == 2:
            self.displayValidData('122', 'data')

    def showChoice1(self):

        if self.menuChoice1.get() == 0:
            self.displayValidData('121', '121')
        elif self.menuChoice1.get() == 1:
            self.displayValidData('121_total', '121')
        elif self.menuChoice1.get() == 2:
            self.displayValidData('121_40', '121')

    def showChoice2(self):

        if self.menuChoice2.get() == 0:
            self.displayValidData('122', '122')
        elif self.menuChoice2.get() == 1:
            self.displayValidData('122_total', '122')
        elif self.menuChoice2.get() == 2:
            self.displayValidData('122_40', '122')


    def displayFile(self, module):  #Show text file content from markdata.dat
    #def displayFile(self, datafile):
        if module == 'data':
            self.editArea0.delete(1.0, tk.END)  #delete content of the scrolled text
            #self.editArea0.insert(tk.INSERT,'Module Stud ID Name CW1 mark Test Mark CW2 mark' + '\n')
            self.editArea0.insert(tk.INSERT, '=' * 25 + 'markdata.dat' + '=' * 25 + '\n')
            #self.editArea0.insert(tk.INSERT, '=' * 25 + datafile + '=' * 25 + '\n')

            for line in fileinput.input(self.datafile):
                self.editArea0.insert(tk.INSERT,line)

        '''
        if module == '121':
            # def displayFile(self, datafile):
            self.editArea1.delete(1.0, tk.END)  # delete content of the scrolled text
            # self.editArea0.insert(tk.INSERT,'Module Stud ID Name CW1 mark Test Mark CW2 mark' + '\n')
            self.editArea1.insert(tk.INSERT, '=' * 25 + 'markdata.dat' + '=' * 25 + '\n')
            # self.editArea0.insert(tk.INSERT, '=' * 25 + datafile + '=' * 25 + '\n')

            for line in fileinput.input(self.datafile):
                self.editArea1.insert(tk.INSERT, line)
        '''

    def averageMark(self, module):

        total = 0

        if module == '121':
            for e in GUIgrade.student121DL:
                total += e.overall()
            average = (total / Student.numStudent)
            average = round(average, 2)

        if module == '122':
            for e in GUIgrade.student122DL:
                total += e.overall()
            average = (total / Student.numStudent)
            average = round(average, 2)

        return str(average)


    def median(selfself, module):

        median = 0

        if module == '121':
            median = (int(max('121')) + int(min('121'))) + 100
            median = median / 2


        if module == '122':
            median = (int(max('122')) + int(min('122'))) + 130
            median = median / 2

        return str(median)

    def max(self, module):

        overall = 0
        max = 0

        if module == '121':
            for e in GUIgrade.student121DL:
                overall = e.overall()

                if overall > max:
                    max = overall
                    max = round(max, 2)


        if module == '122':
            for e in GUIgrade.student122DL:
                overall = e.overall()

                if overall > max:
                    max = overall
                    max = round(max, 2)

        return str(max)



    def min(self, module):

        overall = 0
        min = 1000

        if module == '121':
            for e in GUIgrade.student121DL:
                overall = e.overall()

                if overall < min:
                    min = overall
                    min = round(min, 2)


        if module == '122':
            for e in GUIgrade.student122DL:
                overall = e.overall()

                if overall < min:
                    min = overall
                    min = round(min, 2)

        return str(min)



    def displayHelp(self):  #Display help description
        self.editArea4.delete(1.0, tk.END)
        self.editArea4.insert(tk.INSERT, 'Grade processing system load grade information from a file of grade data, ' + '\n')
        self.editArea4.insert(tk.INSERT, 'process grade for different modules, ' + '\n')
        self.editArea4.insert(tk.INSERT, 'and plot grade ditribution using ttk.Notebook widget to display result in separate windows.' + '\n')

        #for line in fileinput.input(self.datafile):
         #   self.editArea4.insert(tk.INSERT, line)


    def displayValidData(self,module, tab):   #Show 121 marks
        #self.editArea0.delete(1.0, tk.END)
        #total = 0
        if module == '121' and tab == 'data':
            self.editArea0.delete(1.0, tk.END)
            self.editArea0.insert(tk.INSERT, ('%-10s%-10s%-15s%10s%10s%10s%10s\n' % (
            'Module', 'Stud ID', 'Name', 'CW1 mark', 'Test mark', 'CW2 mark', 'Exam mark')))
            self.editArea0.insert(tk.INSERT, '=' * 75 + '\n')
            for e in GUIgrade.student121DL:
                self.editArea0.insert(tk.INSERT, ('%-10s%-10s%-15s%10.2f%10.2f%10.2f%10.2f\n' % (
                '121COM', e.getStudID(), e.getName(), e.getIAsgmt(), e.getTest(),
                e.getGAsgmt(), e.getExam())))
                #total += e.overall()
                #average = total / Student.numStudent
            self.labelStat.config(text='------------- Basic statistics ---------- ')  # display stat label
            self.labelAvgMark.config(text='Average mark is: ' + self.averageMark('121'))  # display average mark
            self.labelMaxMark.config(text='Maximum overall mark is: ' + self.max('121'))  # display max mark
            self.labelMinMark.config(text='Minimum overall mark is: ' + self.min('121'))  # display min mark
            self.labelMedian.config(text='Median mark is: ' + self.median('121'))  # display min mark



        if module == '122' and tab == 'data':
            self.editArea0.delete(1.0, tk.END)
            self.editArea0.insert(tk.INSERT, ('%-10s%-10s%-15s%10s%10s%10s\n' % (
                'Module', 'Stud ID', 'Name', 'CW1 mark', 'Test mark', 'CW2 mark')))
            self.editArea0.insert(tk.INSERT, '=' * 75 + '\n')
            for e in GUIgrade.student122DL:
                self.editArea0.insert(tk.INSERT, ('%-10s%-10s%-15s%10.2f%10.2f%10.2f\n' % (
                    '122COM', e.getStudID(), e.getName(), e.getIAsgmt(), e.getTest(),
                    e.getGAsgmt())))
            self.labelStat.config(text='------------- Basic statistics ---------- ')  # display stat label
            self.labelAvgMark.config(text='Average mark is: ' + self.averageMark('122'))  # display average mark
            self.labelMaxMark.config(text='Maximum overall mark is: ' + self.max('122'))  # display max mark
            self.labelMinMark.config(text='Minimum overall mark is: ' + self.min('122'))  # display min mark
            self.labelMedian.config(text='Median mark is: ' + self.median('122'))  # display min mark



        if module == '121' and tab == '121':
            self.editArea1.delete(1.0, tk.END)
            self.editArea1.insert(tk.INSERT, ('%-10s%-10s%-15s%10s%10s%10s%10s\n' % (
                'Module', 'Stud ID', 'Name', 'CW1 mark', 'Test mark', 'CW2 mark', 'Exam mark')))
            self.editArea1.insert(tk.INSERT, '=' * 75 + '\n')
            for e in GUIgrade.student121DL:
                self.editArea1.insert(tk.INSERT, ('%-10s%-10s%-15s%10.2f%10.2f%10.2f%10.2f\n' % (
                    '121COM', e.getStudID(), e.getName(), e.getIAsgmt(), e.getTest(),
                    e.getGAsgmt(), e.getExam())))
            self.labelStat.config(text='------------- Basic statistics ---------- ')  # display stat label
            self.labelAvgMark.config(text='Average mark is: ' + self.averageMark('121'))  # display average mark
            self.labelMaxMark.config(text='Maximum overall mark is: ' + self.max('121'))  # display max mark
            self.labelMinMark.config(text='Minimum overall mark is: ' + self.min('121'))  # display min mark
            self.labelMedian.config(text='Median mark is: ' + self.median('121'))  # display min mark


        if module == '121_total' and tab == '121':
            self.editArea1.delete(1.0, tk.END)
            self.editArea1.insert(tk.INSERT, ('%-10s%-10s%-15s%10s%10s%10s\n' % (
                'Module', 'Stud ID', 'Name', 'CW mark', 'Exam mark', 'Overall')))
            self.editArea1.insert(tk.INSERT, '=' * 75 + '\n')
            for e in GUIgrade.student121DL:
                self.editArea1.insert(tk.INSERT, ('%-10s%-10s%-15s%10.2f%10.2f%10.2f\n' % (
                    '121COM', e.getStudID(), e.getName(), e.getCoursework(),
                    e.getExam(), e.overall())))
            self.labelStat.config(text='------------- Basic statistics ---------- ')  # display stat label
            self.labelAvgMark.config(text='Average mark is: ' + self.averageMark('121'))  # display average mark
            self.labelMaxMark.config(text='Maximum overall mark is: ' + self.max('121'))  # display max mark
            self.labelMinMark.config(text='Minimum overall mark is: ' + self.min('121'))  # display min mark
            self.labelMedian.config(text='Median mark is: ' + self.median('121'))  # display min mark



        if module == '121_40' and tab == '121':
            self.editArea1.delete(1.0, tk.END)
            self.editArea1.insert(tk.INSERT, ('%-10s%-10s%-15s%10s%10s%10s\n' % (
                'Module', 'Stud ID', 'Name', 'CW mark', 'Exam mark', 'Overall')))
            self.editArea1.insert(tk.INSERT, '=' * 75 + '\n')
            for e in GUIgrade.student121DL:
                if e.overall() >= 40:
                    pass
                else:
                    self.editArea1.insert(tk.INSERT, ('%-10s%-10s%-15s%10.2f%10.2f%10.2f\n' % (
                        '121COM', e.getStudID(), e.getName(), e.getCoursework(),
                        e.getExam(), e.overall())))
            self.labelStat.config(text='------------- Basic statistics ---------- ')  # display stat label
            self.labelAvgMark.config(text='Average mark is: ' + self.averageMark('121'))  # display average mark
            self.labelMaxMark.config(text='Maximum overall mark is: ' + self.max('121'))  # display max mark
            self.labelMinMark.config(text='Minimum overall mark is: ' + self.min('121'))  # display min mark
            self.labelMedian.config(text='Median mark is: ' + self.median('121'))  # display min mark



        if module == '122' and tab == '122':
            self.editArea2.delete(1.0, tk.END)
            self.editArea2.insert(tk.INSERT, ('%-10s%-10s%-15s%10s%10s%10s\n' % (
                'Module', 'Stud ID', 'Name', 'CW1 mark', 'Test mark', 'CW2 mark')))
            self.editArea2.insert(tk.INSERT, '=' * 75 + '\n')
            for e in GUIgrade.student122DL:
                self.editArea2.insert(tk.INSERT, ('%-10s%-10s%-15s%10.2f%10.2f%10.2f\n' % (
                    '122COM', e.getStudID(), e.getName(), e.getIAsgmt(), e.getTest(),
                    e.getGAsgmt())))
            self.labelStat.config(text='------------- Basic statistics ---------- ')  # display stat label
            self.labelAvgMark.config(text='Average mark is: ' + self.averageMark('122'))  # display average mark
            self.labelMaxMark.config(text='Maximum overall mark is: ' + self.max('122'))  # display max mark
            self.labelMinMark.config(text='Minimum overall mark is: ' + self.min('122'))  # display min mark
            self.labelMedian.config(text='Median mark is: ' + self.median('122'))  # display min mark


        if module == '122_total' and tab == '122':
            self.editArea2.delete(1.0, tk.END)
            self.editArea2.insert(tk.INSERT, ('%-10s%-10s%-15s%10s%10s\n' % (
                'Module', 'Stud ID', 'Name', 'CW mark', 'Overall')))
            self.editArea2.insert(tk.INSERT, '=' * 75 + '\n')
            for e in GUIgrade.student122DL:
                self.editArea2.insert(tk.INSERT, ('%-10s%-10s%-15s%10.2f%10.2f\n' % (
                    '122COM', e.getStudID(), e.getName(), e.getCoursework(), e.overall())))
            self.labelStat.config(text='------------- Basic statistics ---------- ')  # display stat label
            self.labelAvgMark.config(text='Average mark is: ' + self.averageMark('122'))  # display average mark
            self.labelMaxMark.config(text='Maximum overall mark is: ' + self.max('122'))  # display max mark
            self.labelMinMark.config(text='Minimum overall mark is: ' + self.min('122'))  # display min mark
            self.labelMedian.config(text='Median mark is: ' + self.median('122'))  # display min mark



        if module == '122_40' and tab == '122':
            self.editArea2.delete(1.0, tk.END)
            self.editArea2.insert(tk.INSERT, ('%-10s%-10s%-15s%10s%10s\n' % (
                'Module', 'Stud ID', 'Name', 'CW mark', 'Overall')))
            self.editArea2.insert(tk.INSERT, '=' * 75 + '\n')
            for e in GUIgrade.student122DL:
                if e.overall() >= 40:
                    pass
                else:
                    self.editArea2.insert(tk.INSERT, ('%-10s%-10s%-15s%10.2f%10.2f\n' % (
                        '122COM', e.getStudID(), e.getName(), e.getCoursework(), e.overall())))
            self.labelStat.config(text='------------- Basic statistics ---------- ')  # display stat label
            self.labelAvgMark.config(text='Average mark is: ' + self.averageMark('122'))  # display average mark
            self.labelMaxMark.config(text='Maximum overall mark is: ' + self.max('122'))  # display max mark
            self.labelMinMark.config(text='Minimum overall mark is: ' + self.min('122'))  # display min mark
            self.labelMedian.config(text='Median mark is: ' + self.median('122'))  # display min mark





    def readFile(self, datafile):
        try:
            fileIn = open(datafile, 'r')

            line = fileIn.readline()

            while line != '':
                studentRec = line.split('_')
                try:
                    if studentRec[0] == '121':
                        GUIgrade.student121DL.append(Student121(line[4:]))
                    if studentRec[0] == '122':
                        GUIgrade.student122DL.append(Student122(line[4:]))
                except ValueError as error:
                    sys.stderr.write(str(error) + ' in input ' + line + '\n')

                line = fileIn.readline()

            if Student.numStudent == 0:
                sys.stderr.write('empty or invalid data only : ' + line + '\n')

            fileIn.close()

        except FileNotFoundError as error:
            sys.stderr.write(str(error) + '\n')








def main(argv):
    root = tk.Tk()
    GUIgrade(root,argv[1])
    root.mainloop()

if __name__ == '__main__':
    main(sys.argv)
