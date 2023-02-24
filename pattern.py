def pattern(num):
        for i in range(0,num):

                k = i+1
                for j in range(0,k):
                        print(end=' ')
                for j in range(0,i+1):
                        print('*', end=' ')
                print('')
        for i in range(num,0,-1):
                for j in range(0,i):
                        print('*', end=' ')
                print('')

pattern(5)