# Trabalho Prático 3 - Qualidade do projeto de código

## Simplicidade

Uma das mais importante características de um bom projeto, a simplicidade não deve nunca ser confudinda com incapacidade. Um projeto simples, ao mesmo tempo que deve ser de fácil entendimento, cumpre seu propósito evitando ao máximo manchas e maus cheiros e de fácil implementação. Isso faz com que a simplicidade esteja diretamente relacionada com as demais características presentes em um bom software. Aumentar a modularirade, tornando os elementos mais atômitos e singulares, significa reduzir a complexidade e facilitar entendimento, remover duplicidades significa evitar retrabalho desnecessário e ao escrever um código 'idiomático' garante-se que qualquer um consiga ler, enteder e trabalhar com ele. Uma construção simples pode inclusive melhorar a eficiência em um projeto quando bem executada.

## Evitar Duplicidade

Um código bem desenvolvido não contém nenhum tipo de duplicidade desnecessária. Um código com muitas repetições perde suas elegância e sua simpliciade. O maior causador desse tipo de problema é o comando "Copiar e Colar" que faz com que o desenvolvedor não procure uma solução e faz com que ele não tenha uma compreensão total do sistema. Essa duplicação dificulta a manutenção no código uma vez que toda mudança em um local exige que também seja realizado em todos os outros que possuem essa repetição.
No projeto foi encontrado problemas desse tipo com os seguintes cheiros:

- Código duplicado

A solução encontrada foi a realização de uma "extração de método" de tal maneira que sempre que for necessário realizar tal rotina só é preciso fazer uma chamada para aquela função. (Link do commit)[https://github.com/Grupo-de-TPPE/tp1-TDD/pull/2/commits/c0626aa8288eb720fa0409bf3679d5e28dc5e0d8]

## Elegância

Incorpora os aspectos estéticos do design, muitas das vezes estando altamente atrelado à simplicidade. Significando que o código não é barroco, não é confuso, não é muito complexo e é muito inteligente.
"Um código bem projetado tem beleza em sua estrutura." (FOWLER, 2006)
Um código elegante tem as seguintes caracterísitcas:

 - Cada parte complementa outras, acrescentando algo distinto e de valor ao projeto.
 - Associa partes semelhantes.
 - Não existem inconsistências e nem situações inesperadas.
 - Design não está repleto de casos especiais.
 - Localidade de mudança (uma mudança em um lugar não deve propagar mudanças para outros trechos do código)
 - Controle do fluído (uma operação não deve percorrer cada componente do código) 

Um design elegante tem a ver com estética e equilíbrio, quase como arte.

Aplicações práticas que garantem elegância ao código:
 - Método em linha
 - Extração de código

## Boa documentação

Não existe regra para a documentação de softwares em metodologias ágeis. Geralmente, a estrutura é aperfeiçoada ao longo do tempo, do mesmo jeito que a própria colaboração e produtividade da equipe se adéqua durante o ciclo de vida de uma aplicação. Mas, em termos gerais, documentos do tipo precisam ter três elementos:

- contextualização de problema: informa cada obstáculo durante o desenvolvimento e em que situação ele ocorreu;
- contextualização de solução: explica as modificações feitas em processos ou no código que corrigiram o problema;
- detalhes técnicos: familiarizam o responsável por aquela parte do desenvolvimento sobre como, quando e por que aquela intervenção foi realizada.

Um projeto bem documentado ajuda a guiar as pessoas que estão mexendo nele e nas pessoas que vão mexer nesse projeto posteriormente. Ainda que um desenvolvedor seja novo na equipe ou esteja procurando soluções para problemas já enfrentados, o histórico de desenvolvimento é uma base para se situar, observar o que já foi feito e evoluir a partir daí, sem nunca ter que dar um passo para trás.

Ter essas informações básicas sobre cada iteração e resolução dentro do desenvolvimento de um software é suficiente para impedir que a equipe ande em círculos e perca tempo com obstáculos já superados no passado. Esse esforço economizado pode servir para adicionar novas funcionalidades à aplicação ou, até mesmo, polir o código para uma maior qualidade de produto.

Uma possível relação da característica com os maus-cheiros de código definidos por Fowler é a de 'comentários', se o código está bem documentado, claro, que o código deve estar limpo e simples, mas com a ajuda da boa documentação os comentários do código não serão mais necessários. E com isto, o nosso exemplo de boa documentação é o nosso README e para potencializar a nossa documentação, seria adicionar os pontos citados.

## Idiomático

Um código idiomático utiliza aquilo que as suas ferramentas tem a oferecer. De acordo com Fowler "Um bom design naturalmente emprega boas práticas, mesclando metodologias do UX com a implementação das normas da linguagem". Isso permite que um usuário que já está acostumado com um padrão de código ter mais facilidade ao interagir com o que você produziu.
No projeto foi encontrado problemas desse tipo com os seguintes cheiros:

- Códigos longos

A solução encontrada foi a remoção de múltiplos condicionais encadeados com o uso de loops iterativos que o python permite, conforme pode ser visto no (commit)[https://github.com/Grupo-de-TPPE/tp1-TDD/pull/2/commits/9f99dcad5bbf11c178318042bedccac38cbd5cd3].


## Referências

- 6 boas práticas para documentação com desenvolvimento ágil de softwares. Disponível em: https://blog.cronapp.io/documentacao-com-desenvolvimento-agil-de-softwares/ Acesso em: 19 de Set. de 2022
