def hcf(x,y):
    if x > y :
        x,y = y,x 
    if x == y:
        return x
    return hcf(x,y-x)


def lcm(x,y):
    return x*y // hcf(x,y)


def generate_answers(filename):
     with open(filename) as f:
        for line in f:
            curr_line = line.rstrip('\n')
            quest,x,y = curr_line.split(' ')
            x = int(x)
            y = int(y)
            ans = None
            if quest == "HCF":
                ans = hcf(x,y)
            if quest == "LCM":
                ans = lcm(x,y)
            
            if quest not in ["LCM","HCF"]:
                raise ValueError("question should be only HCF or LCM")
            print(f"{quest} {x} {y} = {ans}",end="\r\n")


if __name__== '__main__':
    generate_answers('data/questions.txt')
   
    
    
