# Automatizando-o-ajuste-de-hiperpar-metros-do-modelo-CNN-usando-ferramentas-de-DevOps

Automatizando o ajuste de hiperparâmetros do modelo CNN usando ferramentas de DevOps
Necessitamos criar uma imagem de contêiner com o Docker que tenha as bibliotecas Python3, Jupyter-Notebook, Keras, TensorFlow, OpenCV, Numpy e Pandas instaladas usando o Dockerfile. Necessitamos automatizar esse contêiner de forma que assim que inicializamos esse contêiner no Linux REDHAT OS, ele começará automaticamente a treinar o modelo de aprendizado de máquina, que criamos na rede neural convolucional usando um conjunto de dados que temos. Esse modelo consiste em um conjunto de hiperparâmetros que necessitamos afinar cada vez que o modelo é treinado até que ofereça mais de 80 % de precisão. Agora, usando as ferramentas de automatização do Jenkins no RHEL, necessitamos criar 5 tarefas que resolverão automaticamente o problema real.

 ![image](https://user-images.githubusercontent.com/90334631/180627230-50c8cc7b-1423-4be1-8f42-bcae9442f257.png)

# Hiperparâmetro

No aprendizado de máquina, o hiperparâmetro é um parâmetro cujo valor é definido antes do início do processo de aprendizado. Por outro lado, os valores dos outros parâmetros são derivados por treinamento. Eles podem ser classificados como hiperparâmetros do modelo que não podem ser decididos ao ajustar o conjunto de dados à máquina porque dizem respeito à tarefa de seleção do modelo ou hiperparâmetros do algoritmo, que em princípio não têm influência no desempenho do modelo, mas afetam a velocidade e a qualidade do processo de aprendizado. Um exemplo de modelo hiperparamétrico é a topologia e o tamanho da rede neural. exemplos de algoritmos de hiperparâmetros são a taxa de aprendizado e o tamanho do minilote.
Diferentes algoritmos de treinamento de modelo necessitar diferentes hiperparâmetros, alguns algoritmos simples não. Dados esses hiperparâmetros, o algorítmo de aprendizado aprende os parâmetros dos dados. Por exemplo, Lasso é um algorítmo que adiciona um parâmetro regulador a uma regressão linear, que deve ser determinada antes que os parâmetros sejam estimados pelo algorítmo de aprendizado.

Aqui, hiperparâmetro que estamos usando e são usados em nosso modelo CNN.

 ![image](https://user-images.githubusercontent.com/90334631/180627239-f3ac9a44-f5ba-492e-8762-f4f30f2c1053.png)


No código acima existem duas Convolution Layer e duas Pooling Layer e os valores que atravessamos em filtros como Convolution2D e MaxPooling2D, kernel_size é um dos exemplos de hiperparâmetro que necessitamos alterar se nossa acurácia não for boa. Consequentemente, necessitamos alterar o número de camadas de torção e agregação em nosso modelo para melhorar a acurácia.

 ![image](https://user-images.githubusercontent.com/90334631/180627246-0dd88d8f-1259-4bc3-849e-566cd5af3ecf.png)


Há também várias eras na imagem acima. step_per_epoch Este é um exemplo de um hiperparâmetro que iremos customizar.


# Rede Neural Convolucional

A Rede Neural Convolucional (CNN) é um tipo de RNA usado para reconhecimento e processamento de imagens. Ele é projetado especificamente para processar dados de píxel. CNN é uma inteligência artificial que usa processamento de imagem poderoso, aprendizado profundo para executar tarefas generativas e descritivas, geralmente incluindo reconhecimento de imagem e vídeo, além de sistemas recomendados e processamento de linguagem natural. Usar visão de máquina.

Abaixo está a arquitetura do meu modelo CNN antes do ajuste de hiperparâmetros usando DevOps.
![image](https://user-images.githubusercontent.com/90334631/180627250-7d7fbe11-05a7-4d0e-ba7e-2721252e4ab2.png)

 

Agora que criamos essa arquitetura e necessitamos treinar nosso modelo provendo todas as imagens de treinamento no meu caso, tenho imagens My Face e Family Members Aparência como dados de treinamento para o modelo. O processo de otimização ou treinamento do nosso modelo é realizado pelo ambiente Docker. Agora a partir daqui vou trabalhar para citar o trabalho das ferramentas DevOps neste projeto. Os pontos a seguir esclarecem onde Jenkins, Docker e Git são usados para afinar hiperparâmetros para melhor precisão neste projeto.

# Usando Git e GitHub

O Git é usado principalmente para fazer upload e download de alterações de desenvolvedor e automação com comandos simples git push, pull, commit. O Git fará upload e download de código do Github ao mesmo tempo que o Github usando um recurso chamado WebHook. Para dizer ao Jenkins Job para carregar automaticamente o código para executar outras ações. 

# Contêinet Docker

Dockers são conhecidos no mercado por sua mobilidade. que pode iniciar o sistema operacional em apenas 1 ou 2 segundos. Os dockers geralmente usam a tecnologia de contêiner. Neste projeto, o Docker é usado para iniciar ambientes ou sistemas operacionais para executar código de Deep Learning ou código de aprendizado de máquina tradicional nele para obter a melhor precisão para o modelo de ML. Criei uma imagem docker de um pacote de aprendizado profundo para executar meu código Python da CNN.

 ![image](https://user-images.githubusercontent.com/90334631/180627257-ad7f43dc-b7af-4aa5-b80e-a2bd2d61de8e.png)

Para criar uma imagem usando este Dockerfile, basta usar o seguinte comando:

docker build -t "ImageName" "Local do directório que contém o Dockerfile"


# Automação-Jenkins

Jenkins é um servidor de automatização de código aberto gratuito. Ele automatiza parte do desenvolvimento de software relacionado à criação teste e implantação, facilitando a integração e a entrega contínuas. É um sistema de back-end que é executado em um contêiner de servlet, como o Apache Server.

# Emprego Jenkins  - Parte 1

Código de aprendizado de máquina (CNN): este trabalho é configurado para extrair dados automaticamente do Github e armazená-los no espaço de trabalho do Jenkins depois que o desenvolvedor carrega o código atualizado no Github. Também usamos o pipeline de compilação para essa automatização. Ele iniciará automaticamente o segundo trabalho quando o primeiro for concluído.
 
Desde que usei Webhooks para automatizar o upload de código do computador local para o github assim que o código for atualizado.

 ![image](https://user-images.githubusercontent.com/90334631/180627271-f38f37b9-6a55-48f4-8d2d-129d9cfa830d.png)



# Emprego do Jenkins - Parte 2

Tarefa Construir Contêineres: Esta tarefa foi projetada para determinar o tipo de pacotes usados no arquivo python principal. Quando os pacotes usados no arquivo permanecer em execução, a ferramenta de automação Jenkins iniciará um contêiner com todos os pacotes de aprendizado profundo do Python instalados, como Tensorflow, Keras, Numpy e Sklearn.
 
 ![image](https://user-images.githubusercontent.com/90334631/180627296-107013d2-e209-465f-ac8f-cff608ace657.png)

Como sabemos, todos os trabalhos fazem parte do pipeline de construção, portanto, como requisito do pipeline todos os trabalhos devem ser seriais, o que significa que um trabalho após o outro é concluído, então faço esse trabalho ser executado após project_job1 ter um build estável.

![image](https://user-images.githubusercontent.com/90334631/180627301-1bd0f01f-e076-43ad-96c8-9c2cf320d663.png)

 
Quanto à configuração, estou usando a opção create post que me notificará por e-mail sempre que houver uma alteração no project_job2.
 

# Emprego do Jenkins - Parte 3

Tarefa de treinamento de modelo – Esta tarefa é treinada para iniciar o processo de treinamento de nosso modelo de aprendizado profundo ou modelo CNN no respectivo contêiner que foi iniciado pela parte 2 acima.

![image](https://user-images.githubusercontent.com/90334631/180627346-a27fbdf8-6920-4899-8e24-62e5ca1d9fe6.png)

 
Como sabemos, todos os trabalhos fazem parte do pipeline de compilação, portanto, como um requisito do pipeline todos os trabalhos devem ser seriais, o que significa que um trabalho após o outro é concluído, então executam esse trabalho depois que o project_job2 teve uma compilação estável.

![image](https://user-images.githubusercontent.com/90334631/180627350-9eff9006-08c4-44e4-96b5-a3f1ba6e9b3b.png)



# Emprego do Jenkins - Parte 4

Função de ajuste do modelo CNN: Esta função tem esse recurso que irá determinar a acurácia do modelo treinado na etapa anterior e verificar se a acurácia é inferior a 80 %, então ela alterará automaticamente as configurações do Hyper no arquivo Python e o retornará. para o Github para iniciar este ciclo Job1 novamente. Se a precisão do modelo for > 80%, ele notificará o desenvolvedor e não alterará o hiperparâmetro. Este trabalho executa um script python que verifica a acurácia e ajusta o hiperparâmetro para este modelo.

![image](https://user-images.githubusercontent.com/90334631/180627353-8684106c-3d5e-4fba-8b28-fa20d193095c.png)

 

Como sabemos, todos os trabalhos fazem parte do pipeline de construção, portanto, como pré-requisito do pipeline todos os trabalhos devem ser seriais, o que significa que um trabalho após o outro é concluído, por esse motivo, executam este trabalho após project_job3 ter uma compilação estável.
 
 ![image](https://user-images.githubusercontent.com/90334631/180627358-f5b310fb-d941-46e4-a7fa-6a8af32f4b75.png)


Como podemos ver, o arquivo find_accuracy será executado no docker para encontrar a precisão e, se a precisão for inferior a 80 %, o modelo de aprendizado profundo será alterado automaticamente e basta enviá-lo para o Linux GitHub.

Todos os arquivos relacionados estão no meu repositório Git-Hub (link na parte inferior da página . Esses arquivos são muito importantes para este projeto, veja minha conta no GitHub para os motivos por trás disso.

# Emprego do Jenkins - Parte 5

Tarefa do Monitor de Projeto: Essa tarefa é especializada, portanto, será executada em um cronograma para verificar se os contêineres estão funcionando corretamente ou não, se meu contêiner TensorflowOS travar, ele reiniciará esse contêiner. Essa tarefa começa após a parte 2 e verifica o contêiner a cada minuto.
 
![image](https://user-images.githubusercontent.com/90334631/180627366-ef0243d4-816b-4663-bc82-43ca3bd69f02.png)

Como sabemos que todos os trabalhos fazem parte do pipeline de construção, como um requisito do pipeline todos os trabalhos devem ser seriais, o que significa que um trabalho após o outro é concluído, então executam este trabalho depois que project_job2 tem uma compilação estável para isso, também usou a opção Poll SCM que levará a verificar o projeto após cada minuto.
 
 ![image](https://user-images.githubusercontent.com/90334631/180627373-c8434713-b797-42f7-bb84-194e47952113.png)


Assim chegamos ao final deste projeto onde aplicamos a integração de duas das melhores tecnologias disponíveis no mercado ou seja; Aprendizado de máquina e DEVOPS. A combinação dessas duas tecnologias é conhecida como MLOPS. O projeto concluiu com sucesso a tarefa de usar ferramentas DevOps para ajustar os hiperparâmetros do modelo CNNML com uma consideração muito eficiente da complexidade de tempo e espaço.
