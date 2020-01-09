from pynput import keyboard

# The key combination to check
COMBINATIONS = [{'comb1': [keyboard.Key.shift_l, keyboard.Key.enter]},
                {'comb2': [keyboard.Key.shift_r, keyboard.Key.enter]},
                {'comb3': [keyboard.Key.shift_l]},
                {'comb4': [keyboard.Key.alt_l]}]

# 현재 입력받은 키
currentValue = []

# # DB읽어오기
# f = open("./setting/pero_setting_data/gesture3.txt", "r")
# linear3 = f.read()
# f = open("./setting/pero_setting_data/gesture4.txt", "r")
# linear4 = f.read()
# f = open("./setting/pero_setting_data/pero_state.txt", "r")
# pero_state = f.read()
# f = open("./setting/pero_setting_data/default.txt", "rt", encoding="UTF-8")
# default_context = f.read()
# default = default_context.split("\n")
# f.close()
#
# # 세팅
# setting_db = {}
# default_db = {}
#
# linear3_split = linear3.split(":")
# if linear3_split[1] == "시작화면 열기(Default)":
#     setting_db.update({linear3_split[0]: "windows_start"})
# elif linear3_split[1] == "윈도우 작업 보기":
#     setting_db.update({linear3_split[0]: "windows_process"})
# elif linear3_split[1] == "윈도우 검색 창 실행":
#     setting_db.update({linear3_split[0]: "windows_search"})
#
# linear4_split = linear4.split(":")
# if linear4_split[1] == "모든창 최소화(Default)":
#     setting_db.update({linear4_split[0]: "windows_minimize"})
# elif linear4_split[1] == "돋보기 실행":
#     setting_db.update({linear4_split[0]: "windows_zoom"})
# elif linear4_split[1] == "탐색기 실행":
#     setting_db.update({linear4_split[0]: "windows_explorer"})
#
#
# for i in range(2):
#     default_element = default[i].split(":")
#     if default_element[1] == "시작화면 열기(Default)":
#         default_db.update({default_element[0]: "windows_start"})
#     elif default_element[1] == "모든창 최소화(Default)":
#         default_db.update({default_element[0]: "windows_minimize"})

# print(setting_db)
# print(default_db)
# print(pero_state)

keyAction = keyboard.Controller()


# 키보드 에러 핸들링
class MyException(Exception):
    pass


def new_tab():
    currentValue.clear()

    print("new tab")
    keyAction.release(keyboard.Key.shift)

    with keyAction.pressed(keyboard.Key.ctrl):
        keyAction.press('t')
        keyAction.release('t')


def new_window():
    currentValue.clear()

    print("new window")
    keyAction.release(keyboard.Key.shift)

    with keyAction.pressed(keyboard.Key.ctrl):
        keyAction.press('n')
        keyAction.release('n')


def zoom_in():
    currentValue.clear()
    keyAction.release(keyboard.Key.shift)

    print("zoom in")
    with keyAction.pressed(keyboard.Key.ctrl):
        keyAction.press('＝')
        keyAction.release('＝')


def reading():
    currentValue.clear()

    print("reading")
    keyAction.release(keyboard.Key.shift)

    keyAction.press(keyboard.Key.ctrl)
    keyAction.press(keyboard.Key.shift_l)
    keyAction.press('g')
    keyAction.release('g')
    keyAction.release(keyboard.Key.shift_l)
    keyAction.release(keyboard.Key.ctrl)

#############################################


def next_page():
    currentValue.clear()

    keyAction.press(keyboard.Key.page_down)
    keyAction.release(keyboard.Key.page_down)


def previous_page():
    currentValue.clear()

    keyAction.press(keyboard.Key.page_up)
    keyAction.release(keyboard.Key.page_up)


def page_top():
    currentValue.clear()

    keyAction.press(keyboard.Key.home)
    keyAction.release(keyboard.Key.home)


def page_end():
    currentValue.clear()

    keyAction.press(keyboard.Key.end)
    keyAction.release(keyboard.Key.end)


def page_spin():
    currentValue.clear()

    keyAction.release(keyboard.Key.shift)
    keyAction.press(keyboard.Key.f9)
    keyAction.release(keyboard.Key.f9)


def full_screen():
    currentValue.clear()

    keyAction.release(keyboard.Key.shift)
    keyAction.press(keyboard.Key.f11)
    keyAction.release(keyboard.Key.f11)

#########################################


def windows_start():
    currentValue.clear()

    keyAction.press(keyboard.Key.ctrl)
    keyAction.press(keyboard.Key.esc)
    keyAction.release(keyboard.Key.esc)
    keyAction.release(keyboard.Key.ctrl)


def windows_process():
    currentValue.clear()

    keyAction.press(keyboard.Key.cmd)
    keyAction.press(keyboard.Key.tab)
    keyAction.release(keyboard.Key.tab)
    keyAction.release(keyboard.Key.cmd)


def windows_search():
    currentValue.clear()

    keyAction.press(keyboard.Key.cmd)
    keyAction.press('s')
    keyAction.release('s')
    keyAction.release(keyboard.Key.cmd)


def windows_minimize():
    currentValue.clear()

    keyAction.press(keyboard.Key.cmd)
    keyAction.press('m')
    keyAction.release('m')
    keyAction.release(keyboard.Key.cmd)


def windows_zoom():
    currentValue.clear()

    keyAction.press(keyboard.Key.cmd)
    keyAction.press('=')
    keyAction.release('=')
    keyAction.release(keyboard.Key.cmd)


def windows_explorer():
    currentValue.clear()

    keyAction.press(keyboard.Key.cmd)
    keyAction.press('e')
    keyAction.release('e')
    keyAction.release(keyboard.Key.cmd)


#########################################

func_mapping = {"windows_start": windows_start,
                "windows_process": windows_process,
                "windows_search": windows_search,
                "windows_minimize": windows_minimize,
                "windows_zoom": windows_zoom,
                "windows_explorer": windows_explorer}

#########################################

def execute1():
    # print("linear1")
    # new_window()
    pass



def execute2():
    # print("linear2")
    # previous_page()
    pass


def execute3():
    # print("linear3")
    # page_top()

    # DB읽어오기
    f = open("./setting/pero_setting_data/gesture3.txt", "r")
    linear3 = f.read()
    f = open("./setting/pero_setting_data/gesture4.txt", "r")
    linear4 = f.read()
    f = open("./setting/pero_setting_data/pero_state.txt", "r")
    pero_state = f.read()
    f = open("./setting/pero_setting_data/default.txt", "rt", encoding="UTF-8")
    default_context = f.read()
    default = default_context.split("\n")
    f.close()

    # 세팅
    setting_db = {}
    default_db = {}

    linear3_split = linear3.split(":")
    if linear3_split[1] == "시작화면 열기(Default)":
        setting_db.update({linear3_split[0]: "windows_start"})
    elif linear3_split[1] == "윈도우 작업 보기":
        setting_db.update({linear3_split[0]: "windows_process"})
    elif linear3_split[1] == "윈도우 검색 창 실행":
        setting_db.update({linear3_split[0]: "windows_search"})

    linear4_split = linear4.split(":")
    if linear4_split[1] == "모든창 최소화(Default)":
        setting_db.update({linear4_split[0]: "windows_minimize"})
    elif linear4_split[1] == "돋보기 실행":
        setting_db.update({linear4_split[0]: "windows_zoom"})
    elif linear4_split[1] == "탐색기 실행":
        setting_db.update({linear4_split[0]: "windows_explorer"})

    for i in range(2):
        default_element = default[i].split(":")
        if default_element[1] == "시작화면 열기(Default)":
            default_db.update({default_element[0]: "windows_start"})
        elif default_element[1] == "모든창 최소화(Default)":
            default_db.update({default_element[0]: "windows_minimize"})

    if pero_state == "default":
        func_mapping[default_db["linear3"]]()
    elif pero_state == "user":
        func_mapping[setting_db["linear3"]]()


def execute4():
    # print("linear4")
    # page_end()

    # DB읽어오기
    f = open("./setting/pero_setting_data/gesture3.txt", "r")
    linear3 = f.read()
    f = open("./setting/pero_setting_data/gesture4.txt", "r")
    linear4 = f.read()
    f = open("./setting/pero_setting_data/pero_state.txt", "r")
    pero_state = f.read()
    f = open("./setting/pero_setting_data/default.txt", "rt", encoding="UTF-8")
    default_context = f.read()
    default = default_context.split("\n")
    f.close()

    # 세팅
    setting_db = {}
    default_db = {}

    linear3_split = linear3.split(":")
    if linear3_split[1] == "시작화면 열기(Default)":
        setting_db.update({linear3_split[0]: "windows_start"})
    elif linear3_split[1] == "윈도우 작업 보기":
        setting_db.update({linear3_split[0]: "windows_process"})
    elif linear3_split[1] == "윈도우 검색 창 실행":
        setting_db.update({linear3_split[0]: "windows_search"})

    linear4_split = linear4.split(":")
    if linear4_split[1] == "모든창 최소화(Default)":
        setting_db.update({linear4_split[0]: "windows_minimize"})
    elif linear4_split[1] == "돋보기 실행":
        setting_db.update({linear4_split[0]: "windows_zoom"})
    elif linear4_split[1] == "탐색기 실행":
        setting_db.update({linear4_split[0]: "windows_explorer"})

    for i in range(2):
        default_element = default[i].split(":")
        if default_element[1] == "시작화면 열기(Default)":
            default_db.update({default_element[0]: "windows_start"})
        elif default_element[1] == "모든창 최소화(Default)":
            default_db.update({default_element[0]: "windows_minimize"})

    if pero_state == "default":
        func_mapping[default_db["linear4"]]()
    elif pero_state == "user":
        func_mapping[setting_db["linear4"]]()


# 키보드 클릭시(press) 아래 함수 실행
def on_press(key):
    # 미리 설정한 단축키 dictionary값을 입력된 key값과 비교
    try:
        for i in COMBINATIONS:
            for j in i.values():
                for k in j:
                    # 단축키와 입력된key값이 같다면 currentValue에 추가
                    if key == k:
                        currentValue.append(key)
                        raise NotImplementedError
                    else:
                        pass
    except NotImplementedError:
        # currentValue.clear()
        # currentList.clear()
        pass

    # esc버튼 클릭하면 run stop
    # if key == keyboard.Key.esc:
    #     return False


def on_release(key):
    # press에서 확인한 currentValue값에 따라 실행될 함수 호출
    try:
        for m in COMBINATIONS:
            for n, l in m.items():
                if currentValue == l:
                    if n == 'comb1':
                        execute1()
                    elif n == 'comb2':
                        execute2()
                    elif n == 'comb3':
                        execute3()
                    elif n == 'comb4':
                        execute4()
                    raise NotImplementedError
    except NotImplementedError:
        # currentValue.clear()
        # currentList.clear()
        pass

    try:
        currentValue.clear()
    except KeyError:
        pass

    # if key == keyboard.Key.esc:
    #     return False


# 키보드 예외처리도 고려
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        listener.join()
    except MyException as e:
        print('{0} was pressed'.format(e.args[0]))

# listener = keyboard.Listener(on_press=on_press, on_release=on_release)
# listener.start()
