from datetime import datetime, timedelta

def generate_monthly_bill(item_list, target_month):
    bill = {
        "line_items": [],
        "total_revenue": 0
    }

    
    year, month = map(int, target_month.split('-'))
    month_start = datetime(year, month, 1)
    if month == 12:
        month_end = datetime(year + 1, 1, 1) - timedelta(days=1)
    else:
        month_end = datetime(year, month + 1, 1) - timedelta(days=1)
    total_days = (month_end - month_start).days + 1

    for item in item_list:

        
        if 'start_date' not in item or 'stop_date' not in item or 'item_code' not in item:
            continue

       
        start = datetime.strptime(item['start_date'], '%Y-%m-%d')
        end = datetime.strptime(item['stop_date'], '%Y-%m-%d')
        qty = int(item['qty'])
        rate = float(item['rate'])

       
        if start > month_end or end < month_start:
            continue

        
        active_start = max(start, month_start)
        active_end = min(end, month_end)
        active_days = (active_end - active_start).days + 1

        
        amount = round(qty * rate * (active_days / total_days), 2)
        billing_period = f"{active_start.strftime('%Y-%m-%d')} to {active_end.strftime('%Y-%m-%d')}"

       
        found = False
        for line in bill["line_items"]:
            if line['item_code'] == item['item_code'] and line['rate'] == rate and line['billing_period'] == billing_period:
                line['qty'] += qty
                line['amount'] += amount
                found = True
                break

        
        if not found:
            bill['line_items'].append({
                'item_code': item['item_code'],
                'rate': rate,
                'qty': qty,
                'amount': amount,
                'billing_period': billing_period
            })

        
        bill['total_revenue'] += amount

    return bill


# sample
items = [
    {
        "item_code": "ITEM001",
        "start_date": "2024-10-15",
        "stop_date": "2024-11-15",
        "qty": 10,
        "rate": 5.0
    },
    {
        "item_code": "ITEM002",
        "start_date": "2024-11-01",
        "stop_date": "2024-11-30",
        "qty": 2,
        "rate": 100.0
    },
    {
        "item_code": "ITEM001",
        "start_date": "2024-11-10",
        "stop_date": "2024-11-25",
        "qty": 5,
        "rate": 5.0
    },
    {
        "item_code": "ITEM003",
        "start_date": "2024-12-01",
        "stop_date": "2024-12-31",
        "qty": 1,
        "rate": 50.0
    }
]

month = "2024-11"

result = generate_monthly_bill(items, month)
print(result)
