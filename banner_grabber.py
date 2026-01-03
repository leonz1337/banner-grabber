import socket
import threading
import time

host = input("Enter the host:")
ip = socket.gethostbyname(host)

def scan_port(port):
    try:
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.2)
        s.connect((host_ip, port))
        try:
            banner = s.recv(1024).decode()
            print("port {} is open with banner {}".format(port, banner))

        except:
            print("port {} is open ".format(port))

    except:
        pass

start_time = time.time()


for i in range(1,65535+1):
    thread1 = threading.Thread(target=scan_port, args=[i])
    thread1.start()


end_time = time.time()
print(f"Time Duration :{end_time-start_time}")
