import os
import subprocess

def listdir(dir):
  cmd = 'ls -l ' + dir
  print("Command to run:", cmd)   ## good to debug cmd before actually running it
  #(status, output) = subprocess.getstatusoutput(cmd)
  #if status:    ## Error case, print the command's output to stderr and exit
    #sys.stderr.write(output)
    #sys.exit(status)
  #print (output) 

def main():
	listdir('mysite')

if __name__ == '__main__':
	main()