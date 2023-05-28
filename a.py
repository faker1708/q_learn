



from game import game as g0

import random

class main_class():

    def __init__(self):
        self.__main()


    def fm(self,mode,n_episode):

        self.game = g0()
        for i in range(n_episode):
            self.game.reset()
            



    def __main(self):

        q_list = list()
        for _ in range(self.game.state_dimension):
            aql = list()
            for _ in range(self.game.action_dimension):
                q = random.gauss(0,0.1)
                aql.append(q)
            q_list.append(aql)


        # print (q_list)
        # print (len(q_list))

        


        return


if __name__ == '__main__':
    main_class()