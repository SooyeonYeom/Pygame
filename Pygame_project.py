def main3():
    import sys

    print("3스테이지")
    sys.exit()


def main2():
    import pygame
    import random
    import sys

    ####################### < 초기세팅 > ########################
    pygame.init()  # 초기화 (반드시 필요)

    # < 화면 크기 설정 >
    screen_width = 540  # 가로
    screen_height = 960  # 세로
    screen = pygame.display.set_mode((screen_width, screen_height))  # 게임화면 크기 설정

    # < 화면 타이틀 설정 >
    pygame.display.set_caption("< Hello Shooting Star! > ")  # 게임 이름

    # <Frame Per Second>
    clock = pygame.time.Clock()

    ####################### < 필요정보 지정 > ########################
    # ex) 배경 이미지, 스프라이트, 좌표, 속도, 시간, 폰트 등

    # < 배경 이미지 불러오기 >

    background = pygame.image.load("background2.png")

    # < 무대 장식 >
    grass = pygame.image.load("stage_grass.png")
    grass_size = grass.get_rect().size  # 이미지 크기 구해옴
    grass_width = grass_size[0]
    grass_height = grass_size[1]
    grass_x_pos = 0  # 화면 가로의 절반에 위치
    grass_y_pos = screen_height - grass_height  # 화면 세로의 가장 아래

    # < 무대 지정 >
    stage = pygame.image.load("stage2.png")
    stage_size = stage.get_rect().size  # 이미지 크기 구해옴
    stage_width = stage_size[0]
    stage_height = stage_size[1]
    stage_x_pos = 0  # 화면 가로의 절반에 위치
    stage_y_pos = screen_height - stage_height  # 화면 세로의 가장 아래

    # < 타이틀 지정 >
    title = pygame.image.load("stage_info2.png")
    title_size = title.get_rect().size  # 이미지 크기 구해옴
    title_width = title_size[0]
    title_height = title_size[1]
    title_x_pos = (screen_width / 2) - (title_width / 2)
    title_y_pos = 60

    # < 승리 타이틀 지정 >
    succeed = pygame.image.load("succeed.png")
    succeed_size = succeed.get_rect().size  # 이미지 크기 구해옴
    succeed_width = succeed_size[0]
    succeed_height = succeed_size[1]
    succeed_x_pos = (screen_width / 2) - (succeed_width / 2)
    succeed_y_pos = 80

    # < 실패 타이틀 지정 >
    failed = pygame.image.load("failed.png")
    failed_size = failed.get_rect().size  # 이미지 크기 구해옴
    failed_width = failed_size[0]
    failed_height = failed_size[1]
    failed_x_pos = (screen_width / 2) - (failed_width / 2)
    failed_y_pos = 240

    # < 이름 타이틀 지정 >
    name = pygame.image.load("name.png")
    name_size = name.get_rect().size  # 이미지 크기 구해옴
    name_width = name_size[0]
    name_height = name_size[1]
    name_x_pos = (screen_width / 2) - (name_width / 2)
    name_y_pos = screen_height - 30

    # < 시작화면 지정 >
    startbg = pygame.image.load("bg_start2.png")
    startbg_size = startbg.get_rect().size  # 이미지 크기 구해옴
    startbg_width = startbg_size[0]
    startbg_height = startbg_size[1]
    startbg_x_pos = 0
    startbg_y_pos = 0

    def button():

        button = pygame.image.load(
            "level2.png"
        ).convert_alpha()
        screen.blit(button, (100, 460))
        pygame.display.flip()
        b = screen.blit(button, (100, 470))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if b.collidepoint(pos):
                        clicksound.play()
                        return

    def button_try():
        button = pygame.image.load(
            "Try AGAIN.png"
        ).convert_alpha()
        screen.blit(button, (130, 420))
        pygame.display.flip()
        b = screen.blit(button, (130, 420))

        button2 = pygame.image.load(
            "QUIT.png"
        ).convert_alpha()
        screen.blit(button2, (200, 520))
        pygame.display.flip()
        b2 = screen.blit(button2, (200, 520))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if b.collidepoint(pos):
                        print("재시작")
                        clicksound.play()
                        bgsound.stop()
                        main2()
                        return
                    elif b2.collidepoint(pos):
                        print("종료")
                        clicksound.play()
                        sys.exit()
                        return

    def button_try2():
        button = pygame.image.load(
            "Try AGAIN.png"
        ).convert_alpha()
        screen.blit(button, (130, 420))
        pygame.display.flip()
        b = screen.blit(button, (130, 420))

        button2 = pygame.image.load(
            "QUIT.png"
        ).convert_alpha()
        screen.blit(button2, (200, 520))
        pygame.display.flip()
        b2 = screen.blit(button2, (200, 520))

        button3 = pygame.image.load(
            "NEXTSTAGE.png"
        ).convert_alpha()
        screen.blit(button3, (100, 620))
        pygame.display.flip()
        b3 = screen.blit(button3, (100, 620))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if b.collidepoint(pos):
                        print("재시작")
                        clicksound.play()
                        bgsound.stop()
                        main2()
                        return
                    elif b2.collidepoint(pos):
                        print("종료")
                        clicksound.play()
                        sys.exit()
                        return
                    elif b3.collidepoint(pos):
                        print("다음 스테이지")
                        clicksound.play()
                        main3()
                        return

    # < 플레이어 스프라이트 불러오기 >
    character = pygame.image.load("character.png")
    character_size = character.get_rect().size  # 이미지 크기 구해옴
    character_width = character_size[0]
    character_height = character_size[1]
    character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반에 위치
    character_y_pos = screen_height - character_height - 90  # 화면 세로의 가장 아래

    # < 이동할 좌표 >

    to_x = 0
    to_y = 0

    # < 캐릭터 속도 >

    cha_speed = 0.6

    # 게임 화면 토당 프레임 수 X 캐릭터 내재속도 = 실제 캐릭터 출력 속도

    # < 적 스프라이트 불러오기 >
    enemy = pygame.image.load("enemy.png")
    enemy_size = enemy.get_rect().size  # 이미지 크기 구해옴
    enemy_width = enemy_size[0]
    enemy_height = enemy_size[1]
    enemy_x_pos = random.randint(
        0, screen_width - enemy_width
    )  # 가로 왼쪽 끝은 0, 오른쪽 끝은 화면가로값에서 에너미스프라이트 가로길이 뺀 값
    enemy_y_pos = 0
    enemy_speed = 15

    # < 적2 스프라이트 불러오기 >
    enemy2 = pygame.image.load("enemy2.png")
    enemy2_size = enemy2.get_rect().size  # 이미지 크기 구해옴
    enemy2_width = enemy2_size[0]
    enemy2_height = enemy2_size[1]
    enemy2_x_pos = random.randint(
        0, screen_width - enemy2_width
    )  # 가로 왼쪽 끝은 0, 오른쪽 끝은 화면가로값에서 에너미스프라이트 가로길이 뺀 값
    enemy2_y_pos = -480
    enemy2_speed = 15

    # < 텍스트 폰트 설정 >

    game_font = pygame.font.Font("ka1.ttf", 70)  # 폰트 객체 생성 (폰트, 크기)

    # <총 플레이 타임 설정 >
    playtime = 15

    # <Sound>
    bgsound = pygame.mixer.Sound("bgsound.wav")

    clicksound = pygame.mixer.Sound("select.wav")

    winsound = pygame.mixer.Sound("win.wav")

    losesound = pygame.mixer.Sound("lose.wav")

    ####################### < 이벤트 루프 > ########################

    # < 이벤트 루프 > # 계속 running 되게 설정 + 이벤트 반복점검 -> 창이 닫히는 이벤트 발생 시 프로그램도 종료
    running = True  # 게임이 진행 중인가? = True

    screen.blit(startbg, (startbg_x_pos, startbg_y_pos))
    screen.blit(title, (title_x_pos, title_y_pos))
    screen.blit(name, (name_x_pos, name_y_pos))

    bgsound.play()
    button()

    # <시작 시간 정보 받아오기 >
    start_ticks = pygame.time.get_ticks()  # 현재(시작시점) 시간 tick을 받아옴

    flag = False

    while running:

        frame = clock.tick(60)  # 게임화면의 초당 프레임 수 설정
        for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
            if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
                running = False  # 게임 종료

            if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
                if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                    to_x -= cha_speed
                elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                    to_x += cha_speed

            if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0

        # 캐릭터 / 에너미 위치 변화 정의
        character_x_pos += to_x * frame
        character_y_pos += to_y * frame

        enemy_y_pos += enemy_speed  # y좌표 0으로부터 점점 10씩 내려간다
        enemy2_y_pos += enemy2_speed  # y좌표 0으로부터 점점 10씩 내려간다

        # 에너미1 중반까지 떨어지면 에너미2 떨어지기 시작하는 함수 정의

        if enemy_y_pos > 960:  # 만약 끝에 떨어지면

            enemy_y_pos = 0  # 다시 0부터 시작한다

            enemy_x_pos = random.randint(0, screen_width - enemy_width)

        if enemy2_y_pos > 960:

            enemy2_y_pos = 0

            enemy2_x_pos = random.randint(0, screen_width - enemy2_width)

        # 플레이어 가로 경계값 처리
        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width

        # 플레이어 세로 경계값 처리
        if character_y_pos < 0:
            character_y_pos = 0
        elif character_y_pos > screen_height - character_height - 90:
            character_y_pos = screen_height - character_height - 90

        # 충돌 처리를 위한 rect 정보 업데이트
        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        enemy_rect = enemy.get_rect()
        enemy_rect.left = enemy_x_pos
        enemy_rect.top = enemy_y_pos

        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        # 지금까지 흐른 시간 = 현재 시간 tick - 시작 시간 tick
        # 지금까지 흐른 시간, 즉 경과시간(ms)을 1000으로 나누어서 초(s) 단위로 표시한다

        # 충돌 체크
        if character_rect.colliderect(enemy_rect):
            character = pygame.image.load(
                "cha_cry.png"
            )
            losesound.play()
            running = False

        # 만약 시간이 0이하 이면 게임 종료
        if playtime - elapsed_time <= 0:
            character = pygame.image.load(
                "cha_happy.png"
            )
            winsound.play()
            bgsound.fadeout(3000)
            flag = True
            running = False

        screen.blit(background, (0, 0))  # (배경 x좌표 y좌표) 배경 그리기
        # screen.fill(0,0, 255) #RGB 값으로 배경색을 채울 수도 있음
        screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리기
        screen.blit(enemy2, (enemy2_x_pos, enemy2_y_pos))
        screen.blit(stage, (stage_x_pos, stage_y_pos))  # 무대 그리기
        screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
        screen.blit(grass, (grass_x_pos, grass_y_pos))  # 무대장식 그리기

        timer = game_font.render(
            str(int(playtime - elapsed_time)), True, (235, 236, 255)
        )

        # font.render(출력할 텍스트, True, 글자색상)

        screen.blit(timer, ((screen_width / 2) - 30, 10))

        pygame.display.update()  # 게임화면을 계속 다시 그리기!

    if flag:
        screen.blit(succeed, (succeed_x_pos, succeed_y_pos))
        screen.blit(name, (name_x_pos, name_y_pos))
        print("와! 별똥별을 피했어!")

        button_try2()
    else:
        screen.blit(failed, (failed_x_pos, failed_y_pos))
        screen.blit(name, (name_x_pos, name_y_pos))
        print("앗! 별똥별을 맞았어!")

        button_try()

    # 프로그램 종료 전 잠시 대기
    pygame.time.delay(5000)  # running 종료 -> 5초 정도 대기 (ms) -> 프로그램 종료

    # < 프로그램 종료 >
    pygame.quit()


def main():

    import pygame
    import random
    import sys

    ####################### < 초기세팅 > ########################
    pygame.init()  # 초기화 (반드시 필요)

    # < 화면 크기 설정 >
    screen_width = 540  # 가로
    screen_height = 960  # 세로
    screen = pygame.display.set_mode((screen_width, screen_height))  # 게임화면 크기 설정

    # < 화면 타이틀 설정 >
    pygame.display.set_caption("< Hello Shooting Star! > ")  # 게임 이름

    # <Frame Per Second>
    clock = pygame.time.Clock()

    ####################### < 필요정보 지정 > ########################
    # ex) 배경 이미지, 스프라이트, 좌표, 속도, 시간, 폰트 등

    # < 배경 이미지 불러오기 >

    background = pygame.image.load("backgroud.png")

    # < 무대 장식 >
    grass = pygame.image.load("stage_grass.png")
    grass_size = grass.get_rect().size  # 이미지 크기 구해옴
    grass_width = grass_size[0]
    grass_height = grass_size[1]
    grass_x_pos = 0  # 화면 가로의 절반에 위치
    grass_y_pos = screen_height - grass_height  # 화면 세로의 가장 아래

    # < 무대 지정 >
    stage = pygame.image.load("stage.png")
    stage_size = stage.get_rect().size  # 이미지 크기 구해옴
    stage_width = stage_size[0]
    stage_height = stage_size[1]
    stage_x_pos = 0  # 화면 가로의 절반에 위치
    stage_y_pos = screen_height - stage_height  # 화면 세로의 가장 아래

    # < 타이틀 지정 >
    title = pygame.image.load("stage_info.png")
    title_size = title.get_rect().size  # 이미지 크기 구해옴
    title_width = title_size[0]
    title_height = title_size[1]
    title_x_pos = (screen_width / 2) - (title_width / 2)
    title_y_pos = 60

    # < 승리 타이틀 지정 >
    succeed = pygame.image.load("succeed.png")
    succeed_size = succeed.get_rect().size  # 이미지 크기 구해옴
    succeed_width = succeed_size[0]
    succeed_height = succeed_size[1]
    succeed_x_pos = (screen_width / 2) - (succeed_width / 2)
    succeed_y_pos = 80

    # < 실패 타이틀 지정 >
    failed = pygame.image.load("failed.png")
    failed_size = failed.get_rect().size  # 이미지 크기 구해옴
    failed_width = failed_size[0]
    failed_height = failed_size[1]
    failed_x_pos = (screen_width / 2) - (failed_width / 2)
    failed_y_pos = 240

    # < 이름 타이틀 지정 >
    name = pygame.image.load("name.png")
    name_size = name.get_rect().size  # 이미지 크기 구해옴
    name_width = name_size[0]
    name_height = name_size[1]
    name_x_pos = (screen_width / 2) - (name_width / 2)
    name_y_pos = screen_height - 30

    # < 시작화면 지정 >
    startbg = pygame.image.load("bg_start.png")
    startbg_size = startbg.get_rect().size  # 이미지 크기 구해옴
    startbg_width = startbg_size[0]
    startbg_height = startbg_size[1]
    startbg_x_pos = 0
    startbg_y_pos = 0

    def button():

        button = pygame.image.load(
            "level1.png"
        ).convert_alpha()
        screen.blit(button, (100, 460))
        pygame.display.flip()
        b = screen.blit(button, (100, 470))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if b.collidepoint(pos):
                        clicksound.play()
                        return

    def button_try():
        button = pygame.image.load(
            "Try AGAIN.png"
        ).convert_alpha()
        screen.blit(button, (130, 420))
        pygame.display.flip()
        b = screen.blit(button, (130, 420))

        button2 = pygame.image.load(
            "QUIT.png"
        ).convert_alpha()
        screen.blit(button2, (200, 520))
        pygame.display.flip()
        b2 = screen.blit(button2, (200, 520))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if b.collidepoint(pos):
                        print("재시작")
                        clicksound.play()
                        bgsound.stop()
                        main()
                        return
                    elif b2.collidepoint(pos):
                        print("종료")
                        clicksound.play()
                        sys.exit()
                        return

    def button_try2():
        button = pygame.image.load(
            "Try AGAIN.png"
        ).convert_alpha()
        screen.blit(button, (130, 420))
        pygame.display.flip()
        b = screen.blit(button, (130, 420))

        button2 = pygame.image.load(
            "QUIT.png"
        ).convert_alpha()
        screen.blit(button2, (200, 520))
        pygame.display.flip()
        b2 = screen.blit(button2, (200, 520))

        button3 = pygame.image.load(
            "NEXTSTAGE.png"
        ).convert_alpha()
        screen.blit(button3, (100, 620))
        pygame.display.flip()
        b3 = screen.blit(button3, (100, 620))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if b.collidepoint(pos):
                        print("재시작")
                        clicksound.play()
                        bgsound.stop()
                        main()
                        return
                    elif b2.collidepoint(pos):
                        print("종료")
                        clicksound.play()
                        sys.exit()
                        return
                    elif b3.collidepoint(pos):
                        print("다음 스테이지")
                        clicksound.play()
                        main2()
                        return

    # < 플레이어 스프라이트 불러오기 >
    character = pygame.image.load("character.png")
    character_size = character.get_rect().size  # 이미지 크기 구해옴
    character_width = character_size[0]
    character_height = character_size[1]
    character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반에 위치
    character_y_pos = screen_height - character_height - 90  # 화면 세로의 가장 아래

    # < 이동할 좌표 >

    to_x = 0
    to_y = 0

    # < 캐릭터 속도 >

    cha_speed = 0.6

    # 게임 화면 토당 프레임 수 X 캐릭터 내재속도 = 실제 캐릭터 출력 속도

    # < 적 스프라이트 불러오기 >
    enemy = pygame.image.load("enemy.png")
    enemy_size = enemy.get_rect().size  # 이미지 크기 구해옴
    enemy_width = enemy_size[0]
    enemy_height = enemy_size[1]
    enemy_x_pos = random.randint(
        0, screen_width - enemy_width
    )  # 가로 왼쪽 끝은 0, 오른쪽 끝은 화면가로값에서 에너미스프라이트 가로길이 뺀 값
    enemy_y_pos = 0
    enemy_speed = 15

    # < 텍스트 폰트 설정 >

    game_font = pygame.font.Font("ka1.ttf", 70)  # 폰트 객체 생성 (폰트, 크기)

    # <총 플레이 타임 설정 >
    playtime = 10

    # <Sound>
    bgsound = pygame.mixer.Sound("bgsound.wav")

    clicksound = pygame.mixer.Sound("select.wav")

    winsound = pygame.mixer.Sound("win.wav")

    losesound = pygame.mixer.Sound("lose.wav")

    ####################### < 이벤트 루프 > ########################

    # < 이벤트 루프 > # 계속 running 되게 설정 + 이벤트 반복점검 -> 창이 닫히는 이벤트 발생 시 프로그램도 종료
    running = True  # 게임이 진행 중인가? = True

    screen.blit(startbg, (startbg_x_pos, startbg_y_pos))
    screen.blit(title, (title_x_pos, title_y_pos))
    screen.blit(name, (name_x_pos, name_y_pos))

    bgsound.play()
    button()

    # <시작 시간 정보 받아오기 >
    start_ticks = pygame.time.get_ticks()  # 현재(시작시점) 시간 tick을 받아옴

    flag = False

    while running:

        frame = clock.tick(60)  # 게임화면의 초당 프레임 수 설정
        for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
            if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
                running = False  # 게임 종료

            if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
                if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                    to_x -= cha_speed
                elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                    to_x += cha_speed
                # elif event.key == pygame.K_UP:  # 캐릭터를 위로
                #     to_y -= cha_speed
                # elif event.key == pygame.K_DOWN:  # 캐릭터를 아래로
                #     to_y += cha_speed

            if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0
                # elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                #     to_y = 0

        # 캐릭터 / 에너미 위치 변화 정의
        character_x_pos += to_x * frame
        character_y_pos += to_y * frame

        enemy_y_pos += enemy_speed  # y좌표 0으로부터 점점 10씩 내려간다

        # 에너미 하나 떨어지고 다음 거 떨어지는 함수 정의
        if enemy_y_pos > screen_height:  # 만약 에너미가 경계를 넘어갔으면
            enemy_y_pos = 0  # 다시 화면 맨위, y=0으로 올린다
            enemy_x_pos = random.randint(0, screen_width - enemy_width)

        # 플레이어 가로 경계값 처리
        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width

        # 플레이어 세로 경계값 처리
        if character_y_pos < 0:
            character_y_pos = 0
        elif character_y_pos > screen_height - character_height - 90:
            character_y_pos = screen_height - character_height - 90

        # 충돌 처리를 위한 rect 정보 업데이트
        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        enemy_rect = enemy.get_rect()
        enemy_rect.left = enemy_x_pos
        enemy_rect.top = enemy_y_pos

        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        # 지금까지 흐른 시간 = 현재 시간 tick - 시작 시간 tick
        # 지금까지 흐른 시간, 즉 경과시간(ms)을 1000으로 나누어서 초(s) 단위로 표시한다

        # 충돌 체크
        if character_rect.colliderect(enemy_rect):
            character = pygame.image.load(
                "cha_cry.png"
            )
            losesound.play()
            running = False

        # 만약 시간이 0이하 이면 게임 종료
        if playtime - elapsed_time <= 0:
            character = pygame.image.load(
                "cha_happy.png"
            )
            winsound.play()
            bgsound.fadeout(3000)
            flag = True
            running = False

        screen.blit(background, (0, 0))  # (배경 x좌표 y좌표) 배경 그리기
        # screen.fill(0,0, 255) #RGB 값으로 배경색을 채울 수도 있음
        screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리기
        screen.blit(stage, (stage_x_pos, stage_y_pos))  # 무대 그리기
        screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
        screen.blit(grass, (grass_x_pos, grass_y_pos))  # 무대장식 그리기

        timer = game_font.render(
            str(int(playtime - elapsed_time)), True, (235, 236, 255)
        )

        # font.render(출력할 텍스트, True, 글자색상)

        screen.blit(timer, ((screen_width / 2) - 30, 10))

        pygame.display.update()  # 게임화면을 계속 다시 그리기!

    if flag:
        screen.blit(succeed, (succeed_x_pos, succeed_y_pos))
        screen.blit(name, (name_x_pos, name_y_pos))
        print("와! 별똥별을 피했어!")

        button_try2()
    else:
        screen.blit(failed, (failed_x_pos, failed_y_pos))
        screen.blit(name, (name_x_pos, name_y_pos))
        print("앗! 별똥별을 맞았어!")

        button_try()

    # 프로그램 종료 전 잠시 대기
    pygame.time.delay(5000)  # running 종료 -> 5초 정도 대기 (ms) -> 프로그램 종료

    # < 프로그램 종료 >
    pygame.quit()


def launch():

    import pygame
    import sys
    import time

    ####################### < 초기세팅 > ########################
    pygame.init()  # 초기화 (반드시 필요)

    # < 화면 크기 설정 >
    screen_width = 540  # 가로
    screen_height = 960  # 세로
    screen = pygame.display.set_mode((screen_width, screen_height))  # 게임화면 크기 설정

    # < 화면 타이틀 설정 >
    pygame.display.set_caption("< Hello Shooting Star! > ")  # 게임 이름

    # <Frame Per Second>
    clock = pygame.time.Clock()

    ####################### < 필요정보 지정 > ########################
    # ex) 배경 이미지, 스프라이트, 좌표, 속도, 시간, 폰트 등

    # < 이름 타이틀 지정 >
    name = pygame.image.load("name.png")
    name_size = name.get_rect().size  # 이미지 크기 구해옴
    name_width = name_size[0]
    name_height = name_size[1]
    name_x_pos = (screen_width / 2) - (name_width / 2)
    name_y_pos = screen_height - 30

    # < 시작화면 지정 >
    startbg = pygame.image.load("bg_start.png")
    startbg_size = startbg.get_rect().size  # 이미지 크기 구해옴
    startbg_width = startbg_size[0]
    startbg_height = startbg_size[1]
    startbg_x_pos = 0
    startbg_y_pos = 0

    # < 이동할 좌표 >

    to_x = 0
    to_y = 0

    # < 타이틀 내려오기 >
    title = pygame.image.load("Title.png")
    title_size = title.get_rect().size  # 이미지 크기 구해옴
    title_width = title_size[0]
    title_height = title_size[1]
    title_x_pos = (screen_width / 2) - (title_width / 2)
    title_y_pos = -title_height
    title_speed = 6

    # <로딩 타이머 장식 >
    heart = pygame.image.load("heart.png")
    heart_size = heart.get_rect().size  # 이미지 크기 구해옴
    heart_width = title_size[0]
    heart_height = title_size[1]
    heart_x_pos = (screen_width / 2) - (title_width / 2)
    heart_y_pos = 480

    # <로딩 안내>
    waiting = pygame.image.load("waiting.png")
    waiting_size = waiting.get_rect().size  # 이미지 크기 구해옴
    waiting_width = waiting_size[0]
    waiting_height = waiting_size[1]
    waiting_x_pos = (screen_width / 2) - (waiting_width / 2)
    waiting_y_pos = 580

    # < 텍스트 폰트 설정 >
    game_font = pygame.font.Font("ka1.ttf", 20)  # 폰트 객체 생성 (폰트, 크기)
    game_font2 = pygame.font.Font("ka1.ttf", 50)  # 폰트 객체 생성 (폰트, 크기)

    # <로딩 타임 설정 >
    loadingtime = 7

    # <시작 시간 정보 받아오기 >
    start_ticks = pygame.time.get_ticks()  # 현재(시작시점) 시간 tick을 받아옴

    # <Sound>
    bgsound = pygame.mixer.Sound("bgsound.wav")
    clicksound = pygame.mixer.Sound("select.wav")

    ####################### < 이벤트 루프 > ########################

    # < 이벤트 루프 > # 계속 running 되게 설정 + 이벤트 반복점검 -> 창이 닫히는 이벤트 발생 시 프로그램도 종료
    running = True  # 게임이 진행 중인가? = True

    # 1) 타이틀 런칭 + 로딩 구현 (O)
    # 2) 사용자 회원가입 및 로그인 구현 + 인게임 버튼 구현 ()

    bgsound.play()
    flag = False
    while running:

        frame = clock.tick(60)  # 게임화면의 초당 프레임 수 설정
        for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
            if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
                running = False  # 게임 종료

        launch_time = (pygame.time.get_ticks() - start_ticks) / 1000
        # 지금까지 흐른 시간 = 현재 시간 tick - 시작 시간 tick
        # 지금까지 흐른 시간, 즉 경과시간(ms)을 1000으로 나누어서 초(s) 단위로 표시한다

        # 타이틀 위치 변화 정의

        title_y_pos += title_speed  # y좌표 0으로부터 점점 5씩 내려간다

        # 타이틀 내려가다 스땁
        if title_y_pos > 60:  # 만약 타이틀이 경계를 넘어갔으면
            title_y_pos = 60  # 그 경계에서 스땁
            flag = True

        # 만약 시간이 0이하 이면 게임 종료
        if loadingtime - launch_time <= 0:
            bgsound.fadeout(3000)
            running = False

        screen.blit(startbg, (startbg_x_pos, startbg_y_pos))
        screen.blit(title, (title_x_pos, title_y_pos))
        screen.blit(name, (name_x_pos, name_y_pos))

        if flag:

            timer = game_font2.render(
                str(int(loadingtime - launch_time)), True, (171, 104, 157)
            )

            pls = "Please wait for the loading..."

            pls_ren = game_font.render((str(pls)), True, (253, 238, 216))

            # font.render(출력할 텍스트, True, 글자색상)
            screen.blit(waiting, ((screen_width / 2) - 240, 600))
            screen.blit(heart, ((screen_width / 2) - 75, 460))
            screen.blit(timer, ((screen_width / 2) - 20, 490))

        pygame.display.update()  # 게임화면을 계속 다시 그리기!

    # < 프로그램 종료 >
    pygame.quit()


launch()

main()

main2()
