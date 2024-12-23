
def is_simetric(input_string: str) -> bool:
    brakets = {'(': ')','[': ']','{':'}'}
    brakets_stak = []
    for ch in input_string:
        if ch in brakets:
            brakets_stak.append(ch)
        elif ch in brakets.values():
            if not brakets_stak:
                return False
            if ch != brakets[brakets_stak.pop()]:
                return False
    
    if len(brakets_stak) == 0:
        return True
    else:
        return False

test_cases = ["( ){[ 1 ]( 1 + 3 )( ){ }}", "( 23 ( 2 - 3);", "( 11 }"]

for test in test_cases:
    result = is_simetric(test)
    print(f"{test}: {result}") 
            


    