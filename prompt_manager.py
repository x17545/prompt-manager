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


def add_prompt():
    """새로운 프롬프트를 추가합니다."""
    print("\n[프롬프트 추가]")

    while True:
        title = input("제목을 입력하세요: ").strip()
        if title:
            break
        print("제목은 비워둘 수 없습니다.")

    while True:
        content = input("내용을 입력하세요: ").strip()
        if content:
            break
        print("내용은 비워둘 수 없습니다.")

    categories = [
        "텍스트 생성",
        "이미지 생성",
        "영상 생성",
        "페르소나",
        "자동화",
        "기타"
    ]

    print("\n카테고리를 선택하세요.")

    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    while True:
        category_choice = input("카테고리 번호를 입력하세요: ").strip()

        if category_choice.isdigit():
            category_index = int(category_choice)

            if 1 <= category_index <= len(categories):
                category = categories[category_index - 1]
                break

        print("올바른 카테고리 번호를 입력해주세요.")

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)

    print("\n프롬프트가 추가되었습니다.")

def show_list():
    """저장된 모든 프롬프트를 목록으로 보여줍니다."""
    print("\n[프롬프트 목록]")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        favorite_mark = "⭐" if prompt["favorite"] else ""

        print(
            f"{index}. {prompt['title']} "
            f"| 카테고리: {prompt['category']} "
            f"{favorite_mark}"
        )

def show_category():
    """카테고리를 선택하여 해당 프롬프트를 보여줍니다."""
    print("\n[카테고리별 조회]")

    categories = [
        "텍스트 생성",
        "이미지 생성",
        "영상 생성",
        "페르소나",
        "자동화",
        "기타"
    ]

    print("카테고리를 선택하세요.")

    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    while True:
        category_choice = input("카테고리 번호를 입력하세요: ").strip()

        if category_choice.isdigit():
            category_index = int(category_choice)

            if 1 <= category_index <= len(categories):
                selected_category = categories[category_index - 1]
                break

        print("올바른 카테고리 번호를 입력해주세요.")

    found = False

    print(f"\n[{selected_category}] 프롬프트")

    for index, prompt in enumerate(prompts, start=1):
        if prompt["category"] == selected_category:
            favorite_mark = "⭐" if prompt["favorite"] else ""

            print(
                f"{index}. {prompt['title']} "
                f"| 카테고리: {prompt['category']} "
                f"{favorite_mark}"
            )

            found = True

    if not found:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")

def search_prompt():
    """제목 또는 내용에 포함된 키워드로 프롬프트를 검색합니다."""
    print("\n[프롬프트 검색]")

    keyword = input("검색할 키워드를 입력하세요: ").strip()

    if not keyword:
        print("검색어를 입력해주세요.")
        return

    found = False

    print(f"\n'{keyword}' 검색 결과")

    for index, prompt in enumerate(prompts, start=1):
        if keyword.lower() in prompt["title"].lower() or keyword.lower() in prompt["content"].lower():
            favorite_mark = "⭐" if prompt["favorite"] else ""

            print(
                f"{index}. {prompt['title']} "
                f"| 카테고리: {prompt['category']} "
                f"{favorite_mark}"
            )

            found = True

    if not found:
        print("검색 결과가 없습니다.")

def show_detail():
    """선택한 프롬프트의 상세 내용을 보여줍니다."""
    print("\n[프롬프트 상세 보기]")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    while True:
        number = input("상세하게 볼 프롬프트 번호를 입력하세요: ").strip()

        if number.isdigit():
            index = int(number)

            if 1 <= index <= len(prompts):
                prompt = prompts[index - 1]
                break

        print("올바른 프롬프트 번호를 입력해주세요.")

    favorite_mark = "⭐" if prompt["favorite"] else "☆"

    print("\n" + "=" * 40)
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {favorite_mark}")
    print("내용:")
    print(prompt["content"])
    print("=" * 40)

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

        elif choice == "1":
            add_prompt()
            
        elif choice == "2":
            show_list()

        elif choice == "3":
            show_category()

        elif choice == "4":
            search_prompt()

        elif choice == "5":
            show_detail()

        elif choice in ["6", "7"]:
            print("해당 기능은 다음 단계에서 구현합니다.")

        else:
            print("잘못된 번호입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()