import sys

if __name__ == "__main__":

    tests = sys.stdin.readline().strip()
    
    tests = int(tests)

    for test in range(tests):

       a = sys.stdin.readline().strip()
       b = sys.stdin.readline().strip()
    
       match_str = "" 
   
       # each sample has identical length - pick one 
       for char in range(len(a)):
            if(a[char] == b[char]):
                match_str += "."
            else:
                match_str += "*"

       match_str += "\n"

       print(a)
       print(b)
       print(match_str)

             

