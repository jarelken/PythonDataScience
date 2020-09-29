import pandas as pd

pro = {
    'Processo': ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10'],
    'Prioridade': [3,2,5,8,3,1,1,4,6,1],
    'ms': [300, 250, 100, 200, 250, 150, 100, 200, 300, 200]
}

df = pd.DataFrame(data=pro)
df['processou'] = [0,0,0,0,0,0,0,0,0,0]
print('-----------------Valores inicias sem tratamento-----------------\n\n')
print(df)
df = df.sort_values(by=['ms','Prioridade'], ascending=False)
df.index = [1,2,3,4,5,6,7,8,9,10]





def e_robinhood():
    global df
    
    print('\n--------Valores após tratamento, ordenados por tempo e prioridade-------\n\n')
        
    print(df)
    
 
    for ch in range(1,3):
        for x in range(1,11):                    
            a = df.loc[x].at['Processo']
            print("\n****Executando Processo ", a,', na chance número ',ch,"\n\n")              

            df.at[x, 'processou'] = ch
            print(df)



e_robinhood()
