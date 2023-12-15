import pytest
from CodeChallengesModule import u_n_x, SeriesSolver

test_data = [
    (3, 2, 36),
    (4, 0.5, 1.625),
    (7, 8, 16434824),
    (8, 1.6, 7298167)

]


class TestSeriesFunction():

    @pytest.mark.parametrize("n, x, expected_result", [
        (3, 2, 34),
        (4, 0.5, 1.625),
        (7, 8, 16434824),
        (8, 1.6, 729.8166988800003),
    ])
    def test_u_n_x_small_values(self, n, x, expected_result):
        # Test the function with small values
        assert u_n_x(n, x) == expected_result  # Replace 'expected_value' with the actual expected result

    @pytest.mark.parametrize("m, expected_result", [
        (2.0, 0.5),
        (8.0, 0.7034648345913732)
    ])
    def test_series_solver_solve(self, m, expected_result):
        x = SeriesSolver.solve(2.0)
        assert x == expected_result

