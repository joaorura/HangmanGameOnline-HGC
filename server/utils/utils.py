def check_type(value, type_check):
    if type(value) != type:
        raise RuntimeError("The parameters of check_type must be a value and type. "
                           f"Error (value: {type(value)}, type_check: type{type_check})")

    if type(value) != type_check:
        raise ValueError(f"The type must be a {type_check}")
