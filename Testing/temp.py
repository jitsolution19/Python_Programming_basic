import shutil

if shutil.which("ffmpeg"):
    print("✅ FFmpeg is installed and in PATH")
else:
    print("❌ FFmpeg not found. Please install and add to PATH")
