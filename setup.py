import sys, os

try:
	env = sys.argv[1]
except:
	env = "production"

os.system('pip install -r requirements.txt')
os.system('flask run --port 5100')