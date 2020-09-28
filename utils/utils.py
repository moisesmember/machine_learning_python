import csv

class Utils:
    # Recebe os registros do Arquivo e Banco para compartação
    def salvarRegistrosNovos(self, dict_file, dict_banco):       
        inter = []
        reader = csv.reader(dict_file) 
        verificar = Utils()                 
        for data_banco in dict_banco:
            #print(str(value_file[0]))             
            for value_file in reader:
                #print(data_banco['dezenas_sorteadas'])                
                if str(value_file[0]) == str(data_banco['data_sorteio']):
                    inter.append(str(value_file[0]))
                    print(str(value_file[0]))

                '''print(str(value_file[0]))
                print("DB: "+str(data_banco['data_sorteio']) + " == CSV: "+str(value_file[0]))
                if str(value_file[0]) == str(data_banco['data_sorteio']):
                    print("EXISTE")
                else:
                    print("NÃO EXISTE")'''
        return inter

    def intersecao(self, dict_file, dict_banco):
        inter = []
        if dict_file == dict_banco:
            inter.append(dict_file)

        '''for x in dict_file:
            for y in dict_banco:
                if x != y:
                    inter.append(x)'''
        return inter

        '''
        reader = csv.reader(dict_file)               
        for row in reader:
            print(str(row[0]))
       
        for data_banco in dict_banco:
            print(data_banco['data_sorteio'])'''