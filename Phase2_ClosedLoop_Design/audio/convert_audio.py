from pathlib import Path
import numpy as np
import soundfile as sf

BASE = Path(__file__).parent
input_file  = BASE / "input.wav"
output_file = BASE / "audio.wav"

TARGET_SR   = 44100
TARGET_PEAK = 0.30

if not input_file.exists():
    print(f"فایل پیدا نشد: {input_file}")
    print("فایل‌های wav موجود در این پوشه:")
    for f in BASE.glob("*.wav"):
        print("   ", f.name)
    raise SystemExit(1)

data, sr = sf.read(input_file, always_2d=True)

# تبدیل به تک‌کاناله
data = data.mean(axis=1)

# تبدیل نرخ نمونه‌برداری به 44100
if sr != TARGET_SR:
    n_out = int(round(len(data) * TARGET_SR / sr))
    t_in  = np.linspace(0.0, 1.0, len(data), endpoint=False)
    t_out = np.linspace(0.0, 1.0, n_out,    endpoint=False)
    data = np.interp(t_out, t_in, data)
    sr = TARGET_SR

# نرمال‌سازی دامنه
peak = np.max(np.abs(data))
if peak == 0:
    raise SystemExit("فایل ورودی سکوت است")
data = data / peak * TARGET_PEAK

sf.write(output_file, data, sr, subtype="PCM_16")

print(f"channels    : 1")
print(f"sample rate : {sr} Hz")
print(f"duration    : {len(data)/sr:.2f} s")
print(f"peak        : {np.max(np.abs(data)):.3f} V")
print(f"saved to    : {output_file}")