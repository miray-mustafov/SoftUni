class Validator:
    @staticmethod
    def raise_if_len_is_less_than(value, min_len, err_message):
        if len(value) < min_len:
            raise ValueError(err_message)

    def validate_speed_limit(value, min, max, err_message):
        if not min <= value <= max:
            raise ValueError(f"Invalid speed limit! Must be between {min} and {max}!")