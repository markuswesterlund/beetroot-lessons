"""
Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.

You can reassign this value, but you should check whether the new value is Boss.
Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss.
You're not allowed to add instances of Boss class to workers list directly via access to attribute,
use getters and setters instead!

You can refactor the existing code.

id_ - is just a random unique integer
class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []
class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss
"""


class Boss:

    def __init__(self, id_, name, company):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def get_full_info(self):
        return f"id: {self.id}, name: {self.name}, company: {self.company}"

    def add_worker(self, worker):
        if worker not in self.workers:
            self.workers.append(worker)

    def remove_worker(self, worker):
        if worker in self.workers:
            self.workers.remove(worker)

    def print_workers(self):
        print("Worker list:")
        for worker in self.workers:
            print(f"{worker.id}: {worker.name}")


class Worker:

    def __init__(self, id_, name, company, boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    def get_boss(self):
        return f"Boss of {self.name} is: {self.boss}"

    def get_full_info(self):
        return f"id: {self.id}, name: {self.name}, company: {self.company}, boss: {self.boss}"


wor_1 = Worker(5, "Markus", "Microsoft", "Bill Gates")
wor_2 = Worker(6, "Joakim", "Microsoft", "Bill Gates")
boss_1 = Boss(1, "Bill Gates", "Microsoft")

boss_1.add_worker(wor_2)
boss_1.print_workers()
boss_1.add_worker(wor_1)
boss_1.print_workers()
boss_1.remove_worker(wor_2)
boss_1.print_workers()

print("")
print(wor_1.get_boss())
print(wor_1.get_full_info())
print(boss_1.get_full_info())

