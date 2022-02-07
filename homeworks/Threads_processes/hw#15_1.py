import threading


def get_thread_count():
    return threading.active_count()


def print_smt(smt):
    print(f'Printing {smt}')


first = threading.Thread(target=print_smt, args=['smtsmt1', ])
second = threading.Thread(target=print_smt, args=['smtsmt2', ])

print(f"Active thread count before start: {get_thread_count()}")
first.start()
second.start()
print(f"Active thread before join: {get_thread_count()}")
first.join()
second.join()
print(f"All threads: {get_thread_count()} ")
