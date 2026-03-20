distance_mi = 0.5
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = False

# distance false
if not distance_mi:
    print(False)
# 1 > , not raining
elif distance_mi <= 1 and not is_raining:
    print(True)
# 1 > , raining
elif distance_mi <= 1 and is_raining:
    print(False)
# 6 > distance > 1, raining, no bike
elif 6 >= distance_mi > 1 and is_raining and not has_bike:
    print(False)
# 6 > distance > 1, not raining, no bike
elif 6 >= distance_mi > 1 and not is_raining and not has_bike:
    print(False)
# 6 > distance > 1, not raining, has bike
elif 6 >= distance_mi > 1 and not is_raining and has_bike:
    print(True)
# distance > 6, has share app
elif distance_mi > 6 and has_ride_share_app:
    print(True)
# distance > 6, has car
elif distance_mi > 6 and has_car:
    print(True)
# distance > 6, has share app, has car
elif distance_mi > 6 and has_ride_share_app and has_car:
    print(True)
else:
    print(False)