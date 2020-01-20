import psutil
import win32gui
import win32process
from pynput import keyboard

# The key combination to check
COMBINATIONS = [{'comb1': [keyboard.Key.shift_l, keyboard.Key.enter]},
                {'comb2': [keyboard.Key.shift_r, keyboard.Key.enter]},
                {'comb3': [keyboard.Key.shift_l]},
                {'comb4': [keyboard.Key.shift_r]}]

# 현재 입력받은 키
currentValue = []

keyAction = keyboard.Controller()


# 키보드 에러 핸들링
class MyException(Exception):
    pass


#########################################
################# ppt ###################

def presentation_start():
    currentValue.clear()

    keyAction.press(keyboard.Key.f5)
    keyAction.release(keyboard.Key.f5)


def presentation_create():
    currentValue.clear()

    keyAction.press(keyboard.Key.ctrl_l)
    keyAction.press("n")
    keyAction.release("n")
    keyAction.release(keyboard.Key.ctrl_l)


def slide_add():
    currentValue.clear()

    keyAction.press(keyboard.Key.ctrl_l)
    keyAction.press("m")
    keyAction.release("m")
    keyAction.release(keyboard.Key.ctrl_l)


def save_as():
    currentValue.clear()

    keyAction.press(keyboard.Key.f12)
    keyAction.release(keyboard.Key.f12)


def file_home():
    currentValue.clear()

    keyAction.press(keyboard.Key.alt_l)
    keyAction.press("f")
    keyAction.release("f")
    keyAction.release(keyboard.Key.alt_l)


def open_file():
    currentValue.clear()

    keyAction.press(keyboard.Key.ctrl_l)
    keyAction.press("o")
    keyAction.release("o")
    keyAction.release(keyboard.Key.ctrl_l)


#########################################
################ excel ##################

def format_cell():
    currentValue.clear()

    keyAction.press(keyboard.Key.ctrl_l)
    keyAction.press('1')
    keyAction.release('1')
    keyAction.release(keyboard.Key.ctrl_l)


def column_zero():
    currentValue.clear()

    keyAction.press(keyboard.Key.ctrl_l)
    keyAction.press('9')
    keyAction.release('9')
    keyAction.release(keyboard.Key.ctrl_l)


def row_zero():
    currentValue.clear()

    keyAction.press(keyboard.Key.ctrl_l)
    keyAction.press('0')
    keyAction.release('0')
    keyAction.release(keyboard.Key.ctrl_l)


def function_wizard():
    currentValue.clear()

    keyAction.press(keyboard.Key.shift)
    keyAction.press(keyboard.Key.f3)
    keyAction.release(keyboard.Key.f3)
    keyAction.release(keyboard.Key.shift)


#########################################
########### windows default #############

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
                "windows_explorer": windows_explorer,
                "presentation_start": presentation_start,
                "presentation_create": presentation_create,
                "slide_add": slide_add,
                "save_as": save_as,
                "file_home": file_home,
                "open_file": open_file,
                "format_cell": format_cell,
                "column_zero": column_zero,
                "row_zero": row_zero,
                "function_wizard": function_wizard}

#########################################

def funWin():
    pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
    # print(psutil.Process(pid[-1]).name())
    return psutil.Process(pid[-1]).name()

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
    ############# linear3에 대한 함수 #############

    f = open("./setting/pero_setting_data/apply_app.txt", "r")
    apply_app = f.read()
    f = open("./setting/pero_setting_data/apply_gesture.txt", "r")
    apply_ges = f.read()
    apply_ges = apply_ges.split("\n")
    f.close()

    if apply_app == "default":
        ## default.txt를 읽어서 명령에 적용
        f = open("./setting/pero_setting_data/default.txt", "rt", encoding="UTF-8")
        default_list = f.read()
        default_list = default_list.split("\n")
        default_all = {}
        for i in range(len(default_list)):
            default_all.update({default_list[i].split(":")[0]: default_list[i].split(":")[1]})

        for item in list(default_all.keys()):
            if item == "linear3":
                func_mapping["windows_start"]()
    elif apply_app == "excel":
        ## funWin(): 현재 활성화된 어플리케이션 이름을 반환
        if funWin() == "EXCEL.EXE":
            ## 1. 사용할 제스처가 어떤 것인지 파악
            ## 2. 각 제스처 이름의 text파일을 읽어오기
            ## 3. 읽은 text파일의 명령에 따라 각 함수에 연결
            for i in range(len(apply_ges) - 1):
                if apply_ges[i] == "linear3":
                    # 명령값에 대한 함수 실행
                    f = open("./setting/pero_setting_data/linear3.txt", "r")
                    linear3 = f.read()
                    linear3 = linear3.split(":")[1]
                    if linear3 == "다른 이름으로 저장":
                        func_mapping["save_as"]()
                    elif linear3 == "파일(홈)":
                        func_mapping["file_home"]()
                    elif linear3 == "셀서식":
                        func_mapping["format_cell"]()
    elif apply_app == "ppt":
        if funWin() == "POWERPNT.EXE":
            for i in range(len(apply_ges) - 1):
                if apply_ges[i] == "linear3":
                    # 명령값에 대한 함수 실행
                    f = open("./setting/pero_setting_data/linear3.txt", "r")
                    linear3 = f.read()
                    linear3 = linear3.split(":")[1]
                    if linear3 == "프레젠테이션 시작":
                        func_mapping["presentation_start"]()
                    elif linear3 == "새 프레젠테이션 생성":
                        func_mapping["presentation_create"]()
                    elif linear3 == "새 슬라이드 추가":
                        func_mapping["slide_add"]()
    elif apply_app == "windows":
        for i in range(len(apply_ges) - 1):
            if apply_ges[i] == "linear3":
                # 명령값에 대한 함수 실행
                f = open("./setting/pero_setting_data/linear3.txt", "r")
                linear3 = f.read()
                linear3 = linear3.split(":")[1]
                if linear3 == "시작화면 열기(Default)":
                    func_mapping["windows_start"]()
                elif linear3 == "윈도우 작업 보기":
                    func_mapping["windows_process"]()
                elif linear3 == "윈도우 검색 창 실행":
                    func_mapping["windows_search"]()


def execute4():
    f = open("./setting/pero_setting_data/apply_app.txt", "r")
    apply_app = f.read()
    f = open("./setting/pero_setting_data/apply_gesture.txt", "r")
    apply_ges = f.read()
    apply_ges = apply_ges.split("\n")
    f.close()

    if apply_app == "default":
        f = open("./setting/pero_setting_data/default.txt", "rt", encoding="UTF-8")
        default_list = f.read()
        default_list = default_list.split("\n")
        default_all = {}
        for i in range(len(default_list)):
            default_all.update({default_list[i].split(":")[0]: default_list[i].split(":")[1]})

        for item in list(default_all.keys()):
            if item == "linear4":
                func_mapping["windows_minimize"]()
    elif apply_app == "excel":
        if funWin() == "EXCEL.EXE":
            for i in range(len(apply_ges) - 1):
                if apply_ges[i] == "linear4":
                    f = open("./setting/pero_setting_data/linear4.txt", "r")
                    linear4 = f.read()
                    linear4 = linear4.split(":")[1]
                    if linear4 == "열길이 0":
                        func_mapping["column_zero"]()
                    elif linear4 == "행길이 0":
                        func_mapping["row_zero"]()
                    elif linear4 == "함수 마법사":
                        func_mapping["function_wizard"]()
    elif apply_app == "ppt":
        if funWin() == "POWERPNT.EXE":
            for i in range(len(apply_ges) - 1):
                if apply_ges[i] == "linear4":
                    f = open("./setting/pero_setting_data/linear4.txt", "r")
                    linear4 = f.read()
                    linear4 = linear4.split(":")[1]
                    if linear4 == "다른 이름으로 저장":
                        func_mapping["save_as"]()
                    elif linear4 == "파일(홈)":
                        func_mapping["file_home"]()
                    elif linear4 == "파일열기":
                        func_mapping["open_file"]()
    elif apply_app == "windows":
        for i in range(len(apply_ges) - 1):
            if apply_ges[i] == "linear4":
                f = open("./setting/pero_setting_data/linear4.txt", "r")
                linear4 = f.read()
                linear4 = linear4.split(":")[1]
                if linear4 == "모든창 최소화(Default)":
                    func_mapping["windows_minimize"]()
                elif linear4 == "돋보기 실행":
                    func_mapping["windows_zoom"]()
                elif linear4 == "탐색기 실행":
                    func_mapping["windows_explorer"]()


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
                        # execute1()
                        pass
                    elif n == 'comb2':
                        # execute2()
                        pass
                    elif n == 'comb3':
                        # 위로 제스처
                        execute3()
                    elif n == 'comb4':
                        # 아래로 제스처
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



# 키보드 예외처리도 고려
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        listener.join()
    except MyException as e:
        print('{0} was pressed'.format(e.args[0]))
