arr = list(map(int,input().split(',')))
ijk= list(map(int,input().split(',')))
commands = [arr,ijk]
def solution(commands):
    a = arr[ijk[0] - 1: ijk[1]]
    a.sort()
    
    result = print('{0}를 {1}번째부터 {2}번째까지 자른 후 정렬합니다.{3}의 {4} 번째 숫자는 {5}입니다.'.format(arr,ijk[0],ijk[1],a,ijk[2],a[ijk[2]]-1))
    return result
solution(commands)







