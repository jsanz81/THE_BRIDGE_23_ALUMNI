def outer(df):
    
    def inner_1():
        df = inner_2()
        return df
    
    def inner_2():
        pass
    
    def inner_3():
        pass
    
    
    df = inner_1()
    df = inner_3()
    
    return df