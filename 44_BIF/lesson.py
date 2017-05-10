import time as t

class MyTimer():
    def __init__(self):
        self.unit=['year','month','day','hour','min','sec']
        self.prompt='not yet!'
        self.lasted=[]
        self.begin=0
        self.end=0
    def __str__(self):
        return self.prompt

    __repr__=__str__

    def __add__(self,other):
        prompt='total'
        result=[]
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt

    def start(self):
        self.begin=t.localtime()
        self.prompt='please stop first'
        print('start!!')

    def stop(self):
        if not self.begin:
            print('please start first')
        else:
            self.end=t.localtime()
            self._calc()
            print('count end!!')

    def _calc(self):
        self.lasted=[]
        self.prompt='total'

        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            self.prompt+=str(self.lasted[index])


m1=MyTimer()
m1.start()


m2=MyTimer()
m2.start()
