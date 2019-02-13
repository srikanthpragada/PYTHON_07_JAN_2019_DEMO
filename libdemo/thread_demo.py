import threading as th


class ChildThread(th.Thread):
    def run(self):
        for i in range(1, 11):
            print(i)


print(th.current_thread().name)
t1 = ChildThread()
t2 = ChildThread()
t1.start()
t2.start()
print("Back in main")
print("End of main")