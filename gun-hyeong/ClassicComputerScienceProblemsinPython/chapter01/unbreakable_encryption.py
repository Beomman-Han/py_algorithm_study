###OTP###########################################################################
# 원본데이터와 의미 없는 무작위 더미 데이터를 결합하여 원본 데이터를 암호화함                     #
# 프로덕트키 , 더미데이터키                                                           #
# 둘중 하나만 있으면 암호를 풀지 못함                                                   #
# 더미데이터의 기준                                                                 #
    # 원본데이터의 길이와 같아야함                                                     #
    # 무작위여야함 (여기선 secrets 모듈 활용)                                          #
    # 비밀이어야함 (공개되면 안됨 )                                                    #
#################################################################################

from secrets import token_bytes
from typing import Tuple

###사용된 함수 ###

#   token_bytes(n) -> n만큼 임의의 바이트를 생성한다.
#   int.from_bytes(bytes, byteorder) -> 바이트를 비트 문자열로 변환한 후 정수를 반환 한다. 
#   int.to_bytes(length, byteorder)  -> 정수를 바이트로 반환해 준다. 인자로 정수가 변환한 바이트 수를 인자로 취한다.
    #   이때 만약 1바이트에 넣을수 있는 최대수 255를 넘는경우에 int.to_bytes(length, byteorder)에서 length의 1을 넘게 될경우 overflow가 발생한다. 




def random_key(length: int) -> int:
    #length만큼 임의의 바이트를 생성한다.
    tb: bytes = token_bytes(length)  # 10byte -> 80비트 정수 까지 생성 가능 ? 

    #바이트를 비트 문자열로 변환 후 반환
    return int.from_bytes(tb, "big")



b = random_key(1)

print(b)

a= 0b11111111

print(int(a))

def encrypt(original: str) -> Tuple[int, int]:                                        # str ->  byte -> int -> XOR연산 
    original_bytes: bytes = original.encode()  #original을 바이트로 변환
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes , "big")
    encrypted: int = original_key ^ dummy  #XOR연산 
    return dummy, encrypted # 튜플 반환 

def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2 #XOR연산
    temp: bytes = decrypted.to_bytes(decrypted.bit_length()+ 7 // 8, "big")  #7을 더하는 이유 : off-by-one 오류를 피하기 위해서 
    return temp.decode()

if __name__ == "__main__":
    key1, key2 = encrypt("One Time Pad!")
    result : str = decrypt(key1, key2)
    print(result)