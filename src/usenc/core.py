from .encoders import ENCODERS

def encode(text: str, encoder_name: str, **encoder_params) -> str:
    """Encode a single text string"""
    encoder = ENCODERS.get(encoder_name)
    if not encoder:
        raise ValueError(f"Unknown encoder: {encoder_name}")

    return encoder.encode(text, **encoder_params)

def decode(text: str, encoder_name: str, **encoder_params) -> str:
    """Decode a single text string"""
    encoder = ENCODERS.get(encoder_name)
    if not encoder:
        raise ValueError(f"Unknown encoder: {encoder_name}")

    return encoder.decode(text, **encoder_params)

