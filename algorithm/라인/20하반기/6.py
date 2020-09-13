'''
다 못품 문제 잘못이해함
'''
def solution(companies, applicants):
    answer = []

    # 각 회사 별 선호도, 채용가능인원, 채용인원 딕셔너리 생성
    company_dict = dict()
    for company in companies:
        tmp = company.split(' ')
        company_dict[tmp[0]] = [tmp[1], int(tmp[2]), []]

    # 각 지원자 별 선호도, 지원횟수 딕셔너리 생성
    app_dict = dict()
    app_list = []
    for applicant in applicants:
        tmp = applicant.split(' ')
        app_dict[tmp[0]] = [tmp[1], int(tmp[2])]
        app_list.append(tmp[0])

    cur_round = 0
    # 1라운드부터 app_list가 있는동안 반복하기
    while app_list:
        # 원하는 기업에 지원한다.
        # 각 기업별로 지원자를 확인해야함
        tmp_com_dict = dict()
        for app in app_list:
            # 지원횟수 확인 후 지원하기
            if app_dict[app][1] > cur_round:
                ac = app_dict[app][0][cur_round]  # 지원할 회사
                if not tmp_com_dict.get(ac):
                    tmp_com_dict[ac] = [app]
                else:
                    tmp_com_dict[ac].append(app)
        # 각 기업별로 채용 시작

        tmp_app_list = []
        for company, apps in tmp_com_dict.items():
            # 전원 채용 가능하면 전원 채용
            if company_dict[company][1] >= len(apps):
                company_dict[company][1] -= len(apps)
                company_dict[company][2] += apps
            else:
                # 선호도 순으로 조회한다.
                # 조회되면 채용하다가 채용인원 다차면 종료
                tmpset = set()
                tcnt = company_dict[company][1]
                company_dict[company][1] = 0
                for prefer in company_dict[company][0]:
                    if prefer in apps:
                        tmpset.add(prefer)
                        company_dict[company][2].append(prefer)
                        tcnt -= 1
                    if not tcnt:
                        break
                # 채용 안된 인원들만 추가하기
                for app in apps:
                    if app not in tmpset:
                        tmp_app_list.append(app)
        # 채용 라운드 종료
        app_list = tmp_app_list
        cur_round += 1
    # 전체 채용 종료
    for k, v in company_dict.items():
        print(v)
        answer.append("{}_{}".format(k, ''.join(sorted(v[2]))))

    # 리젝되면 그때 지원가능횟수를 줄여야한다
    return answer

print(solution(["A fabdec 2", "B cebdfa 2", "C ecfadb 2"],["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]))