pasta = []
juice = []
for _ in range(3):
    pasta.append(int(input()))
    
for _ in range(2):
    juice.append(int(input()))
    
print(round((min(pasta)+min(juice))*1.1,1))