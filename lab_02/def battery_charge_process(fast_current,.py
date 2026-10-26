
def battery_charge_process(fast_current, capacity=100):
    current_charge = 0.0
    total_time = 0
    fast_limit = capacity * 0.8
    
    # Этап 1: Быстрый заряд (0-80%)
    while current_charge < fast_limit:
        current_charge += fast_current
        total_time += 1
             
    # Этап 2: Капельный заряд (80-100%)
    drip_current = 0.2 * fast_current
    while current_charge < capacity:
        current_charge += drip_current
        total_time += 1
        
    return total_time

# Вызов функции
time_spent = battery_charge_process(13)
print("Общее время заряда:", time_spent, "минут")

