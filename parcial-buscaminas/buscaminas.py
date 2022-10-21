

from re import A


class Buscaminas():
    def __init__(self,rows,columns,bombs):
        self.rows=rows
        self.columns=columns
        self.bombs=bombs
        self.board= [([" "]*8) for i in range(8)]
        self.caso1=None
        self.caso2=None
        self.show=None

    def setUp(self):
        self.caso1 = [['2', 'B', '2', ' ', '1', 'B', 'B', '1'],
                      ['3', 'B', '3', ' ', '1', '3', '3', '2'],
                      ['3', 'B', '3', ' ', ' ', '1', 'B', '1'],
                      ['4', 'B', '3', ' ', ' ', '1', '1', '1'],
                      ['B', 'B', '2', ' ', ' ', ' ', ' ', ' '],
                      ['2', '2', '1', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', '1', '1', '1', ' ', ' ', ' '],
                      [' ', ' ', '1', 'B', '1', ' ', ' ', ' ']]
        self.board=self.caso1

    def win(self):
        count=0
        for i in range(8):
            for j in range (8):
                if self.board[i][j]=="B" and self.show[i][j]=="F":
                    count=count+1
        print(count)            
        if count == self.bombs:
            return True
        else:
            return False
    def lose(self):
        for i in range(8):
            for j in range (8):    
                if self.show[i][j]=="B":
                    return True
        return False    

    def question(self,movs):
       #desarrollar logica por si el pelotudo selecciona una bomba
       # tiene que levantar una excepcion 
        mov=str(input("seleccione el tipo de jugada"))

        row=int(input("seleccione la fila de su jugada"))

        col=int(input("seleccione la columna de su jugada"))

        return mov,row,col
       

    def play(self,mov,row,col):
        if mov == 'uncover':
            self.show[row][col] =str(self.board[row][col])
        if mov == 'flag':
            self.show[row][col] = 'F'
        for i in range (8):
            print(self.board[i])
    
    def play_to_show():
        pass


    
    def proximity_bombs(self):
        count=0
 
        for i in range(7):
            for j in range (7):
                if self.board[i][j]==" " and self.board[i+1][j]=="B":
                    count=count+1
                   
                if self.board[i][j]==" " and self.board[i-1][j]=="B":
                    count=count+1
                   
                if self.board[i][j]==" " and self.board[i][j+1]=="B":
                    count=count+1 
                  
                if self.board[i][j]==" " and self.board[i][j-1]=="B":
                    count=count+1
                    
                if self.board[i][j]==" " and self.board[i+1][j-1]=="B":
                    count=count+1 
                  
                if self.board[i][j]==" " and self.board[i+1][j+1]=="B":
                    count=count+1 
                  
                if self.board[i][j]==" " and self.board[i-1][j-1]=="B":
                    count=count+1
                    
                if self.board[i][j]==" " and self.board[i-1][j+1]=="B":
                    count=count+1
                    
                if count !=0:
                    self.board[i][j]=count
                count=0                 
        
    def set(self):
        self.board[4][4]="B"
        self.board[3][4]="B"


#a1=Buscaminas(8,8,10)    
#a1.set()
#print(a1.caso1)
#a1.proximity_bombs()
#for i in range (8):
#     print(a1.board[i])