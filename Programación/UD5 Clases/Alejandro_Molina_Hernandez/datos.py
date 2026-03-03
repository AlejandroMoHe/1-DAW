from EstudiosAnima import Estudio
from datetime import date


def get_datos(n: int) -> list[Estudio]:
    estudios = [
        [
            Estudio(1, "Walt Disney Pictures", ["Walt Disney", "Roy O. Disney"], date(1923, 10, 16),True ,None, 25800.00, date(2025, 11, 27)),
            Estudio(2, "Warner Bros. Pictures", ["Harry Warner", "Albert Warner", "Sam Warner", "Jack Warner"], date(1923, 4, 4), True, None, 22100.00, date(2025, 7, 12)),
            Estudio(3, "Universal Pictures", ["Carl Laemmle"], date(1912, 4, 30), True, None, 20300.00, date(2025, 6, 14)),
            Estudio(4, "Paramount Pictures", ["Adolph Zukor", "Jesse L. Lasky", "Cecil B. DeMille"], date(1912, 5, 8), True, None, 16600.00, date(2024, 12, 20)),
            Estudio(5, "Sony Pictures Entertainment", ["Akio Morita", "Masaru Ibuka"], date(1987, 11, 18), True, None, 18400.00, date(2025, 9, 5)),
            Estudio(6, "20th Century Studios", ["William Fox", "Darryl F. Zanuck"], date(1935, 5, 31), True, None, 15700.00, date(2025, 3, 21)),
            Estudio(7, "Columbia Pictures", ["Harry Cohn", "Jack Cohn", "Joe Brandt"], date(1924, 1, 10), True, None, 13800.00, date(2024, 8, 2)),
            Estudio(8, "Metro-Goldwyn-Mayer (MGM)", ["Marcus Loew"], date(1924, 4, 17), True, None, 11000.00, date(2024, 11, 15)),
            Estudio(9, "Pixar Animation Studios", ["Edwin Catmull", "Alvy Ray Smith", "Steve Jobs"], date(1986, 2, 3), True, None, 12900.00, date(2025, 6, 19)),
            Estudio(10, "DreamWorks Pictures", ["Steven Spielberg", "Jeffrey Katzenberg", "David Geffen"], date(1994, 10, 12), True, None, 12000.00, date(2024, 10, 30)),
        ],
        [
            Estudio(1, "Toho Co., Ltd.", ["Ichizō Kobayashi"], date(1932, 8, 12), True, None, 2150.00, date(2025, 7, 19)),
            Estudio(2, "Toei Company, Ltd.", ["Keita Goto"], date(1951, 4, 1), True, None, 950.00, date(2024, 12, 7)),
            Estudio(3, "Shochiku Co., Ltd.", ["Takejirō Ōtani", "Matsujirō Shirai"], date(1895, 1, 1), True, None, 45.00, date(2024, 10, 3)),
            Estudio(4, "Studio Ghibli", ["Hayao Miyazaki", "Isao Takahata", "Toshio Suzuki"], date(1985, 6, 15), True, None, 300.00, date(2023, 7, 14)),
            Estudio(5, "Sunrise (Bandai Namco Filmworks)", ["Yoshiyuki Tomino", "Hajime Yatate"], date(1972, 9, 1), True, None, 600.00, date(2024, 5, 22)),
            Estudio(6, "China Film Group Corporation", ["Gobierno de China"], date(1999, 2, 1), True, None, 3500.00, date(2025, 2, 10)),
            Estudio(7, "Huayi Brothers Media", ["Wang Zhongjun", "Wang Zhonglei"], date(1994, 1, 1), True, None, 400.00, date(2024, 9, 18)),
            Estudio(8, "Beijing Enlight Media", ["Wang Changtian"], date(1998, 1, 1), True, None, 900.00, date(2024, 8, 9)),
            Estudio(9, "Universal Pictures Japan", ["Comcast", "NBCUniversal"], date(2001, 3, 31), True, None, 700.00, date(2025, 6, 14)),
            Estudio(10, "Toho-Towa", ["Ichizō Kobayashi"], date(1928, 1, 1), True, None, 250.00, date(2024, 11, 2)),
        ]
    ]

    if n == 0:
        return estudios[0]
    elif n == 1:
        return estudios[1]


