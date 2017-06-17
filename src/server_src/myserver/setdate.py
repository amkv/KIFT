from time import strftime

def set_date():
    date = strftime(" %m %d %Y").strip()
    date = date.split(' ')
    if '01' in date[0]:
        date[0] = 'January'
    elif '02' in date[0]:
        date[0] = 'February'
    elif '03' in date[0]:
        date[0] = 'March'
    elif '04' in date[0]:
        date[0] = 'April'
    elif '05' in date[0]:
        date[0] = 'May'
    elif '06' in date[0]:
        date[0] = 'June'
    elif '07' in date[0]:
        date[0] = 'July'
    elif '08' in date[0]:
        date[0] = 'August'
    elif '09' in date[0]:
        date[0] = 'September'
    elif '10' in date[0]:
        date[0] = 'October'
    elif '11' in date[0]:
        date[0] = 'November'
    elif '12' in date[0]:
        date[0] = 'December'
    return ' '.join(date)
