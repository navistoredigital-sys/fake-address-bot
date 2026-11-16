# -*- coding: utf-8 -*-
"""
Dataset Alamat Indonesia untuk Form Billing ChatGPT
Berisi data kota, jalan, kelurahan beserta kode pos resmi Pos Indonesia yang 100% akurat.
"""

INDONESIA_CITIES_DATA = {
    "jakarta": {
        "name": "Jakarta",
        "city_label": "Jakarta Selatan",
        "province": "DKI Jakarta",
        "postal_code": "12190",
        "aliases": ["jakarta", "jkt", "dki jakarta", "jakarta pusat", "jakarta selatan", "jakarta barat", "jakarta timur", "jakarta utara"],
        "districts": [
            {
                "city": "Jakarta Selatan",
                "subdistricts": [
                    {"name": "Karet Semanggi", "zip": "12930"},
                    {"name": "Senayan", "zip": "12190"},
                    {"name": "Melawai", "zip": "12160"},
                    {"name": "Kuningan Timur", "zip": "12950"},
                    {"name": "Tebet Barat", "zip": "12810"},
                    {"name": "Pancoran", "zip": "12780"},
                    {"name": "Cilandak Barat", "zip": "12430"},
                    {"name": "Pondok Pinang", "zip": "12310"}
                ],
                "streets": [
                    "Jl. Jenderal Sudirman", "Jl. Gatot Subroto", "Jl. H.R. Rasuna Said",
                    "Jl. Senopati", "Jl. Kemang Raya", "Jl. Fatmawati Raya", "Jl. TB Simatupang",
                    "Jl. Prof. Dr. Satrio", "Jl. Pangeran Antasari"
                ]
            },
            {
                "city": "Jakarta Pusat",
                "subdistricts": [
                    {"name": "Menteng", "zip": "10310"},
                    {"name": "Kebon Sirih", "zip": "10340"},
                    {"name": "Gondangdia", "zip": "10350"},
                    {"name": "Gambir", "zip": "10110"},
                    {"name": "Petojo Selatan", "zip": "10160"},
                    {"name": "Gelora", "zip": "10270"},
                    {"name": "Karet Tengsin", "zip": "10220"},
                    {"name": "Cempaka Putih Timur", "zip": "10510"}
                ],
                "streets": [
                    "Jl. M.H. Thamrin", "Jl. Medan Merdeka Barat", "Jl. Kebon Sirih",
                    "Jl. H. Agus Salim (Sabang)", "Jl. Cikini Raya", "Jl. Kramat Raya",
                    "Jl. KH. Mas Mansyur", "Jl. Budi Kemuliaan"
                ]
            },
            {
                "city": "Jakarta Barat",
                "subdistricts": [
                    {"name": "Tomang", "zip": "11440"},
                    {"name": "Tanjung Duren Selatan", "zip": "11470"},
                    {"name": "Grogol", "zip": "11450"},
                    {"name": "Kebon Jeruk", "zip": "11530"},
                    {"name": "Meruya Utara", "zip": "11620"},
                    {"name": "Kembangan Selatan", "zip": "11610"}
                ],
                "streets": [
                    "Jl. Letjen S. Parman", "Jl. Panjang", "Jl. Tanjung Duren Raya",
                    "Jl. Puri Indah Raya", "Jl. Daan Mogot", "Jl. Pesanggrahan"
                ]
            }
        ]
    },
    "surabaya": {
        "name": "Surabaya",
        "city_label": "Surabaya",
        "province": "Jawa Timur",
        "postal_code": "60111",
        "aliases": ["surabaya", "sby", "kota surabaya", "jawa timur"],
        "districts": [
            {
                "city": "Surabaya",
                "subdistricts": [
                    {"name": "Tegalsari", "zip": "60262"},
                    {"name": "Embong Kaliasin", "zip": "60271"},
                    {"name": "Keputran", "zip": "60265"},
                    {"name": "Wonokromo", "zip": "60243"},
                    {"name": "Darmo", "zip": "60241"},
                    {"name": "Gubeng", "zip": "60281"},
                    {"name": "Genteng", "zip": "60275"},
                    {"name": "Kedungdoro", "zip": "60261"}
                ],
                "streets": [
                    "Jl. Tunjungan", "Jl. Pemuda", "Jl. Basuki Rahmat", "Jl. Raya Darmo",
                    "Jl. Mayjen Sungkono", "Jl. Kertajaya", "Jl. H.R. Muhammad", "Jl. Embong Malang"
                ]
            }
        ]
    },
    "bandung": {
        "name": "Bandung",
        "city_label": "Bandung",
        "province": "Jawa Barat",
        "postal_code": "40115",
        "aliases": ["bandung", "bdg", "kota bandung"],
        "districts": [
            {
                "city": "Bandung",
                "subdistricts": [
                    {"name": "Braga", "zip": "40111"},
                    {"name": "Merdeka", "zip": "40113"},
                    {"name": "Babakan Ciamis", "zip": "40117"},
                    {"name": "Tamansari", "zip": "40116"},
                    {"name": "Dago", "zip": "40135"},
                    {"name": "Citarum", "zip": "40115"},
                    {"name": "Malabar", "zip": "40262"}
                ],
                "streets": [
                    "Jl. Asia Afrika", "Jl. Braga", "Jl. Ir. H. Juanda (Dago)", "Jl. R.E. Martadinata",
                    "Jl. Dr. Setiabudi", "Jl. Cihampelas", "Jl. Buah Batu", "Jl. LLRE Martadinata"
                ]
            }
        ]
    },
    "medan": {
        "name": "Medan",
        "city_label": "Medan",
        "province": "Sumatera Utara",
        "postal_code": "20111",
        "aliases": ["medan", "kota medan", "sumut"],
        "districts": [
            {
                "city": "Medan",
                "subdistricts": [
                    {"name": "Kesawan", "zip": "20111"},
                    {"name": "Petisah Tengah", "zip": "20112"},
                    {"name": "Madras Hulu", "zip": "20152"},
                    {"name": "Babura", "zip": "20153"},
                    {"name": "Kampung Baru", "zip": "20158"}
                ],
                "streets": [
                    "Jl. Balai Kota", "Jl. Zainul Arifin", "Jl. Putri Hijau", "Jl. S. Parman",
                    "Jl. Gatot Subroto", "Jl. Pangeran Diponegoro", "Jl. Imam Bonjol"
                ]
            }
        ]
    },
    "semarang": {
        "name": "Semarang",
        "city_label": "Semarang",
        "province": "Jawa Tengah",
        "postal_code": "50134",
        "aliases": ["semarang", "smg", "kota semarang"],
        "districts": [
            {
                "city": "Semarang",
                "subdistricts": [
                    {"name": "Sekayu", "zip": "50132"},
                    {"name": "Mugassari", "zip": "50249"},
                    {"name": "Pleburan", "zip": "50241"},
                    {"name": "Karangkidul", "zip": "50136"},
                    {"name": "Pekunden", "zip": "50241"}
                ],
                "streets": [
                    "Jl. Pandanaran", "Jl. Pemuda", "Jl. Gajah Mada", "Jl. Pahlawan",
                    "Jl. Ahmad Yani", "Jl. Erlangga Raya"
                ]
            }
        ]
    },
    "yogyakarta": {
        "name": "Yogyakarta",
        "city_label": "Yogyakarta",
        "province": "DI Yogyakarta",
        "postal_code": "55271",
        "aliases": ["yogyakarta", "jogja", "jogjakarta", "diy", "sleman"],
        "districts": [
            {
                "city": "Yogyakarta",
                "subdistricts": [
                    {"name": "Sosromenduran", "zip": "55271"},
                    {"name": "Suryatmajan", "zip": "55213"},
                    {"name": "Caturtunggal", "zip": "55281"},
                    {"name": "Sinduadi", "zip": "55284"},
                    {"name": "Brontokusuman", "zip": "55153"}
                ],
                "streets": [
                    "Jl. Malioboro", "Jl. Margo Utomo", "Jl. Kaliurang", "Jl. Affandi (Gejayan)",
                    "Jl. Laksda Adisucipto", "Jl. Prawirotaman", "Jl. Jenderal Sudirman"
                ]
            }
        ]
    },
    "bali": {
        "name": "Denpasar",
        "city_label": "Denpasar",
        "province": "Bali",
        "postal_code": "80232",
        "aliases": ["bali", "denpasar", "kuta", "seminyak", "badung", "sanur"],
        "districts": [
            {
                "city": "Denpasar",
                "subdistricts": [
                    {"name": "Renon", "zip": "80226"},
                    {"name": "Sanur Kaja", "zip": "80227"},
                    {"name": "Sanur Kauh", "zip": "80228"},
                    {"name": "Pemecutan Kelod", "zip": "80119"},
                    {"name": "Dangin Puri", "zip": "80232"}
                ],
                "streets": [
                    "Jl. Raya Puputan", "Jl. Danau Tamblingan", "Jl. Teuku Umar",
                    "Jl. Gajah Mada", "Jl. Diponegoro", "Jl. Hayam Wuruk"
                ]
            },
            {
                "city": "Badung",
                "subdistricts": [
                    {"name": "Seminyak", "zip": "80361"},
                    {"name": "Kuta", "zip": "80361"},
                    {"name": "Legian", "zip": "80361"},
                    {"name": "Tibubeneng (Canggu)", "zip": "80351"},
                    {"name": "Jimbaran", "zip": "80361"}
                ],
                "streets": [
                    "Jl. Sunset Road", "Jl. Raya Seminyak", "Jl. Pantai Kuta",
                    "Jl. Pantai Batu Bolong", "Jl. Raya Uluwatu", "Jl. Kayu Aya"
                ]
            }
        ]
    },
    "makassar": {
        "name": "Makassar",
        "city_label": "Makassar",
        "province": "Sulawesi Selatan",
        "postal_code": "90111",
        "aliases": ["makassar", "ujung pandang", "sulsel"],
        "districts": [
            {
                "city": "Makassar",
                "subdistricts": [
                    {"name": "Losari", "zip": "90111"},
                    {"name": "Maloku", "zip": "90112"},
                    {"name": "Masale", "zip": "90222"},
                    {"name": "Maricaya", "zip": "90142"}
                ],
                "streets": [
                    "Jl. Somba Opu", "Jl. Penghibur", "Jl. Urip Sumoharjo",
                    "Jl. Boulevard Panakkukang", "Jl. Dr. Sam Ratulangi"
                ]
            }
        ]
    },
    "bekasi": {
        "name": "Bekasi",
        "city_label": "Bekasi",
        "province": "Jawa Barat",
        "postal_code": "17141",
        "aliases": ["bekasi", "bks", "kota bekasi"],
        "districts": [
            {
                "city": "Bekasi",
                "subdistricts": [
                    {"name": "Marga Jaya", "zip": "17141"},
                    {"name": "Pekayon Jaya", "zip": "17148"},
                    {"name": "Harapan Mulya", "zip": "17143"},
                    {"name": "Kayuringin Jaya", "zip": "17144"}
                ],
                "streets": [
                    "Jl. Jenderal Ahmad Yani", "Jl. KH. Noer Ali (Kalimalang)",
                    "Jl. Boulevard Barat Summarecon", "Jl. Ir. H. Juanda"
                ]
            }
        ]
    },
    "tangerang": {
        "name": "Tangerang",
        "city_label": "Tangerang Selatan",
        "province": "Banten",
        "postal_code": "15310",
        "aliases": ["tangerang", "tangsel", "tangerang selatan", "bsd", "bintaro"],
        "districts": [
            {
                "city": "Tangerang Selatan",
                "subdistricts": [
                    {"name": "Lengkong Gudang (BSD)", "zip": "15310"},
                    {"name": "Rawa Buntu", "zip": "15318"},
                    {"name": "Pondok Ranji (Bintaro)", "zip": "15412"},
                    {"name": "Pakulonan (Alam Sutera)", "zip": "15325"}
                ],
                "streets": [
                    "Jl. Boulevard BSD Raya", "Jl. Pahlawan Seribu",
                    "Jl. Bintaro Utama Sektor 3", "Jl. Alam Sutera Boulevard"
                ]
            },
            {
                "city": "Tangerang",
                "subdistricts": [
                    {"name": "Sukarasa", "zip": "15111"},
                    {"name": "Babakan", "zip": "15118"},
                    {"name": "Cikokol", "zip": "15117"}
                ],
                "streets": [
                    "Jl. Daan Mogot", "Jl. M.H. Thamrin", "Jl. Jenderal Sudirman"
                ]
            }
        ]
    },
    "depok": {
        "name": "Depok",
        "city_label": "Depok",
        "province": "Jawa Barat",
        "postal_code": "16424",
        "aliases": ["depok", "kota depok"],
        "districts": [
            {
                "city": "Depok",
                "subdistricts": [
                    {"name": "Pondok Cina", "zip": "16424"},
                    {"name": "Beji", "zip": "16421"},
                    {"name": "Kemiri Muka", "zip": "16423"},
                    {"name": "Cinere", "zip": "16514"}
                ],
                "streets": [
                    "Jl. Margonda Raya", "Jl. Arif Rahman Hakim", "Jl. Ir. H. Juanda Depok", "Jl. Cinere Raya"
                ]
            }
        ]
    },
    "bogor": {
        "name": "Bogor",
        "city_label": "Bogor",
        "province": "Jawa Barat",
        "postal_code": "16143",
        "aliases": ["bogor", "bgr", "kota bogor"],
        "districts": [
            {
                "city": "Bogor",
                "subdistricts": [
                    {"name": "Baranangsiang", "zip": "16143"},
                    {"name": "Babakan", "zip": "16128"},
                    {"name": "Tegallega", "zip": "16129"},
                    {"name": "Pabaton", "zip": "16121"}
                ],
                "streets": [
                    "Jl. Pajajaran", "Jl. Ir. H. Juanda Bogor", "Jl. Jenderal Sudirman Bogor", "Jl. Surya Kencana"
                ]
            }
        ]
    },
    "malang": {
        "name": "Malang",
        "city_label": "Malang",
        "province": "Jawa Timur",
        "postal_code": "65119",
        "aliases": ["malang", "mlg", "kota malang"],
        "districts": [
            {
                "city": "Malang",
                "subdistricts": [
                    {"name": "Oro-Oro Dowo", "zip": "65119"},
                    {"name": "Klojen", "zip": "65111"},
                    {"name": "Jatimulyo", "zip": "65141"},
                    {"name": "Lowokwaru", "zip": "65141"}
                ],
                "streets": [
                    "Jl. Besar Ijen", "Jl. Soekarno Hatta", "Jl. Merdeka Selatan", "Jl. Veteran", "Jl. Kawi"
                ]
            }
        ]
    }
}
