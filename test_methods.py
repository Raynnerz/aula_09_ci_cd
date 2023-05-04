import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_soma():
    a = 2
    b = 3
    output = methods.soma(a, b)
    assert output == 5

def test_sub():
    a = 9
    b = 4
    output = methods.sub(a, b)
    assert output == 5

def test_mult():
    a = 0.5
    b = 10
    output = methods.mult(a, b)
    assert output == 5

def test_div():
    a = 2.5
    b = 0.5
    output = methods.div(a, b)
    assert output == 5