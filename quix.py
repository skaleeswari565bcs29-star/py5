class InvalidOptionError(Exception):
    pass
class quiz:
    def __init__(self):
        self.questions=["1.Capital of Japan?\nA.Tokyo\nB.Hiroshima\nC,Nagoya","\n2.Largest Planet?\nA.Earth\nB.Jupiter\nC.Mars","\nSun Rises In?\nA.West\nB.east\nC.North","\n4.Fastest Land Animal?\nA.Lion\nB.Cheetah\nC.Tiger","\n5.Largest Ocean?\nA.Atlantic\nB.Indian\nC.Pacific","\n6.Capital of USA?\nA.New York\nB.Boston\nC.Washington,D.c.","\n7.Largest Mammal?\nA.blue WHALE\nb.Elephant\nC.Tiger","\n8.Number Of Continents?\nA.8\nB.5\nC.7"]
        self.answers=['A','B','B','B','C','C','A','C']
        self.score=0
    def start_quiz(self):
        for i in range(len(self.questions)):
            try:
                print(self.questions[i])
                ans=input("\nEnter Option(A/B/C):").upper()
                if ans not in ['A','B','C']:
                    raise InvalidOptionError
                if self.answers[i]==ans:
                    self.score+=1
                else:
                    print("Wrong Answer")
            except InvalidOptionError:
                print("IvalidOptionError")
        return self.score
    def display_score(self):
        print("Total Score:",self.score,"/ 8\n",end='')
c=quiz()
print("\t\t...Quiz Started...")
c.start_quiz()
print("\t\t...Quiz Finished...")
c.display_score()
