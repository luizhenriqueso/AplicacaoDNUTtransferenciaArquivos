import socket
import threading
import os

import buffer

HOST = '127.0.0.1'
PORT = 44414

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

with s:
    sbuf = buffer.Buffer(s)

    hash_type = 'a'

    files = input('Digite o nome dos arquivos: ')
    files_to_send = files.split()

    for file_name in files_to_send:
        print(file_name)
        sbuf.put_utf8(hash_type)
        sbuf.put_utf8(file_name)

        file_size = os.path.getsize(file_name)
        sbuf.put_utf8(str(file_size))

        with open(file_name, 'rb') as f:
            sbuf.put_bytes(f.read())
        print('arquivo enviado')
