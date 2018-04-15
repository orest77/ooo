import sys , os
import paramiko

fld = os.path.join(os.path.expanduser('~'),'usr')
host = sys.argv[1]
port = int(sys.argv[2])
command = sys.argv[3]
uname = 'Orest'
passwd = '123'


def function():
	try:
		for i in range(1,21):
			os.mkdir(fld + str(i),551)
	except OSError:
    	print('Oops, error!')
	else:
    	print('Folder is created')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port=port, username=uname, password=passwd) 
stdin, stdout, stderr = ssh.exec_command(function())

print stdout.read()

ssh.close()