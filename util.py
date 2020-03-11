lines=[]
with open('file.txt','r') as f:
	lines = [line.rstrip() for line in f]
	

func=dict()
for item in lines:
	flag=0
	s=''
	for c in item:
		if(c=='('):
			flag=1
			break
		s+=c
	if(flag==1):
		if not func.get(s):
			func[s]=0
		func[s]=func[s]+1
	

print(func)
