import socket
import time
host = input("Enter Host: ")
port = int(input("Enter port: "))
print("HTTP Security Headers")
print("--------------------------------")
start_time=time.time()
def scan_port(host,port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(100)
        try:
         s.connect((host,port))
         return "sucess"
        except (socket.timeout, socket.error):
            return "NoT RECOGNIZED","NONE"
def check_http(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
           s.settimeout(100)
           try:
            s.connect((host,port))
            request = (
            f"GET / HTTP/1.1\r\n"
            f"Host: {host}\r\n"
            f"Connection: close\r\n"
             f"\r\n")
            s.sendall(request.encode())
            response=s.recv(4024)
            text=response.decode()
            for line in text.splitlines():
                if "HTTP/" in line:
                    return text
            return "NoT RECOGNIZED","NONE" 
           except (socket.timeout, socket.error):
               return "NoT RECOGNIZED","NONE"
def check_security_headers(text):
     security_headers = {}
     security_headers["X-Frame-Options"]="MISSING"
     security_headers["Content-Security-Policy"]="MISSING"
     security_headers["Strict-Transport-Security"]="MISSING"
     security_headers["X-Content-Type-Options"]="MISSING"
     for line in text.splitlines():
            if line.startswith("X-Frame-Options:") :
                value = line.split(":", 1)[1].strip()
                security_headers["X-Frame-Options"] = value
            elif line.startswith("Content-Security-Policy:"):
                value = line.split(":", 1)[1].strip()
                security_headers["Content-Security-Policy"] = value
            elif line.startswith("Strict-Transport-Security:"):
                value = line.split(":", 1)[1].strip()
                security_headers["Strict-Transport-Security"] = value
            elif line.startswith("X-Content-Type-Options:"):
                value = line.split(":", 1)[1].strip()
                security_headers["X-Content-Type-Options"] = value     
     return security_headers
 
open_port=scan_port(host,port)
if open_port == "sucess":
    text=check_http(host, port)
    security = check_security_headers(text)
    for header, value in security.items():
       print(f"{header}: {value}")
end_time=time.time()
total_time=end_time - start_time
print(f"Open_port:{open_port}")
print(f"total time:{total_time:.2f}second")
              
            
