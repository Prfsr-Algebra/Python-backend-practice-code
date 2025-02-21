class school:
    def __init__(self, name: str):
        self.name = name
    def status(self):
        print(f"you've been employed mr(s) {self.name}")
class teacher(school):
    def __init__(self, name: str):
        super().__init__(name)
class worker(teacher):
    def __init__(self, name: str):
        super().__init__(name)
new_worker = worker("Muhammad")
new_worker.status()
