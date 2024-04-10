from datetime import datetime


def get_stripe_api_version_as_date(stripe):
    return datetime.strptime(stripe.api_version, "%Y-%m-%d")

def get_stripe_version():
    current_date = datetime.now().date()
    checkpoint_date = datetime(current_date.year, 6, 22).date()
    return not current_date < checkpoint_date