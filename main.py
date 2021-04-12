if __name__ == '__main__':
    print("Hello world")
    left1 = 24
    left2 = 23
    right1 = 22
    right2 = 27
    en = 25

    robot1 = rhode(left1, left2, right1, right2, en)
    while 1:
        ins = input()
        if ins == 'f':
            robot1.forward()
        elif ins == 'b':
            robot1.backward()
        elif ins == 's':
            robot1.stop()
        elif ins == 'r':
            robot1.turn_right()
        elif ins == 'l':
            robot1.turn_left()
        elif ins == 'e':
            robot1.stop()
            break
        else:
            print('Invalid Instruction Given!!') 
