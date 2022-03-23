import array
def sigmoid_fuction (input):
    e=2.71828
    return (1/(1+pow(e,-input)))

def neuralmodel (input):
    output=0
    l0n0=(input[0]-1201.52)/(40000.0-1201.52)
    l0n1=(input[1]-22.19)/(32.04-22.19)
    l0n2=(input[2]-27.9)/(93.81-27.9)

    l1n0=max(0,((l0n0*-0.40)+(l0n1*-0.45)+(l0n2*-0.56)))
    l1n1=max(0,((l0n0*-0.20)+(l0n1*0.69)+(l0n2*1.41)) - 0.047)
    l1n2=max(0,((l0n0*-0.81)+(l0n1*0.04)+(l0n2*-0.85))-0.008)

    l2n0= max(0,((l1n0*0.11)+(l1n1*1.51)+(l1n2*-0.38))-0.011)
    l2n1= max(0,((l1n0*0.37)+(l1n1*-0.41)+(l1n2*-0.23))+1.025)
    l2n2=max(0,((l1n0*0.002)+(l1n1*-0.08)+(l1n2*-0.95)))

    l3n0=sigmoid_fuction(((l2n0*1.58)+(l2n1*-0.85)+(l2n2*-0.69))-0.5874)
    if l3n0 < 0.5:
        return 0
    else:
        return 1
