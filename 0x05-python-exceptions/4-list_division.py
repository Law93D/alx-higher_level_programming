#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                val_1 = my_list_1[i] if i < len(my_list_1) else None
                val_2 = my_list_2[i] if i < len(my_list_2) else None
                
                if not (isinstance(val_1, (int, float)) and isinstance(val_2, (int, float))):
                    if not isinstance(val_1, (int, float)):
                        print("out of range")
                    if not isinstance(val_2, (int, float)):
                        print("wrong type")
                    result.append(0)
                elif val_2 == 0:
                    print("division by 0")
                    result.append(0)
                else:
                    result.append(val_1 / val_2)
                    
            except (IndexError, TypeError):
                print("out of range")
                result.append(0)
    
    except:
        pass
    
    return result
