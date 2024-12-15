import sqlite3

def create_db():
    # Connexion à la base de données (elle sera créée si elle n'existe pas)
    conn = sqlite3.connect('bdd/database.db')
    c = conn.cursor()
    
    # Création de la table des rendez-vous
    c.execute('''
    CREATE TABLE IF NOT EXISTS rendezvous (
        id INTEGER PRIMARY KEY, 
        phone TEXT,
        user_name TEXT, 
        date TEXT, 
        time TEXT,
        service TEXT,
        doctor TEXT
    )
    ''')

    c.execute('''
                  CREATE TABLE IF NOT EXISTS horaires_visite (
        id INTEGER PRIMARY KEY, 
        phone TEXT,
        user_name TEXT,
        date TEXT,
        start_time TEXT,
        end_time TEXT
    )
    ''')
    

    conn.commit()
    conn.close()

create_db()

def add_rendezvous(phone, name, date, time, department, doctor):
    try:
        conn = sqlite3.connect('bdd/database.db')
        c = conn.cursor()
        
        c.execute('''
        INSERT INTO rendezvous (phone, user_name, date, time,service, doctor)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (phone, name, date, time, department, doctor))
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Une erreur s'est produite : {e}")
    finally:
        if conn:
            conn.close()

def add_horaire_visite(phone, name, date, start_time, end_time):
    try:
        conn = sqlite3.connect('bdd/database.db')
        c = conn.cursor()
        
        c.execute('''
        INSERT INTO horaires_visite (phone, user_name, date, start_time, end_time)
        VALUES (?, ?, ?, ?, ?)
        ''', (phone, name, date, start_time, end_time))
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Une erreur s'est produite : {e}")
    finally:
        if conn:
            conn.close()

def get_rendezvous(user_name):
    conn = sqlite3.connect('bdd/database.db')
    c = conn.cursor()
    
    # Sélectionner le rendez-vous de l'utilisateur
    c.execute('''
    SELECT date, time FROM rendezvous WHERE user_name = ?
    ''', (user_name,))
    
    result = c.fetchone()
    conn.close()
    
    return result

def get_horaire_visite(user_name):
    try:
        conn = sqlite3.connect('bdd/database.db')
        c = conn.cursor()
        
        # Sélectionner l'horaire de visite de l'utilisateur
        c.execute('''
        SELECT date, start_time, end_time FROM horaires_visite WHERE user_name = ?
        ''', (user_name,))
        
        result = c.fetchall()
    except sqlite3.Error as e:
        print(f"Une erreur s'est produite : {e}")
        result = []
    finally:
        if conn:
            conn.close()
    
    return result

# Appels de fonctions
add_rendezvous('0748989898','Jean Dupont', '2021-12-25', '15:00', 'Cardiologie', 'Dr. Martin')
add_horaire_visite('0748989898','Jean Dupont', '2021-12-25', '09:00', '12:00')
add_horaire_visite('0748989898','Jean Dupont', '2021-12-25', '14:00', '18:00')

add_rendezvous('0748989898','Yannick Claire', '2021-12-25', '16:00', 'Consultation', 'Dr. Bertrand')
add_horaire_visite('0748989898','Yannick Claire', '2021-12-25', '09:00', '12:00')
add_horaire_visite('0748989898','Yannick Claire', '2021-12-25', '14:00', '18:00')

add_rendezvous('0748989898','Marie Durand', '2021-12-25', '17:00', 'Radiologie', 'Dr. Simon')
add_horaire_visite('0748989898','Marie Durand', '2021-12-25', '09:00', '12:00')
add_horaire_visite('0748989898','Marie Durand', '2021-12-25', '14:00', '18:00')

add_rendezvous('0748989898','Jean Jacques', '2021-12-25', '18:00', 'Pédiatrie', 'Dr. Jules')
add_horaire_visite('0748989898','Jean Jacques', '2021-12-25', '09:00', '12:00')
add_horaire_visite('0748989898','Jean Jacques', '2021-12-25', '14:00', '18:00')
