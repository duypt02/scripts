import socket
import sys
import itertools

des = "192.168.113.139" # change IP

def return_port(raw):
    if len(raw) < 0:
        return None
    
    raw = raw.decode("utf-8")
    raw = raw.replace('[', '')
    raw = raw.replace(']', '')
    raw_list = raw.split(',')
    
    ports=[]
    for i in raw_list:
        ports.append(int(i))
        
    return ports

def get_port():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((des, 1337))
    except Exception as ex:
        sys.exit()
        
    raw_list = sock.recv(24)
    
    ports = return_port(raw_list)
    
    # Sau khi lấy được port trả về, sẽ kết nối với từng port đó
    for i in itertools.permutations(ports):
        for j in i:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            print(j)
            sock.connect_ex((des, j))
            sock.close()
    
def main():
    get_port()
    

if __name__=='__main__':
    main()

#bc_ngductung