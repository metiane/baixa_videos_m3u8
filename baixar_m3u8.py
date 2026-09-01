import os
import yt_dlp


def hook_progresso(d):
    """
    Exibe uma barra de progresso dinâmica no terminal com porcentagem,
    tamanho baixado/total em MB, velocidade e tempo restante (ETA).
    """
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate') or 0
        downloaded = d.get('downloaded_bytes', 0)
        speed = d.get('speed', 0) or 0
        eta = d.get('eta', 0) or 0

        if total > 0:
            porcentagem = (downloaded / total) * 100

            # Converte bytes para MegaBytes (MB)
            downloaded_mb = downloaded / (1024 * 1024)
            total_mb = total / (1024 * 1024)
            speed_mb = speed / (1024 * 1024)

            # Desenha a barra visual no terminal
            barra_tamanho = 20
            preenchido = int(barra_tamanho * downloaded // total)
            barra = '█' * preenchido + '░' * (barra_tamanho - preenchido)

            print(
                f"\r⬇️ [{barra}] {porcentagem:.1f}% | "
                f"{downloaded_mb:.1f}MB / ~{total_mb:.1f}MB | "
                f"Velocidade: {speed_mb:.1f}MB/s | ETA: {eta}s",
                end="",
                flush=True
            )
    elif d['status'] == 'finished':
        print(
            "\n\n🎉 Download dos segmentos concluído! Unificando áudio e vídeo com o FFmpeg...")


def baixar_video(url_do_stream):
    pasta_destino = os.path.expanduser("~/Downloads")

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(pasta_destino, '%(title)s.%(ext)s'),
        'nopart': True,
        'cookiesfrombrowser': ('brave',),
        'http_headers': {
            'Referer': 'https://play.hotmart.com/',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        },
        # Registra o hook e desativa a saída padrão redundante
        'progress_hooks': [hook_progresso],
        'quiet': True,
        'no_warnings': True,
        'external_downloader_args': {
            'ffmpeg': ['-loglevel', 'repeat+level+error']
        },
    }

    print(f"Iniciando o processamento do vídeo...")
    print(f"Destino dos downloads: {pasta_destino}\n")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url_do_stream])
        print("✅ Processo concluído com sucesso!")
    except Exception as e:
        print(f"\n❌ Erro ao processar o vídeo: {e}")


if __name__ == "__main__":
    url = input("Digite a URL (.m3u8 ou da aula): ").strip()
    if url:
        baixar_video(url)
    else:
        print("URL inválida.")