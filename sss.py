def is_valid_substitution_cipher(original, encoded):
    if len(original) != len(encoded):
        return False  # Lengths must match
    
    mapping = {}  # Maps original letters to encoded letters
    reverse_mapping = {}  # Ensures unique substitution (one-to-one)

    for o, e in zip(original, encoded):
        if o in mapping:
            if mapping[o] != e:
                return False  # Inconsistent mapping
        else:
            if e in reverse_mapping:
                return False  # Ensures one-to-one mapping
            mapping[o] = e
            reverse_mapping[e] = o  # Reverse mapping to prevent reuse
    
    return True

# Example cases
print(is_valid_substitution_cipher("BOOK", "CXYZ"))  # False (O → X, O → Y)
print(is_valid_substitution_cipher("BOOK", "CXXK"))  # False (K → K)
print(is_valid_substitution_cipher("BOOK", "CXXZ"))  # True (Valid mapping)
