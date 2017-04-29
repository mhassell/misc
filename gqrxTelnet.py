import telnetlib

host = '127.0.0.1'
port = 7356

tn = telnetlib.Telnet(host, port)
tn.write('f\n'.encode('ascii'))
response = tn.read_some().decode('ascii').strip()
print response
tn.write('c\n'.encode('ascii'))
tn.close()
