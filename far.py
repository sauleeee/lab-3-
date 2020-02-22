import os
def error(e):
    print("ERROR:" + str(e))
def help():
    print("1) cd path - walk to directory")
    print("2) rename )
    print("1) ls -f ")
    print("1) ls -d")
    print("1) mkdir ./ +name")
    print("1) rm -d name")
    
os.chdir('.')


while True:
    cmd = input(os.path.abspath('.') + ": ").split()
    if cmd[0] == 'cd':   
        try:
            os.chdir("./" + cmd[1])
        except Exception as e:
            error(e)

    elif cmd[0] == 'ls':  
        try:
            if cmd[1] == '-f':  
                for root, dirs, files in os.walk("."):
                    print(len(files))
                    break
            elif cmd[1] == '-d': 
                for root, dirs, files in os.walk("."):
                    print(len(dirs))
                    break
            else:
                print(os.listdir()) 
        except:
            print(os.listdir()) 
        

    elif cmd[0] == 'mkdir':  
        os.mkdir('./' + cmd[1])



    elif cmd[0] == 'rm':    

        if cmd[1] == '-d':    
            try:
                os.rmdir("./" + cmd[2])   
            except Exception as e:
                error(e)
        elif cmd[1] == '-f':  
            try:
                os.remove("./" + cmd[2])
            except Exception as e:
                error(e)
        else:
            print("command not found")
    
    elif cmd[0] == 'rename': 
        try:
            os.rename(cmd[1], cmd[2])
        except Exception as e:
            error(e)
        
    elif cmd[0] == 'open':
        try:
            f = open(cmd[1], cmd[2])
            if cmd[2] == 'r': 
                print(f.read())  
            else:             
                text = input("Enter text to write:")
                f.write(text + '\n')
            f.close()
        except Exception as e:
            error(e)
    elif cmd[0] == 'help':
        help()
     


    
    