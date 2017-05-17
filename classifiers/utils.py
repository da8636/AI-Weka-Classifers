from math import pi,sqrt,exp

def norm(x, mean, std):
    return exp(-1*(((x-mean)**2)/(2*(std**2)))) / (sqrt(2*pi)*std)
