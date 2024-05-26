from datetime import datetime

now_date = int(datetime.now().strftime("%Y")) + 1


def year_choice():
    return ((year, year) for year in range(2011, now_date))


RATING = (
    (1, '★✩✩✩✩'),
    (2, '★★✩✩✩'),
    (3, '★★★✩✩'),
    (4, '★★★★✩'),
    (5, '★★★★★'),
)


GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )


DISCOUNT_CHOICES = (
    (5, "5% off"),
    (10, "10% off"),
    (15, "15% off"),
    (20, "20% off"),
    (25, "25% off"),
    (30, "30% off"),
    (40, "40% off"),
    (50, "50% off"),
)


HOUSE_STATUS_CHOICES = (
    (10, "10% off"),
    (15, "15% off"),
    (20, "20% off"),
    (25, "25% off"),
    (200, "from 200$"),
    (230, "from 230$"),
    (250, "from 250$"),
    (300, "from 300$"),
)


TICKET_STATUS_CHOICES = (
    ("Pending", "Pending"),
    ("Canceled", "Canceled"),
    ("Approved", "Approved"),
)


PARKING_AREAS_CHOICES = (
    ("Nonstop", "Nonstop"),
    ("1 Stop", "1 Stop"),
    ("2+ Stop", "2+ Stop"),
)


CARD_TYPE_CHOICES = (
    ("Visa", "Visa"),
    ("Mastercard", "Mastercard"),
)


WORK_TYPE = (
    ("Part time", "Part Time"),
    ("Full time", "Full Time"),
    ("Shift work", "Shift Work"),
)


STATUS = (
    ("active", "Active"),
    ("deactive", "Deactive"),
)


WORKING_CONDITION = (
    ("remote", "Remote"),
    ("in office", "In office"),
)


CLASS_OF_SERVİCES_CHOICES = (
    ("economy", "Economy"),
    ("comfort", "Comfort"),
    ("business", "Business"),
    ("first", "First"),
)


ROOMS_COUNT_CHOICES = (
    (1, "1 Room"),
    (2, "2 Rooms"),
    (3, "3 Rooms"),
    (4, "4 Rooms and more"),
)


POSITION_CHOICES = (
    ("Frontend developer", "Frontend Developer"),
    ("Backend developer", "Backend Developer"),
    ("Database administrator", "Database Administrator"),
    ("Sales representative", "Sales Representative"),
    ("Sales manager", "Sales Manager"),
    ("Web developer", "Web Developer"),
    ("senior travel assistant", "Senior Travel Assistant"),
    ("Travel coordinator", "Travel Coordinator"),
)