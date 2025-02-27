from logdeco import logcall

@logcall
def alpha():
    print("alpha")

@logcall
def beta(repeat):
    print("beta" * repeat)

@logcall
def gamma():
    print("gamma")

alpha()
beta(5)
gamma()
gamma()
beta(10)
gamma()
alpha()