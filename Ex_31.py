C_kPa_PSI = 6.895
C_kPa_mmHg = 7.501
C_kPa_ATM = 101.3

pressure_kPa = float(input('Введите давление в кПа: '))
psi = pressure_kPa / C_kPa_PSI
mmHg = pressure_kPa * C_kPa_mmHg
atm = pressure_kPa / C_kPa_ATM
print('Давление в PSI %.3f; Давление в мм.рт.ст %.3f; Атмосферное давление %.3f.' % (psi, mmHg, atm)) 