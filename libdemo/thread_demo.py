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
print("\nNo. of threads : ", th.active_count() ,"\n")

print("\nWaiting for threads to terminate\n")

t1.join()  # wait until t1 is terminated
t2.join()  # wait until t2 is terminated

# for t in th.enumerate():
#     print(t)

print("End of main")