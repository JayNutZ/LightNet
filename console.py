
class Console:
    filename = 'console.log'
    
    def __init__(self):
        self.log('')

    def log(self, msg):
        with open(self.filename, 'a') as console:
            console.write(msg + '\n')
