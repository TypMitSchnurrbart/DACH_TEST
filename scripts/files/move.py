#!/usr/bin/python3
#!-*- coding: utf-8 -*-

from files.const import DATA_HANDLE

def make_move(data_array):
    """
    Insert the Move into the Database
    param:  {array} data_array
    return
    """
    #Data_array looks like this: [['email', 'test@mail.de'], ['raum', 'H213b'], ['next_param', 'from_move']]

    #Get IDs out of the data_array
    DATA_HANDLE[0].execute(f"""SELECT uid FROM user WHERE email LIKE '{data_array[0][1]}'""")
    user_id = DATA_HANDLE[0].fetchall()
    DATA_HANDLE[0].execute(f"""SELECT room_id FROM room WHERE description LIKE '{data_array[1][1]}'""")
    room_id = DATA_HANDLE[0].fetchall()

    if user_id == [] or room_id == []:
        print("Error. Unknown User or Room. This should not be possible considering that every move comes from the app, therefore user should be existing and room-string comes from QR Code")
        return 

    user_id = user_id[0][0]
    room_id = room_id[0][0]


    #Make sure Person isnt already logged in another room; if so log out of last room and login in current
    DATA_HANDLE[0].execute(f"""SELECT move_id, room FROM movement WHERE person = {user_id} AND end IS NULL""")
    old_move = DATA_HANDLE[0].fetchall()                                                                        #old_move should look like this: [(move_id, room)]
   
    #New Login into a room
    if old_move == []:
        DATA_HANDLE[0].execute(f"""INSERT INTO movement (person, room, date, begin) VALUES ({user_id}, {room_id}, CURDATE(), CURTIME())""")
    
    #Logout of an room
    elif old_move[0][1] == room_id:
        DATA_HANDLE[0].execute(f"""UPDATE movement SET end = CURTIME() WHERE move_id = {old_move[0][0]}""")

    #Forgot to logout of old room and try to login in new room
    elif old_move[0][1] != room_id:
        DATA_HANDLE[0].execute(f"""UPDATE movement SET end = CURTIME() WHERE move_id = {old_move[0][0]}""")
        DATA_HANDLE[0].execute(f"""INSERT INTO movement (person, room, date, begin) VALUES ({user_id}, {room_id}, CURDATE(), CURTIME())""")

    
    print("Done. <br/> This is a Testpage for Movement.")
    #TODO Here we could implement the delete of 14?-day old info

    return