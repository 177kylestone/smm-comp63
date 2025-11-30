def raw_to_vwc(raw):
    try:
        r = float(raw)
    except Exception:
        raise ValueError('raw must be numeric')
    v = (r / 1023.0) * 0.5
    return max(0.0, min(0.5, v))
