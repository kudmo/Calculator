from calc_processor import Calculator

calculator = Calculator()

def test_operandsCheck():
    assert calculator.operandsCheck("1++2")==False
    assert calculator.operandsCheck("(123*(-12-3))/(-12+3)")==True
    assert calculator.operandsCheck("-12-3-(+2)") == False
    assert calculator.operandsCheck("23*3 - (-3)") == True

def test_bracesCheck():
    assert calculator.bracesCheck(list("(123*[3-2]*(-2)-3)/[2+3]")) == True
    assert calculator.bracesCheck(list("[([]()[()])]")) == True
    assert calculator.bracesCheck(list("((()[)])")) == False
    assert calculator.bracesCheck(calculator.absProcessing("(2-|-2*3|/4)*(16*|5-5|-|3+2|)"))==True

def test_absProcessng():
    assert calculator.absProcessing("(2-|-2*3|/4)*(16*|5-5|-|3+2|)") == list("(2-abs[-2*3]/4)*(16*abs[5-5]-abs[3+2])")