



from game import game as g0

from q_learn import agent

class main_class():

    def __init__(self):
        self.__main()


    def fm(self,mode,n_episode):

        epsilon = 1
        if(mode =='train'):
            epsilon = 0.9

        for _ in range(n_episode):
            perception,flag,out,score = self.game.reset()
            exp_list = list()
            while(1):
                action = self.agent.take_action(perception,epsilon)
                perception,flag,terminate,score = self.game.step(action)

                # print('action',action)

                exp = [perception,action,0]
                exp_list.append(exp)
                if(terminate):
                    break
            
            # print('score',score)
            
            for _ ,exp in enumerate(exp_list):
                exp[2] = score    

            self.agent.store(exp_list)

        # print(self.agent.)


    def __main(self):



        # print (q_list)
        # print (len(q_list))

        self.game = g0()
        self.agent = agent(self.game.state_dimension,self.game.action_dimension)
        while(1):
            self.fm('train',2**16)
        


        return


if __name__ == '__main__':
    main_class()