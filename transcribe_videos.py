import os
import glob
import subprocess
import speech_recognition as sr

base_dir = r"C:\Users\RAFA\Documents\ECOMM\CREACION DE CONTENIDO ECOMM\WART REMOVER\videos_drive"
videos = glob.glob(os.path.join(base_dir, "**", "*.mp4"), recursive=True)
print(f"Total videos encontrados: {len(videos)}")

r = sr.Recognizer()
results = []

for v in sorted(videos):
    name = os.path.basename(v)
    rel_path = os.path.relpath(v, base_dir)
    print(f"Procesando: {name}...")
    
    # ffprobe duration
    dur_cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', v]
    try:
        dur = float(subprocess.run(dur_cmd, capture_output=True, text=True).stdout.strip())
        dur_str = f"{int(dur // 60)}:{int(dur % 60):02d}"
    except Exception:
        dur_str = "N/A"
    
    wav_temp = os.path.join(base_dir, f"temp_{os.getpid()}.wav")
    cmd = ['ffmpeg', '-y', '-i', v, '-vn', '-acodec', 'pcm_s16le', '-ar', '16000', '-ac', '1', wav_temp]
    subprocess.run(cmd, capture_output=True)
    
    text = ""
    try:
        with sr.AudioFile(wav_temp) as source:
            audio = r.record(source)
            text = r.recognize_google(audio, language='es-ES')
    except sr.UnknownValueError:
        text = "[Video sin locución / Solo música de fondo o instrumental]"
    except Exception as e:
        text = f"[No detectado: {e}]"
    
    if os.path.exists(wav_temp):
        os.remove(wav_temp)
        
    print(f"-> {dur_str} | {text[:60]}...")
    results.append({
        'file': name,
        'path': rel_path,
        'duration': dur_str,
        'transcription': text
    })

out_md = os.path.join(base_dir, "TRANSCRIPCIONES_VIDEOS_DRIVE.md")
with open(out_md, "w", encoding="utf-8") as f:
    f.write("# TRANSCRIPCIONES DE VIDEOS OFICIALES DE DRIVE (WART REMOVER)\n\n")
    for item in results:
        f.write(f"### 🎬 {item['file']} ({item['duration']})\n")
        f.write(f"* **Archivo:** `{item['path']}`\n")
        f.write(f"* **Transcripción:**\n> \"{item['transcription']}\"\n\n---\n\n")

print(f"\n¡Listo! Transcripciones guardadas en: {out_md}")
