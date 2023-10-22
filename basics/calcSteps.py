
seed =6
ttl =0
for floor in range(100):
    if (floor < 5):
        ttl +=seed    
        seed+=3            
    else: 
        ttl+=seed
        seed+=7
	
print("total: {}".format(ttl))
	