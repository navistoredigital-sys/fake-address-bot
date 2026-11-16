# -*- coding: utf-8 -*-
"""
Telegram Bot untuk Generate Fake Address ChatGPT (Mode Vietnam 🇻🇳 & Mode Indonesia 🇮🇩)
Dibuat menggunakan python-telegram-bot v21+ (Hemat CPU & RAM)
"""

import os
import sys
import asyncio
import gc

# Pastikan konsol Windows dapat menampilkan output UTF-8 dengan aman
if sys.platform.startswith("win"):
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import logging
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters
)
from generator import VietnamAddressGenerator

# Konfigurasi logging hemat CPU (redam log polling berulang dari httpx/httpcore)
logging.basicConfig(
    format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
    level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Load file .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Inisialisasi generator alamat
generator = VietnamAddressGenerator()

def get_user_mode(context: ContextTypes.DEFAULT_TYPE) -> str:
    """Mengambil mode negara aktif user ('vn' atau 'id')"""
    if context.user_data is None:
        return "vn"
    return context.user_data.get("mode", "vn")

def set_user_mode(context: ContextTypes.DEFAULT_TYPE, mode: str):
    """Menyimpan mode negara aktif user"""
    if context.user_data is not None:
        context.user_data["mode"] = mode

def get_address_keyboard(city_query: str, country: str = "vn") -> InlineKeyboardMarkup:
    """Membuat tombol aksi di bawah hasil generate alamat sesuai negara"""
    if country == "id":
        keyboard = [
            [
                InlineKeyboardButton(f"🔄 Generate Lagi ({city_query.title()})", callback_data=f"regen:id:{city_query}"),
                InlineKeyboardButton("🎲 Kota Acak 🇮🇩", callback_data="city:id:random"),
            ],
            [
                InlineKeyboardButton("🏙️ Jakarta", callback_data="city:id:jakarta"),
                InlineKeyboardButton("🌆 Surabaya", callback_data="city:id:surabaya"),
                InlineKeyboardButton("🏖️ Bali (Denpasar)", callback_data="city:id:bali"),
            ],
            [
                InlineKeyboardButton("🏢 Bandung", callback_data="city:id:bandung"),
                InlineKeyboardButton("🌾 Semarang", callback_data="city:id:semarang"),
                InlineKeyboardButton("🏛️ Yogyakarta", callback_data="city:id:yogyakarta"),
            ],
            [
                InlineKeyboardButton("🇻🇳 Ganti ke Mode Vietnam", callback_data="set_mode:vn"),
            ]
        ]
    else:
        keyboard = [
            [
                InlineKeyboardButton(f"🔄 Generate Lagi ({city_query.title()})", callback_data=f"regen:vn:{city_query}"),
                InlineKeyboardButton("🎲 Kota Acak 🇻🇳", callback_data="city:vn:random"),
            ],
            [
                InlineKeyboardButton("🏙️ Hà Nội", callback_data="city:vn:ha noi"),
                InlineKeyboardButton("🌆 TP. HCM", callback_data="city:vn:ho chi minh"),
                InlineKeyboardButton("🏖️ Đà Nẵng", callback_data="city:vn:da nang"),
            ],
            [
                InlineKeyboardButton("⚓ Hải Phòng", callback_data="city:vn:hai phong"),
                InlineKeyboardButton("🌾 Cần Thơ", callback_data="city:vn:can tho"),
                InlineKeyboardButton("🏢 Bình Dương", callback_data="city:vn:binh duong"),
            ],
            [
                InlineKeyboardButton("🇮🇩 Ganti ke Mode Indonesia", callback_data="set_mode:id"),
            ]
        ]
    return InlineKeyboardMarkup(keyboard)

def get_main_menu_keyboard(mode: str = "vn") -> InlineKeyboardMarkup:
    """Membuat tombol menu utama dengan toggle mode negara"""
    if mode == "id":
        keyboard = [
            [
                InlineKeyboardButton("🇮🇩 Mode Indonesia [AKTIF]", callback_data="set_mode:id"),
                InlineKeyboardButton("🇻🇳 Mode Vietnam", callback_data="set_mode:vn"),
            ],
            [
                InlineKeyboardButton("🏙️ Jakarta", callback_data="city:id:jakarta"),
                InlineKeyboardButton("🌆 Surabaya", callback_data="city:id:surabaya"),
            ],
            [
                InlineKeyboardButton("🏖️ Bali (Denpasar/Kuta)", callback_data="city:id:bali"),
                InlineKeyboardButton("🏢 Bandung", callback_data="city:id:bandung"),
            ],
            [
                InlineKeyboardButton("🌾 Semarang", callback_data="city:id:semarang"),
                InlineKeyboardButton("🏛️ Yogyakarta", callback_data="city:id:yogyakarta"),
            ],
            [
                InlineKeyboardButton("🎲 Acak Kota Indonesia", callback_data="city:id:random"),
                InlineKeyboardButton("ℹ️ Bantuan", callback_data="menu:help"),
            ]
        ]
    else:
        keyboard = [
            [
                InlineKeyboardButton("🇻🇳 Mode Vietnam [AKTIF]", callback_data="set_mode:vn"),
                InlineKeyboardButton("🇮🇩 Mode Indonesia", callback_data="set_mode:id"),
            ],
            [
                InlineKeyboardButton("🏙️ Hà Nội (Hanoi)", callback_data="city:vn:ha noi"),
                InlineKeyboardButton("🌆 TP. Hồ Chí Minh", callback_data="city:vn:ho chi minh"),
            ],
            [
                InlineKeyboardButton("🏖️ Đà Nẵng", callback_data="city:vn:da nang"),
                InlineKeyboardButton("⚓ Hải Phòng", callback_data="city:vn:hai phong"),
            ],
            [
                InlineKeyboardButton("🌾 Cần Thơ", callback_data="city:vn:can tho"),
                InlineKeyboardButton("🏢 Bình Dương", callback_data="city:vn:binh duong"),
            ],
            [
                InlineKeyboardButton("🎲 Acak Kota Vietnam", callback_data="city:vn:random"),
                InlineKeyboardButton("ℹ️ Bantuan", callback_data="menu:help"),
            ]
        ]
    return InlineKeyboardMarkup(keyboard)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk perintah /start"""
    user_first_name = update.effective_user.first_name if update.effective_user else "Pengguna"
    mode = get_user_mode(context)
    mode_label = "Vietnam 🇻🇳" if mode == "vn" else "Indonesia 🇮🇩"
    welcome_text = (
        f"🤖 <b>FAKE ADDRESS FOR CHATGPT</b> 🤖\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"Halo, <b>{user_first_name}</b>! 👋\n\n"
        f"Bot ini mendukung <b>2 MODE NEGARA</b> sesuai format form billing ChatGPT:\n\n"
        f"🇻🇳 <b>1. Mode Vietnam:</b>\n"
        f"• 1️⃣ Dòng địa chỉ 1\n"
        f"• 2️⃣ Thành phố\n"
        f"• 3️⃣ Tỉnh\n"
        f"• 4️⃣ Mã bưu chính\n\n"
        f"🇮🇩 <b>2. Mode Indonesia:</b>\n"
        f"• 1️⃣ Baris alamat 1\n"
        f"• 2️⃣ Kota\n"
        f"• 3️⃣ Provinsi\n"
        f"• 4️⃣ Kode Pos\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📌 <b>Mode Aktif:</b> <b>{mode_label}</b>\n\n"
        f"👉 <b>Cara Pakai Sangat Mudah:</b>\n"
        f"Ketik langsung nama kota di chat (bot otomatis mendeteksi negara!):\n"
        f"• Vietnam: <code>ha noi</code>, <code>ho chi minh</code>, <code>da nang</code>\n"
        f"• Indonesia: <code>jakarta</code>, <code>surabaya</code>, <code>bandung</code>, <code>bali</code>\n\n"
        f"Atau pilih tombol kota di bawah ini:"
    )
    await update.message.reply_html(welcome_text, reply_markup=get_main_menu_keyboard(mode))

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk perintah /help"""
    mode = get_user_mode(context)
    help_text = (
        f"📖 <b>PANDUAN 2 MODE CHATGPT</b> 🇮🇩🇻🇳\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"<b>1. Mode Vietnam (🇻🇳):</b>\n"
        f"• Ketik: <code>ha noi</code>, <code>ho chi minh</code>, <code>da nang</code>, dll.\n"
        f"• Output: Dòng địa chỉ 1, Thành phố, Tỉnh, Mã bưu chính\n\n"
        f"<b>2. Mode Indonesia (🇮🇩):</b>\n"
        f"• Ketik: <code>jakarta</code>, <code>surabaya</code>, <code>bandung</code>, <code>bali</code>, dll.\n"
        f"• Output: Baris alamat 1, Kota, Provinsi, Kode Pos\n\n"
        f"<b>3. Perintah Cepat:</b>\n"
        f"• /indo atau /id - Beralih ke Mode Indonesia\n"
        f"• /vietnam atau /vn - Beralih ke Mode Vietnam\n"
        f"• /random - Generate alamat acak sesuai mode aktif\n"
        f"• /start - Menu utama\n\n"
        f"<i>💡 Tip: Tap / klik kotak kode abu-abu untuk menyalin otomatis ke clipboard!</i>"
    )
    await update.message.reply_html(help_text, reply_markup=get_main_menu_keyboard(mode))

async def set_mode_indo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Perintah beralih ke Mode Indonesia"""
    set_user_mode(context, "id")
    text = (
        f"🇮🇩 <b>MODE INDONESIA DIAKTIFKAN!</b>\n\n"
        f"Sekarang bot menghasilkan data alamat Indonesia untuk Form Billing ChatGPT:\n"
        f"• 1️⃣ Baris alamat 1\n"
        f"• 2️⃣ Kota\n"
        f"• 3️⃣ Provinsi\n"
        f"• 4️⃣ Kode Pos\n\n"
        f"Ketik nama kota (misal: <code>jakarta</code>, <code>surabaya</code>, <code>bandung</code>) atau pilih tombol di bawah:"
    )
    await update.message.reply_html(text, reply_markup=get_main_menu_keyboard("id"))

async def set_mode_vietnam_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Perintah beralih ke Mode Vietnam"""
    set_user_mode(context, "vn")
    text = (
        f"🇻🇳 <b>MODE VIETNAM DIAKTIFKAN!</b>\n\n"
        f"Sekarang bot menghasilkan data alamat Vietnam untuk Form Billing ChatGPT:\n"
        f"• 1️⃣ Dòng địa chỉ 1\n"
        f"• 2️⃣ Thành phố\n"
        f"• 3️⃣ Tỉnh\n"
        f"• 4️⃣ Mã bưu chính\n\n"
        f"Ketik nama kota (misal: <code>ha noi</code>, <code>ho chi minh</code>, <code>da nang</code>) atau pilih tombol di bawah:"
    )
    await update.message.reply_html(text, reply_markup=get_main_menu_keyboard("vn"))

async def random_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk perintah /random atau /acak"""
    mode = get_user_mode(context)
    address_data = generator.generate_address(query="random", country=mode)
    msg_html = generator.format_telegram_message(address_data)
    keyboard = get_address_keyboard(address_data["city_name"].lower(), country=address_data["country_code"])
    await update.message.reply_html(msg_html, reply_markup=keyboard)

async def text_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handler pesan teks pengguna.
    Otomatis mendeteksi apakah kota Vietnam atau Indonesia.
    """
    user_text = update.message.text.strip()
    if not user_text:
        return

    logger.info("Menerima query dari user @%s: '%s'", update.effective_user.username, user_text)

    current_mode = get_user_mode(context)

    # Deteksi otomatis negara berdasarkan input kota
    detected = generator.detect_country(user_text)
    if detected:
        current_mode = detected
        set_user_mode(context, detected)

    # Generate alamat
    address_data = generator.generate_address(query=user_text, country=current_mode)

    if address_data:
        country_code = address_data.get("country_code", current_mode)
        msg_html = generator.format_telegram_message(address_data)
        keyboard = get_address_keyboard(address_data["city_name"].lower(), country=country_code)
        await update.message.reply_html(msg_html, reply_markup=keyboard)
    else:
        # Jika nama kota tidak dikenali di kedua negara
        not_found_text = (
            f"⚠️ Maaf, kota <b>'{user_text}'</b> tidak ditemukan.\n\n"
            f"Contoh kota yang bisa Anda ketik:\n"
            f"• <b>Vietnam:</b> <code>ha noi</code>, <code>ho chi minh</code>, <code>da nang</code>, <code>hai phong</code>\n"
            f"• <b>Indonesia:</b> <code>jakarta</code>, <code>surabaya</code>, <code>bandung</code>, <code>bali</code>, <code>medan</code>\n\n"
            f"Atau pilih langsung dari menu di bawah ini:"
        )
        await update.message.reply_html(not_found_text, reply_markup=get_main_menu_keyboard(current_mode))

async def callback_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handler tombol interaktif (Inline Keyboard)
    """
    query = update.callback_query
    await query.answer()

    data = query.data
    logger.info("Callback query diterima: %s", data)

    # 1. Ganti Mode Negara
    if data == "set_mode:id":
        set_user_mode(context, "id")
        text = (
            f"🇮🇩 <b>MODE INDONESIA DIAKTIFKAN!</b>\n\n"
            f"Pilih kota di bawah ini atau ketik langsung di chat (misal: <code>jakarta</code>, <code>surabaya</code>, <code>bandung</code>):"
        )
        await query.edit_message_text(text=text, parse_mode=ParseMode.HTML, reply_markup=get_main_menu_keyboard("id"))

    elif data == "set_mode:vn":
        set_user_mode(context, "vn")
        text = (
            f"🇻🇳 <b>MODE VIETNAM DIAKTIFKAN!</b>\n\n"
            f"Pilih kota di bawah ini atau ketik langsung di chat (misal: <code>ha noi</code>, <code>ho chi minh</code>, <code>da nang</code>):"
        )
        await query.edit_message_text(text=text, parse_mode=ParseMode.HTML, reply_markup=get_main_menu_keyboard("vn"))

    # 2. Tombol Regenerate
    elif data.startswith("regen:"):
        # Format: regen:country:city_query
        parts = data.split(":")
        if len(parts) >= 3:
            country = parts[1]
            city_query = parts[2]
        else:
            country = get_user_mode(context)
            city_query = parts[1]

        address_data = generator.generate_address(query=city_query, country=country)
        if address_data:
            country_code = address_data.get("country_code", country)
            msg_html = generator.format_telegram_message(address_data)
            keyboard = get_address_keyboard(address_data["city_name"].lower(), country=country_code)
            await query.edit_message_text(text=msg_html, parse_mode=ParseMode.HTML, reply_markup=keyboard)

    # 3. Tombol Pilih Kota
    elif data.startswith("city:"):
        # Format: city:country:city_query
        parts = data.split(":")
        if len(parts) >= 3:
            country = parts[1]
            city_query = parts[2]
        else:
            country = get_user_mode(context)
            city_query = parts[1]

        set_user_mode(context, country)
        address_data = generator.generate_address(query=city_query, country=country)
        if address_data:
            country_code = address_data.get("country_code", country)
            msg_html = generator.format_telegram_message(address_data)
            keyboard = get_address_keyboard(address_data["city_name"].lower(), country=country_code)
            await query.message.reply_html(msg_html, reply_markup=keyboard)

    # 4. Bantuan
    elif data == "menu:help":
        mode = get_user_mode(context)
        help_text = (
            f"ℹ️ <b>BANTUAN MODE DUA NEGARA</b>\n\n"
            f"• <b>Vietnam:</b> Ketik <code>ha noi</code> atau <code>ho chi minh</code>\n"
            f"• <b>Indonesia:</b> Ketik <code>jakarta</code> atau <code>surabaya</code>\n\n"
            f"Klik tombol ganti mode untuk mengubah menu tombol:"
        )
        await query.message.reply_html(help_text, reply_markup=get_main_menu_keyboard(mode))

def main():
    """Fungsi utama untuk menjalankan Bot"""
    # Pastikan event loop tersedia (kompatibilitas Python 3.12 - 3.14+)
    try:
        asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    if not BOT_TOKEN or BOT_TOKEN == "YOUR_TELEGRAM_BOT_TOKEN_HERE":
        print("\n" + "=" * 60)
        print("❌ PERHATIAN: BOT_TOKEN BELUM DIISI!")
        print("=" * 60)
        print("1. Buka Telegram dan cari bot: @BotFather")
        print("2. Kirim perintah /newbot dan ikuti langkahnya untuk membuat bot baru.")
        print("3. Copy API Token yang diberikan oleh @BotFather.")
        print("4. Buka file '.env' di folder ini, lalu ganti:")
        print("   BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN_HERE")
        print("   menjadi token bot Telegram kamu.")
        print("5. Jalankan kembali script ini (atau jalankan run_bot.bat)!")
        print("=" * 60 + "\n")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("🚀 BOT TELEGRAM FAKE ADDRESS (INDONESIA & VIETNAM) SEDANG BERJALAN...")
    print("Tekan Ctrl + C di terminal untuk menghentikan bot.")
    print("=" * 60 + "\n")

    # Inisialisasi Application telegram dengan concurrent_updates & lightweight pool
    application = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .concurrent_updates(True)
        .connection_pool_size(4)
        .build()
    )

    # Registrasi command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("indo", set_mode_indo_command))
    application.add_handler(CommandHandler("id", set_mode_indo_command))
    application.add_handler(CommandHandler("vietnam", set_mode_vietnam_command))
    application.add_handler(CommandHandler("vn", set_mode_vietnam_command))
    application.add_handler(CommandHandler("random", random_command))
    application.add_handler(CommandHandler("acak", random_command))

    # Handler tombol interaktif
    application.add_handler(CallbackQueryHandler(callback_query_handler))

    # Handler pesan teks (auto detect Vietnam atau Indonesia)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_message_handler))

    # Bersihkan memori sebelum polling dimulai
    gc.collect()

    import threading
    is_main_thread = (threading.current_thread() is threading.main_thread())
    poll_kwargs = {
        "allowed_updates": ["message", "callback_query"],
        "drop_pending_updates": True,
        "timeout": 30,
        "poll_interval": 0.0,
    }
    if not is_main_thread:
        poll_kwargs["stop_signals"] = None

    # Jalankan bot polling hemat CPU & RAM
    application.run_polling(**poll_kwargs)

if __name__ == "__main__":
    main()
