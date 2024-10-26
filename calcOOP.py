class Calculator:
    def __init__(self,query):
        self.entry=str(query)
        self.caller()
        
    def caller(self):
        signs=['+','-','*','/']
        for i in signs:
            if i in self.entry:
                splited_entry=self.entry.split(f"{i}")
                a=splited_entry[0]
                b=splited_entry[-1]
                if i=="+":
                    self.add(a,b)
                elif i=="-":
                    self.sub(a,b)
                elif i=="*":
                    self.mul(a,b)
                elif i=="/":
                    self.div(a,b)
                else:
                    return 'Sorry, your input is not supported'
    
    
    def add(self,a,b):
        print(int(a) + int(b))
    def sub(self,a,b):
        print(int(a) - int(b))
    def mul(self,a,b):
        print(int(a) * int(b))
    def div(self,a,b):
        print(int(a) / int(b))
        
        
query=input('Enter the math\n')
Calculator(query)
        

