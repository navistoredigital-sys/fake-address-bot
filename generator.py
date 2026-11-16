# -*- coding: utf-8 -*-
"""
Vietnam Fake Address & Identity Generator Engine
"""

import random
import re
import unicodedata
import gc
from functools import lru_cache
from datetime import datetime, timedelta
from data.vietnam_data import (
    VIETNAMESE_NAMES,
    TELCO_PREFIXES,
    PROVINCES_DATA,
    ALL_VIETNAM_PROVINCES,
    GENERIC_DISTRICTS,
    GENERIC_WARDS,
    GENERIC_STREETS
)
from data.indonesia_data import INDONESIA_CITIES_DATA

# Precompile regex sekali di memori untuk performa ultra-cepat & hemat CPU
RE_ALPHANUM = re.compile(r"[^a-z0-9\s]")
RE_SPACES = re.compile(r"\s+")

@lru_cache(maxsize=512)
def remove_vietnamese_accents(text: str) -> str:
    """
    Menghilangkan tanda aksen / diakritik bahasa Vietnam
    Menggunakan LRU Cache agar pencarian berulang berkecepatan mikrodetik (O(1)) tanpa beban CPU.
    """
    if not text:
        return ""
    text = text.lower().strip()
    
    # Penggantian khusus huruf đ / Đ
    text = text.replace("đ", "d").replace("Đ", "d")
    
    # Normalisasi NFD untuk memisahkan karakter dasar dan diakritik
    nfkd = unicodedata.normalize('NFD', text)
    cleaned = "".join([c for c in nfkd if not unicodedata.combining(c)])
    
    # Hapus karakter selain huruf dan angka serta spasi
    cleaned = RE_ALPHANUM.sub(" ", cleaned)
    cleaned = RE_SPACES.sub(" ", cleaned).strip()
    return cleaned

class VietnamAddressGenerator:
    def __init__(self):
        self.provinces_data = PROVINCES_DATA
        self.all_provinces = ALL_VIETNAM_PROVINCES
        self.indonesia_data = INDONESIA_CITIES_DATA
        self._build_lookup_index()
        # Bersihkan memori startup yang tidak lagi terpakai
        gc.collect()

    def _build_lookup_index(self):
        """Membuat index pencarian cepat untuk nama kota / alias Vietnam & Indonesia"""
        self.alias_map = {}
        
        # Index data detail Vietnam
        for key, data in self.provinces_data.items():
            norm_key = remove_vietnamese_accents(key)
            self.alias_map[norm_key] = key
            
            norm_name = remove_vietnamese_accents(data["name"])
            self.alias_map[norm_name] = key
            
            if "english_name" in data:
                norm_en = remove_vietnamese_accents(data["english_name"])
                self.alias_map[norm_en] = key
                
            for alias in data.get("aliases", []):
                norm_alias = remove_vietnamese_accents(alias)
                self.alias_map[norm_alias] = key

        # Index 63 provinsi nasional Vietnam
        for prov in self.all_provinces:
            norm_name = remove_vietnamese_accents(prov["name"])
            if norm_name not in self.alias_map:
                self.alias_map[norm_name] = prov["key"]

        # Index data kota Indonesia
        self.id_alias_map = {}
        for key, data in self.indonesia_data.items():
            norm_key = remove_vietnamese_accents(key)
            self.id_alias_map[norm_key] = key
            norm_name = remove_vietnamese_accents(data["name"])
            self.id_alias_map[norm_name] = key
            for alias in data.get("aliases", []):
                norm_alias = remove_vietnamese_accents(alias)
                self.id_alias_map[norm_alias] = key

    def find_indonesia_city(self, query: str):
        """Mencari data kota Indonesia berdasarkan input user"""
        if not query:
            return None
        norm_query = remove_vietnamese_accents(query)
        if norm_query in self.id_alias_map:
            key = self.id_alias_map[norm_query]
            return self.indonesia_data.get(key)
        compact = norm_query.replace(" ", "")
        for alias, key in self.id_alias_map.items():
            if alias.replace(" ", "") == compact:
                return self.indonesia_data.get(key)
        for alias, key in self.id_alias_map.items():
            if norm_query in alias or alias in norm_query:
                return self.indonesia_data.get(key)
        return None

    def detect_country(self, query: str) -> str:
        """
        Mendeteksi negara berdasarkan nama kota:
        Return 'id' untuk Indonesia, 'vn' untuk Vietnam, atau None jika acak/tidak ditemukan
        """
        if not query:
            return None
        norm = remove_vietnamese_accents(query)
        if norm in ["random", "acak", "semua"]:
            return None
        if self.find_indonesia_city(norm):
            return "id"
        if self.find_province(norm):
            return "vn"
        return None

    def find_province(self, query: str):
        """
        Mencari data provinsi berdasarkan input user (fleksibel: 'ha noi', 'hanoi', 'Hà Nội', dll.)
        """
        if not query:
            return None
            
        norm_query = remove_vietnamese_accents(query)
        
        # 1. Cek kecocokan langsung
        if norm_query in self.alias_map:
            key = self.alias_map[norm_query]
            return self._get_province_payload(key)
            
        # 2. Cek tanpa spasi (misal 'hanoi' -> 'ha noi')
        compact_query = norm_query.replace(" ", "")
        for alias, key in self.alias_map.items():
            if alias.replace(" ", "") == compact_query:
                return self._get_province_payload(key)
                
        # 3. Cek apakah query ada di dalam alias (substring match)
        for alias, key in self.alias_map.items():
            if norm_query in alias or alias in norm_query:
                # Prioritaskan jika kata kunci penting cocok
                return self._get_province_payload(key)
                
        return None

    def _get_province_payload(self, key: str):
        """Mengambil data lengkap atau fallback untuk provinsi tertentu"""
        if key in self.provinces_data:
            return self.provinces_data[key]
            
        # Jika ada di list 63 provinsi tapi belum punya data detail distrik
        for prov in self.all_provinces:
            if prov["key"] == key or remove_vietnamese_accents(prov["name"]) == remove_vietnamese_accents(key):
                return {
                    "name": prov["name"],
                    "english_name": prov["name"],
                    "postal_code": prov["code"],
                    "postal_range": (int(prov["code"]), int(prov["code"]) + 5000),
                    "aliases": [remove_vietnamese_accents(prov["name"])],
                    "districts": [
                        {
                            "district": f"Thành phố {prov['name']}",
                            "wards": GENERIC_WARDS,
                            "streets": GENERIC_STREETS
                        },
                        {
                            "district": "Huyện Trung Tâm",
                            "wards": GENERIC_WARDS,
                            "streets": GENERIC_STREETS
                        }
                    ]
                }
        return None

    def get_random_province(self):
        """Memilih provinsi acak dari database"""
        choice = random.choice(list(self.provinces_data.keys()))
        return self.provinces_data[choice]

    def generate_name(self, gender: str = None):
        """
        Membuat nama khas Vietnam yang realistis
        Format umum Vietnam: Họ + Tên Đệm + Tên (contoh: Nguyễn Văn Minh, Trần Thị Mai)
        """
        if not gender:
            gender = random.choice(["male", "female"])
            
        last_name = random.choice(VIETNAMESE_NAMES["last_names"])
        
        if gender == "male":
            middle_name = random.choice(VIETNAMESE_NAMES["male_middle_names"])
            first_name = random.choice(VIETNAMESE_NAMES["male_first_names"])
            gender_label = "Nam (Laki-laki)"
        else:
            middle_name = random.choice(VIETNAMESE_NAMES["female_middle_names"])
            first_name = random.choice(VIETNAMESE_NAMES["female_first_names"])
            gender_label = "Nữ (Perempuan)"
            
        # 20% kemungkinan nama 4 kata (misal: Nguyễn Hoàng Minh Anh)
        if random.random() < 0.2:
            second_middle = random.choice(
                VIETNAMESE_NAMES["male_middle_names"] if gender == "male" else VIETNAMESE_NAMES["female_middle_names"]
            )
            full_name = f"{last_name} {second_middle} {middle_name} {first_name}"
        else:
            full_name = f"{last_name} {middle_name} {first_name}"
            
        return {
            "full_name": full_name,
            "gender": gender_label,
            "gender_code": gender,
            "last_name": last_name,
            "first_name": first_name
        }

    def generate_phone(self):
        """Membuat nomor telepon Vietnam yang valid (format Viettel, Vinaphone, Mobifone)"""
        telco = random.choice(list(TELCO_PREFIXES.keys()))
        prefix = random.choice(TELCO_PREFIXES[telco])
        suffix = "".join([str(random.randint(0, 9)) for _ in range(7)])
        
        # Format lokal: 098xxxxxxx
        local_phone = f"{prefix}{suffix}"
        
        # Format internasional: +84 98xxxxxxx
        int_phone = f"+84{prefix[1:]}{suffix}"
        
        return {
            "telco": telco,
            "local_format": local_phone,
            "international_format": int_phone
        }

    def generate_birthday(self, min_age: int = 18, max_age: int = 55):
        """Membuat tanggal lahir dan umur realistis"""
        days_old = random.randint(min_age * 365, max_age * 365)
        # Assuming current year around 2026
        birth_date = datetime.now() - timedelta(days=days_old)
        age = (datetime.now() - birth_date).days // 365
        return {
            "birth_date": birth_date.strftime("%d/%m/%Y"),
            "age": age
        }

    def generate_email(self, full_name: str, birth_year: str):
        """Membuat alamat email realistis berdasarkan nama"""
        cleaned_name = remove_vietnamese_accents(full_name).replace(" ", "")
        domains = ["gmail.com", "yahoo.com", "outlook.com", "icloud.com"]
        domain = random.choice(domains)
        tag = random.choice([birth_year[-2:], birth_year, str(random.randint(10, 999))])
        email = f"{cleaned_name.lower()}{tag}@{domain}"
        return email

    def generate_vietnam_address(self, query: str = None):
        """
        Generate alamat palsu Vietnam yang panjang, lengkap, dan berstruktur resmi
        dengan Kode Pos (Zip Code) yang 100% akurat sesuai distrik/quận.
        """
        if query and remove_vietnamese_accents(query) not in ["random", "acak", "semua"]:
            prov_data = self.find_province(query)
            if not prov_data:
                return None
        else:
            prov_data = self.get_random_province()

        # Pilih distrik (quận/huyện)
        districts = prov_data.get("districts", [])
        if districts:
            district_obj = random.choice(districts)
            district_name = district_obj.get("district", "Quận 1")
            wards = district_obj.get("wards", GENERIC_WARDS)
            streets = district_obj.get("streets", GENERIC_STREETS)
            # Kode pos akurat sesuai distrik
            postal_code = district_obj.get("postal_code", prov_data.get("postal_code", "100000"))
        else:
            district_name = "Quận Trung Tâm"
            wards = GENERIC_WARDS
            streets = GENERIC_STREETS
            postal_code = prov_data.get("postal_code", "100000")

        ward_name = random.choice(wards)
        street_name = random.choice(streets)
        house_num = random.randint(15, 380)
        lane = random.randint(12, 180)
        sublane = random.randint(2, 45)
        floor = random.randint(3, 35)
        room = f"{floor:02d}{random.randint(1, 12):02d}"

        # Pola alamat Vietnam yang panjang, berbobot, dan lengkap:
        city_lower = remove_vietnamese_accents(prov_data["name"])
        if "ha noi" in city_lower:
            address_styles = [
                f"Tòa nhà Discovery Complex, Tầng {floor}, Phòng {room}, Số {house_num} {street_name}, {ward_name}",
                f"Căn hộ {room} Tòa R4 Khu đô thị Royal City, Số {house_num} {street_name}, {ward_name}",
                f"Tòa nhà Keangnam Landmark 72, Tầng {floor}, Phòng {room}, {street_name}, {ward_name}",
                f"Khu đô thị Times City, Tòa Park {random.randint(1, 12)}, Căn hộ {room}, Số {house_num} {street_name}, {ward_name}",
                f"Chung cư Golden Palace, Tháp A, Tầng {floor}, Số {house_num} {street_name}, {ward_name}",
                f"Tòa nhà Lotte Center Hanoi, Tầng {floor}, Số 54 {street_name}, {ward_name}",
                f"Khu đô thị Ngoại Giao Đoàn, Tòa N03-T2, Căn {room}, {street_name}, {ward_name}",
                f"Liền kề LK-{random.randint(2, 28)} Khu Đô Thị Trung Hòa - Nhân Chính, Số {house_num} {street_name}, {ward_name}",
                f"Số {house_num} Ngõ {lane}/{sublane} {street_name}, {ward_name}",
                f"Số {house_num} Ngách {lane}/{sublane}/{random.randint(2, 18)} {street_name}, {ward_name}"
            ]
        elif "ho chi minh" in city_lower:
            address_styles = [
                f"Tòa nhà Landmark 81, Tầng {floor}, Căn hộ L81-{room}, Số {house_num} {street_name}, {ward_name}",
                f"Tòa nhà Bitexco Financial Tower, Tầng {floor}, Phòng {room}, Số {house_num} {street_name}, {ward_name}",
                f"Chung cư Vinhomes Central Park, Tòa Landmark {random.randint(1, 8)}, Căn {room}, Số {house_num} {street_name}, {ward_name}",
                f"Chung cư Masteri Thảo Điền, Tháp T{random.randint(1, 5)}, Tầng {floor}, Căn {room}, Số {house_num} {street_name}, {ward_name}",
                f"Tòa nhà Saigon Centre, Tháp 2, Tầng {floor}, Số {house_num} {street_name}, {ward_name}",
                f"Khu phức hợp Hado Centrosa Garden, Tòa Iris {random.randint(1, 4)}, Tầng {floor}, Căn {room}, {street_name}, {ward_name}",
                f"Khu dân cư Him Lam, Lô C-{random.randint(5, 30)}, Số {house_num} {street_name}, {ward_name}",
                f"Số {house_num}/{lane}/{sublane} Hẻm {lane} {street_name}, {ward_name}",
                f"Số {house_num}/{lane} {street_name}, {ward_name}"
            ]
        elif "da nang" in city_lower:
            address_styles = [
                f"Tòa nhà Indochina Riverside Towers, Tầng {floor}, Phòng {room}, Số {house_num} {street_name}, {ward_name}",
                f"Chung cư HAGL Lake View, Tháp B, Tầng {floor}, Căn {room}, Số {house_num} {street_name}, {ward_name}",
                f"Tòa nhà Azura Tower, Tầng {floor}, Căn hộ {room}, Số {house_num} {street_name}, {ward_name}",
                f"Khu biệt thự Euro Village, Lô B2-{random.randint(1, 20)}, Số {house_num} {street_name}, {ward_name}",
                f"Số {house_num} Ngõ {lane}/{sublane} {street_name}, {ward_name}",
                f"Số {house_num}/{lane} {street_name}, {ward_name}"
            ]
        else:
            address_styles = [
                f"Tòa nhà Trung tâm Thương mại Plaza, Tầng {floor}, Phòng {room}, Số {house_num} {street_name}, {ward_name}",
                f"Khu Đô Thị Mới, Lô B-{random.randint(1, 30)}, Số {house_num} {street_name}, {ward_name}",
                f"Chung cư Cao cấp Central, Tòa A, Căn hộ {room}, Số {house_num} {street_name}, {ward_name}",
                f"Số {house_num} Ngõ {lane}/{sublane} {street_name}, {ward_name}",
                f"Số {house_num}/{lane} {street_name}, {ward_name}"
            ]

        # 1. Dòng địa chỉ 1: Format dài, lengkap, dan meyakinkan
        dong_dia_chi_1 = random.choice(address_styles)
        thanh_pho = district_name
        tinh = prov_data["name"]
        ma_buu_chinh = postal_code

        full_single_line = f"{dong_dia_chi_1}, {thanh_pho}, {tinh} {ma_buu_chinh}, Vietnam"

        return {
            "country_code": "vn",
            "country_name": "Vietnam",
            "flag": "🇻🇳",
            "city_name": prov_data["name"],
            "city_english": prov_data.get("english_name", prov_data["name"]),
            "district": district_name,
            "ward": ward_name,
            "dong_dia_chi_1": dong_dia_chi_1,
            "thanh_pho": thanh_pho,
            "tinh": tinh,
            "ma_buu_chinh": ma_buu_chinh,
            "postal_code": postal_code,
            "country": "Vietnam",
            "full_address": full_single_line
        }

    def generate_indonesia_address(self, query: str = None):
        """
        Membuat fake address Indonesia yang panjang, lengkap, dan berstruktur resmi
        dengan Kode Pos (Zip Code) yang 100% akurat sesuai kelurahan/kecamatan Pos Indonesia.
        """
        city_data = None
        if query and remove_vietnamese_accents(query) not in ["random", "acak", "semua"]:
            city_data = self.find_indonesia_city(query)
            if not city_data:
                return None
        else:
            choice_key = random.choice(list(self.indonesia_data.keys()))
            city_data = self.indonesia_data[choice_key]

        districts = city_data.get("districts", [])
        district_obj = random.choice(districts) if districts else {}
        city_name = district_obj.get("city", city_data.get("city_label", "Jakarta"))
        subdistricts = district_obj.get("subdistricts", [])
        streets = district_obj.get("streets", ["Jl. Jenderal Sudirman", "Jl. Gatot Subroto"])

        # Pilih kelurahan dan ambil KODE POS RESMI yang 100% cocok
        if subdistricts:
            subdistrict_item = random.choice(subdistricts)
            if isinstance(subdistrict_item, dict):
                subdistrict = subdistrict_item["name"]
                postal_code = subdistrict_item["zip"]
            else:
                subdistrict = str(subdistrict_item)
                postal_code = city_data.get("postal_code", "12190")
        else:
            subdistrict = "Menteng"
            postal_code = city_data.get("postal_code", "12190")

        street = random.choice(streets)
        house_num = random.randint(5, 240)
        floor = random.randint(3, 42)
        room = f"{floor:02d}{random.randint(1, 15):02d}"
        rt = random.randint(1, 14)
        rw = random.randint(1, 10)
        block = f"{random.choice(['A', 'B', 'C', 'D', 'E'])}{random.randint(1, 9)}"

        city_key = remove_vietnamese_accents(city_data["name"])
        if "jakarta" in city_key:
            address_styles = [
                f"Gedung Menara BCA Lt. {floor} Suite {room}, Jl. M.H. Thamrin No. 1, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}",
                f"Apartemen Sudirman Park Tower B Lt. {floor} Unit B-{room}, Jl. KH. Mas Mansyur Kav. 35, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}",
                f"Gedung Pacific Century Place Lt. {floor}, Kawasan SCBD Lot 10, Jl. Jenderal Sudirman Kav. 52-53, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}",
                f"Menara Prima Lt. {floor} Unit {room}, Kawasan Mega Kuningan Barat Kav. E4.3, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}",
                f"Perumahan Citra Garden City 2 Blok {block} No. {house_num}, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}",
                f"Apartemen Mediterania Garden Residences 2 Tower Jasmine Lt. {floor} Unit J-{room}, {street}, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}",
                f"Komp. Perumahan Puri Indah Blok {block} No. {house_num}, {street}, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}",
                f"Gedung Wisma 46 Kota BNI Lt. {floor}, Jl. Jenderal Sudirman Kav. 1, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}",
                f"{street} No. {house_num}{random.choice(['A', 'B', 'C'])}, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}"
            ]
        elif "surabaya" in city_key:
            address_styles = [
                f"Pakuwon Tower Tunjungan Plaza 6 Lt. {floor} Unit {room}, Jl. Embong Malang No. 21-31, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}",
                f"Kompleks Ruko Darmo Square Blok {block} No. {house_num}, Jl. Raya Darmo No. 54, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}",
                f"Apartemen Grand Sungkono Lagoon Tower Venetian Lt. {floor} Unit V-{room}, {street} No. 12, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}",
                f"Perumahan Graha Family Blok {block} No. {house_num}, {street}, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}",
                f"{street} No. {house_num}, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}"
            ]
        elif "bandung" in city_key:
            address_styles = [
                f"Apartemen The Jarrdin Cihampelas Tower B Lt. {floor} Unit {room}, {street} No. 10, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}",
                f"Komp. Dago Asri Residence Blok {block} No. {house_num}, {street}, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}",
                f"Ruko Dago Plaza Blok {block} No. {house_num}, {street}, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}",
                f"{street} No. {house_num}, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}"
            ]
        elif "bali" in city_key or "denpasar" in city_key:
            address_styles = [
                f"Kompleks Villa Seminyak Estate Blok {block} No. {house_num}, {street}, Kel. {subdistrict}",
                f"Komp. Pertokoan Sunset Star Blok {block} No. {house_num}, {street}, Kel. {subdistrict}",
                f"Komp. Perumahan Sanur Indah Blok {block} No. {house_num}, {street}, Kel. {subdistrict}",
                f"{street} No. {house_num}, Kel. {subdistrict}"
            ]
        else:
            address_styles = [
                f"Kompleks Perumahan Graha Indah Blok {block} No. {house_num}, {street}, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}",
                f"Gedung Plaza Central Lt. {floor} Suite {room}, {street} No. {house_num}, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}",
                f"Komp. Ruko Niaga Blok {block} No. {house_num}, {street}, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}",
                f"{street} No. {house_num}, RT {rt:02d}/RW {rw:02d}, Kel. {subdistrict}"
            ]

        # 1. Baris alamat 1: Format panjang, lengkap, dan resmi
        address_line_1 = random.choice(address_styles)
        kota = city_name
        provinsi = city_data["province"]

        full_single_line = f"{address_line_1}, {kota}, {provinsi} {postal_code}, Indonesia"

        return {
            "country_code": "id",
            "country_name": "Indonesia",
            "flag": "🇮🇩",
            "city_name": city_data["name"],
            "dong_dia_chi_1": address_line_1,
            "thanh_pho": kota,
            "tinh": provinsi,
            "ma_buu_chinh": postal_code,
            "full_address": full_single_line
        }

    def generate_address(self, query: str = None, country: str = "vn"):
        """
        Generate alamat palsu (otomatis mendeteksi negara atau menggunakan mode country)
        """
        # Cek apakah query secara spesifik mengarah ke negara tertentu
        if query and remove_vietnamese_accents(query) not in ["random", "acak", "semua"]:
            detected = self.detect_country(query)
            if detected:
                country = detected

        if country == "id":
            return self.generate_indonesia_address(query)
        else:
            return self.generate_vietnam_address(query)

    def format_telegram_message(self, data: dict) -> str:
        """
        Format data persis sesuai kolom Formulir Billing ChatGPT (OpenAI):
        Mendukung Mode Indonesia (🇮🇩) dan Mode Vietnam (🇻🇳)
        """
        if data.get("country_code") == "id":
            html = (
                f"🤖 <b>FAKE ADDRESS FOR CHATGPT (INDONESIA)</b> 🇮🇩\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                f"📍 <i>Format Form Billing / Subscription ChatGPT</i>\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                f"1️⃣ <b>Baris alamat 1:</b>\n"
                f"<code>{data['dong_dia_chi_1']}</code>\n\n"
                f"2️⃣ <b>Kota:</b>\n"
                f"<code>{data['thanh_pho']}</code>\n\n"
                f"3️⃣ <b>Provinsi:</b>\n"
                f"<code>{data['tinh']}</code>\n\n"
                f"4️⃣ <b>Kode Pos:</b>\n"
                f"<code>{data['ma_buu_chinh']}</code>\n\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                f"📋 <b>Alamat Lengkap 1 Baris:</b>\n"
                f"<code>{data['full_address']}</code>\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                f"💡 <i>Tip: Tap kotak abu-abu di atas satu per satu untuk copy langsung ke form ChatGPT!</i>"
            )
        else:
            html = (
                f"🤖 <b>FAKE ADDRESS FOR CHATGPT (VIETNAM)</b> 🇻🇳\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                f"📍 <i>Format Form Billing / Subscription ChatGPT</i>\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                f"1️⃣ <b>Dòng địa chỉ 1:</b>\n"
                f"<code>{data['dong_dia_chi_1']}</code>\n\n"
                f"2️⃣ <b>Thành phố:</b>\n"
                f"<code>{data['thanh_pho']}</code>\n\n"
                f"3️⃣ <b>Tỉnh:</b>\n"
                f"<code>{data['tinh']}</code>\n\n"
                f"4️⃣ <b>Mã bưu chính:</b>\n"
                f"<code>{data['ma_buu_chinh']}</code>\n\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                f"📋 <b>Alamat Lengkap 1 Baris:</b>\n"
                f"<code>{data['full_address']}</code>\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                f"💡 <i>Tip: Tap kotak abu-abu di atas satu per satu untuk copy langsung ke form ChatGPT!</i>"
            )
        return html
