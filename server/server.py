import socket
import os

import buffer

HOST = ''
PORT = 12000

# If server and client run in same local directory,
# need a separate place to store the uploads.
try:
    os.mkdir('uploads')
except FileExistsError:
    pass

s = socket.socket()
s.bind((HOST, PORT))
s.listen(10)
print("Esperando por uma conexao.....")

while True:
    conn, addr = s.accept()
    print("Got a connection from ", addr)
    connbuf = buffer.Buffer(conn)

    while True:
        hash_type = connbuf.get_utf8()
        if not hash_type:
            break
        print('hash type: ', hash_type)

        file_name = connbuf.get_utf8()
        if not file_name:
            break
        file_name = os.path.join('uploads',file_name)
        print('Nome do arquivo: ', file_name)
        try:
            file_size = int(connbuf.get_utf8())
        except ValueError:
            file_size = 0
            pass
        print('Tamanho do arquivo: ', file_size, 'Bytes')

        with open(file_name, 'wb') as f:
            remaining = file_size
            while remaining:
                chunk_size = 4096 if remaining >= 4096 else remaining
                chunk = connbuf.get_bytes(chunk_size)
                if not chunk: break
                f.write(chunk)
                remaining -= len(chunk)
            if remaining:
                print('Arquivo recebido.  Missing',remaining,'bytes.')
            else:
                print('Arquivo recebido.')
    print('Conexao fechada.')
    conn.close()
