import subprocess, shlex
from datetime import datetime 
import socket

#Creo una funcion principal

def principal():

  nombreso=subprocess.run(shlex.split('uname -a'), stdout=subprocess.PIPE, shell=True)

  version_so=subprocess.run(shlex.split('uname -r'), stdout=subprocess.PIPE, shell=True)

  usuarios_activos=subprocess.run(shlex.split('w'), stdout=subprocess.PIPE, shell=True)

  info_cpu=subprocess.run(shlex.split('lscpu'), stdout=subprocess.PIPE, shell=True)

  listado_procesos=subprocess.run(shlex.split('ps aux'), stdout=subprocess.PIPE, shell=True)

  server_name=subprocess.run(shlex.split('hostname -i'), stdout=subprocess.PIPE, shell=True)

  jsonresultado = [
    [{'nombre_servidor': server_name.stdout.decode("utf-8")},
        {'info_servidor': [{'info_cpu': info_cpu.stdout.decode("utf-8")},
          {'listado_procesos': listado_procesos.stdout.decode("utf-8")},
          {'usuarios_activos': usuarios_activos.stdout.decode("utf-8")},
          {'nombreso': nombreso.stdout.decode("utf-8")},
          {'version_so': version_so.stdout.decode("utf-8")}
        ]}
    ]
      
  ]

  return jsonresultado

def servername():
  ip=socket.gethostbyname(socket.gethostname())
  

  return ip

def fecha_servidor():
  
  fecha_server=datetime.today().strftime('%Y-%m-%d')

  return fecha_server

principal()
servername()
fecha_servidor()
