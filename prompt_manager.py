# 기본 프롬프트 데이터
prompts = [
    {
        "title": "블로그 글 작성",
        "content": "주어진 주제로 초보자도 이해하기 쉬운 블로그 글을 작성해줘.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "이미지 생성 프롬프트",
        "content": "고품질의 사실적인 풍경 이미지를 생성하기 위한 프롬프트를 작성해줘.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "업무 자동화 아이디어",
        "content": "반복적인 업무를 자동화할 수 있는 아이디어를 구체적인 단계로 제안해줘.",
        "category": "자동화",
        "favorite": False
    }
]


def show_menu():
    """프로그램의 메인 메뉴를 출력합니다."""
    print("\n" + "=" * 40)
    print("          Prompt Manager")
    print("=" * 40)
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록 보기")
    print("0. 종료")
    print("=" * 40)


def main():
    """프로그램을 실행합니다."""
    print("Prompt Manager를 시작합니다.")

    while True:
        show_menu()

        choice = input("메뉴 번호를 선택하세요: ")

        if choice == "0":
            print("프로그램을 종료합니다.")
            break

        elif choice in ["1", "2", "3", "4", "5", "6", "7"]:
            print("해당 기능은 다음 단계에서 구현합니다.")

        else:
            print("잘못된 번호입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()