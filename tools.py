import  threading , sys , time


def menu():
    choix=['0','1','2']    
 
    m="""
    ╔══════════════════════════════════════╗
    ║       PRODUCT WITH DISCOUNT          ║
    ╠══════════════════════════════════════╣
    ║ 1. Scraping data                     ║
    ║ 2. Update data base                  ║
    ║ 3. View dashboard                    ║
    ║ 0. Exit                              ║
    ╚══════════════════════════════════════╝
    """
    x = input(m)
    
    while(x not in choix):
        print('no action selected, please try again')
        x=input(m)
    return int(x)




loading_done = False
def loading_animation(msg):
    global loading_done
    i = 0
    while not loading_done:
        sys.stdout.write(f'\r {msg}' + '.' * (i % 7) + ' ' * (6 - i % 7))
        sys.stdout.flush()
        i += 1
        time.sleep(0.5)
    print('OK')

def loading(msg,slow_fn):
    global loading_done
    t = threading.Thread(target=loading_animation,args=(msg,))
    t.start()        
    data = slow_fn()
    loading_done = True
    t.join()
    loading_done=False
    return data