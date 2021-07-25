FROM python:3

LABEL version="1.0.0" description="Transferencia de arquivos  Servidor TCP do Kurose do Departamento DNUT" maintainer="Luiz Henrique de souza bressane <luiz.bressane@dcomp.ufs.br>"

WORKDIR /usr/src/dnutransferenciaclient

COPY . .

EXPOSE 7000

CMD ["python3", "-m", "http.server", "7000"]