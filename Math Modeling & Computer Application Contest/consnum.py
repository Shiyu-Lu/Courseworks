import numpy as np

def consnum(x,confirm,quant,p):
    if x==1:
        return ({'type': 'eq', 'fun': lambda x: sum(x)-quant},\
        {'type': 'eq', 'fun': lambda x:np.dot(p,x)-confirm},\
            {'type': 'ineq', 'fun': lambda x:x[0]})
    elif x==2:
        return ({'type': 'eq', 'fun': lambda x: sum(x)-quant},\
        {'type': 'eq', 'fun': lambda x:np.dot(p,x)-confirm},\
            {'type': 'ineq', 'fun': lambda x:x[0]},\
                {'type': 'ineq', 'fun': lambda x:x[1]})
    elif x==3:
        return ({'type': 'eq', 'fun': lambda x: sum(x)-quant},\
        {'type': 'eq', 'fun': lambda x:np.dot(p,x)-confirm},\
            {'type': 'ineq', 'fun': lambda x:x[0]},\
                {'type': 'ineq', 'fun': lambda x:x[1]},\
                    {'type': 'ineq', 'fun': lambda x:x[2]})
    elif x==4:
        return ({'type': 'eq', 'fun': lambda x: sum(x)-quant},\
        {'type': 'eq', 'fun': lambda x:np.dot(p,x)-confirm},\
            {'type': 'ineq', 'fun': lambda x:x[0]},\
                {'type': 'ineq', 'fun': lambda x:x[1]},\
                    {'type': 'ineq', 'fun': lambda x:x[2]},\
                        {'type': 'ineq', 'fun': lambda x:x[3]})
    elif x==5:
        return ({'type': 'eq', 'fun': lambda x: sum(x)-quant},\
        {'type': 'eq', 'fun': lambda x:np.dot(p,x)-confirm},\
            {'type': 'ineq', 'fun': lambda x:x[0]},\
                {'type': 'ineq', 'fun': lambda x:x[1]},\
                    {'type': 'ineq', 'fun': lambda x:x[2]},\
                        {'type': 'ineq', 'fun': lambda x:x[3]},\
                            {'type': 'ineq', 'fun': lambda x:x[4]})
    elif x==6:
        return ({'type': 'eq', 'fun': lambda x: sum(x)-quant},\
        {'type': 'eq', 'fun': lambda x:np.dot(p,x)-confirm},\
            {'type': 'ineq', 'fun': lambda x:x[0]},\
                {'type': 'ineq', 'fun': lambda x:x[1]},\
                    {'type': 'ineq', 'fun': lambda x:x[2]},\
                        {'type': 'ineq', 'fun': lambda x:x[3]},\
                            {'type': 'ineq', 'fun': lambda x:x[4]},\
                                {'type': 'ineq', 'fun': lambda x:x[5]})
    elif x==7:
        return ({'type': 'eq', 'fun': lambda x: sum(x)-quant},\
        {'type': 'eq', 'fun': lambda x:np.dot(p,x)-confirm},\
            {'type': 'ineq', 'fun': lambda x:x[0]},\
                {'type': 'ineq', 'fun': lambda x:x[1]},\
                    {'type': 'ineq', 'fun': lambda x:x[2]},\
                        {'type': 'ineq', 'fun': lambda x:x[3]},\
                            {'type': 'ineq', 'fun': lambda x:x[4]},\
                                {'type': 'ineq', 'fun': lambda x:x[5]},\
                                    {'type': 'ineq', 'fun': lambda x:x[6]})
    elif x==8:
        return ({'type': 'eq', 'fun': lambda x: sum(x)-quant},\
        {'type': 'eq', 'fun': lambda x:np.dot(p,x)-confirm},\
            {'type': 'ineq', 'fun': lambda x:x[0]},\
                {'type': 'ineq', 'fun': lambda x:x[1]},\
                    {'type': 'ineq', 'fun': lambda x:x[2]},\
                        {'type': 'ineq', 'fun': lambda x:x[3]},\
                            {'type': 'ineq', 'fun': lambda x:x[4]},\
                                {'type': 'ineq', 'fun': lambda x:x[5]},\
                                    {'type': 'ineq', 'fun': lambda x:x[6]},\
                                        {'type': 'ineq', 'fun': lambda x:x[7]})          
    elif x==9:
                return ({'type': 'eq', 'fun': lambda x: sum(x)-quant},\
        {'type': 'eq', 'fun': lambda x:np.dot(p,x)-confirm},\
            {'type': 'ineq', 'fun': lambda x:x[0]},\
                {'type': 'ineq', 'fun': lambda x:x[1]},\
                    {'type': 'ineq', 'fun': lambda x:x[2]},\
                        {'type': 'ineq', 'fun': lambda x:x[3]},\
                            {'type': 'ineq', 'fun': lambda x:x[4]},\
                                {'type': 'ineq', 'fun': lambda x:x[5]},\
                                    {'type': 'ineq', 'fun': lambda x:x[6]},\
                                        {'type': 'ineq', 'fun': lambda x:x[7]},\
                                            {'type': 'ineq', 'fun': lambda x:x[8]})
    elif x==10:
        return ({'type': 'eq', 'fun': lambda x: sum(x)-quant},\
        {'type': 'eq', 'fun': lambda x:np.dot(p,x)-confirm},\
            {'type': 'ineq', 'fun': lambda x:x[0]},\
                {'type': 'ineq', 'fun': lambda x:x[1]},\
                    {'type': 'ineq', 'fun': lambda x:x[2]},\
                        {'type': 'ineq', 'fun': lambda x:x[3]},\
                            {'type': 'ineq', 'fun': lambda x:x[4]},\
                                {'type': 'ineq', 'fun': lambda x:x[5]},\
                                    {'type': 'ineq', 'fun': lambda x:x[6]},\
                                        {'type': 'ineq', 'fun': lambda x:x[7]},\
                                            {'type': 'ineq', 'fun': lambda x:x[8]},\
                                                {'type': 'ineq', 'fun': lambda x:x[9]})
    elif x==11:
        return ({'type': 'eq', 'fun': lambda x: sum(x)-quant},\
        {'type': 'eq', 'fun': lambda x:np.dot(p,x)-confirm},\
            {'type': 'ineq', 'fun': lambda x:x[0]},\
                {'type': 'ineq', 'fun': lambda x:x[1]},\
                    {'type': 'ineq', 'fun': lambda x:x[2]},\
                        {'type': 'ineq', 'fun': lambda x:x[3]},\
                            {'type': 'ineq', 'fun': lambda x:x[4]},\
                                {'type': 'ineq', 'fun': lambda x:x[5]},\
                                    {'type': 'ineq', 'fun': lambda x:x[6]},\
                                        {'type': 'ineq', 'fun': lambda x:x[7]},\
                                            {'type': 'ineq', 'fun': lambda x:x[8]},\
                                                {'type': 'ineq', 'fun': lambda x:x[9]},\
                                                    {'type': 'ineq', 'fun': lambda x:x[10]})