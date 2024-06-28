import pyautogui

# size = pyautogui.size() #현재 화면의 스크린 사이즈를 가져옴
# print(size) #가로, 세로 크기를 알 수 있음
## size[0] : width
## size[1] : height


### mouse

# pyautogui.moveTo(100,100) #지정한 위치로 마우스를 이동
# pyautogui.moveTo(100,200,duration=0.25)

#상대 좌표로 마우스 이동
# pyautogui.move(100,100,duration=0.25)
# print(pyautogui.position())
# p = pyautogui.position()
# print(p[0],p[1])
# print(p.x,p.y)

# pyautogui.sleep(3)
# print(pyautogui.position())

# pyautogui.click(64,17)
# pyautogui.mouseDown()
# pyautogui.mouseUp()
# pyautogui.doubleClick()
# pyautogui.click(clicks=500)
# pyautogui.rightClick()
# pyautogui.middleClick()
# pyautogui.drag(100,0)
# pyautogui.dragTo(1515,349)
# pyautogui.mouseInfo()
# pyautogui.PAUSE = 1 #모든 동작에 1초씩 sleep적용
# for i in range(10) :
    # pyautogui.move(100,100)
    # pyautogui.sleep(1)


### screen

#스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save('screebshot.png') #파일로 저장

# pixel = pyautogui.pixel(28,18)
# print(pixel)

# print(pyautogui.pixelMatchesColor(28,18,(24,24,24)))
# locateOnWindow.__doc__ = pyscreeze.locateOnScreen.__doc__

# locateOnScreen 쓰려면 PyScreeze 다운그레이드 pip install --upgrade PyScreeze==버전
# file_menu = pyautogui.locateOnScreen('file_menu.png')
# print(file_menu)
# pyautogui.click(file_menu)

# trach_icon = pyautogui.locateOnScreen('delete_icon.png')
# pyautogui.moveTo(trach_icon)

# for i in pyautogui.locateAllOnScreen('check_box.png') :
#     print(i)
#     pyautogui.click(i,duration=0.25)
    
# checkbox = pyautogui.locateOnScreen('check_box.png')
# pyautogui.click(checkbox)

# #속도 개선
# # 1. grayScale
# checkbox = pyautogui.locateOnScreen('check_box.png',grayscale =True)
# pyautogui.click(checkbox)
# # 2. 범위 지정
# # region=(x,y,width,height) mouseInfo
# checkbox = pyautogui.locateOnScreen('check_box.png',grayscale =True, region=(1488,623,1881-1488,137))
# pyautogui.click(checkbox)

# #3. 정확도 조정
# # pip install opencv-python
# checkbox = pyautogui.locateOnScreen('check_box.png', confidence=0.9) #90%
# pyautogui.click(checkbox)

#자동화 대상이 바로 보여지지 않는 경우
#1. 계속 기다리기
file_menu = pyautogui.locateOnScreen('memo_file.png')
# if file_menu :
#     pyautogui.click(file_menu)
# else :
#     print('발견 실패')
    
# while file_menu is None :
#     file_menu = pyautogui.locateOnScreen('memo_file.png')
#     print('발견실패')
# pyautogui.click(file_menu)
#2. 일정 시간동안 기다리기 (Timeout)
import time
import sys
timeout =10 #10초 대기
# start = time.time() #시작 시간 설정
# file_menu = None
# while file_menu is None :
#     file_menu = pyautogui.locateOnScreen('memo_file.png')
#     end = time.time() #종료 시간 설정
#     if end -start > timeout : #지정한 시간 초과하면
#         print('시간종료')
#         sys.exit()
# pyautogui.click(file_menu)

def find_target(img_file, timeout=30) :
    start = time.time()
    target =None
    while target is None :
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout :
            break
    return target

def my_click(img_file, timeout=30) :
    target = find_target(img_file,timeout)
    if target :
        pyautogui.click(target)
    else :
        print(f'[Timeout {timeout}s] Target not found({img_file}. Terminate program.)')
        sys.exit()
        
my_click('memo_file.png', 10)