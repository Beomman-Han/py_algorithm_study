class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)
    
    def _compress(self, gene: str)-> None:
        self.bit_string: int = 1 #왜 1로 시작하는지 ?? 
        for nucleotide in gene.upper():
            self.bit_string <<= 2

            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError(f"유효하지 않은 뉴클레오티드 입니다: {nucleotide}")
    def decompress(self) -> str:
        gene: str = ""
        for i in range(0,self.bit_string.bit_length()-1, 2):    #ex) a=4 , bin(a) : 0b100 a.bit_length() : 3 
            bits: int = self.bit_string >> i & 0b11  #마지막 2비트를 추출한다.   (1이면 1 0이면 0 을 반환 한다.)
            if bits == 0b00: # A
                gene += "A"
            elif bits == 0b01: # C
                gene += "C"
            elif bits == 0b10: # G
                gene += "G"
            elif bits == 0b11: # T
                gene += "T"
            else:
                raise ValueError(f"Invaild bits:{bits}")
        return gene[::-1]
    def __str__(self) -> str:
        return self.decompress()

if __name__ =="__main__":
    from sys import getsizeof  # byte알려주는 함수 
    original: str = "ATGACAGATAGACCACAGAGAATAAGACAGAGACA" * 100
    print(f"원본: {getsizeof(original)} 바이트")
    compressed: CompressedGene = CompressedGene(original)
    print(f"압축: {getsizeof(compressed.bit_string)} 바이트")
    print(compressed) #압축해제 print 호출 되면서 __str__ 메소드 호출 되고 decompress 메소드 호출되어 압축 해제 됨
    print(f"원본 문자열과 압축 해제한 문자열은 같습니까? {original == compressed.decompress()}")



# a = CompressedGene("ATGC")

#print(bin(a.bit_string))