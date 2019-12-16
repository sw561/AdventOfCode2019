
import cProfile

with cProfile.Profile() as pr:
    # import test
    import solve
    solve.main()

pr.print_stats('cumulative')
