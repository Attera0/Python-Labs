import sys

from mod_variant import calculate_shift_consumption, get_peak_hours


def main():
    # Чтение лимита из консоли.
    if len(sys.argv) > 1:
        peak_limit = float(sys.argv[0])
    

    # Исходный суточный профиль потребления (24 часа)
    hourly_power = [
        150, 140, 130, 140, 160, 200, 350, 420,
        450, 480, 460, 430, 410, 440, 470, 490,
        420, 380, 300, 250, 210, 180, 160, 150
    ]

    # Расчет и вывод результатов
    s1, s2, s3 = calculate_shift_consumption(hourly_power)
    
    print("=== АУДИТ ЭЛЕКТРОПОТРЕБЛЕНИЯ ===")
    print("Потребление по сменам:")
    print(f"  - Смена 1 (Ночь): {s1} кВт*ч")
    print(f"  - Смена 2 (День): {s2} кВт*ч")
    print(f"  - Смена 3 (Вечер): {s3} кВт*ч")
    
    # Считаем пиковые часы в отдельную переменную
    peaks = get_peak_hours(hourly_power, peak_limit)
    print(f"Пиковые часы (>{(peak_limit)} кВт): {peaks}")


if __name__ == '__main__':
    main()
