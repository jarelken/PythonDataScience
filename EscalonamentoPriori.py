import pandas as pd


processos_p4 = {
    'processo': ['p1', 'p2', 'p3', 'p4','p25','p45'] #não entendi o motivo da criação de p24 e p45
}

df4 = pd.DataFrame(data=processos_p4)
df4.index = [1,2,3,4,5,6]
df4['processou'] = [0,0,0,0,0,0]


processos_p2 = {
    'processo': ['p5', 'p6', 'p7']
}

df2 = pd.DataFrame(data=processos_p2)
df2.index = [1,2,3]
df2['processou'] = [0,0,0]
    
processos_p1 = {
    'processo': ['p9', 'p10']
}

df1 = pd.DataFrame(data=processos_p1)
df1.index = [1,2]
df1['processou'] = [0,0]


def esc_prior():
    
    global df4
    global df2
    global df1
    
    print("Fila Prioridade 4")
    print(df4)
    print("**********")
    
    print("\n\nFila Prioridade 2")
    print(df2)
    print("**********")

    print("\n\nFila Prioridade 1")
    print(df1)
    print("**********")
    
   
    ciclo = 1
    
    #controle das filas para indicar qual processo está executando e em qual etapa está
    p4_fila = 1
    p4_etapa = 1
    
    
    p2_fila = 1
    p2_etapa = 1
    
    p1_fila = 1
    p1_etapa = 1
    
    #inicia ciclo de execução
    while ciclo <= 4:
        print('\n\nCiclo: ',ciclo)
        #processos com prioridade 4 terão 4 quantuns cada vez que passa na fila
        x4 = 1
        while x4 <= 4:       
            #identifico o processo atual e vejo quantos quantums falta para terminar
            a = df4.loc[p4_fila].at['processo']   # carrega o processo a ser executado
            prc = df4.loc[p4_fila].at['processou'] # reserva a quantidade de vezes que já foi executado

            print("****Executando Processo ", a,' de prioridade 4 no quantum  ',x4) # executa o processo                                  
            ##testa se já executou 3 vezes
            novaetapa = prc + 1
            df4.at[p4_fila, 'processou'] = novaetapa   #atualiza a quantidade de vezes que foi executado      
            
            if novaetapa >= 3:
                p4_fila = p4_fila + 1
                p4_etapa = 1
                
            x4 = x4 + 1
        print(df4,"\n\n")

       #processos com prioridade 2 terão 2 quantuns cada vez que passa na fila
        x2 = 1
        while x2 <= 2:        
            a2 = df2.loc[p2_fila].at['processo'] 
            prc2 = df2.loc[p2_fila].at['processou'] # reserva a quantidade de vezes que já foi executado
            print("****Executando Processo ", a2,' de prioridade 2 no quantum  ',x2) # executa o processo              
            novaetapa2 = prc2 + 1
            df2.at[p2_fila, 'processou'] = novaetapa2   #atualiza a quantidade de vezes que foi executado     
            
             
            if novaetapa2 >= 3:
                p2_fila = p2_fila + 1
                p2_etapa = 1
            x2 = x2+1 
        print(df2,"\n\n")


        #processos com prioridade 1 terão 1 quantum cada vez que passa na fila
        x1 = 1
        while x1 <= 1:        
            a1 = df1.loc[p1_fila].at['processo'] 
            prc1 = df1.loc[p1_fila].at['processou'] # reserva a quantidade de vezes que já foi executado
            print("****Executando Processo ", a1,' de prioridade 1 no quantum  ',x1) # executa o processo              
            novaetapa1 = prc1 + 1
            df1.at[p1_fila, 'processou'] = novaetapa1   #atualiza a quantidade de vezes que foi executado       
            
            if novaetapa1 >= 3:                
                p1_fila = p1_fila + 1
                p1_etapa = 1
            
            x1 = x1+1
        print(df1,"\n\n")
        
        ciclo = ciclo + 1
        print("****************************************************")
esc_prior()
