import sys , os
import paramiko

fld = os.path.join(os.path.expanduser('~'),'usr')
host = sys.argv[1]
port = int(sys.argv[2])
command = sys.argv[3]
uname = 'Orest'
passwd = '123'


def mkdir(self, fld, mode=551):
	path = self._adjust_cwd(fld)
	try:
		for i in range(1,21):
			self._log(DEBUG, 'mkdir(%r, %r)' % (path, mode))
	attr = SFTPAttributes()
	attr.st_mode = mode
	self._request(CMD_MKDIR, path, attr)


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port=port, username=uname, password=passwd) 
stdin, stdout, stderr = ssh.exec_command(function())

print stdout.read()

ssh.close()


