# 📹 Video Downloader HLS (`.m3u8`)

Script em Python projetado para automação, extração e download de vídeo-aulas hospedadas em plataformas protegidas (como a Hotmart), utilizando as ferramentas `yt-dlp` e `FFmpeg`.

> 🎓 **Projeto acadêmico** desenvolvido para o curso de Ciência da Computação, focado no estudo de protocolos de streaming HLS (*HTTP Live Streaming*) e automação de requisições web.

---

## 🛠️ Tecnologias e Dependências

- **Python 3.10+**
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp):** Biblioteca principal de extração e parsing do manifesto de streaming.
- **[FFmpeg](https://ffmpeg.org/):** Processamento e multiplexação dos segmentos `.ts` em contêiner `.mp4`.

### Instalação no Arch Linux / CachyOS:

No terminal (Fish Shell), execute o comando de instalação do ecossistema:

```fish
sudo pacman -S ffmpeg yt-dlp
