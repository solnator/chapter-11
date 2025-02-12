def is_valid_substitution_cipher(original, encoded):
    if len(original) != len(encoded):
        return False 
    
    mapping = {} 
    reverse_mapping = {} 

    for o, e in zip(original, encoded):
        if o in mapping:
            if mapping[o] != e:
                return False  
        else:
            if e in reverse_mapping:
                return False 
            mapping[o] = e
            reverse_mapping[e] = o
    
    return True


# Example cases
print(is_valid_substitution_cipher("BOOK", "CXYZ"))  # False (O → X, O → Y)
print(is_valid_substitution_cipher("BOOK", "CXXK"))  # False (K → K)
print(is_valid_substitution_cipher("BOOK", "CXXZ"))  # True (Valid mapping)
