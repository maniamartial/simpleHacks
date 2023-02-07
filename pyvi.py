import time
import rotatescreen as rs
pd = rs.get_primary_display()
angles = [90, 180, 270, 0]

for i in range(5):
    for x in angles:
        pd.rotate_to(x)
        time.sleep(0.5)
        print("Mania")
