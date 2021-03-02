from datetime import datetime

from django.core.exceptions import ValidationError


def validate_year(year):
    current_year = datetime.now().year
    if year > current_year:
        raise ValidationError(
            f'Title cannot be created later than {current_year}'
        )


def validate_score(score):
    if score < 1 or score > 10:
        raise ValidationError(
            f'Score cannot be less than 1 or greater than 10'
        )
