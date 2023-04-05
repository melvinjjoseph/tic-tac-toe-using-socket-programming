import socket 
import pickle 

from tic_tac_toe import TicTacToe

HOST = '127.0.0.1'  
PORT = 12783        

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print(f"\nConnected to {s.getsockname()}!")

player_o = TicTacToe("O")

rematch = True
while rematch == True:    
    print(f"\n\n TIC-TAC-TOE")
    player_o.draw_grid()    
    print(f"\nWaiting for other player...")
    x_symbol_list = s.recv(1024)
    x_symbol_list = pickle.loads(x_symbol_list)
    player_o.update_symbol_list(x_symbol_list)
    while player_o.did_win("O") == False and player_o.did_win("X") == False and player_o.is_draw() == False:
        print(f"\n       Your turn!")
        player_o.draw_grid()
        player_coord = input(f"Enter coordinate: ")
        player_o.edit_square(player_coord)
        player_o.draw_grid()
        o_symbol_list = pickle.dumps(player_o.symbol_list)
        s.send(o_symbol_list)
        
        if player_o.did_win("O") == True or player_o.is_draw() == True:
            break

        print(f"\nWaiting for other player...")
        x_symbol_list = s.recv(1024)
        x_symbol_list = pickle.loads(x_symbol_list)
        player_o.update_symbol_list(x_symbol_list)

    if player_o.did_win("O") == True:
        print(f"Congrats, you won!")
        player_o.score += 1
    elif player_o.is_draw() == True:
        print(f"It's a draw!")
    else:
        print(f"Sorry, the host won.")

    x_score_recv = s.recv(1024)
    x_score_recv = pickle.loads(x_score_recv)
    o_score_send = pickle.dumps(player_o.score)
    s.send(o_score_send)

    print(f"\nYour score: {player_o.score}")
    print(f"Opponent score: {x_score_recv}")

    print(f"\nWaiting for host...")
    host_response = s.recv(1024)
    host_response = pickle.loads(host_response)
    client_response = "N"
    
    if host_response == "Y":
        print(f"\nThe host would like a rematch!")
        client_response = input("Rematch? (Y/N): ")
        client_response = client_response.capitalize()
        temp_client_resp = client_response
        
        client_response = pickle.dumps(client_response)
        s.send(client_response)

        if temp_client_resp == "Y":
            player_o.restart()
        else:
            rematch = False
    else:
        print(f"\nThe host does not want a rematch.")
        rematch = False

spacer = input(f"\nThank you for playing!\nPress enter to quit...\n")

s.close()