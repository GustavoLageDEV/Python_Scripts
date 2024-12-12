#Email Generator

import csv, random
domain = "example.com"

def generate_email(name, email_counts):
    name_parts = name.lower().split()
    if len(name_parts) >= 2:
        first_name = name_parts[0]
        last_name = name_parts[-1]
        email_base = f"{first_name}.{last_name}"
    else:
        email_base = name_parts[0]
            
    # Substitui caracteres especiais e acentuação
    email_base = ''.join(char for char in email_base if char.isalnum() or char == '.')
    
    # Gerencia duplicatas
    if email_base in email_counts:
        email_counts[email_base] += 1
        email = f"{email_base}{email_counts[email_base]}@{domain}"
    else:
        email_counts[email_base] = 1
        email = f"{email_base}@{domain}"
    
    return email

if __name__ == "__main__":

    email_counts = {}
    domains_list = ("hotmail.com","gmail.com","outlook.com","yahoo.com","mail.ru")
    users_updated = []

    with open(r"C:\Users\Gustavo Lage\Desktop\ESTUDO\Portifólio_Scripts\Mylibrary_project\csv_files\users.csv", mode='r', encoding = 'utf-8') as data:
        csv_data = csv.reader(data)
        data_lines = list(csv_data)

        for row in data_lines[1:]:
            domain = domains_list[random.randint(0,4)]
            name = row[1]
            row[2] = generate_email(name, email_counts)

    with open(r"C:\Users\Gustavo Lage\Desktop\ESTUDO\Portifólio_Scripts\Mylibrary_project\csv_files\users_updated.csv", mode='w',newline='', encoding = 'utf-8') as updated_data:
        
        csv_updated_data = csv.writer(updated_data)
        csv_updated_data.writerows(data_lines)