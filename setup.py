import sys, os

try:
	env = sys.argv[1]
except:
	env = "production"

os.system('pip install -r requirements.txt')
os.system('gunicorn app:app -b 0.0.0.0:5100')