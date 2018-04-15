import sys , os
import paramiko

fld = os.path.join(os.path.expanduser('~'),'usr')
host = sys.argv[1]
port = int(sys.argv[2])
command = sys.argv[3]
uname = 'root'
passwd = 'orest777777'




ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port=port, username=uname, password=passwd) 
stdin, stdout, stderr = ssh.exec_command('mkdir -p ' + fld)

print stdout.read()

ssh.close()

transport = paramiko.Transport((host, 22))
transport.connect(username=uname, password=passwd)

sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put(local_path, remote_path)
sftp.close()

transport.close()
