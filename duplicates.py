from queue import Queue
import imagehash
import threading
import os

class diff_image(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            files = self.queue.get()
            self.image_different(files.split('|')[0],files.split('|')[1])        
            self.queue.task_done()   

    def image_different(self, path_1, path_2):
        try:    
            if not path_1.endswith(('.jpg', '.jpeg', 'png')):
                return None
            if not path_2.endswith(('.jpg', '.jpeg', 'png')):
                return None    
            image_1 = imagehash.Image.open(path_1)
            image_2 = imagehash.Image.open(path_2)
            hash_1 = imagehash.phash(image_1)
            hash_2 = imagehash.phash(image_2)
            if hash_2 - hash_1 < 1:
                print(path_1+' '+path_2 + " SAME")
            return hash_2 - hash_1 > 0
        except Exception as e:
            print(e)
            print(path_1)
            print(path_2)

        
def check_doubles(path):
    imgs=os.listdir(path)
    queue = Queue()   
    
    for i in range(8): 
        t = diff_image(queue)
        t.setDaemon(True)
        t.start()  
       
    check_file=0
    current_file=0

    while check_file < len(imgs):
        if current_file==check_file:
            current_file+=1
            continue
        queue.put(path+imgs[current_file]+'|'+path+imgs[check_file]) 
        current_file+=1
        if current_file==len(imgs):
            check_file+=1
            current_file=check_file   
    queue.join()

def check_existence(folder, image):
    imgs=os.listdir(folder)
    queue = Queue()

    for i in range(8): 
        t = diff_image(queue)
        t.setDaemon(True)
        t.start() 
    
    for i, file in enumerate(imgs):
        queue.put(image+"|"+folder+file)

    queue.join()

def main():
    path="D:\\hen\\"
    image = "C:\\Users\\radko\Desktop\\-68j_iX6GZU.jpg"
    #check_doubles(path)
    check_existence(path, image)

if __name__ == "__main__":
    main()
