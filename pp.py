import subprocess

risultato = subprocess.run('echo somaro',shell = True).decode('utf-8')
print(risultato)
