from dlgo.gotypes import  Player
#获取各自的分数
#帖子


#获取气

class grade():
    def __init__(self,grid):
        self.pointBlack=set()
        self.gasBlack=set()
        self.pointWhite=set()
        self.gasWhite=set()
        self.go_post=7.5
        self.grades={Player.black:{},Player.white:{}}
        for key,value in grid.items():
            if value is None or value.color is None :
                continue

            if value.color==Player.black:
                #print(value.stones)
                #print('pointBlack：',self.pointBlack)
                if value.stones is not None :
                    self.pointBlack=self.pointBlack.union(value.stones)
                if value.liberties is not None:
                    print(value.liberties)
                    self.gasBlack=self.gasBlack.union(value.liberties)
            if value.color == Player.white:
                #print(value.stones)
                #print('pointBlack：', self.pointWhite)
                if value.stones is not None:
                    self.pointWhite = self.pointWhite.union(value.stones)
                if value.liberties is not None:
                    self.gasWhite = self.gasWhite.union(value.liberties)
        self.grades = {Player.black: {'gas':len( self.gasBlack),'point':len(self.pointBlack),'go_post':0},
                      Player.white: {'gas':len( self.gasWhite),'point':len(self.pointWhite),'go_post':7.5 } }
        if len( self.gasBlack)+len(self.pointBlack)>len( self.gasWhite)+len(self.pointWhite)+self.go_post:
            self.winner='black'
        else:
            self.winner='white'
        self.message='winner is '+self.winner+':'+ str(len( self.gasBlack))+' '+str(len(self.pointBlack))+' ,'+str(len( self.gasWhite))+' '+str(len(self.pointWhite))

    # print('------start-----')
    # print(key, value)
    # print(value.color)
    # print('value.liberties:',len(value.liberties))
    # print('value.stones:',value.stones)
    # print('-------end----')
#
