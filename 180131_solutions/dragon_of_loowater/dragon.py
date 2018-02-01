
import sys


if __name__ == "__main__":

    while 1:
     
        line = sys.stdin.readline().strip()
 
        if line == "0 0":
            exit()
        
        else: 

            (heads, knights) = line.split(" ")

            heads = int(heads)
            knights = int(knights)

            headlist = []
            knightlist = []

            for i in range(int(heads)):
                headlist.append( int( sys.stdin.readline() ) )

            for j in range(int(knights)):
                knightlist.append( int( sys.stdin.readline() ) )

            headlist.sort()
            knightlist.sort() 

            cost = 0

            head = 0
            knight = 0

            while( head < len(headlist) and knight < len(knightlist)):
               
                if(headlist[head] <= knightlist[knight]):
                    cost += knightlist[knight]
                    head += 1
                    knight += 1
                else:
                    knight += 1

            if( head < len(headlist) ):
                print("Loowater is doomed!")
            else:
                print cost 

