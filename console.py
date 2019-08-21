class Console:
    filename = 'console.log'
    
    def __init__(self):
        self.log('')

    def log(self, msg):
        with open(self.filename, 'w+') as console:
            full = console.read() + '\n' + msg
            console.write(full)
