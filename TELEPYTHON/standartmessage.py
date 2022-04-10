
def standartmessagecoding (normalsend):
    
        
    for i in range(len(normalsend)+1):
        
        if normalsend[i]=="a":
            normalsend=normalsend.replace("a", "000")
            
        if normalsend[i]=="b":
            normalsend=normalsend.replace("b", "001") 
            
        if normalsend[i]=="c":
            normalsend=normalsend.replace("c", "010") 
            
        if normalsend[i]=="d":
            normalsend=normalsend.replace("d", "011")
            
        if normalsend[i]=="e":
            normalsend=normalsend.replace("e", "100") 
            
        if normalsend[i]=="f":
            normalsend=normalsend.replace("f", "101") 
            
        if normalsend[i]=="g":
            normalsend=normalsend.replace("g", "110") 
            
            
        
    
            
 
    return normalsend