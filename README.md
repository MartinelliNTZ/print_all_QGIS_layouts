# 🧭 Manual de Uso — Script de Exportação de Layouts QGIS
  **Criado por:** M. Martinelli  
  **Data de criação:** 30/10/2025  
  **Última alteração:** 31/10/2025  

  ---

  ## 📘 Objetivo do Script
        Este script tem como finalidade **exportar automaticamente todos os layouts existentes** em um projeto do **QGIS** para os formatos **PDF** e **PNG**, garantindo uma exportação limpa e padronizada, sem modificar nada no projeto original.

        Ideal para gerar impressões rápidas de todos os layouts com um único comando, de forma segura e controlada.

  ---

  ## ⚙️ Pré-requisitos
        1. O **projeto QGIS (.qgz)** deve estar **salvo** antes da execução.  
        2. Execute o script no **Console Python do QGIS** (`Ctrl + Alt + P`).  
        3. Certifique-se de que o projeto contém layouts criados.

  ---

  ## 📂 Estrutura e Comportamento

    ### 🧱 Criação da Pasta de Saída
          - O script cria automaticamente uma pasta chamada **`exports`** dentro do **diretório onde o projeto está salvo**.  
            Exemplo:
            C:\MeusProjetosQGIS\Projeto_A\exports

          - Caso prefira, é possível definir um caminho fixo no código, alterando esta linha:
          ```python
          #output_folder = r"C:\Users\Public\Documentos de Exportação QGIS"

    🔄 Controle de Arquivos Existentes

          O comportamento ao lidar com arquivos já existentes é controlado pela variável:

          modo_arquivos = "renomear"

          Opções disponíveis:

          "renomear" → Cria versões numeradas quando o arquivo já existe.
          Exemplo:

          MapaPrincipal.pdf
          MapaPrincipal_1.pdf
          MapaPrincipal_2.pdf


          "substituir" → Sobrescreve automaticamente os arquivos existentes.

    🖨️ Processo de Exportação

          Para cada layout encontrado no projeto, o script executa as seguintes etapas:

          Limpeza do nome do layout: remove caracteres inválidos (<>:"/\|?*).

          Exportação para PDF: utiliza QgsLayoutExporter.PdfExportSettings().

          Exportação para PNG: usa QgsLayoutExporter.ImageExportSettings(), mantendo o DPI original.

          Mensagens de status são exibidas no console, informando o progresso e eventuais erros.

          Exemplo de saída:

    🖨️ Exportando 3 layout(s) para C:\ProjetosQGIS\exports...

          ✅ Mapa_Topografico exportado como PDF e PNG.
          ✅ Carta_Geologica exportado como PDF e PNG.
          ✅ Perfil_Solo exportado como PDF e PNG.

    🎉 Exportação concluída com sucesso!

    ⚠️ Tratamento de Erros

          Mostra mensagens de erro individualmente por layout.

          Continua exportando os demais layouts mesmo após um erro.

          Interrompe apenas se o valor de modo_arquivos for inválido.

          Captura erros inesperados e exibe a mensagem completa no console.

    🧩 Resumo Técnico do Funcionamento

          Importação dos módulos

          QgsProject e QgsLayoutExporter para acessar e exportar os layouts.

          os e datetime para manipulação de caminhos e arquivos.

          Obtenção do caminho do projeto

          Usa QgsProject.instance().homePath() para localizar o diretório atual.

          Criação da pasta de saída (exports)

          É criada automaticamente se ainda não existir.

          Listagem e exportação dos layouts

          O script percorre todos os layouts e gera arquivos PDF e PNG para cada um.

          Mensagens de feedback no console

          Exibe status detalhado de cada exportação, informando sucesso ou erro.

    💡 Boas Práticas

          Dê nomes curtos e sem caracteres especiais aos layouts.

          Salve o projeto antes de executar o script.

          Evite caminhos de rede (use locais no disco).

          Faça backup da pasta exports se for usar o modo "substituir".

          Pode ser integrado a atalhos ou botões personalizados no QGIS.

    ✅ Resultado Final

          Após a execução, você terá:

          Todos os layouts do projeto exportados automaticamente.

          Arquivos em PDF e PNG prontos para uso.

          Nenhuma alteração feita no projeto QGIS original.

    🧾 Informações Complementares

          Autor: M. Martinelli

          Data: 31/10/2025

          Compatível com: QGIS 3.22 ou superior

          Linguagem: Python 3

          Ambiente: Console Python do QGIS

    🪶 Licença e Uso

          Este script pode ser usado e adaptado livremente, desde que mantida a autoria original.
          Recomenda-se documentar alterações com data e autor para controle de versões.
