#!/usr/bin/python3
#

try:
	from subprocess import *
	import sys

except ImportError as i_err:
	print(i_err)


def main():
	sys_cmds = ['systemctl', 'status', 'start', 'restart']
	check_srv_state = ['--type=service', '--state=active']

	#check package status.
	srv = Popen([sys_cmds[0], sys_cmds[1], sys.argv[1]], stderr=PIPE, stdout=PIPE)

	output, error = srv.communicate()

	if srv.returncode != 0:
		print(f"Error checking service status: {error.decode('utf-8')} {srv.returncode}")

		print("\n")

		print(f"Starting {sys.argv[1]} service")

		Popen([sys_cmds[0], sys_cmds[2], sys.argv[1]], stderr=PIPE, stdout=PIPE)


	else:
		print("Output")
		print("\n")
		print(f"Service nginx is running: {output.decode('utf-8')}")
main()
