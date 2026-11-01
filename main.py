def on_on_a():
    turkey.turkey_jump()
turkey.on_a(on_on_a)

def on_start_simple():
    turkey.add_turkey()
turkey.on_start_simple(on_start_simple)

def on_on_cages():
    turkey.turkey_win()
turkey.on_cages(15, on_on_cages)

def on_turkey_overlap_cage():
    turkey.change_score_override(1)
    turkey.free_turkey()
turkey.turkey_overlap_cage(on_turkey_overlap_cage)
