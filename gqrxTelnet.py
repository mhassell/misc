import telnetlib

HOST = '127.0.0.1'
port = 7356

tn = telnetlib.Telnet(HOST, port=port)
tn.open(HOST, port=port)
tn.write('f')
tn.read_eager()
tn.close()
