from qgis.core import (
    QgsProject,
    QgsLayoutExporter
)
import os
from datetime import datetime
import re

"""
🧭 Script de Exportação de Layouts QGIS
Autor: M. Martinelli
Criado em: 30/10/2025 | Atualizado: 31/10/2025

Descrição:
Exporta automaticamente todos os layouts do projeto QGIS para PDF e PNG,
sem alterar o projeto original.

Uso:
- Salve o projeto antes de executar.
-⚠️⚠️⚠️⚠️⚠️⚠️SEMPRE CRIE UMA COPIA DO PROJETO ANTES DE EXECUTAR O SCRIPT⚠️⚠️⚠️⚠️⚠️⚠️⚠️
- Rode o script no Console Python do QGIS (Ctrl + Alt + P).
- Cada layout será exportado para PDF e PNG dentro da pasta 'exports'.

Configurações:
modo_arquivos = "renomear"  → cria versões numeradas
modo_arquivos = "substituir" → sobrescreve arquivos existentes

Saída:
Pasta 'exports' contendo todos os layouts em PDF e PNG.

Observações:
- Remove caracteres inválidos dos nomes.
- Mostra mensagens de sucesso ou erro no console.
- Não altera o projeto QGIS original.
"""

# Opções: "substituir" ou "renomear"
modo_arquivos = "renomear"  # altere para "substituir" se quiser sobrescrever

# Pasta de saída (fica dentro do diretório do projeto) 
output_folder = os.path.join(QgsProject.instance().homePath(), "exports")

#Método para caminho absoluta da pasta de saida
#output_folder = r"C:\Users\Public\Documentos de Exportação QGIS"


# Cria a pasta se não existir
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# === EXECUÇÃO ===
project = QgsProject.instance()
layouts = project.layoutManager().layouts()

if not layouts:
    print("⚠️ Nenhum layout encontrado no projeto.")
else:
    print(f"🖨️ Exportando {len(layouts)} layout(s) para {output_folder}...\n")

    for layout in layouts:
        layout_name = layout.name().strip()
        # Remove caracteres inválidos em nomes de arquivo (Windows, Linux, macOS)
        layout_name = re.sub(r'[<>:"/\\|?*]', '', layout_name)
        pdf_path = os.path.join(output_folder, f"{layout_name}.pdf")
        png_path = os.path.join(output_folder, f"{layout_name}.png")

        # Se o arquivo já existir, decide o que fazer
        if modo_arquivos.lower() == "renomear":
            base_name = layout_name
            count = 1
            while os.path.exists(pdf_path) or os.path.exists(png_path):
                layout_name = f"{base_name}_{count}"
                pdf_path = os.path.join(output_folder, f"{layout_name}.pdf")
                png_path = os.path.join(output_folder, f"{layout_name}.png")
                count += 1
        elif modo_arquivos.lower() == "substituir":
            # Apenas segue em frente, sobrescrevendo
            pass
        else:
            print(f"⚠️ Modo '{modo_arquivos}' inválido. Use 'renomear' ou 'substituir'.")
            break

        # === Exportação ===
        try:
            exporter = QgsLayoutExporter(layout)

            # Exportar para PDF
            pdf_settings = QgsLayoutExporter.PdfExportSettings()
            result_pdf = exporter.exportToPdf(pdf_path, pdf_settings)
            if result_pdf != QgsLayoutExporter.Success:
                print(f"❌ Erro ao exportar PDF de {layout_name} (código {result_pdf})")

            # Exportar para PNG (usa DPI do layout, não força)
            img_settings = QgsLayoutExporter.ImageExportSettings()
            result_png = exporter.exportToImage(png_path, img_settings)
            if result_png != QgsLayoutExporter.Success:
                print(f"❌ Erro ao exportar PNG de {layout_name} (código {result_png})")

            # Se chegou até aqui, tudo certo
            if result_pdf == QgsLayoutExporter.Success and result_png == QgsLayoutExporter.Success:
                print(f"✅ {layout_name} exportado como PDF e PNG.")

        except Exception as e:
            print(f"❌ Erro inesperado ao exportar {layout_name}: {e}")

    print("\n🎉 Exportação concluída com sucesso!")

    """
🧭 Docstring detalhado — Script de Exportação de Layouts QGIS (passo a passo)
Script: Exportação automática de layouts para PDF e PNG
Autor: M. Martinelli
Criado em: 30/10/2025 | Atualizado: 31/10/2025

Objetivo:
Exportar todos os layouts do projeto QGIS atual para arquivos PDF e PNG,
salvando-os numa pasta de saída local, sem modificar camadas ou dados do projeto.

AVISO IMPORTANTE:
⚠️⚠️⚠️ SEMPRE FAÇA UMA CÓPIA DO PROJETO ANTES DE EXECUTAR. ⚠️⚠️⚠️

Passo a passo (funcionamento interno):

1) Importações e preparação
   - O script importa módulos necessários (QgsProject, QgsLayoutExporter, os, datetime).
   - Observação: o script usa a função re.sub para sanitizar nomes, portanto
     é necessário `import re` se não estiver presente.

2) Configuração do modo de arquivo
   - Variável `modo_arquivos` controla como lidar com arquivos já existentes:
       - "renomear": cria versões numeradas (ex.: Layout, Layout_1, Layout_2...)
       - "substituir": sobrescreve os arquivos existentes com o mesmo nome
   - Se `modo_arquivos` estiver com valor inválido, o script para e imprime aviso.

3) Definição da pasta de saída
   - `output_folder` é construída a partir do diretório do projeto (`QgsProject.instance().homePath()`)
     e o nome "exports", a menos que você descomente e defina um caminho absoluto.
   - O script cria a pasta de saída se ela não existir (`os.makedirs(output_folder)`).

4) Carregamento do projeto e coleta de layouts
   - `project = QgsProject.instance()` obtém a instância atual do projeto aberto no QGIS.
   - `layouts = project.layoutManager().layouts()` retorna a lista de layouts (objetos QgsLayout).

5) Validação inicial
   - Se não houver layouts, o script imprime aviso e termina.
   - Caso contrário, imprime quantos layouts serão exportados e o caminho de saída.

6) Loop por cada layout
   - Para cada layout:
     a) Obtém o nome do layout (`layout.name().strip()`).
     b) Remove caracteres inválidos para nomes de arquivo usando expressão regular:
        `re.sub(r'[<>:"/\\|?*]', '', layout_name)` — evita problemas em Windows/Linux/macOS.
     c) Define caminhos completos para PDF e PNG (`pdf_path`, `png_path`).

7) Política de arquivos já existentes
   - Se `modo_arquivos` == "renomear":
       - Incrementa um sufixo `_1`, `_2`, ... até encontrar nomes livres para PDF e PNG.
   - Se `modo_arquivos` == "substituir":
       - Prossegue com os caminhos definidos, sobrescrevendo arquivos existentes.
   - Se `modo_arquivos` for inválido:
       - Imprime erro e interrompe a execução.

8) Exportação propriamente dita
   - Cria um `QgsLayoutExporter(layout)` para o layout em questão.
   - Exporta PDF:
       - `pdf_settings = QgsLayoutExporter.PdfExportSettings()`
       - `result_pdf = exporter.exportToPdf(pdf_path, pdf_settings)`
       - Verifica se `result_pdf == QgsLayoutExporter.Success`; se não, imprime erro.
   - Exporta PNG:
       - `img_settings = QgsLayoutExporter.ImageExportSettings()`
       - `result_png = exporter.exportToImage(png_path, img_settings)`
       - Verifica se `result_png == QgsLayoutExporter.Success`; se não, imprime erro.
   - Se ambos os exports retornarem sucesso, imprime mensagem de confirmação.

9) Tratamento de exceções
   - A exportação é envolvida em blocos try/except para capturar erros inesperados
     (ex.: problemas de I/O, permissões, objetos corrompidos) e imprimir uma mensagem
     com o erro capturado sem encerrar o processamento dos demais layouts.

10) Finalização
    - Após o loop, imprime mensagem de conclusão.
    - Nota: O script **não altera** o conteúdo do projeto (camadas, estilos, dados).
    - Arquivos gerados ficam na pasta `output_folder` e são permanentes no disco.

Limitações e recomendações:
- O script usa as configurações padrão de exportação (PdfExportSettings / ImageExportSettings).
  Se precisar ajustar DPI, compressão, resolução de imagem, papel, recortes ou camadas visíveis,
  deve configurar explicitamente os objetos `PdfExportSettings` / `ImageExportSettings`.
- Teste em um projeto de cópia antes de rodar em produção.
- Se os nomes dos layouts forem muito longos ou repetitivos, considere truncar ou padronizar
  nomes antes da exportação para evitar path demasiado longo.
- Se o projeto estiver em uma pasta com espaços (ex.: "Meus Documentos/Export QGIS"), o script
  funciona normalmente — `os.path.join` lida com espaços. Caso prefira, defina explicitamente um caminho
  bruto (r-prefixed) em `output_folder`.

Resultados esperados:
- Pasta `exports` contendo para cada layout dois arquivos: `<layout_name>.pdf` e `<layout_name>.png`
  (ou versões numeradas se `modo_arquivos` = "renomear").
- Mensagens de log no console com sucesso/erro por layout.

Segurança:
- O script não grava/overwrita o arquivo .qgz do projeto — ele apenas lê o projeto em memória e escreve
  arquivos de exportação no disco. Ainda assim, sempre faça backup antes de executar.

"""

