import socket 
import pickle 

from tic_tac_toe import TicTacToe

#HOST = '127.0.0.1'  
HOST='192.168.63.9'
PORT = 12783       

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

client_socket, client_address = s.accept()
print(f"\nConnnected to {client_address}!")

player_x = TicTacToe("X")

rematch = True

while rematch == True:
    print(f"\n\n TIC-TAC-TOE")    
    while player_x.did_win("X") == False and player_x.did_win("O") == False and player_x.is_draw() == False:        
        print(f"\n       Your turn!")
        player_x.draw_grid()
        player_coord = input(f"Enter coordinate: ")
        player_x.edit_square(player_coord)        
        player_x.draw_grid()
        
        x_symbol_list = pickle.dumps(player_x.symbol_list)
        client_socket.send(x_symbol_list)
        
        if player_x.did_win("X") == True or player_x.is_draw() == True:
            break
        
        print(f"\nWaiting for other player...")
        o_symbol_list = client_socket.recv(1024)
        o_symbol_list = pickle.loads(o_symbol_list)
        player_x.update_symbol_list(o_symbol_list)
    
    if player_x.did_win("X") == True:
        print(f"Congrats, you won!")
        player_x.score+=1
    elif player_x.is_draw() == True:
        print(f"It's a draw!")
    else:
        print(f"Sorry, the client won.")
    
    x_score_send = pickle.dumps(player_x.score)
    client_socket.send(x_score_send)
    o_score_recv = client_socket.recv(1024)
    o_score_recv = pickle.loads(o_score_recv)
    
    print(f"\nYour score: {player_x.score}")
    print(f"Opponent score: {o_score_recv}")
    
    host_response = input(f"\nRematch? (Y/N): ")
    host_response = host_response.capitalize()
    temp_host_resp = host_response
    client_response = ""
    
    host_response = pickle.dumps(host_response)
    client_socket.send(host_response)
    
    if temp_host_resp == "N":
        rematch = False    
    else:
        print(f"Waiting for client response...")
        client_response = client_socket.recv(1024)
        client_response = pickle.loads(client_response)
        if client_response == "N":
            print(f"\nThe client does not want a rematch.")
            rematch = False
        else:
            player_x.restart()

spacer = input(f"\nThank you for playing!\nPress enter to quit...\n")

client_socket.close()