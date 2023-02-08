from multiprocessing import Process
import kiosk_app as ka
import virtual_mouse as vm

def webApp():
    ka.main()
def mouse():
    vm.main()
    
p1 = Process(target=mouse)
p2 = Process(target=webApp)

if __name__ == '__main__':
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

# webApp()