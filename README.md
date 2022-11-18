# TP: Classificação de Atividades Humanas 
### Projeto TCD - MECD (2022/2023)

## Autores

- Duarte Meneses - 2019216949 - [@DMeneses01](https://github.com/DMeneses01)
- Patricia Costa - 2019213995 - [@patii01](https://github.com/patii01)

## Metas

| Meta              | Data                  |
| ----------------- | --------------------- |
| Parte A           | 4 de novembro de 2022 |
| Parte B           | 15 de dezembro de 2022|
| Defesa Oral       | 16 de dezembro de 2022|

### Parte A

1. [x] Criação do 'mainActivity.py'
2. [x] Leitura do ficheiro
3. [ ] Análise e tratamento de Outliers
    1. [x] Boxplot
    2. [x] Densidade
    3. [x] Rotina - Z-Score
    4. [x] Z-Score: k = 3, 3.5, 4 
    5. [x] Discussão de resultados (3.1. e 3.4.)
    6. [x] Rotina - K-Means
    7. [x] K-Means: diferentes nºs de clusters e comparação com resultados do 3.4.
        1. [ ] Bónus: DBSCAN
    8. [x] Rotina - Injeção de Outliers
    9. [ ] Rotina - Modelo Linear
    10. [ ] Modelo Linear com 10% de injeção de ouliers e determinação do melhor p com LOO
        i. [ ] Distribuição do erro 
        ii. [ ] Exemplos de plots contendo o valor previsto e real
    11. [ ] Repetição do 3.10. com uma janela de dimensão pcentrada no instante a prever, comparação com o 3.10.
4. [x] Extração de informação característica
    1. [x] Significância estatística dos seus valores médios  nas diferentes atividades
    2. [x] Rotina - Extração do feature set temporal e espectral sugerido no artigo [4](https://pdfs.semanticscholar.org/8522/ce2bfce1ab65b133e411350478183e79fae7.pdf)
    3. [x] Implementação do PCA
    4. [x] Importância de cada vetor principal na explicação  da variabilidade do espaço de features
        1. [x] Indicar como obter as features relativas a esta compressão e exemplicar para um instante à escolha
        2. [x] Vantagens e limitações da abordagem
    5. [ ] Fisher feature Score e ReliefF 
    6. [ ] 10 melhores features com Fisher Score e ReliefF
        1. [ ] Indicar como obter as features relativas a esta compressão e exemplicar para um instante à escolha
        2. [ ] Vantagens e limitações da abordagem

    > O 4.5 e 4.6 serão transferidos para a Parte B


### Parte B

1. [x] Data splitting e métricas de exactidãoem machine learning
    1. [x] Data Splitting
        1. [x] Train-Test (TT) e Train-Validation-Test
        2. [x] K-fold
    2. [x] Métricas de exactidação
        1. [x] Matriz de confusão
        2. [x] Recall
        3. [x] Precision
        4. [x] F1-score
2. [ ] Experiências inciais com classificador simples
    - [x] k-Nearest  Neighbours (kNN)
    - [x] dataset Iris
    1. [x] Avaliar a capacidade de previsão, k = 1
        1. [x] Train-only, TT 70-30 e 10x10-fold cross-validation (10CV)
        2. [x] Train-only, TVT 40-30-30 e 10x10CV, k = 1 ,3 ,5 , ..., 15
        3. [ ] Análise em termos bias-variancee underfitting-overfitting
    2. [ ] Repetir 2.1. com ReliefF e selecionar o modelo ideal
        1. [ ] Utilizar F1-score
        2. [ ] Gráfico do cotovelo
        3. [ ] Apresentar no conjunto de validação para todas as combinações de features e parâmetros testados. Análise em termos bias-variancee underfitting-overfitting
        4. [ ] Apresentar modelo ideal no conjunto de testes. Comparar com o conjunto de validação. Concluões.
    3. [ ] Repetir 2.2. com o algoritmo forward feature selection (FFS)
    4. [ ] Repetir 2.3. restringindo a classe iris-versicolor a 30 e a 10. Analisar em termos do impacto da class imbalance.
3. [ ] Repetir 2. restringindo a seleção de features ao algoritmo ReliefF
4. [ ] Repetir 2. usando TVT, MLP com 3 camadas, nº variável de neurónios na camda escondida, função de ativação logística, batch learnig
    1. [ ] Velocidade de aprendizagem fixa
    2. [ ] Velocidade de aprendizagem variável
    3. [ ] Coeficiente de momentum
    4. [ ] Discussão do 4.1. a 4.3. com 2. a 3.
5. [ ] Rede neuronal de raíz usando para treino o algoritmo de retropropagação do erro
        



