import sqlite3 as sq

def sql_start():
    global base, cur
    base = sq.connect('base1.db')
    cur = base.cursor()
    if base:
        print('Data base connected')
    else:
        print('База пішла по пизді')
    base.execute('CREATE TABLE IF NOT EXISTS menu(id TEXT, dm TEXT, vm TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()
        print('Success commit')

# async def sql_add_dm():
#     cur.execute('INSERT INTO menu(dm TEXT) VALUES (?)', message.text)
