
Gerar um grafo com base no código abaixo para identificar os caminhos a serem testados. 

```JS
public boolean saque(double valor){
    boolean status = false;
    if(valor <= saldo){
        saldo = saldo - valor;
        status = true;
    }
    
    else{
        if(valor <= limiteCredito){
            limiteCredito = limiteCredito - valor;
            status = true;
        }
    }

    return status;
}
```
## Resultado do Teste

O resultado final dos caminhos para teste deste software é o grafo representado abaixo:

 ```JS
public boolean saque(double valor){
    boolean status = false;//1
    if(valor <= saldo){//1
        saldo = saldo - valor;//2
        status = true;//2
    }
    
    else{//3
        if(valor <= limiteCredito){//3
            limiteCredito = limiteCredito - valor;//4
            status = true;//4
        }
    }

    return status;//5
}
```

# Grafo

![[Pasted image 20250812193142.png]]