class cline:
    def __init__(self,first="") -> None:
        self.first=first
        self.empty=first==""
        if self.empty:
            self.data=""
        else:
            self.data="<"+first+">"
    def add(self,data):
        self.data+=data
    def finish(self):
        if not self.empty:
            self.data+="</"+self.first+">"
        return self.data

tags=["style","p","body","html","script","h1","h2","h3","h4","h5","link"]

def translate(script):
    outs=[]
    for line in script.split("\n"):
        if line.split(" ")[0] in tags:
            if line[-1]==">":
                outs.append("<"+line)
                continue
            line_obj=cline(line.split(" ")[0])
            line=line[len(line.split(" ")[0])+1:]
        else:
            line_obj=cline()
        line_obj.add(line)
        outs.append(line_obj.finish()+"\n")
    return ''.join(outs)
if __name__=="__main__":
    script=open("pre.html").read()
    print(translate(script))