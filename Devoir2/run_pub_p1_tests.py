from binary_domain import *

if __name__ == "__main__":
    test1 = ["10100011", "10110100", "00010111"]
    test2 = ["10101111", "11000110", "01101001"]
    test3 = ["11001101", "01001001","101001101", "01100111"]
    test4 = ["00001011", "01100101","101001101", "01010000"]
    test5 = ["11101111", "101001101","01001101"]
    test6 = ["01011000","101001101", "10100010"]

    #1) Addition tests
    SCORE = 0
    bd = BinaryDomains()
    SCORE += (bd.add(test1[0],test1[1]) == test1[2])*0.5
    SCORE += (bd.add(test2[0],test2[1]) == test2[2])*0.5

    print("Votre note pour les tests 'add' est de "+str(SCORE)+"/1.0")

    #2) Multiply tests
    SCORE = 0
    SCORE += (bd.multiply(test3[0],test3[1],test3[2]) == test3[3])*0.5
    SCORE += (bd.multiply(test4[0],test4[1],test4[2]) == test4[3])*0.5

    print("Votre note pour les tests 'multiply' est de "+str(SCORE)+"/1.0")

    #3) Inverse tests
    SCORE = 0
    SCORE += (bd.inverse(test5[0],test5[1]) == test5[2])*0.5
    SCORE += (bd.inverse(test6[0],test6[1]) == test6[2])*0.5

    print("Votre note pour les tests 'inverse' est de "+str(SCORE)+"/1.0")
    