# -*- coding: utf-8 -*-
"""
Vietnam Address & Identity Dataset
Berisi data komprehensif wilayah Vietnam (63 Provinsi/Kota), nama autentik,
kode pos, format nomor telepon, dan pola alamat Vietnam.
"""

# Nama-nama khas Vietnam
VIETNAMESE_NAMES = {
    "last_names": [
        "Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Phan", "Vũ", "Võ",
        "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", "Dương", "Lý", "Đinh", "Đoàn",
        "Lâm", "Mai", "Trịnh", "Đào", "Cao", "Lưu", "Lương", "Thái", "Châu",
        "Tạ", "Phùng", "Tô", "Vương", "Văn", "Tăng", "Quách", "Hà", "Chu"
    ],
    "male_middle_names": [
        "Văn", "Hữu", "Đức", "Quang", "Minh", "Đình", "Quốc", "Hoàng", "Thanh",
        "Ngọc", "Trọng", "Tiến", "Công", "Xuân", "Anh", "Duy", "Bảo", "Tuấn",
        "Thành", "Hải", "Khắc", "Gia", "Đăng", "Phước"
    ],
    "male_first_names": [
        "An", "Bình", "Cường", "Dũng", "Giang", "Hải", "Hùng", "Huy", "Khoa",
        "Linh", "Long", "Minh", "Nam", "Phúc", "Quân", "Sơn", "Tâm", "Thắng",
        "Tuấn", "Tùng", "Đức", "Trung", "Kiên", "Phong", "Thịnh", "Khôi",
        "Toàn", "Đạt", "Trí", "Hiếu", "Hoàng", "Trọng", "Thành", "Việt",
        "Lâm", "Hào", "Nghĩa", "Vinh", "Khánh", "Duy"
    ],
    "female_middle_names": [
        "Thị", "Ngọc", "Thu", "Thanh", "Phương", "Kim", "Mỹ", "Thùy", "Hồng",
        "Diệu", "Khánh", "Mai", "Quỳnh", "Hoài", "Tuyết", "Bích", "Như", "Ánh",
        "Hương", "Hà", "Lan", "Trâm", "Gia", "Bảo"
    ],
    "female_first_names": [
        "Anh", "Trang", "Mai", "Lan", "Vy", "Hương", "Thảo", "Phương", "Ngọc",
        "Huyền", "Linh", "Nhung", "Hằng", "Thủy", "Oanh", "Hà", "Dung", "Yến",
        "Chi", "Nga", "Quyên", "Trâm", "Loan", "Vân", "Tâm", "Hoa", "Trúc",
        "Liên", "Ly", "Diệp", "Châu", "Ngân", "Quỳnh", "Giang", "Hiền", "Tú"
    ]
}

# Prefix Provider Seluler Vietnam
TELCO_PREFIXES = {
    "Viettel": ["086", "096", "097", "098", "032", "033", "034", "035", "036", "037", "038", "039"],
    "Vinaphone": ["088", "091", "094", "081", "082", "083", "084", "085"],
    "Mobifone": ["089", "090", "093", "070", "076", "077", "078", "079"],
    "Vietnamobile": ["092", "056", "058"]
}

# Data detail kota-kota utama dan seluruh 63 provinsi di Vietnam
PROVINCES_DATA = {
    # 1. HÀ NỘI (Thủ Đô)
    "ha noi": {
        "name": "Hà Nội",
        "english_name": "Hanoi",
        "postal_code": "100000",
        "postal_range": (100000, 150000),
        "aliases": ["ha noi", "hanoi", "hn", "thu do ha noi", "tp ha noi", "thanh pho ha noi"],
        "districts": [
            {
                "district": "Quận Ba Đình",
                "postal_code": "118000",
                "wards": [
                    "Phường Cống Vị", "Phường Điện Biên", "Phường Đội Cấn", "Phường Giảng Võ",
                    "Phường Kim Mã", "Phường Liễu Giai", "Phường Ngọc Hà", "Phường Ngọc Khánh",
                    "Phường Quán Thánh", "Phường Thành Công", "Phường Trúc Bạch", "Phường Vĩnh Phúc"
                ],
                "streets": [
                    "Đường Đội Cấn", "Đường Kim Mã", "Đường Liễu Giai", "Đường Hoàng Hoa Thám",
                    "Đường Quán Thánh", "Đường Phan Đình Phùng", "Đường Giảng Võ", "Đường Nguyễn Chí Thanh",
                    "Đường Ngọc Khánh", "Đường Văn Cao", "Đường Đốc Ngữ", "Đường Linh Lang"
                ]
            },
            {
                "district": "Quận Hoàn Kiếm",
                "postal_code": "110000",
                "wards": [
                    "Phường Hàng Bạc", "Phường Hàng Bài", "Phường Hàng Bồ", "Phường Hàng Bông",
                    "Phường Hàng Buồm", "Phường Hàng Đào", "Phường Hàng Gai", "Phường Hàng Mã",
                    "Phường Tràng Tiền", "Phường Lý Thái Tổ", "Phường Cửa Đông", "Phường Cửa Nam",
                    "Phường Đồng Xuân", "Phường Phan Chu Trinh", "Phường Phúc Tân"
                ],
                "streets": [
                    "Phố Tràng Tiền", "Phố Hàng Bài", "Phố Hàng Bông", "Phố Đinh Tiên Hoàng",
                    "Phố Lý Thường Kiệt", "Phố Hai Bà Trưng", "Phố Hàng Đào", "Phố Trần Hưng Đạo",
                    "Phố Hàng Gai", "Phố Nhà Thờ", "Phố Hàng Ngang", "Phố Lương Ngọc Quyến"
                ]
            },
            {
                "district": "Quận Cầu Giấy",
                "postal_code": "122000",
                "wards": [
                    "Phường Dịch Vọng", "Phường Dịch Vọng Hậu", "Phường Mai Dịch", "Phường Nghĩa Đô",
                    "Phường Nghĩa Tân", "Phường Quan Hoa", "Phường Trung Hòa", "Phường Yên Hòa"
                ],
                "streets": [
                    "Đường Cầu Giấy", "Đường Xuân Thủy", "Đường Trần Thái Tông", "Đường Duy Tân",
                    "Đường Trung Kính", "Đường Hoàng Quốc Việt", "Đường Nguyễn Phong Sắc", "Đường Phạm Hùng",
                    "Đường Nguyễn Khang", "Đường Vũ Phạm Hàm", "Đường Dương Đình Nghệ", "Đường Trần Đăng Ninh"
                ]
            },
            {
                "district": "Quận Đống Đa",
                "postal_code": "115000",
                "wards": [
                    "Phường Cát Linh", "Phường Hàng Bột", "Phường Khâm Thiên", "Phường Khương Thượng",
                    "Phường Kim Liên", "Phường Láng Hạ", "Phường Láng Thượng", "Phường Ô Chợ Dừa",
                    "Phường Phương Mai", "Phường Quang Trung", "Phường Quốc Tử Giám", "Phường Thịnh Quang",
                    "Phường Trung Liệt", "Phường Trung Phụng", "Phường Trung Tự", "Phường Văn Miếu"
                ],
                "streets": [
                    "Đường Láng", "Đường Tây Sơn", "Đường Tôn Đức Thắng", "Đường Xã Đàn",
                    "Đường Chùa Bộc", "Đường Thái Hà", "Đường Huỳnh Thúc Kháng", "Đường Nguyễn Lương Bằng",
                    "Đường Hoàng Cầu", "Đường Đặng Văn Ngữ", "Đường Phạm Ngọc Thạch", "Đường Yên Lãng"
                ]
            },
            {
                "district": "Quận Hai Bà Trưng",
                "postal_code": "112000",
                "wards": [
                    "Phường Bách Khoa", "Phường Bạch Đằng", "Phường Bạch Mai", "Phường Cầu Dền",
                    "Phường Đống Mác", "Phường Đồng Nhân", "Phường Đồng Tâm", "Phường Lê Đại Hành",
                    "Phường Minh Khai", "Phường Phố Huế", "Phường Quỳnh Lôi", "Phường Quỳnh Mai",
                    "Phường Thanh Lương", "Phường Thanh Nhàn", "Phường Trương Định", "Phường Vĩnh Tuy"
                ],
                "streets": [
                    "Đường Phố Huế", "Đường Bà Triệu", "Đường Bạch Mai", "Đường Đại Cồ Việt",
                    "Đường Minh Khai", "Đường Trần Khát Chân", "Đường Lạc Trung", "Đường Lò Đúc",
                    "Đường Kim Ngưu", "Đường Lê Thanh Nghị", "Đường Tạ Quang Bửu", "Đường Tam Trinh"
                ]
            },
            {
                "district": "Quận Tây Hồ",
                "postal_code": "124000",
                "wards": [
                    "Phường Bưởi", "Phường Nhật Tân", "Phường Phú Thượng", "Phường Quảng An",
                    "Phường Thụy Khuê", "Phường Tứ Liên", "Phường Xuân La", "Phường Yên Phụ"
                ],
                "streets": [
                    "Đường Lạc Long Quân", "Đường Âu Cơ", "Đường Thụy Khuê", "Đường Võ Chí Công",
                    "Đường Xuân Diệu", "Đường Yên Phụ", "Đường Nghi Tàm", "Đường Quảng An",
                    "Đường Tô Ngọc Vân", "Đường Trích Sài", "Đường Nhật Chiêu"
                ]
            },
            {
                "district": "Quận Thanh Xuân",
                "postal_code": "120000",
                "wards": [
                    "Phường Hạ Đình", "Phường Khương Đình", "Phường Khương Mai", "Phường Khương Trung",
                    "Phường Kim Giang", "Phường Nhân Chính", "Phường Phương Liệt", "Phường Thanh Xuân Bắc",
                    "Phường Thanh Xuân Nam", "Phường Thanh Xuân Trung", "Phường Thượng Đình"
                ],
                "streets": [
                    "Đường Nguyễn Trãi", "Đường Lê Văn Lương", "Đường Khuất Duy Tiến", "Đường Nguyễn Tuân",
                    "Đường Vũ Tông Phan", "Đường Hoàng Văn Thái", "Đường Trường Chinh", "Đường Khương Đình",
                    "Đường Tô Vĩnh Diện", "Đường Chính Kinh", "Đường Quan Nhân"
                ]
            },
            {
                "district": "Quận Nam Từ Liêm",
                "postal_code": "128000",
                "wards": [
                    "Phường Cầu Diễn", "Phường Đại Mỗ", "Phường Mễ Trì", "Phường Mỹ Đình 1",
                    "Phường Mỹ Đình 2", "Phường Phú Đô", "Phường Tây Mỗ", "Phường Trung Văn",
                    "Phường Xuân Phương"
                ],
                "streets": [
                    "Đường Lê Đức Thọ", "Đường Mễ Trì", "Đường Phạm Hùng", "Đường Nguyễn Hoàng",
                    "Đường Đình Thôn", "Đường Tố Hữu", "Đường Hàm Nghi", "Đường Trần Hữu Dực",
                    "Đường Nguyễn Cơ Thạch", "Đường Đại Mỗ", "Đường Sa Đôi"
                ]
            },
            {
                "district": "Quận Bắc Từ Liêm",
                "postal_code": "129000",
                "wards": [
                    "Phường Cổ Nhuế 1", "Phường Cổ Nhuế 2", "Phường Đông Ngạc", "Phường Đức Thắng",
                    "Phường Phúc Diễn", "Phường Phú Diễn", "Phường Xuân Đỉnh", "Phường Xuân Tảo"
                ],
                "streets": [
                    "Đường Phạm Văn Đồng", "Đường Cổ Nhuế", "Đường Hoàng Công Chất", "Đường Văn Tiến Dũng",
                    "Đường Nguyễn Đình Tứ", "Đường Võ Quý Huân", "Đường Tân Xuân"
                ]
            },
            {
                "district": "Quận Hà Đông",
                "postal_code": "152000",
                "wards": [
                    "Phường Quang Trung", "Phường Yết Kiêu", "Phường Nguyễn Trãi", "Phường Văn Quán",
                    "Phường Mộ Lao", "Phường Hà Cầu", "Phường Vạn Phúc", "Phường La Khê",
                    "Phường Phú La", "Phường Kiến Hưng", "Phường Yên Nghĩa"
                ],
                "streets": [
                    "Đường Quang Trung", "Đường Trần Phú", "Đường Lê Trọng Tấn", "Đường Vạn Phúc",
                    "Đường Phùng Hưng", "Đường Tô Hiệu", "Đường Nguyễn Văn Lộc", "Đường Tố Hữu"
                ]
            },
            {
                "district": "Quận Long Biên",
                "postal_code": "132000",
                "wards": [
                    "Phường Bồ Đề", "Phường Cự Khối", "Phường Đức Giang", "Phường Gia Thụy",
                    "Phường Giang Biên", "Phường Long Biên", "Phường Ngọc Lâm", "Phường Ngọc Thụy",
                    "Phường Phúc Đồng", "Phường Phúc Lợi", "Phường Sài Đồng", "Phường Thạch Bàn",
                    "Phường Thượng Thanh", "Phường Việt Hưng"
                ],
                "streets": [
                    "Đường Nguyễn Văn Cừ", "Đường Ngọc Lâm", "Đường Ngô Gia Tự", "Đường Cổ Linh",
                    "Đường Nguyễn Sơn", "Đường Thạch Bàn", "Đường Chu Huy Mân", "Đường Đoàn Khuê"
                ]
            },
            {
                "district": "Quận Hoàng Mai",
                "postal_code": "127000",
                "wards": [
                    "Phường Đại Kim", "Phường Định Công", "Phường Giáp Bát", "Phường Hoàng Liệt",
                    "Phường Hoàng Văn Thụ", "Phường Lĩnh Nam", "Phường Mai Động", "Phường Tân Mai",
                    "Phường Thịnh Liệt", "Phường Trần Phú", "Phường Tương Mai", "Phường Vĩnh Hưng",
                    "Phường Yên Sở"
                ],
                "streets": [
                    "Đường Giải Phóng", "Đường Kim Đồng", "Đường Tam Trinh", "Đường Trương Định",
                    "Đường Tân Mai", "Đường Lĩnh Nam", "Đường Định Công", "Đường Nguyễn Cảnh Dị"
                ]
            }
        ]
    },

    # 2. THÀNH PHỐ HỒ CHÍ MINH (SÀI GÒN)
    "ho chi minh": {
        "name": "Thành phố Hồ Chí Minh",
        "english_name": "Ho Chi Minh City",
        "postal_code": "700000",
        "postal_range": (700000, 760000),
        "aliases": ["ho chi minh", "hcm", "tphcm", "tp hcm", "saigon", "sai gon", "thanh pho ho chi minh", "sg"],
        "districts": [
            {
                "district": "Quận 1",
                "postal_code": "710000",
                "wards": [
                    "Phường Bến Nghé", "Phường Bến Thành", "Phường Cô Giang", "Phường Cầu Kho",
                    "Phường Cầu Ông Lãnh", "Phường Đa Kao", "Phường Nguyễn Cư Trinh", "Phường Nguyễn Thái Bình",
                    "Phường Phạm Ngũ Lão", "Phường Tân Định"
                ],
                "streets": [
                    "Đường Nguyễn Huệ", "Đường Lê Lợi", "Đường Đồng Khởi", "Đường Pasteur",
                    "Đường Hai Bà Trưng", "Đường Lê Thánh Tôn", "Đường Nam Kỳ Khởi Nghĩa", "Đường Bùi Viện",
                    "Đường Đinh Tiên Hoàng", "Đường Trần Hưng Đạo", "Đường Nguyễn Thị Minh Khai", "Đường Calmette"
                ]
            },
            {
                "district": "Quận 3",
                "postal_code": "722000",
                "wards": [
                    "Phường 1", "Phường 2", "Phường 3", "Phường 4", "Phường 5",
                    "Phường 9", "Phường 10", "Phường 11", "Phường 12", "Phường 14", "Phường Võ Thị Sáu"
                ],
                "streets": [
                    "Đường Cách Mạng Tháng 8", "Đường Võ Văn Tần", "Đường Nguyễn Đình Chiểu", "Đường Điện Biên Phủ",
                    "Đường Nam Kỳ Khởi Nghĩa", "Đường Lý Chính Thắng", "Đường Lê Văn Sỹ", "Đường Trương Định",
                    "Đường Bà Huyện Thanh Quan", "Đường Cao Thắng", "Đường Tú Xương"
                ]
            },
            {
                "district": "Quận 5",
                "postal_code": "727000",
                "wards": [
                    "Phường 1", "Phường 2", "Phường 3", "Phường 4", "Phường 5",
                    "Phường 6", "Phường 7", "Phường 8", "Phường 9", "Phường 10",
                    "Phường 11", "Phường 12", "Phường 13", "Phường 14"
                ],
                "streets": [
                    "Đường Trần Hưng Đạo", "Đường Nguyễn Trãi", "Đường An Dương Vương", "Đường Hồng Bàng",
                    "Đường Châu Văn Liêm", "Đường Hải Thượng Lãn Ông", "Đường Ngô Gia Tự", "Đường Nguyễn Tri Phương"
                ]
            },
            {
                "district": "Quận 7",
                "postal_code": "729000",
                "wards": [
                    "Phường Tân Thuận Đông", "Phường Tân Thuận Tây", "Phường Tân Kiểng", "Phường Tân Hưng",
                    "Phường Bình Thuận", "Phường Tân Quy", "Phường Phú Thuận", "Phường Tân Phú",
                    "Phường Tân Phong", "Phường Phú Mỹ"
                ],
                "streets": [
                    "Đường Nguyễn Văn Linh", "Đường Huỳnh Tấn Phát", "Đường Nguyễn Thị Thập", "Đường Nguyễn Hữu Thọ",
                    "Đường Lâm Văn Bền", "Đường Lê Văn Lương", "Đường Hoàng Quốc Việt", "Đường Phạm Thái Bường"
                ]
            },
            {
                "district": "Quận 10",
                "postal_code": "725000",
                "wards": [
                    "Phường 1", "Phường 2", "Phường 4", "Phường 6", "Phường 8",
                    "Phường 9", "Phường 10", "Phường 11", "Phường 12", "Phường 13", "Phường 14", "Phường 15"
                ],
                "streets": [
                    "Đường 3 Tháng 2", "Đường Lý Thường Kiệt", "Đường Sư Vạn Hạnh", "Đường Thành Thái",
                    "Đường Tô Hiến Thành", "Đường Cách Mạng Tháng 8", "Đường Lê Hồng Phong", "Đường Nguyễn Tri Phương"
                ]
            },
            {
                "district": "Quận Bình Thạnh",
                "postal_code": "723000",
                "wards": [
                    "Phường 1", "Phường 2", "Phường 3", "Phường 5", "Phường 6",
                    "Phường 7", "Phường 11", "Phường 12", "Phường 13", "Phường 14",
                    "Phường 15", "Phường 17", "Phường 19", "Phường 21", "Phường 22",
                    "Phường 24", "Phường 25", "Phường 26", "Phường 27", "Phường 28"
                ],
                "streets": [
                    "Đường Điện Biên Phủ", "Đường Xô Viết Nghệ Tĩnh", "Đường Bạch Đằng", "Đường Phan Đăng Lưu",
                    "Đường Nơ Trang Long", "Đường Đinh Bộ Lĩnh", "Đường D2 (Nguyễn Gia Trí)", "Đường Chu Văn An"
                ]
            },
            {
                "district": "Quận Tân Bình",
                "postal_code": "721000",
                "wards": [
                    "Phường 1", "Phường 2", "Phường 3", "Phường 4", "Phường 5",
                    "Phường 6", "Phường 7", "Phường 8", "Phường 9", "Phường 10",
                    "Phường 11", "Phường 12", "Phường 13", "Phường 14", "Phường 15"
                ],
                "streets": [
                    "Đường Cộng Hòa", "Đường Trường Chinh", "Đường Hoàng Văn Thụ", "Đường Lê Văn Sỹ",
                    "Đường Phổ Quang", "Đường Bạch Đằng", "Đường Lý Thường Kiệt", "Đường Trường Sơn"
                ]
            },
            {
                "district": "Quận Phú Nhuận",
                "wards": [
                    "Phường 1", "Phường 2", "Phường 3", "Phường 4", "Phường 5",
                    "Phường 7", "Phường 8", "Phường 9", "Phường 10", "Phường 11",
                    "Phường 13", "Phường 15", "Phường 17"
                ],
                "streets": [
                    "Đường Phan Xích Long", "Đường Phan Đăng Lưu", "Đường Nguyễn Văn Trỗi", "Đường Hoàng Văn Thụ",
                    "Đường Huỳnh Văn Bánh", "Đường Thích Quảng Đức", "Đường Phan Đình Phùng"
                ]
            },
            {
                "district": "Thành phố Thủ Đức",
                "postal_code": "713000",
                "wards": [
                    "Phường Thảo Điền", "Phường An Phú", "Phường Hiệp Phú", "Phường Linh Trung",
                    "Phường Linh Chiểu", "Phường Phước Long B", "Phường Bình Thọ", "Phường Hiệp Bình Chánh",
                    "Phường Linh Tây", "Phường Phước Bình", "Phường Tăng Nhơn Phú A"
                ],
                "streets": [
                    "Đường Xa Lộ Hà Nội", "Đường Võ Văn Ngân", "Đường Mai Chí Thọ", "Đường Nguyễn Duy Trinh",
                    "Đường Đỗ Xuân Hợp", "Đường Đặng Văn Bi", "Đường Quốc Hương", "Đường Nguyễn Văn Hưởng"
                ]
            },
            {
                "district": "Quận Gò Vấp",
                "postal_code": "714000",
                "wards": [
                    "Phường 1", "Phường 3", "Phường 5", "Phường 6", "Phường 7",
                    "Phường 8", "Phường 9", "Phường 10", "Phường 11", "Phường 12",
                    "Phường 14", "Phường 15", "Phường 16", "Phường 17"
                ],
                "streets": [
                    "Đường Quang Trung", "Đường Phan Văn Trị", "Đường Nguyễn Oanh", "Đường Lê Đức Thọ",
                    "Đường Nguyễn Văn Lượng", "Đường Thống Nhất", "Đường Phạm Văn Đồng"
                ]
            }
        ]
    },

    # 3. ĐÀ NẴNG
    "da nang": {
        "name": "Đà Nẵng",
        "english_name": "Da Nang",
        "postal_code": "550000",
        "postal_range": (550000, 560000),
        "aliases": ["da nang", "danang", "dn", "tp da nang", "thanh pho da nang"],
        "districts": [
            {
                "district": "Quận Hải Châu",
                "wards": [
                    "Phường Hải Châu 1", "Phường Hải Châu 2", "Phường Thạch Thang", "Phường Thanh Bình",
                    "Phường Thuận Phước", "Phường Hòa Thuận Đông", "Phường Hòa Thuận Tây", "Phường Nam Dương",
                    "Phường Phước Ninh", "Phường Bình Hiên", "Phường Bình Thuận", "Phường Hòa Cường Bắc"
                ],
                "streets": [
                    "Đường Bạch Đằng", "Đường Trần Phú", "Đường Lê Duẩn", "Đường Nguyễn Văn Linh",
                    "Đường Hùng Vương", "Đường 2 Tháng 9", "Đường Phan Châu Trinh", "Đường Hoàng Diệu",
                    "Đường Quang Trung", "Đường Pasteur", "Đường Trưng Nữ Vương"
                ]
            },
            {
                "district": "Quận Thanh Khê",
                "postal_code": "551000",
                "wards": [
                    "Phường Tam Thuận", "Phường Thanh Khê Tây", "Phường Thanh Khê Đông", "Phường Xuân Hà",
                    "Phường Tân Chính", "Phường Chính Gián", "Phường Vĩnh Trung", "Phường Thạc Gián",
                    "Phường An Khê", "Phường Hòa Khê"
                ],
                "streets": [
                    "Đường Điện Biên Phủ", "Đường Hà Huy Tập", "Đường Nguyễn Tất Thành", "Đường Trần Cao Vân",
                    "Đường Dũng Sĩ Thanh Khê", "Đường Lê Độ", "Đường Hải Phòng", "Đường Hùng Vương"
                ]
            },
            {
                "district": "Quận Sơn Trà",
                "postal_code": "552000",
                "wards": [
                    "Phường An Hải Bắc", "Phường An Hải Đông", "Phường An Hải Tây", "Phường Mân Thái",
                    "Phường Phước Mỹ", "Phường Thọ Quang", "Phường Nại Hiên Đông"
                ],
                "streets": [
                    "Đường Võ Nguyên Giáp", "Đường Phạm Văn Đồng", "Đường Ngô Quyền", "Đường Hoàng Sa",
                    "Đường Trần Hưng Đạo", "Đường Hồ Nghinh", "Đường Võ Văn Kiệt", "Đường Vương Thừa Vũ"
                ]
            },
            {
                "district": "Quận Ngũ Hành Sơn",
                "postal_code": "553000",
                "wards": [
                    "Phường Mỹ An", "Phường Khuê Mỹ", "Phường Hòa Quý", "Phường Hòa Hải"
                ],
                "streets": [
                    "Đường Lê Văn Hiến", "Đường Võ Nguyên Giáp", "Đường Trường Sa", "Đường Châu Thị Vĩnh Tế",
                    "Đường An Dương Vương", "Đường Nam Kỳ Khởi Nghĩa", "Đường Phan Tứ"
                ]
            },
            {
                "district": "Quận Cẩm Lệ",
                "postal_code": "554000",
                "wards": [
                    "Phường Khuê Trung", "Phường Hòa Thọ Đông", "Phường Hòa Thọ Tây",
                    "Phường Hòa An", "Phường Hòa Phát", "Phường Hòa Xuân"
                ],
                "streets": [
                    "Đường Cách Mạng Tháng 8", "Đường Trường Chinh", "Đường Lê Đại Hành",
                    "Đường Nguyễn Phước Tần", "Đường Tôn Đản", "Đường Văn Tiến Dũng"
                ]
            }
        ]
    },

    # 4. HẢI PHÒNG
    "hai phong": {
        "name": "Hải Phòng",
        "english_name": "Hai Phong",
        "postal_code": "180000",
        "postal_range": (180000, 190000),
        "aliases": ["hai phong", "haiphong", "hp", "tp hai phong", "thanh pho hai phong"],
        "districts": [
            {
                "district": "Quận Hồng Bàng",
                "wards": [
                    "Phường Hoàng Văn Thụ", "Phường Minh Khai", "Phường Phan Bội Châu",
                    "Phường Quán Toan", "Phường Sở Dầu", "Phường Thượng Lý", "Phường Trại Chuối"
                ],
                "streets": [
                    "Đường Đinh Tiên Hoàng", "Đường Điện Biên Phủ", "Đường Hoàng Văn Thụ",
                    "Đường Bạch Đằng", "Đường Quang Trung", "Đường Trần Hưng Đạo", "Đường Hùng Vương"
                ]
            },
            {
                "district": "Quận Ngô Quyền",
                "postal_code": "182000",
                "wards": [
                    "Phường Cầu Đất", "Phường Cầu Tre", "Phường Đằng Giang", "Phường Đông Khê",
                    "Phường Đồng Quốc Bình", "Phường Gia Viên", "Phường Lạc Viên", "Phường Lạch Tray"
                ],
                "streets": [
                    "Đường Lạch Tray", "Đường Lê Lợi", "Đường Đà Nẵng", "Đường Lê Hồng Phong",
                    "Đường Cầu Đất", "Đường Trần Phú", "Đường Nguyễn Bỉnh Khiêm"
                ]
            },
            {
                "district": "Quận Lê Chân",
                "postal_code": "183000",
                "wards": [
                    "Phường An Biên", "Phường An Dương", "Phường Cát Dài", "Phường Dư Hàng",
                    "Phường Dư Hàng Kênh", "Phường Hàng Kênh", "Phường Hồ Nam", "Phường Kênh Dương"
                ],
                "streets": [
                    "Đường Tô Hiệu", "Đường Trần Nguyên Hãn", "Đường Tôn Đức Thắng",
                    "Đường Nguyễn Văn Linh", "Đường Chợ Hàng", "Đường Hai Bà Trưng"
                ]
            }
        ]
    },

    # 5. CẦN THƠ
    "can tho": {
        "name": "Cần Thơ",
        "english_name": "Can Tho",
        "postal_code": "900000",
        "postal_range": (900000, 910000),
        "aliases": ["can tho", "cantho", "tp can tho", "thanh pho can tho"],
        "districts": [
            {
                "district": "Quận Ninh Kiều",
                "wards": [
                    "Phường An Bình", "Phường An Cư", "Phường An Hòa", "Phường An Khánh",
                    "Phường An Nghiệp", "Phường Cái Khế", "Phường Hưng Lợi", "Phường Tân An",
                    "Phường Thới Bình", "Phường Xuân Khánh"
                ],
                "streets": [
                    "Đường 30 Tháng 4", "Đường Đại Lộ Hòa Bình", "Đường Nguyễn Trãi", "Đường Mậu Thân",
                    "Đường Trần Hưng Đạo", "Đường Lý Tự Trọng", "Đường Hai Bà Trưng", "Đường Cách Mạng Tháng 8"
                ]
            },
            {
                "district": "Quận Cái Răng",
                "postal_code": "902000",
                "wards": [
                    "Phường Ba Láng", "Phường Hưng Phú", "Phường Hưng Thạnh", "Phường Lê Bình",
                    "Phường Phú Thứ", "Phường Tân Phú", "Phường Yên Đỗ"
                ],
                "streets": [
                    "Đường Phạm Hùng", "Đường Quang Trung", "Đường Võ Nguyên Giáp", "Đường Trần Hưng Đạo"
                ]
            }
        ]
    },

    # 6. BÌNH DƯƠNG
    "binh duong": {
        "name": "Bình Dương",
        "english_name": "Binh Duong",
        "postal_code": "820000",
        "postal_range": (820000, 830000),
        "aliases": ["binh duong", "binhduong", "bd", "tinh binh duong"],
        "districts": [
            {
                "district": "Thành phố Thủ Dầu Một",
                "wards": ["Phường Phú Cường", "Phường Hiệp Thành", "Phường Phú Hòa", "Phường Phú Lợi", "Phường Định Hòa", "Phường Chánh Nghĩa"],
                "streets": ["Đại Lộ Bình Dương", "Đường Yersin", "Đường Cách Mạng Tháng 8", "Đường Thích Quảng Đức", "Đường 30 Tháng 4"]
            },
            {
                "district": "Thành phố Thuận An",
                "postal_code": "821000",
                "wards": ["Phường Lái Thiêu", "Phường An Thạnh", "Phường Thuận Giao", "Phường An Phú", "Phường Bình Hòa"],
                "streets": ["Đường DT743", "Đường Nguyễn Văn Tiết", "Đường Cách Mạng Tháng 8", "Đại Lộ Bình Dương"]
            },
            {
                "district": "Thành phố Dĩ An",
                "postal_code": "822000",
                "wards": ["Phường Dĩ An", "Phường Tân Đông Hiệp", "Phường Tân Bình", "Phường An Bình", "Phường Đông Hòa"],
                "streets": ["Đường Trần Hưng Đạo", "Đường Nguyễn An Ninh", "Đường Lý Thường Kiệt", "Đường DT743A"]
            }
        ]
    },

    # 7. ĐỒNG NAI
    "dong nai": {
        "name": "Đồng Nai",
        "english_name": "Dong Nai",
        "postal_code": "810000",
        "postal_range": (810000, 820000),
        "aliases": ["dong nai", "dongnai", "tinh dong nai", "bien hoa"],
        "districts": [
            {
                "district": "Thành phố Biên Hòa",
                "wards": ["Phường Quyết Thắng", "Phường Trung Dũng", "Phường Thống Nhất", "Phường Tân Tiến", "Phường Tân Mai", "Phường Trảng Dài"],
                "streets": ["Đường Nguyễn Ái Quốc", "Đường Đồng Khởi", "Đường Phạm Văn Thuận", "Đường Võ Thị Sáu", "Đường Cách Mạng Tháng 8"]
            },
            {
                "district": "Huyện Long Thành",
                "postal_code": "812000",
                "wards": ["Thị trấn Long Thành", "Xã An Phước", "Xã Long Đức", "Xã Bình Sơn", "Xã Lộc An"],
                "streets": ["Đường Lê Duẩn", "Đường Tôn Đức Thắng", "Đường Quốc Lộ 51"]
            }
        ]
    },

    # 8. KHÁNH HÒA (NHA TRANG)
    "khanh hoa": {
        "name": "Khánh Hòa",
        "english_name": "Khanh Hoa",
        "postal_code": "650000",
        "postal_range": (650000, 660000),
        "aliases": ["khanh hoa", "khanhhoa", "nha trang", "nhatrang", "tinh khanh hoa"],
        "districts": [
            {
                "district": "Thành phố Nha Trang",
                "wards": ["Phường Lộc Thọ", "Phường Tân Lập", "Phường Phước Tiến", "Phường Vĩnh Hải", "Phường Vĩnh Nguyên", "Phường Phương Sài"],
                "streets": ["Đường Trần Phú", "Đường Lê Thánh Tôn", "Đường Nguyễn Thiện Thuật", "Đường Hùng Vương", "Đường 2 Tháng 4", "Đường Thái Nguyên"]
            }
        ]
    },

    # 9. THỪA THIÊN HUẾ (HUẾ)
    "thua thien hue": {
        "name": "Thừa Thiên Huế",
        "english_name": "Thua Thien Hue",
        "postal_code": "530000",
        "postal_range": (530000, 540000),
        "aliases": ["thua thien hue", "hue", "tth", "thua thien", "tinh thua thien hue"],
        "districts": [
            {
                "district": "Thành phố Huế",
                "wards": ["Phường Vĩnh Ninh", "Phường Phú Hội", "Phường Phú Nhuận", "Phường Thuận Thành", "Phường Tây Lộc", "Phường Kim Long"],
                "streets": ["Đường Lê Lợi", "Đường Hùng Vương", "Đường Trần Hưng Đạo", "Đường Nguyễn Huệ", "Đường Đống Đa", "Đường Hà Nội"]
            }
        ]
    },

    # 10. BÀ RỊA - VŨNG TÀU
    "ba ria vung tau": {
        "name": "Bà Rịa - Vũng Tàu",
        "english_name": "Ba Ria - Vung Tau",
        "postal_code": "790000",
        "postal_range": (790000, 800000),
        "aliases": ["ba ria vung tau", "vung tau", "vungtau", "ba ria", "baria", "brvt"],
        "districts": [
            {
                "district": "Thành phố Vũng Tàu",
                "wards": ["Phường 1", "Phường 2", "Phường 3", "Phường 7", "Phường 8", "Phường Thắng Tam", "Phường Nguyễn An Ninh"],
                "streets": ["Đường Thùy Vân", "Đường Hạ Long", "Đường Trần Phú", "Đường Lê Hồng Phong", "Đường Ba Cu", "Đường Trương Công Định"]
            },
            {
                "district": "Thành phố Bà Rịa",
                "postal_code": "791000",
                "wards": ["Phường Phước Hưng", "Phường Phước Trung", "Phường Phước Nguyên", "Phường Long Toàn"],
                "streets": ["Đường Bạch Đằng", "Đường Cách Mạng Tháng 8", "Đường Nguyễn Hữu Thọ"]
            }
        ]
    },

    # 11. QUẢNG NINH (HẠ LONG)
    "quang ninh": {
        "name": "Quảng Ninh",
        "english_name": "Quang Ninh",
        "postal_code": "200000",
        "postal_range": (200000, 210000),
        "aliases": ["quang ninh", "quangninh", "ha long", "halong", "tinh quang ninh"],
        "districts": [
            {
                "district": "Thành phố Hạ Long",
                "wards": ["Phường Bãi Cháy", "Phường Hồng Gai", "Phường Bạch Đằng", "Phường Hồng Hải", "Phường Cao Xanh"],
                "streets": ["Đường Hạ Long", "Đường Trần Hưng Đạo", "Đường Lê Thánh Tông", "Đường 25 Tháng 4", "Đường Nguyễn Văn Cừ"]
            }
        ]
    },

    # 12. BẮC NINH
    "bac ninh": {
        "name": "Bắc Ninh",
        "english_name": "Bac Ninh",
        "postal_code": "790000",
        "postal_range": (220000, 230000),
        "aliases": ["bac ninh", "bacninh", "tinh bac ninh"],
        "districts": [
            {
                "district": "Thành phố Bắc Ninh",
                "postal_code": "160000",
                "wards": ["Phường Suối Hoa", "Phường Tiền An", "Phường Ninh Xá", "Phường Vệ An", "Phường Đại Phúc"],
                "streets": ["Đường Trần Hưng Đạo", "Đường Ngô Gia Tự", "Đường Nguyễn Cao", "Đường Huyền Quang"]
            }
        ]
    },

    # 13. LÂM ĐỒNG (ĐÀ LẠT)
    "lam dong": {
        "name": "Lâm Đồng",
        "english_name": "Lam Dong",
        "postal_code": "670000",
        "postal_range": (670000, 680000),
        "aliases": ["lam dong", "lamdong", "da lat", "dalat", "tinh lam dong"],
        "districts": [
            {
                "district": "Thành phố Đà Lạt",
                "wards": ["Phường 1", "Phường 2", "Phường 3", "Phường 4", "Phường 8", "Phường 10"],
                "streets": ["Đường Nguyễn Thị Minh Khai", "Đường Trần Phú", "Đường Phan Đình Phùng", "Đường Bùi Thị Xuân", "Đường Ba Tháng Hai"]
            }
        ]
    },

    # 14. AN GIANG
    "an giang": {
        "name": "An Giang",
        "english_name": "An Giang",
        "postal_code": "880000",
        "postal_range": (880000, 890000),
        "aliases": ["an giang", "angiang", "long xuyen", "chau doc"],
        "districts": [
            {
                "district": "Thành phố Long Xuyên",
                "wards": ["Phường Mỹ Long", "Phường Mỹ Bình", "Phường Mỹ Xuyên", "Phường Mỹ Phước"],
                "streets": ["Đường Trần Hưng Đạo", "Đường Hà Hoàng Hổ", "Đường Lê Lợi", "Đường Thoại Ngọc Hầu"]
            }
        ]
    },

    # 15. KIÊN GIANG (PHÚ QUỐC)
    "kien giang": {
        "name": "Kiên Giang",
        "english_name": "Kien Giang",
        "postal_code": "920000",
        "postal_range": (920000, 930000),
        "aliases": ["kien giang", "kiengiang", "phu quoc", "phuquoc", "rach gia"],
        "districts": [
            {
                "district": "Thành phố Phú Quốc",
                "postal_code": "922000",
                "wards": ["Phường Dương Đông", "Phường An Thới", "Xã Cửa Cạn", "Xã Gành Dầu", "Xã Hàm Ninh"],
                "streets": ["Đường Trần Hưng Đạo", "Đường 30 Tháng 4", "Đường Nguyễn Trung Trực", "Đường Hùng Vương"]
            },
            {
                "district": "Thành phố Rạch Giá",
                "wards": ["Phường Vĩnh Thanh Vân", "Phường Vĩnh Lạc", "Phường Vĩnh Bảo", "Phường An Hòa"],
                "streets": ["Đường Trần Phú", "Đường Nguyễn Trung Trực", "Đường Lâm Quang Ky"]
            }
        ]
    },

    # 16. BÌNH ĐỊNH (QUY NHƠN)
    "binh dinh": {
        "name": "Bình Định",
        "english_name": "Binh Dinh",
        "postal_code": "590000",
        "postal_range": (590000, 600000),
        "aliases": ["binh dinh", "binhdinh", "quy nhon", "quynhon"],
        "districts": [
            {
                "district": "Thành phố Quy Nhơn",
                "wards": ["Phường Lê Lợi", "Phường Trần Phú", "Phường Ngô Mây", "Phường Nguyễn Văn Cừ", "Phường Ghềnh Ráng"],
                "streets": ["Đường Xuân Diệu", "Đường An Dương Vương", "Đường Nguyễn Tất Thành", "Đường Trần Hưng Đạo"]
            }
        ]
    },

    # 17. NGHỆ AN (VINH)
    "nghe an": {
        "name": "Nghệ An",
        "english_name": "Nghe An",
        "postal_code": "460000",
        "postal_range": (460000, 470000),
        "aliases": ["nghe an", "nghean", "vinh", "tp vinh"],
        "districts": [
            {
                "district": "Thành phố Vinh",
                "wards": ["Phường Lê Mao", "Phường Quang Trung", "Phường Hưng Bình", "Phường Trường Thi", "Phường Hà Huy Tập"],
                "streets": ["Đường Lê Lợi", "Đường Quang Trung", "Đường Trần Phú", "Đường Nguyễn Thị Minh Khai"]
            }
        ]
    },

    # 18. THANH HÓA
    "thanh hoa": {
        "name": "Thanh Hóa",
        "english_name": "Thanh Hoa",
        "postal_code": "440000",
        "postal_range": (440000, 450000),
        "aliases": ["thanh hoa", "thanhhoa"],
        "districts": [
            {
                "district": "Thành phố Thanh Hóa",
                "wards": ["Phường Điện Biên", "Phường Ba Đình", "Phường Lam Sơn", "Phường Ngọc Trạo", "Phường Đông Thọ"],
                "streets": ["Đường Trần Phú", "Đường Lê Hoàn", "Đường Quang Trung", "Đường Bà Triệu"]
            }
        ]
    },

    # 19. THÁI NGUYÊN
    "thai nguyen": {
        "name": "Thái Nguyên",
        "english_name": "Thai Nguyen",
        "postal_code": "250000",
        "postal_range": (250000, 260000),
        "aliases": ["thai nguyen", "thainguyen"],
        "districts": [
            {
                "district": "Thành phố Thái Nguyên",
                "wards": ["Phường Phan Đình Phùng", "Phường Trưng Vương", "Phường Hoàng Văn Thụ", "Phường Quang Trung"],
                "streets": ["Đường Hoàng Văn Thụ", "Đường Lương Ngọc Quyến", "Đường Cách Mạng Tháng 8"]
            }
        ]
    },

    # 20. BẮC GIANG
    "bac giang": {
        "name": "Bắc Giang",
        "english_name": "Bac Giang",
        "postal_code": "220000",
        "postal_range": (220000, 230000),
        "aliases": ["bac giang", "bacgiang"],
        "districts": [
            {
                "district": "Thành phố Bắc Giang",
                "wards": ["Phường Ngô Quyền", "Phường Trần Phú", "Phường Lê Lợi", "Phường Hoàng Văn Thụ"],
                "streets": ["Đường Hùng Vương", "Đường Lê Lợi", "Đường Nguyễn Thị Lưu"]
            }
        ]
    },

    # 21. VĨNH PHÚC
    "vinh phuc": {
        "name": "Vĩnh Phúc",
        "english_name": "Vinh Phuc",
        "postal_code": "280000",
        "postal_range": (280000, 290000),
        "aliases": ["vinh phuc", "vinhphuc", "vinh yen"],
        "districts": [
            {
                "district": "Thành phố Vĩnh Yên",
                "wards": ["Phường Ngô Quyền", "Phường Tích Sơn", "Phường Liên Bảo", "Phường Đống Đa"],
                "streets": ["Đường Mê Linh", "Đường Lam Sơn", "Đường Nguyễn Tất Thành"]
            }
        ]
    },

    # 22. HẢI DƯƠNG
    "hai duong": {
        "name": "Hải Dương",
        "english_name": "Hai Duong",
        "postal_code": "170000",
        "postal_range": (170000, 180000),
        "aliases": ["hai duong", "haiduong"],
        "districts": [
            {
                "district": "Thành phố Hải Dương",
                "wards": ["Phường Trần Phú", "Phường Lê Thanh Nghị", "Phường Nguyễn Trãi", "Phường Quang Trung"],
                "streets": ["Đường Bạch Đằng", "Đường Trần Hưng Đạo", "Đường Nguyễn Lương Bằng"]
            }
        ]
    },

    # 23. NAM ĐỊNH
    "nam dinh": {
        "name": "Nam Định",
        "english_name": "Nam Dinh",
        "postal_code": "420000",
        "postal_range": (420000, 430000),
        "aliases": ["nam dinh", "namdinh"],
        "districts": [
            {
                "district": "Thành phố Nam Định",
                "wards": ["Phường Trần Hưng Đạo", "Phường Vị Hoàng", "Phường Phan Đình Phùng", "Phường Cửa Bắc"],
                "streets": ["Đường Trần Hưng Đạo", "Đường Hàng Thao", "Đường Quang Trung", "Đường Lê Hồng Phong"]
            }
        ]
    },

    # 24. THÁI BÌNH
    "thai binh": {
        "name": "Thái Bình",
        "english_name": "Thai Binh",
        "postal_code": "410000",
        "postal_range": (410000, 420000),
        "aliases": ["thai binh", "thaibinh"],
        "districts": [
            {
                "district": "Thành phố Thái Bình",
                "wards": ["Phường Lê Hồng Phong", "Phường Bồ Xuyên", "Phường Đề Thám", "Phường Kỳ Bá"],
                "streets": ["Đường Lê Lợi", "Đường Hai Bà Trưng", "Đường Lý Bôn", "Đường Trần Hưng Đạo"]
            }
        ]
    },

    # 25. TIỀN GIANG (MỸ THO)
    "tien giang": {
        "name": "Tiền Giang",
        "english_name": "Tien Giang",
        "postal_code": "860000",
        "postal_range": (860000, 870000),
        "aliases": ["tien giang", "tiengiang", "my tho", "mytho"],
        "districts": [
            {
                "district": "Thành phố Mỹ Tho",
                "wards": ["Phường 1", "Phường 2", "Phường 4", "Phường 5", "Phường 7"],
                "streets": ["Đường Ấp Bắc", "Đường Hùng Vương", "Đường Lý Thường Kiệt", "Đường Lê Lợi"]
            }
        ]
    },

    # 26. QUẢNG NAM (HỘI AN)
    "quang nam": {
        "name": "Quảng Nam",
        "english_name": "Quang Nam",
        "postal_code": "560000",
        "postal_range": (560000, 570000),
        "aliases": ["quang nam", "quangnam", "hoi an", "hoian", "tam ky"],
        "districts": [
            {
                "district": "Thành phố Hội An",
                "wards": ["Phường Minh An", "Phường Cẩm Phô", "Phường Sơn Phong", "Phường Cẩm Châu", "Phường Cửa Đại"],
                "streets": ["Đường Trần Phú", "Đường Nguyễn Thái Học", "Đường Bạch Đằng", "Đường Cửa Đại", "Đường Hai Bà Trưng"]
            },
            {
                "district": "Thành phố Tam Kỳ",
                "wards": ["Phường An Mỹ", "Phường An Xuân", "Phường Phước Hòa"],
                "streets": ["Đường Phan Bội Châu", "Đường Hùng Vương", "Đường Trần Cao Vân"]
            }
        ]
    },

    # 27. ĐẮK LẮK (BUÔN MA THUỘT)
    "dak lak": {
        "name": "Đắk Lắk",
        "english_name": "Dak Lak",
        "postal_code": "630000",
        "postal_range": (630000, 640000),
        "aliases": ["dak lak", "daklak", "dac lac", "buon ma thuot", "bmt"],
        "districts": [
            {
                "district": "Thành phố Buôn Ma Thuột",
                "wards": ["Phường Thắng Lợi", "Phường Tân Lợi", "Phường Tân An", "Phường Tự An", "Phường Tân Hòa"],
                "streets": ["Đường Lê Duẩn", "Đường Nguyễn Tất Thành", "Đường Phan Chu Trinh", "Đường Y Jut"]
            }
        ]
    }
}

# Daftar seluruh 63 provinsi & kode pos nasional (untuk provinsi lainnya di Vietnam)
ALL_VIETNAM_PROVINCES = [
    {"name": "Hà Nội", "code": "100000", "key": "ha noi"},
    {"name": "Hồ Chí Minh", "code": "700000", "key": "ho chi minh"},
    {"name": "Đà Nẵng", "code": "550000", "key": "da nang"},
    {"name": "Hải Phòng", "code": "180000", "key": "hai phong"},
    {"name": "Cần Thơ", "code": "900000", "key": "can tho"},
    {"name": "An Giang", "code": "880000", "key": "an giang"},
    {"name": "Bà Rịa - Vũng Tàu", "code": "790000", "key": "ba ria vung tau"},
    {"name": "Bắc Giang", "code": "220000", "key": "bac giang"},
    {"name": "Bắc Kạn", "code": "960000", "key": "bac kan"},
    {"name": "Bạc Liêu", "code": "260000", "key": "bac lieu"},
    {"name": "Bắc Ninh", "code": "790000", "key": "bac ninh"},
    {"name": "Bến Tre", "code": "930000", "key": "ben tre"},
    {"name": "Bình Định", "code": "590000", "key": "binh dinh"},
    {"name": "Bình Dương", "code": "820000", "key": "binh duong"},
    {"name": "Bình Phước", "code": "830000", "key": "binh phuoc"},
    {"name": "Bình Thuận", "code": "800000", "key": "binh thuan"},
    {"name": "Cà Mau", "code": "970000", "key": "ca mau"},
    {"name": "Cao Bằng", "code": "270000", "key": "cao bang"},
    {"name": "Đắk Lắk", "code": "630000", "key": "dak lak"},
    {"name": "Đắk Nông", "code": "640000", "key": "dak nong"},
    {"name": "Điện Biên", "code": "380000", "key": "dien bien"},
    {"name": "Đồng Nai", "code": "810000", "key": "dong nai"},
    {"name": "Đồng Tháp", "code": "870000", "key": "dong thap"},
    {"name": "Gia Lai", "code": "600000", "key": "gia lai"},
    {"name": "Hà Giang", "code": "310000", "key": "ha giang"},
    {"name": "Hà Nam", "code": "400000", "key": "ha nam"},
    {"name": "Hà Tĩnh", "code": "480000", "key": "ha tinh"},
    {"name": "Hải Dương", "code": "170000", "key": "hai duong"},
    {"name": "Hậu Giang", "code": "910000", "key": "hau giang"},
    {"name": "Hòa Bình", "code": "350000", "key": "hoa binh"},
    {"name": "Hưng Yên", "code": "160000", "key": "hung yen"},
    {"name": "Khánh Hòa", "code": "650000", "key": "khanh hoa"},
    {"name": "Kiên Giang", "code": "920000", "key": "kien giang"},
    {"name": "Kon Tum", "code": "580000", "key": "kon tum"},
    {"name": "Lai Châu", "code": "390000", "key": "lai chau"},
    {"name": "Lâm Đồng", "code": "670000", "key": "lam dong"},
    {"name": "Lạng Sơn", "code": "240000", "key": "lang son"},
    {"name": "Lào Cai", "code": "330000", "key": "lao cai"},
    {"name": "Long An", "code": "850000", "key": "long an"},
    {"name": "Nam Định", "code": "420000", "key": "nam dinh"},
    {"name": "Nghệ An", "code": "460000", "key": "nghe an"},
    {"name": "Ninh Bình", "code": "430000", "key": "ninh binh"},
    {"name": "Ninh Thuận", "code": "660000", "key": "ninh thuan"},
    {"name": "Phú Thọ", "code": "290000", "key": "phu tho"},
    {"name": "Phú Yên", "code": "620000", "key": "phu yen"},
    {"name": "Quảng Bình", "code": "510000", "key": "quang binh"},
    {"name": "Quảng Nam", "code": "560000", "key": "quang nam"},
    {"name": "Quảng Ngãi", "code": "570000", "key": "quang ngai"},
    {"name": "Quảng Ninh", "code": "200000", "key": "quang ninh"},
    {"name": "Quảng Trị", "code": "520000", "key": "quang tri"},
    {"name": "Sóc Trăng", "code": "950000", "key": "soc trang"},
    {"name": "Sơn La", "code": "360000", "key": "son la"},
    {"name": "Tây Ninh", "code": "840000", "key": "tay ninh"},
    {"name": "Thái Bình", "code": "410000", "key": "thai binh"},
    {"name": "Thái Nguyên", "code": "250000", "key": "thai nguyen"},
    {"name": "Thanh Hóa", "code": "440000", "key": "thanh hoa"},
    {"name": "Thừa Thiên Huế", "code": "530000", "key": "thua thien hue"},
    {"name": "Tiền Giang", "code": "860000", "key": "tien giang"},
    {"name": "Trà Vinh", "code": "940000", "key": "tra vinh"},
    {"name": "Tuyên Quang", "code": "300000", "key": "tuyen quang"},
    {"name": "Vĩnh Long", "code": "890000", "key": "vinh long"},
    {"name": "Vĩnh Phúc", "code": "280000", "key": "vinh phuc"},
    {"name": "Yên Bái", "code": "320000", "key": "yen bai"}
]

# Generic fallback districts, wards, streets for smaller provinces
GENERIC_DISTRICTS = ["Thành phố Trung tâm", "Quận 1", "Quận 2", "Huyện Châu Thành", "Thị xã Trung tâm"]
GENERIC_WARDS = ["Phường 1", "Phường 2", "Phường 3", "Phường Trần Phú", "Phường Lê Lợi", "Phường Quang Trung", "Xã An Bình", "Xã Tân Tiến"]
GENERIC_STREETS = [
    "Đường Hùng Vương", "Đường Trần Hưng Đạo", "Đường Lê Lợi", "Đường Nguyễn Huệ",
    "Đường Quang Trung", "Đường Lý Thường Kiệt", "Đường Phan Chu Trinh", "Đường Hai Bà Trưng",
    "Đường Cách Mạng Tháng 8", "Đường Điện Biên Phủ", "Đường Hoàng Hoa Thám", "Đường Nguyễn Trãi"
]
