import pygame
import random
import modules.data_base as m_data
import modules.ships as m_ships

def place():
    test = 0
    while test < 1:
        target = random.randint(0, 99)
        test1 = 1
        rotate = random.randint(0, 3) * 90
        if rotate % 180 == 0:

            for count in range(4):
                if target + count > 99 or m_data.list_map2[target + count].NAME != 0 or m_data.list_map2[target + count].ROW != m_data.list_map2[target].ROW:
                    test1 = 0
        else:
            for count in range(4):
                if target + count * 10 > 99 or m_data.list_map2[target + count * 10].NAME != 0:
                    test1 = 0
        
        if test1:
            if rotate % 180 == 0:
                
                m_data.list_map2[target].NAME = 4
                m_data.list_map2[target + 1].NAME = 4
                m_data.list_map2[target + 1 + 1].NAME = 4
                m_data.list_map2[target + 1 + 1 + 1].NAME = 4
                m_data.list_map2[target].block_cells(m_data.list_map2, target)
                m_data.list_map2[target + 1].block_cells(m_data.list_map2, target + 1)
                m_data.list_map2[target + 1 + 1].block_cells(m_data.list_map2, target + 1 + 1)
                m_data.list_map2[target + 1 + 1 + 1].block_cells(m_data.list_map2, target + 1 + 1 + 1)
            else:
                m_data.list_map2[target].NAME = 4
                m_data.list_map2[target + 1 * 10].NAME = 4
                m_data.list_map2[target + 2 * 10].NAME = 4
                m_data.list_map2[target + 3 * 10].NAME = 4
                m_data.list_map2[target].block_cells(m_data.list_map2, target)
                m_data.list_map2[target + 1 * 10].block_cells(m_data.list_map2, target + 1 * 10)
                m_data.list_map2[target + 2 * 10].block_cells(m_data.list_map2, target + 2 * 10)
                m_data.list_map2[target + 3 * 10].block_cells(m_data.list_map2, target + 3 * 10)
            test += 1
            m_data.enemy_ships.append((m_data.list_map2[target].X1, m_data.list_map2[target].Y1,rotate, target))

    test = 0  
    while test < 2:
        target = random.randint(0, 99)
        test1 = 1
        rotate = random.randint(0, 3) * 90
        if rotate % 180 == 0:
            for count in range(3):
                if target + count > 99 or m_data.list_map2[target + count].NAME != 0 or m_data.list_map2[target + count].ROW != m_data.list_map2[target].ROW:
                    test1 = 0
        else:
            for count in range(3):
                if target + count * 10 > 99 or m_data.list_map2[target + count * 10].NAME != 0:
                    test1 = 0
        if test1:
            if rotate % 180 == 0:
                m_data.list_map2[target].NAME = 3
                m_data.list_map2[target + 1].NAME = 3
                m_data.list_map2[target + 1 + 1].NAME = 3
                m_data.list_map2[target].block_cells(m_data.list_map2, target)
                m_data.list_map2[target + 1].block_cells(m_data.list_map2, target + 1)
                m_data.list_map2[target + 1 + 1].block_cells(m_data.list_map2, target + 1 + 1) 
            else:
                m_data.list_map2[target].NAME = 3
                m_data.list_map2[target + 1 * 10].NAME = 3
                m_data.list_map2[target + 2 * 10].NAME = 3
                m_data.list_map2[target].block_cells(m_data.list_map2, target)
                m_data.list_map2[target + 1 * 10].block_cells(m_data.list_map2, target + 1 * 10)
                m_data.list_map2[target + 2 * 10].block_cells(m_data.list_map2, target + 2 * 10) 
            
            test += 1
            m_data.enemy_ships[2].append((m_data.list_map2[target].X1, m_data.list_map2[target].Y1, rotate, target))

    test = 0
    while test < 3:
        target = random.randint(0, 99)
        test1 = 1
        rotate = random.randint(0, 3) * 90
        if not rotate % 180:
            for count in range(2): 
                if target + count > 99 or m_data.list_map2[target + count].NAME != 0 or m_data.list_map2[target + count].ROW != m_data.list_map2[target].ROW:
                    test1 = 0 
        else:
             for count in range(2): 
                if target + count * 10 > 99 or m_data.list_map2[target + count * 10].NAME != 0:
                    test1 = 0 
                        
        if test1:
            m_data.list_map2[target].NAME = 2
            if rotate % 180 < 2:
                m_data.list_map2[target + 1].NAME = 2
                test += 1
                m_data.list_map2[target].block_cells(m_data.list_map2, target)
                m_data.list_map2[target + 1].block_cells(m_data.list_map2, target + 1)
                # m_data.enemy_ships[1].append((m_data.list_map2[target].X1, m_data.list_map2[target].Y1, rotate))
            else:
                m_data.list_map2[target + 10].NAME = 2
                test += 1
                m_data.list_map2[target].block_cells(m_data.list_map2, target)
                m_data.list_map2[target + 10].block_cells(m_data.list_map2, target + 10)
            m_data.enemy_ships[1].append((m_data.list_map2[target].X1, m_data.list_map2[target].Y1, rotate, target))  
    test = 0
    while test < 4:
        target = random.randint(0, 99)
        rotate = random.randint(0, 3)
        #print(1)
        if m_data.list_map2[target].NAME == 0:
            m_data.list_map2[target].NAME = 1
            test += 1
            m_data.list_map2[target].block_cells(m_data.list_map2, target)
            m_data.enemy_ships[0].append((m_data.list_map2[target].X1, m_data.list_map2[target].Y1, rotate * 90, target))
# place()

def attack2(target1, check = 1):
    pe = 1
    
    if m_data.hit1 and check:
        attack2(m_data.last_attack1, 0)
    else:
        target = 0
        target += target1
        #print()
        if target - 1 > -1 and m_data.list_map1 [target - 1].ATTACKED == 0 and m_data.list_map1[target - 1].ROW == m_data.list_map1[target].ROW and m_data.rotate == 0:
            target -= 1
        elif target + 1 < 100 and m_data.list_map1 [target + 1].ATTACKED == 0 and m_data.list_map1[target + 1].ROW == m_data.list_map1[target].ROW and m_data.rotate == 1:
            target += 1
        elif target - 10 > -1 and m_data.list_map1 [target - 10].ATTACKED == 0 and m_data.list_map1[target - 10].ROW == m_data.list_map1[target].ROW - 1 and m_data.rotate == 2: 
            target -= 10
        elif target + 10 < 100 and m_data.list_map1 [target + 10].ATTACKED == 0 and m_data.list_map1[target + 10].ROW == m_data.list_map1[target].ROW + 1 and m_data.rotate == 3:
            target += 10
        
        else:
            pe = 0
            if m_data.hit1:
                m_data.hit = 0
                m_data.hit1 = 0
                m_data.hit2 = 0
                #print(-112, m_data.last_attack, m_data.last_attack1, m_data.rotate)
                #print(target + 10 , m_data.list_map1[target + 10].ATTACKED, 0, m_data.list_map1[target + 10].ROW, m_data.list_map1[target].ROW + 1)
            else:
                m_data.hit1 = 1
                if m_data.rotate == 2:
                    m_data.rotate = 3
                elif m_data.rotate == 3:
                    m_data.rotate = 2
                else: 
                    m_data.rotate = not m_data.rotate
                    
        if m_data.list_map1[target].ATTACKED == 0:
            if m_data.list_map1[target].NAME == 0 or m_data.list_map1[target].NAME == 5:
                m_data.turn = 0
                if m_data.hit1:
                    m_data.hit = 0
                    m_data.hit1 = 0
                    m_data.hit2 = 0
                    #print(117)
                else:
                    m_data.hit1 = 1
                    if m_data.rotate == 2:
                        m_data.rotate = 3
                    elif m_data.rotate == 3:
                        m_data.rotate = 2
                    else:
                        m_data.rotate = not m_data.rotate
            else:

                if m_data.hit1:
                    m_data.last_attack1 = target
                else:
                    m_data.last_attack = target
            m_data.list_map1[target].ATTACKED = 1
    
def attack1(target, check = 1):
    rotate = 0
    if m_data.hit2 and check:
        attack2(m_data.last_attack, 1)
    else:
        m_data.hit1 = 0
        if target > 0 and m_data.list_map1 [target - 1].ATTACKED == 0 and m_data.list_map1[target - 1].ROW == m_data.list_map1[target].ROW:
            target -= 1
            rotate = 0
        elif target < 99 and m_data.list_map1 [target + 1].ATTACKED == 0 and m_data.list_map1[target + 1].ROW == m_data.list_map1[target].ROW:
            target += 1
            rotate = 1
        elif target > 10 and m_data.list_map1 [target - 10].ATTACKED == 0 and m_data.list_map1[target - 10].ROW == m_data.list_map1[target].ROW - 1:
            target -= 10
            rotate = 2
        elif target < 90 and m_data.list_map1 [target + 10].ATTACKED == 0 and m_data.list_map1[target + 10].ROW == m_data.list_map1[target].ROW + 1:
            target += 10
            rotate = 3 
        
        else:
           m_data.hit = 0
        if m_data.list_map1[target].ATTACKED == 0:
            if m_data.list_map1[target].NAME == 0 or m_data.list_map1[target].NAME == 5:
                m_data.turn = 0
            else:
                m_data.rotate = rotate
                m_data.hit2 = 1
                
                m_data.last_attack = target
            m_data.list_map1[target].ATTACKED = 1
    
def attack():
    if m_data.hit == 1:
        attack1(m_data.last_attack)
    else:
        
        while True:
            target = random.randint(0, 99)
            if  not m_data.list_map1[target].ATTACKED:
                m_data.list_map1[target].ATTACKED  = 1
                if m_data.list_map1[target].NAME == 0 or m_data.list_map1[target].NAME == 5:
                    m_data.turn = 0

                else:
                    m_data.hit = 1
                    m_data.last_attack = target
                    m_data.last_attack1 = target
                    
                break

        