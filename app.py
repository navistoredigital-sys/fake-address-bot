# -*- coding: utf-8 -*-
"""
Hugging Face Spaces Entrypoint (Gradio SDK + ZeroGPU & CPU Compatible)
Menjalankan Web UI Gradio sekaligus menjalankan Telegram Bot di latar belakang.
"""

import os
import sys
import threading
from dotenv import load_dotenv

# Konfigurasi output konsol
if sys.platform.startswith("win"):
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()

# Deteksi ZeroGPU Hugging Face secara dinamis
try:
    import spaces
    def gpu_decorator(fn):
        return spaces.GPU(fn)
    print("⚡ ZeroGPU mode detected and active.")
except Exception:
    def gpu_decorator(fn):
        return fn
    print("ℹ️ Standard CPU mode active.")

# Jalankan bot telegram di background worker thread
def run_telegram_bot():
    if not BOT_TOKEN or BOT_TOKEN == "YOUR_TELEGRAM_BOT_TOKEN_HERE":
        print("\n⚠️ PERINGATAN: BOT_TOKEN belum diset di Secrets!")
        return
    try:
        print("\n🚀 Memulai Telegram Bot worker thread...")
        from bot import main as start_bot
        start_bot()
    except Exception as e:
        print(f"❌ Error Telegram Bot: {e}")

bot_thread = threading.Thread(target=run_telegram_bot, daemon=True)
bot_thread.start()

# Jalankan Web UI
try:
    import gradio as gr
    from generator import VietnamAddressGenerator

    generator = VietnamAddressGenerator()

    # Fungsi yang dipanggil oleh tombol UI (wajib didekorasi GPU jika di ZeroGPU)
    @gpu_decorator
    def generate_vietnam_ui():
        addr = generator.generate_vietnam_address()
        return (
            addr["street_address"],
            addr["city"],
            addr["province"],
            addr["postal_code"],
            f"📍 {addr['full_address']}"
        )

    @gpu_decorator
    def generate_indonesia_ui():
        addr = generator.generate_indonesia_address()
        return (
            addr["street_address"],
            addr["city"],
            addr["province"],
            addr["postal_code"],
            f"📍 {addr['full_address']}"
        )

    with gr.Blocks(title="Fake Address Telegram Bot") as demo:
        gr.Markdown(
            """
            # 🤖 Telegram Fake Address Bot
            ### Status: 🟢 **ONLINE & BERJALAN 24/7**
            
            Bot Telegram Anda (**@fakevietnam_bot**) aktif melayani permintaan generate alamat Vietnam 🇻🇳 & Indonesia 🇮🇩.
            
            👉 **[Buka Bot @fakevietnam_bot di Telegram](https://t.me/fakevietnam_bot)**
            ---
            """
        )

        with gr.Tab("🇻🇳 Mode Vietnam"):
            btn_vn = gr.Button("🎲 Generate Alamat Vietnam Baru", variant="primary")
            with gr.Row():
                vn_line1 = gr.Textbox(label="Dòng địa chỉ 1 (Alamat Baris 1)")
                vn_city = gr.Textbox(label="Thành phố (Distrik)")
            with gr.Row():
                vn_prov = gr.Textbox(label="Tỉnh (Provinsi)")
                vn_zip = gr.Textbox(label="Mã bưu chính (Kode Pos)")
            vn_full = gr.Textbox(label="Format Lengkap", lines=2)
            btn_vn.click(
                fn=generate_vietnam_ui,
                outputs=[vn_line1, vn_city, vn_prov, vn_zip, vn_full]
            )

        with gr.Tab("🇮🇩 Mode Indonesia"):
            btn_id = gr.Button("🎲 Generate Alamat Indonesia Baru", variant="primary")
            with gr.Row():
                id_line1 = gr.Textbox(label="Alamat Baris 1")
                id_city = gr.Textbox(label="Kota / Kabupaten")
            with gr.Row():
                id_prov = gr.Textbox(label="Provinsi")
                id_zip = gr.Textbox(label="Kode Pos")
            id_full = gr.Textbox(label="Format Lengkap", lines=2)
            btn_id.click(
                fn=generate_indonesia_ui,
                outputs=[id_line1, id_city, id_prov, id_zip, id_full]
            )

    if __name__ == "__main__":
        port = int(os.getenv("PORT", "7860"))
        demo.launch(server_name="0.0.0.0", server_port=port, share=False)

except Exception as e:
    # Fallback jika gradio belum terpasang di lokal
    from http.server import HTTPServer, BaseHTTPRequestHandler

    class FallbackHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"<h1>Fake Address Bot is Running</h1>")

        def log_message(self, format, *args):
            return

    port = int(os.getenv("PORT", "7860"))
    server = HTTPServer(("0.0.0.0", port), FallbackHandler)
    server.serve_forever()
