import math

def first(a,b,c,d,e,f,g,h):
    b=b-1 if a==5 else b-2
    capacity=c*pow(2,30)
    stripes_units=capacity/(e*d)
    blocks=capacity/d
    calculate=h*stripes_units
    read=blocks*f*b
    write=g*blocks
    ans=(calculate+read+write)/(pow(10,6)*60)
    return f'Первое задание {int(ans)}'
def second(pointers, pointer_bit , block_size, file_size):
    file_blocks = math.ceil(file_size / block_size)
    pointer_byte = pointer_bit / 8
    pointers_in_block = math.floor(block_size / pointer_byte)

    result = file_blocks

    first_level = -1
    second_level = -1
    third_level = -1

    if file_blocks % (pointers_in_block * pointers_in_block) > 0:
        third_level = math.floor(file_blocks / (pointers_in_block * pointers_in_block))
        file_blocks -= third_level * pointers_in_block * pointers_in_block

    if file_blocks % pointers_in_block > 0:
        second_level = math.floor(file_blocks / (pointers_in_block))
        file_blocks -= second_level * pointers_in_block

    if file_blocks < pointers_in_block and file_blocks > pointers:
        first_level = file_blocks

    result += 0 if first_level == -1 else 1
    result += 0 if second_level == -1 else 1 + second_level
    result += 0 if third_level == -1 else 1 + third_level + third_level * pointers_in_block

    print(result)




def third(byte, sector, track, surface, records, byte_rec):
    byte_track = byte * sector
    byte_surface = byte_track * track
    byte_disk = byte_surface * surface
    file_size = records * byte_rec
    print(f'1 сектор: {byte} байт')
    print(f'1 дорожка: {byte} * {sector} = {byte_track} байт')
    print(f'1 поверхность: {track} * {byte_track} = {byte_surface} байт')
    print(f'1 диск: {surface} * {byte_surface} = {byte_disk} байт')
    print(f'Размер файла: {records} * {byte_rec} = {file_size} байт')

    records_in_one_sector = int(byte / byte_rec)

    # Количество секторов для файла:
    sectors_for_file = int(records / records_in_one_sector) + 1 if (records / records_in_one_sector) != int(
        records / records_in_one_sector) else int(records / records_in_one_sector)

    # Количество дорожек для файла:
    tracks_for_file = int(sectors_for_file / sector) + 1 if int(
        sectors_for_file / sector) != sectors_for_file / sector else int(sectors_for_file / sector)

    # Количество секторов в последней дорожке:
    sectors_on_last_track = sectors_for_file - int(sectors_for_file / sector) * sector

    # Какое полное количество байт (включая потери фрагментации) займет файл?
    real_size_file = sectors_for_file * byte



    print('\nРешение 1:')
    print(f'Какое общее количество секторов необходимо для хранения всех записей? Ответ: {sectors_for_file}')

    print('\nРешение 2:')
    print(f'Какой общее количество дорожек необходимо для хранения всех записей? Ответ: {tracks_for_file}')

    print('\nРешение 3:')
    print(f'Какое полное количество байт (включая потери фрагментации) займет файл? Ответ: {real_size_file}')

    print('\nРешение 4:')
    print(f'Сколько секторов будет занято на последней дорожке файла? Ответ: {sectors_on_last_track}')

def fifth(a,b,c,d,e,f,g,h):

    '''
    Вы уверены, что вопрос звучит так?
    На сколько уменьшится время работы программы, если
    1) данные локального узла попадут в кэш
    2) ОС перенесет удаленную память в память локального кэша
    '''
    AGREEMENT = True

    assert AGREEMENT == True, 'До свидания'

    reg_speed = 1 / a

    before = reg_speed * e + b * f + c * g + d * h

    f += g
    g = h
    h = 0

    after = reg_speed * e + b * f + c * g + d * h

    answer = before - after

    print(answer, '[нс]')

