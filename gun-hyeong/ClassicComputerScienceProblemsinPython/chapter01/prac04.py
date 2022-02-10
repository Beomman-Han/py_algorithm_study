from typing import Tuple
from sys import getsizeof
from secrets import token_bytes

class Image_EncAndDec:
    def __init__(self, filename):
        self._file_bytes : bytes = open(filename, "rb").read()

    def encrypt(self) -> Tuple[int, int]:                                        # str ->  byte -> int -> XOR연산   
        dummy: int = int.from_bytes(token_bytes(len(self._file_bytes)) , "big" )
        original_key: int = int.from_bytes(self._file_bytes , "big")
        encrypted: int = original_key ^ dummy  #XOR연산 
        return dummy, encrypted # 튜플 반환 

    def decrypt(self, key1, key2) -> str:
        decrypted: int = key1 ^ key2 #XOR연산
        temp: bytes = decrypted.to_bytes(len(self._file_bytes)  , "big")
        return temp




if __name__ == "__main__":
    test = Image_EncAndDec("/home/coder/py_algorithm_study/gun-hyeong/ClassicComputerScienceProblemsinPython/chapter01/birth.PNG")
    key1, key2 = test.encrypt()
    #print(type(key1))
    p#rint(type(key2))
    result : str = test.decrypt(key1,key2)
    print(result)
    print(f"원본과 비교 :{test._file_bytes == result}")


