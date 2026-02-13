from EstudiosAnima import Estudio
from datetime import datetime


def get_datos(n: int) -> list[Estudio]:
    pass

estudios_occidente = [
    Estudio(1, "Walt Disney Pictures", ["Walt Disney", "Roy O. Disney"], datetime(1923, 10, 16), True, 28.00, datetime(2025, 11, 27)),
    Estudio(2, "Warner Bros. Pictures", ["Harry Warner", "Albert Warner", "Sam Warner", "Jack Warner"], datetime(1923, 4, 4), True, 24.00, datetime(2025, 7, 12)),
    Estudio(3, "Universal Pictures", ["Carl Laemmle"], datetime(1912, 4, 30), True, 22000.00, datetime(2025, 6, 14)),
    Estudio(4, "Paramount Pictures", ["Adolph Zukor", "Jesse L. Lasky", "Cecil B. DeMille"], datetime(1912, 5, 8), True, 18.00, datetime(2024, 12, 20)),
    Estudio(5, "Sony Pictures Entertainment", ["Akio Morita", "Masaru Ibuka"], datetime(1987, 11, 18), True, 20.00, datetime(2025, 9, 5)),
    Estudio(6, "20th Century Studios", ["William Fox", "Darryl F. Zanuck"], datetime(1935, 5, 31), True, 17.00, datetime(2025, 3, 21)),
    Estudio(7, "Columbia Pictures", ["Harry Cohn", "Jack Cohn", "Joe Brandt"], datetime(1924, 1, 10), True, 15.00, datetime(2024, 8, 2)),
    Estudio(8, "Metro-Goldwyn-Mayer (MGM)", ["Marcus Loew"], datetime(1924, 4, 17), True, 12.00, datetime(2024, 11, 15)),
    Estudio(9, "Pixar Animation Studios", ["Edwin Catmull", "Alvy Ray Smith", "Steve Jobs"], datetime(1986, 2, 3), True, 14.00, datetime(2025, 6, 19)),
    Estudio(10, "DreamWorks Pictures", ["Steven Spielberg", "Jeffrey Katzenberg", "David Geffen"], datetime(1994, 10, 12), True, 13.00, datetime(2024, 10, 30)),
]

estudios_oriente = [
    Estudio(1, "Toho Co., Ltd.", ["Ichizō Kobayashi"], datetime(1932, 8, 12), True, 6500.00, datetime(2025, 7, 19)),
    Estudio(2, "Toei Company, Ltd.", ["Keita Goto"], datetime(1951, 4, 1), True, 4200.00, datetime(2024, 12, 7)),
    Estudio(3, "Shochiku Co., Ltd.", ["Takejirō Ōtani", "Matsujirō Shirai"], datetime(1895, 1, 1), True, 3800.00, datetime(2024, 10, 3)),
    Estudio(4, "Studio Ghibli", ["Hayao Miyazaki", "Isao Takahata", "Toshio Suzuki"], datetime(1985, 6, 15), True, 3100.00, datetime(2023, 7, 14)),
    Estudio(5, "Sunrise (Bandai Namco Filmworks)", ["Yoshiyuki Tomino", "Hajime Yatate"], datetime(1972, 9, 1), True, 2900.00, datetime(2024, 5, 22)),
    Estudio(6, "China Film Group Corporation", ["Gobierno de China"], datetime(1999, 2, 1), True, 8500.00, datetime(2025, 2, 10)),
    Estudio(7, "Huayi Brothers Media", ["Wang Zhongjun", "Wang Zhonglei"], datetime(1994, 1, 1), True, 2600.00, datetime(2024, 9, 18)),
    Estudio(8, "Beijing Enlight Media", ["Wang Changtian"], datetime(1998, 1, 1), True, 2400.00, datetime(2024, 8, 9)),
    Estudio(9, "Universal Pictures Japan", ["Comcast", "NBCUniversal"], datetime(2001, 3, 31), True, 570.00, datetime(2025, 6, 14)),
    Estudio(10, "Toho-Towa", ["Ichizō Kobayashi"], datetime(1928, 1, 1), True, 2100.00, datetime(2024, 11, 2)),
]

get_datos(0)

