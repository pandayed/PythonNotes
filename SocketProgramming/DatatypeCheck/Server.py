import socket as so

s = so.socket()

print("socket made")

port = 1234

s.bind(('localhost', port))

s.listen(3)

print('waiting for connection')

while True:
    c, addr = s.accept()
    datarecv = c.recv(1024).decode()
    typeofdata = 'INT'
    print("Connected with client: ", addr)
    print("Data:", datarecv)
    for i in datarecv:
        if (i == '~' or i == '!' or i == '#' or i == '$' or i == '%' or i == '^' or i == '&' or i == '*'):
            typeofdata = 'Special Character'
            break
    for i in datarecv:
        if (i == '.'):
            typeofdata = 'Decimal Number'
            break
    for i in datarecv:
        if (i >= 'a' and i <= 'z'):
            typeofdata = 'String'
            break
        if (i >= 'A' and i <= 'Z'):
            typeofdata = 'String'
            break
    if (len(datarecv) == 1 and typeofdata == 'String'):
        typeofdata = 'Character'
    c.send(bytes(f"{datarecv} : {typeofdata} ", 'utf-8'))