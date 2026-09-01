====================================================================
                        VIDEO DOWNLOADER
====================================================================

DESCRICAO:
  Script em Python desenvolvido para automacao e extração de 
  video-aulas e midias protegidas (HLS/.m3u8) via web, utilizando 
  yt-dlp e FFmpeg com suporte a bypass de autenticacao/headers.

====================================================================
1. PRE-REQUISITOS E DEPENDENCIAS
====================================================================

- Python 3.10 ou superior
- FFmpeg (Processador e multiplexador de midia)
- yt-dlp (Extrator de fluxos de video)

Instalacao via terminal no Arch Linux / CachyOS:
  $ sudo pacman -S ffmpeg yt-dlp

====================================================================
2. ESTRUTURA DE ARQUIVOS
====================================================================

  Video Downloads/
  |-- baixa_m3u8-V2.py  # Script principal otimizado (Final)
  |-- baixa_video.py    # Script legado de testes
  |-- README.md         # Documentacao formatada para GitHub/GitLab
  `-- README.txt        # Este arquivo de documentacao simplificada

====================================================================
3. FLUXO DE USO E EXECUCAO
====================================================================

PASSO 1: Obter a URL do fluxo (.m3u8) no navegador
--------------------------------------------------------------------
1. Acesse a pagina da video-aula no seu navegador (Brave/Firefox).
2. Pressione F12 para abrir as Ferramentas do Desenvolvedor (DevTools).
3. Selecione a aba "Rede" (Network) e clique na sub-aba "Fetch/XHR".
4. No campo de busca/filtro, digite: m3u8
5. De Play no video para dar inicio ao carregamento da midia.
6. Localize a requisicao do manifesto principal (ex: master.m3u8).
7. Clique com o botao direito sobre ela -> Copiar -> Copiar endereco do link.

PASSO 2: Executar o script Python
--------------------------------------------------------------------
Via Terminal (Fish / Bash):
1. Navegue ate a pasta do projeto.
2. Execute o comando:
     $ python baixa_m3u8-V2.py
3. Cole a URL .m3u8 obtida no Passo 1 e pressione Enter.

Via PyCharm:
1. Abra o arquivo 'baixa_m3u8-V2.py'.
2. Pressione Ctrl + Shift + F10 (ou clique com o botao direito no 
   editor e selecione "Run 'baixa_m3u8-V2'").
3. Cole a URL .m3u8 no terminal interno da IDE quando solicitado.

====================================================================
4. AUTENTICACAO E CONFIGURACOES AVANCADAS
====================================================================

- Sessao do Navegador: O script utiliza a opcao 'cookiesfrombrowser' 
  configurada para ('brave',). Caso utilize outro navegador, altere 
  para 'firefox', 'chrome' ou 'edge' no dicionario ydl_opts.

- Cabecalhos HTTP: Inclui simulacao de Referer ('https://play.hotmart.com/') 
  e User-Agent para evitar erros de acesso negado (HTTP 403 Forbidden).

- Destino dos Arquivos: Os videos finalizados em formato .mp4 sao 
  salvos automaticamente na pasta ~/Downloads do usuario.
====================================================================
