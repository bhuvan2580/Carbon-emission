def choose_best_dc(dc_list):
    return sorted(dc_list, key=lambda x: x['carbon_intensity'])[0]