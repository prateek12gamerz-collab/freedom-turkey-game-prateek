turkey.onA(function on_on_a() {
    turkey.turkeyJump()
})
turkey.onStartSimple(function on_start_simple() {
    turkey.addTurkey()
})
turkey.onCages(15, function on_on_cages() {
    turkey.turkeyWin()
})
turkey.turkeyOverlapCage(function on_turkey_overlap_cage() {
    turkey.changeScoreOverride(1)
    turkey.freeTurkey()
})
