import modules.data_base as m_data
import modules.restart as m_restart

def win_lose(map):
    check = 1
    for cell in map:
        if cell.NAME != 0 and cell.NAME != 5:
            if cell.ATTACKED == 0:
                check = 0
    return check


