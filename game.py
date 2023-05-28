



import random


class game():

    def __init__(self):
        self.__main()



    def __main(self):

        self.state_dimension = 8
        self.action_dimension = 3   # idle 左右

        return

    def reset(self):
        self.ss = random.randint(0,self.state_dimension-1)
        self.__step_count = 0

        flag = 1
        terminate = 0
        score = 0
        perception = self.ss
        return perception,flag,terminate,score
    
    def __is_terminate(self):
        if(self.ss ==3):
            terminate = 1
            score = 1/self.__step_count
        else:
            terminate = 0
            score = 0

        return terminate,score

    
    def step(self,action):

        if(action ==1):
            # left
            self.ss -=1
        elif(action ==2):
            self.ss+=1
        
        if(self.ss<=-1):
            self.ss = 0
        elif(self.ss>= self.state_dimension):
            self.ss = self.state_dimension-1
        
        self.__step_count+=1
        terminate,score = self.__is_terminate()
        
        flag = 1
        perception = self.ss
        return perception,flag,terminate,score
