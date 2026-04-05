import threading


def print_numbers():
    for i in range(100):
        print(i)


my_thread1 = threading.Thread(target=print_numbers)
my_thread2 = threading.Thread(target=print_numbers)

my_thread1.start()
my_thread2.start()

my_thread1.join()
my_thread2.join()

