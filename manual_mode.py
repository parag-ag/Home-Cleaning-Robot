def start_manual_mode(robot):
    print("f - forward, b - backward, s - stop, r - turn-right, l - turn-left, e - exit")
    while 1:
        ins = input()
        if ins == 'f':
            robot.forward()
        elif ins == 'b':
            robot.backward(1)
        elif ins == 's':
            robot.stop()
        elif ins == 'r':
            robot.turn_right(1)
        elif ins == 'l':
            robot.turn_left(1)
        elif ins == 'e':
            robot.stop()
            break
        else:
            print('Invalid Instruction Given!!') 


# if __name__ == '__main__':
#     print("Hello world")
#     left1 = 24
#     left2 = 23
#     right1 = 22
#     right2 = 27
#     en = 25

#     robot1 = rhode(left1, left2, right1, right2, en)
#     while 1:
#         ins = input()
#         if ins == 'f':
#             robot1.forward()
#         elif ins == 'b':
#             robot1.backward()
#         elif ins == 's':
#             robot1.stop()
#         elif ins == 'r':
#             robot1.turn_right()
#         elif ins == 'l':
#             robot1.turn_left()
#         elif ins == 'e':
#             robot1.stop()
#             break
#         else:
#             print('Invalid Instruction Given!!') 
