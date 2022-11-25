class fispy:
    #some random init
    precise_operate = True
    precision = 4
    def __init__(self):
        pass
    
    #expression simplifier,
    def simplify(self,_result):
        result = None
        if self.precision == None or not self.precision >=1:
            print("ERROR: PRECISION DIMENSION!")
            return
        try:
            
            if self.precise_operate == True:

                if (float(_result[0]))>= 0:
                    if float(_result[0]) >= 1.0:
                        if _result[1]<0:
                            simp_status = _result[0]
                            index = 0
                            while simp_status >=9:
                                simp_status = simp_status/10
                                index += +1
                            result = (f"{simp_status}E{_result[1]+index}")
                        else:
                            simp_status = _result[0]
                            index = 0
                            while simp_status >=9:
                                simp_status = simp_status/10
                                index += 1
                            result = (f"{simp_status}E{_result[1]+index}")
                        
                    elif float(_result[0]) < 1.0:
                        simp_status = _result[0]
                        index = 1
                        print(simp_status)
                        while simp_status <=0:
                            simp_status = simp_status*10
                            index += 1
                        result =(f"{simp_status}E{_result[1]-index}")
                else :
                    simp_status = -_result[0]
                    index = 0
                    while simp_status >=9:
                        simp_status = simp_status/10
                        index += 1
                    
                    result =(f"{-simp_status}E{_result[1]+index}")
                    res = str(result).split('.')
                    result =(f"{res[1][:self.precision]}")#{_result[1]+index}")
                    print(f"{res[0]}.{result}")
                    return
                
                res = str(result).split('.')
                result =(f"{res[1][:self.precision]}")#{_result[1]+index}")
                print(f"{res[0]}.{result}")
               
            else:
                
                    res = str(_result[0]).split('.')
                    result =(f"{res[1][:self.precision]}")#{_result[1]-index}")
                    print(f"{res[0]}.{result}")
            
        except:
            
            res = str(_result).split('.')
            result =(f"{res[1][:self.precision]}")
            print(f"{res[0]}.{result}")
    #once i finished uploading the tables, will actually do conversions
    def conversion(self,arg1,arg2):
        operator, unit = arg1
        destination_unit = arg2

    #basic scientific notation operations
    def operation(self,arg1, arg2, operation):
        try:

            if "e" in arg1.lower():
                operand = [float(arg1.lower().split("e")[0]),int(arg1.lower().split("e")[1])]
            else:
                operand = [float(arg1.lower()),0]
                
            if "e" in arg2.lower():
                operand_ = [float(arg2.lower().split("e")[0]),int(arg2.lower().split("e")[1])] 
            else:
                operand_ = [float(arg2.lower()),0]
            
        except Exception as E:
            print(f"{E}ERROR: Invalid input")
        
        if operation == "*":
            result = self.multiplicate(operand,operand_)
            self.simplify((result[0],result[1]))
        if operation == "/":
            result = self.divide(operand_,operand)
            if result[1]!=0:
                self.simplify((result[0],result[1]))
            else:
                self.simplify((result[0]))
        if operation == "+":
            result = self.sum(operand,operand_)
            self.simplify((result[0],result[1]))
        if operation == "-":
            result = self.sub(operand,operand_)
            self.simplify((result[0],result[1]))
    #some unit multipliers equivalences
    def equality(self,arg1, arg2, operation):
        pass 
    
    #all the operations
    def multiplicate(self,ope_,ope):
        return (ope[0]*ope_[0],ope[1]+ope_[1])
    def divide(self,ope_,ope):
        return (ope[0]/ope_[0],ope[1]-ope_[1])
    
    def sum(self,ope_,ope):
        if ope[1]< ope_[1]:
            threshold = ope[1]
            var_ = ope
            var = ope_
            
            while var[1] > threshold:
                var[1] =  var[1]-1
                var[0] = var[0] * 10

            return (var[0]+var_[0],threshold)
        
        if ope_[1]< ope[1]:
            threshold = ope_[1]
            var_ = ope_
            var = ope

            while var[1] > threshold:
                var[1] =  var[1]-1
                var[0] = var[0] * 10
            return (ope_[0]+var[0],threshold)
    
    def sub(self,ope_,ope):
        if ope[1]< ope_[1]:
            threshold = ope[1]
            var_ = ope
            var = ope_
            while var[1] > threshold:
                var[1] =  var[1]-1
                var[0] = var[0] * 10
            return (var[0]-var_[0],threshold)
        
        if ope_[1]< ope[1]:
            threshold = ope_[1]
            var_ = ope_
            var = ope

            while var[1] > threshold:
                var[1] =  var[1]-1
                var[0] = var[0] * 10
            return (ope_[0]-var[0],threshold)


if __name__ =="__main__":

    operator = fispy()
    operator.operation("2e7","5e24","*")