# 📹 Video Downloader HLS (`.m3u8`)

Script em Python desenvolvido para automação, extração e download de vídeo-aulas e mídias protegidas por streaming (HLS/`.m3u8`) via web, utilizando `yt-dlp` e `FFmpeg` com suporte a bypass de autenticação e cabeçalhos HTTP.

> 🎓 **Projeto acadêmico** desenvolvido para a disciplina de Programação Estruturada do curso de Ciência da Computação, focado no estudo de protocolos de streaming HLS (*HTTP Live Streaming*) e automação de requisições web.

---

## 🛠️ 1. Pré-requisitos e Dependências

- **Python 3.10** ou superior
- **FFmpeg:** Processador e multiplexador de mídia
- **yt-dlp:** Extrator de fluxos de vídeo

### Instalação das dependências no Arch Linux / CachyOS:

No terminal (Fish Shell / Bash), execute:

sudo pacman -S ffmpeg yt-dlp

---

## 📁 2. Estrutura de Arquivos
```text
Video Downloads/
      ├── baixa_m3u8-V2.py
      ├── baixa_video.py
      ├── README.md
      └── README.txt
```
---

## 🚀 3. Fluxo de Uso e Execução

PASSO 1: Obter a URL do fluxo (.m3u8) no navegador
Acesse a página da vídeo-aula no seu navegador (Brave, Firefox, Chrome).

Pressione F12 para abrir as Ferramentas do Desenvolvedor (DevTools).
Selecione a aba Rede (Network) e clique no filtro Fetch/XHR.
No campo de busca/filtro, digite: m3u8
Dê Play no vídeo para dar início ao carregamento da mídia.
Localize a requisição do manifesto principal (ex: master-pkg-t-...m3u8 ou master.m3u8).
Clique com o botão direito sobre ela → Copiar → Copiar endereço do link (Copy link address).

PASSO 2: Executar o script Python
Via Terminal (Fish / Bash):
Navegue até a pasta do projeto:

Snippet de código
cd "Video Downloads"
Execute o script principal:

Snippet de código
python baixa_m3u8-V2.py
Cole a URL .m3u8 obtida no Passo 1 e pressione Enter.

Via PyCharm:
Abra o arquivo baixa_m3u8-V2.py.

Pressione Ctrl + Shift + F10 (ou clique com o botão direito no editor e selecione Run 'baixa_m3u8-V2').

Cole a URL .m3u8 no terminal interno da IDE quando solicitado e pressione Enter.

Alguns fluxos da Hotmart e players embarcados não usam .m3u8 com ponto no nome do arquivo final da requisição 
(muitas vezes vem como master ou em parâmetros com hash sem extensão explícita).

Como fazer a requisição aparecer:
      Caso não apareça nada, limpe a caixa de busca e selecione a aba All (em vez de Fetch/XHR).
      Recarregue a página.
      Pressione F5 (com o DevTools aberto).
      Dê Play no vídeo caso ele não inicie sozinho.

---

## ⚡ 4. Autenticação e Recursos Avançados

Sessão do Navegador (cookiesfrombrowser): O script utiliza a extração de cookies configurada por padrão para o navegador brave. Caso utilize outro navegador, altere para 'firefox', 'chrome' ou 'edge' no dicionário ydl_opts.

Cabeçalhos HTTP (Bypass 403 Forbidden): Inclui simulação de Referer (https://play.hotmart.com/) e User-Agent para burlar a checagem de origem do player nativo.
Gravação Direta (nopart: True): Elimina a criação do arquivo temporário com extensão .part, gravando diretamente o arquivo definitivo .mp4.
Tratamento de Logs do FFmpeg: Injeção do parâmetro -loglevel repeat+level+error para suprimir mensagens e avisos amarelados irrelevantes de invalid timestamps.

Destino dos Arquivos: Os vídeos finalizados em formato .mp4 são salvos automaticamente na pasta ~/Downloads do sistema.
