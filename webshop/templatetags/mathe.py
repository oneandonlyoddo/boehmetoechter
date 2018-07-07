from django import template

#Django template custom math filters
#Ref : https://code.djangoproject.com/ticket/361
register = template.Library()

def mult(value, arg):
    "Multiplies the arg and the value"
    answer = float(value) * float(arg)
    return ('%.2f' % answer).replace('.', ',')

def multStrConV(value, arg):
    "Multiplies the arg and the value"
    v = value.replace(',', '.')
    answer = float(v) * float(arg)
    return ('%.2f' % answer).replace('.', ',')

def multPoint(value, arg):
    "Multiplies the arg and the value"
    answer = float(value) * float(arg)
    return ('%.2f' % answer)

def addFloat(value, arg):
    "Add Floats the arg and the value"
    answer = float(value) + float(arg)
    return ('%.2f' % answer).replace('.', ',')

def addFloatPoint(value, arg):
    "Add Floats the arg and the value"
    answer = float(value) + float(arg)
    return ('%.2f' % answer)

def sub(value, arg):
    "Subtracts the arg from the value"
    answer= float(value) - float(arg)
    return ('%.2f' % answer).replace('.', ',')

def div(value, arg):
    "Divides the value by the arg"
    answer = float(value) / float(arg)
    return ('%.2f' % answer).replace('.', ',')





register.filter('mult', mult)
register.filter('multPoint', multPoint)
register.filter('multStrConV', multStrConV)
register.filter('addFloat', addFloat)
register.filter('addFloatPoint', addFloatPoint)
register.filter('sub', sub)
register.filter('div', div)