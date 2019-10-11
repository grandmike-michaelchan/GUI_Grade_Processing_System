from Student import Student

'''
Student121 class 

Created on Oct 5, 2018

@author: dcywchan
'''
class Student121(Student):
    '''
    Student121 class to represent each 121COM student object
    '''
    CW1weight = 0.2 # class variable for weights for the coursework 1
    CW2weight = 0.2 # class variable for weights for the coursework 2 
    CW3weight = 0.6 # class variable for weights for the coursework 3
    
    CWweight = 0.7 # class variable for weights for the coursework 
    EXweight = 0.3 # class variable for weights for the exam 
       
       
    def __init__(self,dataLine):
        '''
                constructor method

                Parameters:
                - dataLine with following data feilds
                    - studID: student ID
                    - name: name of student
                    - test: test mark
                    - iAsgn: individual assignment mark
                    - gAsgn: group assignment mark
                    - exam: exam mark
                '''

        tokens = dataLine.split('_')
        if (float(tokens[2]) < 0 or
                float(tokens[2]) > 100 or
                float(tokens[3]) < 0 or
                float(tokens[3]) > 100 or
                float(tokens[4]) < 0 or
                float(tokens[4]) > 100 or
                float(tokens[5]) < 0 or
                float(tokens[5]) > 100):
            raise ValueError("invalid mark value")
        elif tokens[1] == '':
            raise ValueError("invalid student name")
        elif len(tokens[0]) != 8:
            raise ValueError("invalid student number")

        Student.__init__(self, int(tokens[0]), tokens[1])
        self.__test = float(tokens[2])
        self.__iAsgmt = float(tokens[3])
        self.__gAsgmt = float(tokens[4])
        self.__exam = float(tokens[5])

    def getTest(self):
        '''
        accessor method to get student test mark
        '''
        return self.__test
    
    def getIAsgmt(self):
        '''
        accessor method to get student nindividual assignment mark
        '''
        return self.__iAsgmt
            
    def getGAsgmt(self):
        '''
        accessor method to get student group assignment mark
        '''
        return self.__gAsgmt
    
    def getExam(self):
        '''
        accessor method to get student examination mark
        '''        
        return self.__exam    
    
    def getCoursework(self):
        '''
        accessor method to get student coursework mark
        '''              
        return Student121.CW1weight * self.getTest() + \
                Student121.CW2weight * self.getIAsgmt() + \
                Student121.CW3weight * self.getGAsgmt() 
                   
    def overall(self):
        '''
        service method to calculate overall mark from the weighted sum of the coursework mark and the the exam mark
        '''
        return Student121.CWweight * self.getCoursework() + \
                Student121.EXweight * self.getExam()
           
    def __str__(self):
        '''
        String representation of student object
        '''
        return '%-10s%25s%10.2f%10.2f'%('121COM',Student.__str__(self),self.getCoursework(),self.getExam())
            
