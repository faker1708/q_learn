


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

        self.q_list = q_list

        return

