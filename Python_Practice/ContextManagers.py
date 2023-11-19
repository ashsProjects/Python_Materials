# Uses the "with" keyword 
from contextlib import contextmanager
#Using class as a context manager
class Open_File():
    def __init__(self, filename, mode) -> None:
        self.filename = filename
        self.mode = mode
        
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, traceback) -> None:
        self.file.close()

#Using function as a context manager
@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()
    
# with open_file('sample.txt', 'w') as f:
#     f.write("Lorem ipsum")

