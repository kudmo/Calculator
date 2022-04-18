import math
import re
from typing import Union,Optional

from numpy import mat

class Trigonomethry():
    """
    This class describes trigonometric functions of increased accuracy on tabular values
    """
    @staticmethod
    def new_sin(x):
        p = math.pi
        if x%(p)==0:
            return 0
        elif x%(2*p)==p/6 or x%(2*p)==5*p/6:
            return 0.5
        elif x%(2*p)==p+p/6 or x%(2*p)==p+5*p/6:
            return -0.5
        else:
            return math.sin(x)
    
    @staticmethod
    def new_cos(x):
        p = math.pi
        if x%(2*p)==p/3 or x%(2*p)==2*p - p/3:
            return 0.5
        elif x%(2*p)==p+p/3 or x%(2*p)==2*p-2*p/6:
            return -0.5
        elif x%(p/2)==0:
            return 0
        else:
            return math.sin(x)
    
    @staticmethod
    def new_tan(x):
        p = math.pi
        if x%(p)==p/4:
            return 1
        elif x%(p) == 3*p/4:
            return -1
        elif x%(p)==0:
            return 0
        elif x%(p)==p/2:
            return 1/0
        else:
            return math.tan(p)
        


class Calculator():
    func_operands = ['sin','cos','tg','log','abs']
    operations = '+-*/^'
    ans = 0
    functions ={
        '+': lambda s,self: self.executionOfOperations(s[1]) + self.executionOfOperations(s[2]),
        '-': lambda s,self: self.executionOfOperations(s[1]) - self.executionOfOperations(s[2]),
        '/': lambda s,self: self.executionOfOperations(s[1]) / self.executionOfOperations(s[2]),
        '*': lambda s,self: self.executionOfOperations(s[1]) * self.executionOfOperations(s[2]),
        '^': lambda s,self: self.executionOfOperations(s[1]) ** self.executionOfOperations(s[2]),
        'sin': lambda s,self: Trigonomethry.new_sin(self.executionOfOperations(s[1])),
        'cos': lambda s,self: Trigonomethry.new_cos(self.executionOfOperations(s[1])),
        'tg': lambda s,self: Trigonomethry.new_tan(self.executionOfOperations(s[1])),
        'log': lambda s,self: math.log2(self.executionOfOperations(s[1])),
        'abs': lambda s,self: abs(self.executionOfOperations(s[1])),
    }
    
    def functionsCheck(self, inp:str)->bool:
        """
        Returns whether the entered functions are syntactically correct
        """
        for i in range(len(inp)-3):
            if (inp[i]+inp[i+1]+inp[i+2] in self.func_operands and inp[i+3]!='(') or (inp[i]+inp[i+1] in self.func_operands and inp[i+2]!='('):
                return False
        return True
    
    def numbersCheck(self, inp:str)->bool:
        """
        Returns whether there is an operation between each number
        """
        is_it_number = False
        was_there_an_operation = False
        status = 0
        for i in inp:
            if status>1:
                return False
            if i in '0123456789' and not is_it_number:
                is_it_number = True
                status+=1
            elif (not i in '0123456789') and is_it_number:
                is_it_number= False
            
            if i in self.operations:
                if not was_there_an_operation:
                    status-=1
                    was_there_an_operation = True
                elif was_there_an_operation:
                    was_there_an_operation = False

        return True

    def spacesCheck(self,inp:str)->bool:
        """
        Returns whether the input is correct in terms of spaces
        """
        return self.numbersCheck(inp) and self.functionsCheck(inp)
    
    def bracesCheck(self,inp:list)->bool:
        """
        Returns whether the parenthesized input expressions are correct
        """
        braces_stack = []
        for i in inp:
            if i=='(' or i =='[':
                braces_stack.append(i)
            elif i==')' or i ==']':
                try:
                    c = braces_stack.pop()
                    assert(c=='[' and i==']' or c=='(' and i==')')
                except:
                    return False
        if( len(braces_stack)==0):
            return True
        else:
            return False
    
    def operandsCheck(self,inp:list)->bool:
        """
        Returns whether the input is correct in terms of arithmetic operations
        """
        if inp[-1] in self.operations:
            return False
        for i in range(len(inp)-1):
            if (((inp[i] == '(' or inp[i] == '[') and inp[i+1] in '+*/^') or
                ((inp[i]==')'or inp[i] == ']') and inp[i+1] in ['1','2','3','4','5','6','7','8','9','0']) or
                inp[i] in ['1','2','3','4','5','6','7','8','9','0']) and ((inp[i+1]=='('or inp[i+1] == '[') or
                (inp[i] in self.operations and inp[i+1] in self.operations)):
                return False
        return True
    
    def checkingCorrectness(self,inp:list)->bool:
        """
        Returns whether the input without spaces is correct
        """
        return self.operandsCheck(inp) and self.bracesCheck(inp)


    def absProcessing(self,inp:str)->list:
        """
        Decomposes the input according to the expressions enclosed in the module( abs)
        """
        indicator = True
        abs_count = 0
        output = ''
        for i in range(len(inp)):
            if inp[i]=='|':
                if indicator:
                    abs_count+=1
                    output = output + 'abs['
                    indicator = False
                else:
                    if inp[i-1] in self.operations or inp[i-1] in self.func_operands:
                        abs_count+=1
                        output = output+'abs['
                    else:
                        output = output+']'
                        abs_count-=1
                        if abs_count<=0:
                            indicator = True           
                        
            else:
                output = output+inp[i]

        return list(output)

    def numbersProcessing(self,inp):
        """
        Splits a string into numbers and operations
        """
        parced = []
        number = ''
        for i in inp:
            if i in self.operations+'()[]':
                if number!='':
                    parced.append(number)
                    number = ''
                parced.append(i)
            else:
                number+=i
        if number!='':
            parced.append(number)        
        return parced

    def subelementsProcessing(self,input_str):
            """
                Find all braces subelements and operands between it, than do it for all subelements
            """
            if not isinstance(input_str,list):
                # If it isn't list, we not need to parse it
                return input_str

            preparsed_subelements_list = []     # Pre-processed ist
            braces_status = 0                   # It's show how many braces is already open
            subelement_index = 0                # Index that show index of current subelement
            subelement_status = False           # Show, Are we set subelement right now


            for i in input_str:
                # If now we not set SUB we just see element by element, while we not find open braces
                
                if not subelement_status:
                    
                    # If we find it: increase braces_status, set correct SUB_status and append SUB list
                    if i == '(':
                        preparsed_subelements_list.append([]) 
                        braces_status+=1
                        subelement_status = True
                    else:
                        subelement_index+=1
                        preparsed_subelements_list.append(i)
                else:
                    if i == '(':
                        preparsed_subelements_list[subelement_index].append(i)
                        braces_status+=1
                    elif i==')':
                        # If count of open braces the same as count of End braces - it's mean that SUB is end
                        braces_status-=1
                        if braces_status==0:
                            subelement_index+=1
                            subelement_status = False
                        else:
                            preparsed_subelements_list[subelement_index].append(i)
                    else:
                        preparsed_subelements_list[subelement_index].append(i)
            
            parsed_list = []
            
            if preparsed_subelements_list[0]=='-':
                preparsed_subelements_list = ['0','-'] + preparsed_subelements_list[1:]
            
            for i in preparsed_subelements_list:
                parsed_list.append(self.subelementsProcessing(i))
            return parsed_list


    def operationPriority(self,operand:Union[str,list])->int:
        """
        Return priority of operand
        """
        if isinstance(operand,str):
            if operand in '+-': return 1
            elif operand in '*/': return 2
            elif operand in '^': return 3
            elif operand in self.func_operands: return 4
        return 50
    
    def executionOrderProcessing(self,inp_str:Union[list,str])->Union[list,str]:
        """
        Return actions ordered in Polish notation
        """
        # If it isn't list there is no operands
        if isinstance(inp_str,list):
            if len(inp_str)==1: inp_str = inp_str[0]
            
            if isinstance(inp_str,list):
                min_operand_priority = 100
                min_operand_index = 0

                # If len of input str is 2, this means that it's function and argument
                if len(inp_str)==2:
                    if inp_str[0] in self.func_operands:
                        
                        # return list in wich first is function, second is argument
                        return [inp_str[0],self.executionOrderProcessing(inp_str[1])]
                
                # In other case this means that it's ariphmethic operation
                else:   

                    # Find last operand with min priority
                    for i in range(0,len(inp_str)):
                        if self.operationPriority(inp_str[i])<=min_operand_priority:
                            min_operand_priority = self.operationPriority(inp_str[i])
                            min_operand_index = i
                    
                    # return list in wich first is operand, second and third are elements before operand and after
                    return [inp_str[min_operand_index],self.executionOrderProcessing(inp_str[0:min_operand_index]),self.executionOrderProcessing(inp_str[min_operand_index+1:])]
        
        # If input isn't list it's just some number
        return inp_str
    
    def executionOfOperations(self,operation_element:Union[str,list])->float:
        """
        Return result of execution of operations
        """
        
        if not isinstance(operation_element,list):
            if operation_element=='pi': return math.pi
            if operation_element=='e': return math.e
            if operation_element=='Ans': return self.ans
            else: return float(operation_element)
        else:
            return self.functions[operation_element[0]](operation_element,self)
    
    def run(self,inp:str):
        if not self.spacesCheck(inp):
            return None
        abs_preparsed = self.absProcessing(inp.replace(' ',''))
        if not self.checkingCorrectness(abs_preparsed):
            return None
        else:
            inp = ''.join(abs_preparsed)
            result = self.calculate(inp)
            self.ans = result
            return result

    def calculate(self,inp:str)->Optional[float]:
        """
        Return result of mathematic order
        """
        s = list(inp.replace('[','(').replace(']',')').replace(',','.'))

        s_number_parced = self.numbersProcessing(s)
        s_parced = self.subelementsProcessing(s_number_parced)
        s_operands = self.executionOrderProcessing(s_parced)  
        s_result = self.executionOfOperations(s_operands)

        return s_result

    def __call__(self):
        print('Calculator is running')
        print('To stop it precc Control C')
        while True:
            try:
                inp = input()
                res = self.run(inp)
                if not(res is None):
                    print('res:',res)
                else:
                    print('Input is not correct')
            except KeyboardInterrupt:
                print('Stopped')
                break
            except:
                print('Someting goes wrong')
                break
