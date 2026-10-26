

def calculate_shift_consumption(hourly_power):
    #Считает расход электроэнергии суммарно по трем 8-часовым сменам.
    return sum(hourly_power[0:8]), sum(hourly_power[8:16]), sum(hourly_power[16:24])

def get_peak_hours(hourly_power, peak_level):
    #Возвращает список часов, когда мощность превышала лимит.
    return [hr for hr, pwr in enumerate(hourly_power) if pwr > peak_level]

