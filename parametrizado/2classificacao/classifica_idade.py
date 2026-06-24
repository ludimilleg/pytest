def classifica_idade(idade):
    if idade < 12:
        return "Criança"
    elif idade < 18:
        return "Teen"
    elif idade < 60:
        return "Adulto"
    else:
        return "Idoso"
        
    
