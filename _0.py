def _0():
    for row in range(7):
        for col in range(5):
            if ((col==0 or col==4) and (row!=0 and row!=6)) or (col>0 and col<4) and (row==0 or row==6) or (row+col==5):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
