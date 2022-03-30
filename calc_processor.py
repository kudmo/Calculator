import math
from typing import Union,Optional

class Calculator():
    func_operands = ['sin','cos','tg','log','abs']
    operations = '+-*/^'
    ans = 0
    functions ={
        '+': lambda s,self: self.execution_of_operations(s[1]) + self.execution_of_operations(s[2]),
        '-': lambda s,self: self.execution_of_operations(s[1]) - self.execution_of_operations(s[2]),
        '/': lambda s,self: self.execution_of_operations(s[1]) / self.execution_of_operations(s[2]),
        '*': lambda s,self: self.execution_of_operations(s[1]) * self.execution_of_operations(s[2]),
        '^': lambda s,self: self.execution_of_operations(s[1]) ** self.execution_of_operations(s[2]),
        'sin': lambda s,self: math.sin(self.execution_of_operations(s[1])),
        'cos': lambda s,self: math.cos(self.execution_of_operations(s[1])),
        'tg': lambda s,self: math.tan(self.execution_of_operations(s[1])),
        'log': lambda s,self: math.log2(self.execution_of_operations(s[1])),
        'abs': lambda s,self: abs(self.execution_of_operations(s[1])),
    }
    

    def braces_check(self,inp:str)->bool:
        """
        Return are input correct by braces
        """
        braces_stack = []
        for i in inp:
            if i=='(':
                braces_stack.append(i)
            elif i==')':
                try:
                    braces_stack.pop()
                except:
                    return False
        if( len(braces_stack)==0):
            return True
        else:
            return False
    
    def operands_check(self,inp:str)->bool:
        """
        Return are input correct by operands
        """
        for i in range(len(inp)-1):
            if ((inp[i] == '(' and inp[i+1] in '+*/^') or
                (inp[i]==')' and inp[i+1] in ['1','2','3','4','5','6','7','8','9','0']) or
                (inp[i] in self.operations and inp[i+1] in self.operations)):
                return False
        return True

    def abc_parse(self,inp:str)->list:
        k = True
        a = 0
        s = ''
        for i in range(len(inp)):
            if inp[i]=='|':
                if k:
                    a+=1
                    s = s + 'abs('
                    k = False
                else:
                    if inp[i-1] in self.operations or inp[i-1] in self.func_operands:
                        a+=1
                        s = s+'abs('
                    else:
                        s = s+')'
                        a-=1
                        if a<=0:
                            k = True           
                        
            else:
                s = s+inp[i]

        return list(s)

    def subelements_parse(self,input_str:Union[list,str])->Union[list,str]:
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
                    
                    # Else, if it not operation, we fill out current elemen by one number 
                    if i not in self.operations:
                        if len(preparsed_subelements_list)>0:
                            
                            if preparsed_subelements_list[-1] not in self.operations:
                                preparsed_subelements_list[-1]+=i
                            else:
                                subelement_index+=1
                                preparsed_subelements_list.append(i)
                        else:
                            subelement_index+=1
                            preparsed_subelements_list.append(i)
                    # If it operation, stop fill out current and append operation
                    else:
                        subelement_index+=1
                        preparsed_subelements_list.append(i)
                    # After appending new element increase SUB_index
            # If we fiiling out subelemet right now, we do thr same operations, but append elements in subelement, not in result list
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
                    if i not in self.operations:
                        if len(preparsed_subelements_list[subelement_index])>0:
                            if preparsed_subelements_list[subelement_index][-1] not in self.operations+'()':
                                preparsed_subelements_list[subelement_index][-1]+=i
                            else:
                                preparsed_subelements_list[subelement_index].append(i)
                        else:
                            preparsed_subelements_list[subelement_index].append(i)
                    else:
                        preparsed_subelements_list[subelement_index].append(i)
        
        parsed_list = []
        
        # If first element is - it's means that first element if negative number
        if preparsed_subelements_list[0]=='-':
            preparsed_subelements_list = ['0','-'] + preparsed_subelements_list[1:]
        
        
        # For all subelement we need to parse it too
        for i in preparsed_subelements_list:
            parsed_list.append(self.subelements_parse(i))
        return parsed_list

    def operand_priority(self,operand:Union[str,list])->int:
        """
        Return priority of operand
        """
        if isinstance(operand,str):
            if operand in '+-': return 1
            elif operand in '*/': return 2
            elif operand in '^': return 3
            elif operand in self.func_operands: return 4
        return 50
    
    def execution_order_parse(self,inp_str:Union[list,str])->Union[list,str]:
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
                        return [inp_str[0],self.execution_order_parse(inp_str[1])]
                
                # In other case this means that it's ariphmethic operation
                else:   

                    # Find last operand with min priority
                    for i in range(0,len(inp_str)):
                        if self.operand_priority(inp_str[i])<=min_operand_priority:
                            min_operand_priority = self.operand_priority(inp_str[i])
                            min_operand_index = i
                    
                    # return list in wich first is operand, second and third are elements before operand and after
                    return [inp_str[min_operand_index],self.execution_order_parse(inp_str[0:min_operand_index]),self.execution_order_parse(inp_str[min_operand_index+1:])]
        
        # If input isn't list it's just some number
        return inp_str
    
    def execution_of_operations(self,operation_element:Union[str,list])->float:
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
    

    def calculate(self,inp:str)->Optional[float]:
        """
        Return result of mathematic order
        """
        inp = inp.replace(' ','')

        if not( self.braces_check(inp) and self.operands_check(inp)):
            return None
        
        s = self.abc_parse(inp)  
 
        s_parced = self.subelements_parse(s)
        s_operands = self.execution_order_parse(s_parced)  
        s_result = self.execution_of_operations(s_operands)
        self.ans = s_result

        return s_result

    def __call__(self):
        print('Calculator is running')
        print('To stop it precc Control C')
        while True:
            try:
                res = self.calculate(input())
                if not(res is None):
                    print('res:',res)
                else:
                    print('Input is not correct')
            except KeyboardInterrupt:
                break
            except:
                print('Someting goes wrong')
                break
