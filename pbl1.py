#Autor: Vivian Martins Moura
#Componente Curricular: MI-Algoritmos 
#Concluido em: 21/03/2025
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

#definição de variáveis e o input para o usuário definir o valor da passagem
passagem=float(input('Digite o valor da passagem:'))
saldo=0
saldoinicial=print(f'Saldo inicial={saldo} reais')
passageminicial=passagem
idoso=1
padrao=2
social=3
recarga=1
cpassagem=2
sair=3
relat=4
categorias=5
valorrecargatotal=0
valorrecargaidoso=0
valorrecargapadrao=0
valorrecargasocial=0
recargatotal=0
recargatotal1=0
recargatotal2=0
recargatotal3=0
quantdepassagem=0
quantdepassagem1=0
quantdepassagem2=0
#Opção pro usuário escolher sua categoria e os ifs para caso ele escolha uma categoria diferente da padrão o preço da passagem mude
categorias=print(f'Categorias: {idoso}=idoso ou estudante /  {padrao}=padrão /  {social}=social')
categorias=5
usuario=int(input('Digite qual a sua categoria:'))
if usuario==idoso:
    passagem= passagem/2
    print(f'Sua passagem com desconto custa {passagem} reais')
elif usuario==padrao:
    passagem=passagem
    print(f'Sua passagem custa {passagem} reais')
elif usuario==social:
    passagem=passagem/5
    print(f'Sua passagem com desconto custa {passagem} reais')
#criação da variável para o usuário escolher o que ele quer fazer
us=('Digite o que você deseja fazer em seguida:')
#Criação do loop utilizando while, que enquanto o usuário escolher uma opção do menu diferente de 3(que é para sair) ele vai continuar rodando o loop
while(us!=3): 
        print(f'{recarga}=recarga / {cpassagem}=comprar passagem / {sair}=sair do sistema / {relat}=relatório / {categorias}=mudar de usuário')
        us=int(input('Digite o que você deseja fazer em seguida:'))
        if us==1: #Criação do if para o caso do usuário querer recarregar, que é representado pelo número 1
                r=int(input('Digite o valor que você deseja adicionar no seu saldo:'))
                saldo=(saldo+r)
                print(f'Seu saldo atual após a recarga é de {saldo} reais')
                recargatotal+=1
                valorrecargatotal+=r
                if usuario==1 and us==1:
                        recargatotal1+=1
                        valorrecargaidoso+=r
                        saldoidoso=saldo
                elif usuario==2 and us==1:
                        valorrecargapadrao+=r
                        recargatotal2+=1
                        saldopadrao=saldo
                elif usuario==3 and us==1:
                        valorrecargasocial+=r
                        recargatotal3+=1
                        saldosocial=saldo
        elif us==2: #Criação do if para o caso do usuário querer comprar passagem, que é representado pelo número 2
                if usuario==1 and saldo>=passagem:
                        saldo=(saldo-passagem)
                        print(f'Sua compra foi feita com sucesso! Seu saldo restante é:{saldo} reais')
                        quantdepassagem+=1
                        passagemidoso=passagem
                elif usuario==1 and saldo<passagem:
                        print('Seu saldo atual é insuficiente!')
                if usuario==2 and saldo>=passagem:
                        saldo=(saldo-passagem)
                        print(f'Sua compra foi feita com sucesso! Seu saldo restante é:{saldo} reais')
                        quantdepassagem1+=1 
                        passagempadrao=passagem
                elif usuario==2 and saldo<passagem:
                        print('Seu saldo atual é insuficiente!')    
                if usuario==3 and saldo>=passagem:
                        saldo=(saldo-passagem)
                        print(f'Sua compra foi feita com sucesso! Seu saldo restante é:{saldo} reais')
                        quantdepassagem2+=1
                        passagemsocial=passagem
                elif usuario==3 and saldo<passagem:
                        print('Seu saldo atual é insuficiente!')
        
        elif us==4: #Criação do if para o caso do usuário querer ver o relatório, que é representado pelo número 4
                print('Relatório:')
                print(f'Valor total das recargas: {valorrecargatotal} reais')
                print(f'Valor total das recargas na categoria idoso/estudante:{valorrecargaidoso} reais')
                print(f'Valor total das recargas na categoria padrão: {valorrecargapadrao} reais')
                print(f'Valor total das recargas na categoria social: {valorrecargasocial} reais')
                print('                                                                               ')
                print(f'Quantidade de recargas feitas:{recargatotal}')
                print(f'Quantidade de recargas feitas na categoria idoso/estudante: {recargatotal1}')
                print(f'Quantidade de recargas feitas na categoria padrão: {recargatotal2}')
                print(f'Quantidade de recargas feitas na categoria social: {recargatotal3}')
                print('                                                                              ')
                print(f'Quantidade de passagens usadas na categoria idoso/estudante: {quantdepassagem}') 
                print(f'Quantidade de passagens usadas na categoria padrão: {quantdepassagem1}')
                print(f'Quantidade de passagens usadas na categoria social: {quantdepassagem2}')
                print('                                                                               ')
                if usuario==1 or usuario==2 or usuario==3:
                        valorgastoidoso=(quantdepassagem*passagemidoso)
                        print(f'Valor gasto com passagem na categoria idoso/estudante:{valorgastoidoso}')
                        valorgastopadrao=(quantdepassagem1*passagempadrao)
                        print(f'Valor gasto com passagem na categoria padrão:{valorgastopadrao}')
                        valorgastosocial=(quantdepassagem2*passagemsocial)
                        print(f'Valor gasto com passagem na categoria social:{valorgastosocial}')
                print('                                                                    ')
                if usuario==1 or usuario==2 or usuario==3:
                        usuario1=print(f'Saldo restante na categoria idoso/estudante:{saldoidoso}')
                        usuario2=print(f'Saldo restante na categoria padrão:{saldopadrao}')
                        usuario3=print(f'Saldo restante na categoria social:{saldosocial}')
        elif us==5: #criação do if para o caso do usuário querer mudar de categoria
               print(f'Categorias: {idoso}=idoso ou estudante /  {padrao}=padrão /  {social}=social')
               usuario=int(input('Digite qual usuário você se encaixa:'))
               passagem=passageminicial
               saldo=0
               print('Saldo inicial=0 reais')
               if usuario==1:
                      passagem=passagem/2
               if usuario==2:
                      passagem=passagem
               if usuario==3:
                      passagem=passagem/5
                      
