# ctrl.py

class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self):    
        # Placeholder for calculation logic
        pass    
            
    def connectSignals(self):
        #self.view.btn1.clicked.connect(self.view.activateMessage) 
        self.view.btn1.clicked.connect(self.calculate)  
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def sum(self, a, b):    # 예외 처리 추가
        try:
            return str(a + b)
        except:
            return 'Caiculation Error'
        
    

