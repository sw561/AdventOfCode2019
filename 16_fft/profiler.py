
import cProfile

with cProfile.Profile() as pr:
    import test

pr.print_stats('cumulative')
