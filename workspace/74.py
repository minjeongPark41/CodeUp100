base = ord(input()) #입력 문자를 ord 숫자로 변환
start = ord('a') #a부터 출력해줘야 하니 있어야지

while base>=start: #입력값이 a보다 클 때 ~ 
    print(chr(start)) #먼저 a를 출력하고
    start+=1 # 다음은 b를 출력해야겠지
