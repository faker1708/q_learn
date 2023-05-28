



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
        out = 0
        score = 0
        return self.ss,flag,out,score
    
    def __is_terminate(self):
        if(self.ss ==3):
            out = 1
        else:
            out = 0

        score = 1/self.__step_count
        return out,score

    
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
        out,score = self.__is_terminate()
        
        flag = 1
        return self.ss,flag,out,score
