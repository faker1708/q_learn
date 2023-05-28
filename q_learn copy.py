


import random

class agent():

    def __init__(self):
        self.__main()


    def __main(self):

        q_list = list()
        for _ in range(self.game.state_dimension):
            aql = list()
            for _ in range(self.game.action_dimension):
                q = random.gauss(0,0.1)
                aql.append(q)
            q_list.append(aql)

        self.__q_list = q_list

        return

    def take_action(self,perception,epsilon):

        # explore
        # exploitate
        ev = 2**10
        ra = random.randint(0,ev-1)
        if(ra/ev<epsilon):
            explore = 0
        else:
            explore = 1
        
        if(explore):
            action = random.randint()


        return
    
    def store(self,exp_list):



        return
    
    def __update(self):

