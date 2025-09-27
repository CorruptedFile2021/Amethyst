def scaled_for_screen(base_w, base_h, base_screen_w, base_screen_h, current_screen_w, current_screen_h):
    # Compute scaling factors
    scale_w = current_screen_w / base_screen_w
    scale_h = current_screen_h / base_screen_h
    # Take the smaller scale to keep proportions
    scale = min(scale_w, scale_h)
    
    new_w = int(base_w * scale)
    new_h = int(base_h * scale)
    
    return new_w, new_h




