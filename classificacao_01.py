# caracteristicas [é gordinho?, tem perninha curta?, faz auau?]
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]

cachorro4 = [1, 1, 1]
cachorro5 = [0, 1, 1]
cachorro6 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro4, cachorro5, cachorro6]

#1 = porco, -1 = cachorro
marcadores = [1, 1, 1, -1, -1, -1]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados, marcadores)


misterioso1 = [1,1,1]
misterioso2 = [1,0,0]
misterioso3 = [0,0,1]

teste = [misterioso1, misterioso2, misterioso3]

resultado = modelo.predict(teste)


print(resultado)