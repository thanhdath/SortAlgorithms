def HNTower(n, toa_mot, toa_hai, toa_ba):
	if n == 1:
		print("chuyen tu ", toa_mot, " sang ", toa_ba)
	else:
		HNTower(n-1, toa_mot, toa_ba, toa_hai)
		print("chuyen tu ", toa_mot, " sang ", toa_ba)
		HNTower(n-1, toa_hai, toa_mot, toa_ba)
