from src.transform import run_all_queries


def test_run_queries():

    results = run_all_queries()

    assert "delays_by_airline" in results
    assert "delays_by_airport" in results
    assert "monthly_delay_trend" in results