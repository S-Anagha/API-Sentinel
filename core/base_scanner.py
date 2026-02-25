class BaseScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def run(self):
        raise NotImplementedError("Scanner must implement run() method.")