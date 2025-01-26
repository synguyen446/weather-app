def input_string(prompt, target_character=False, max_character=False):
    if not max_character and not target_character:
        user_input = input(prompt)
        return user_input
    elif target_character:
        user_input = input(prompt)
        while len(user_input) != target_character:
            print(f"Input must be exactly {target_character} charactes")
            user_input = input(prompt)
        return user_input
    else:
        user_input = input(prompt)
        while len(user_input) > max_character:
            print(f"Input must be less than {max_character} characters")
            user_input = input(prompt)
        return user_input
