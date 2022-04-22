from calc_processor import Calculator

calculator = Calculator()

def test_functionCheck():
    assert calculator.functionsCheck("sin(2 -       (-3)    )") == True
    assert calculator.functionsCheck("sin(cos)(12-3)") ==False

def test_numberCheck():
    assert calculator.numbersCheck("(1,23*[3-2]*(-2)-3)/[2+3]")==True
    assert calculator.numbersCheck("        12+3-4") == True
    assert calculator.numbersCheck("1,2+    (-3)*3") == True
    assert calculator.numbersCheck("1     -3 4+ 2") == False
    assert calculator.numbersCheck("0,47849239 + 12,") == False
    assert calculator.numbersCheck("09,123") == False
    assert calculator.numbersCheck("109,123") == True


def test_bracesCheck():
    assert calculator.bracesCheck(list("(123*[3-2]*(-2)-3)/[2+3]")) == True
    assert calculator.bracesCheck(list("[([]()[()])]")) == True
    assert calculator.bracesCheck(list("((()[)])")) == False
    assert calculator.bracesCheck(calculator.absProcessing("(2-|-2*3|/4)*(16*|5-5|-|3+2|)"))==True

def test_operandsCheck():
    assert calculator.operandsCheck("1++2")==False
    assert calculator.operandsCheck(list("(123*(-12-3))/(-12+3)"))==True
    assert calculator.operandsCheck(list("-12-3-(+2)")) == False
    assert calculator.operandsCheck("23*3 - (-3)") == True

def test_checkingCorrectness():
    assert calculator.bracesCheck(list("(123*[3-2]*(-2)-3)/[2+3]")) == True
    assert calculator.bracesCheck(calculator.absProcessing("(2-|-2*3|/4)*(16*|5-5|-|3+2|)"))==True
    assert calculator.operandsCheck("1++2")==False
    assert calculator.operandsCheck(list("(1,23*(-12-3))/(-12+3)"))==True
    assert calculator.operandsCheck(list("-12-3-(+2)")) == False
    assert calculator.operandsCheck("23*3 - (-3)") == True
    assert calculator.operandsCheck("(-23)-(-23,1)") == True

def test_absProcessng():
    assert calculator.absProcessing("(2-|-2*3|/4)*(16*|5-5|-|3+2|)") == list("(2-abs[-2*3]/4)*(16*abs[5-5]-abs[3+2])")
    assert calculator.absProcessing("|12-|34+4||") == list("abs[12-abs[34+4]]")

def test_numbersProcessing():
    assert calculator.numbersProcessing('123+12-(3875*34)') == ['123','+','12','-','(','3875','*','34',')']
    assert calculator.numbersProcessing('-123,321') == ['-','123,321']
    assert calculator.numbersProcessing('Ans+sin(12)') == ['Ans','+','sin','(','12',')']

def test_subelementProcessing():
    assert calculator.subelementsProcessing(['1.23']) == ['1.23']
    assert calculator.subelementsProcessing(['43','+','(','32','-','4',')','*','6']) == ['43','+',['32','-','4'],'*','6']

def test_executionOrderProcessing():
    assert calculator.executionOrderProcessing(['43', '+', '3']) == ['+','43','3']
    assert calculator.executionOrderProcessing(['43','+',['32','-','4'],'*','6'])  == ['+', '43', ['*', ['-', '32', '4'], '6']]
    assert calculator.executionOrderProcessing(['12']) == '12'

def test_executionOfOperations():
    assert calculator.executionOfOperations('12') == 12.0
    assert calculator.executionOfOperations(['+','43','3']) == 46.0
    assert calculator.executionOfOperations(['+', '43', ['*', ['-', '32', '4'], '6']]) == 211
    assert calculator.executionOfOperations(['+',['*', ['-', '32', '4'], '6'], '42.5',]) == 210.5
    assert calculator.executionOfOperations(['+','0.2','0.3']) == 0.5

def test_run():
    assert calculator.run("12-2*3") == 6
    assert calculator.ans == 6
    assert calculator.run('2*Ans-7') == 5
    assert calculator.run('Ans^(Ans-3)') == 25
    assert calculator.ans == 25
