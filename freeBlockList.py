from block import Block


# 할당 :
# free space를 쭉 돌면서 최대한 딱 맞는 메모리 공간을 찾는다
# 만약 공간이 크면 쪼개서 남는 메모리를 free list에 넣어준다
# 공간 없으면 OS에게 chunk 요청 => 재할당 시도
# 연결리스트는 무조건 크기순으로 정렬되어 있어야 한다
class FreeBlockList:
    def __init__(self, total_size):
        pass

