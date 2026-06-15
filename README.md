# GURGEL

## Integrantes

* Integrante 1: Júlia Lemos Souza - RM 569089
* Integrante 2: Erick Yu Xiang Li - RM 569305
* Integrante 3: Erick Banhos de Castro - RM 572131
* Integrante 4: Victor Henrique Nogueira Bezerra Azevedo de Souza - RM 570021
* Integrante 5: Carlos Henrique - RM 573334
* Integrante 6: Gustavo Araújo Ramos da Silva - RM 574156

---

## Sobre o Projeto

A Gurgel é uma plataforma desenvolvida para auxiliar no gerenciamento energético de eletropostos para veículos elétricos.

O projeto utiliza conceitos de automação, inteligência artificial baseada em regras e energias renováveis para distribuir energia de forma mais eficiente entre os veículos conectados.

A proposta busca demonstrar como a tecnologia pode contribuir para uma mobilidade mais sustentável, reduzindo desperdícios energéticos e melhorando a utilização dos recursos disponíveis.

---

## Problema

Com o crescimento da mobilidade elétrica, aumenta também a demanda por estações de carregamento.

Em horários de pico, diversos veículos podem solicitar energia simultaneamente, gerando sobrecarga na rede elétrica e utilização ineficiente dos recursos energéticos.

Além disso, existe o desafio de integrar fontes renováveis de energia, como a energia solar, a sistemas capazes de tomar decisões rápidas e inteligentes.

---

## Solução Proposta

A Gurgel monitora a energia disponível, identifica a necessidade de carregamento dos veículos conectados e distribui a potência de forma automática.

O sistema também utiliza tarifação dinâmica, ajustando o valor da energia de acordo com a demanda observada.

Dessa forma, busca-se melhorar a eficiência energética da operação e incentivar um consumo mais equilibrado.

---

## Funcionalidades

* Simulação de geração de energia solar
* Monitoramento dos veículos conectados
* Priorização de carregamento baseada no nível de bateria
* Distribuição inteligente de potência
* Tarifação dinâmica
* Relatório operacional
* Simulação de diferentes cenários de geração energética

---

## Arquitetura do Sistema

```text
Energia Solar Simulada
          |
          v
Monitoramento dos Veículos
          |
          v
Análise das Informações
          |
          v
Motor de Decisão
(Inteligência Artificial baseada em regras)
          |
          v
Distribuição de Potência
          |
          v
Relatório e Monitoramento
```

![Fluxo Visual do Sistema]

## Fluxo de Funcionamento

1. O sistema gera uma quantidade simulada de energia solar.
2. Os veículos conectados informam seus níveis de bateria.
3. A plataforma analisa quais veículos possuem maior necessidade de carregamento.
4. A energia disponível é distribuída conforme as prioridades definidas.
5. O sistema calcula a tarifa de acordo com a demanda energética.
6. Um relatório final é apresentado ao usuário.

---

## Tecnologias Utilizadas

* Python
* Random
* Estruturas de decisão (if, elif e else)
* Estruturas de repetição (for)

---

## Interoperabilidade

A solução foi projetada para possibilitar integração futura com diferentes eletropostos, sistemas de pagamento e plataformas de monitoramento energético.

A arquitetura permite que informações de veículos, energia disponível e tarifação sejam compartilhadas entre diferentes sistemas, favorecendo a expansão da rede de carregamento inteligente.

---

## Sustentabilidade

A solução utiliza uma simulação de geração solar para representar o uso de fontes renováveis de energia.

Além disso, o gerenciamento inteligente da distribuição energética contribui para:

* Redução de desperdícios
* Melhor aproveitamento da energia disponível
* Incentivo ao uso de fontes limpas
* Apoio ao crescimento da mobilidade elétrica sustentável

## Inteligência Artificial Utilizada

A inteligência artificial da Gurgel foi simulada através de regras de decisão.

O sistema analisa automaticamente o nível de bateria dos veículos conectados e identifica qual possui maior necessidade de carregamento.

Com base nessa análise, a plataforma define prioridades e distribui a energia disponível de forma mais eficiente.

Embora seja uma prova de conceito, essa abordagem demonstra como técnicas simples de tomada de decisão podem ser aplicadas ao gerenciamento inteligente de eletropostos.


---

## Evolução da Sprint 1

Na Sprint 1 foi apresentada a proposta conceitual da solução, incluindo o problema identificado, a arquitetura planejada e os benefícios esperados.

Na Sprint 2 foi desenvolvido um protótipo funcional capaz de simular cenários reais de geração e consumo energético, aplicar regras de decisão automática e demonstrar o funcionamento da solução na prática.

Essa evolução permitiu validar tecnicamente a proposta e comprovar sua viabilidade inicial.

---

## Considerações Finais

A Gurgel demonstra como conceitos de automação, inteligência artificial e energias renováveis podem ser utilizados para desenvolver soluções mais eficientes para o gerenciamento energético de eletropostos.

O projeto representa uma prova de conceito funcional e um primeiro passo para aplicações mais avançadas voltadas à mobilidade elétrica sustentável.

---

## Demonstração do Projeto

### Vídeo de Apresentação

https://youtu.be/DAt07ansOv0

### Slides da Apresentação

https://canva.link/085hc6r3zxnjtu9

https://canva.link/cal60z3qbt560kl

---

### Kanban de organização

https://trello.com/invite/b/69e017199b63551c0ab1d73a/ATTI0eedf610ca70dc2e390796d26150040aC6F549C7/gurgel

---

## Repositório

GitHub do projeto:

https://github.com/jucalemos/sprint2.1_gurgel.git


---

## Como Executar

1. Abra o projeto no PyCharm.
2. Execute o arquivo `main.py`.
3. O sistema irá gerar automaticamente um cenário de operação.
4. Os resultados serão exibidos diretamente no terminal.

