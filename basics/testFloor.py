
seed =5
ttl =0
for floor in range(10):
    if (floor < 4):
        ttl +=seed    
        seed+=2            
    else: 
        ttl+=seed
        seed+=7
	
print("total: {}".format(ttl))