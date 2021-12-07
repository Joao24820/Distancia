dm = float(input('Informe a distancia em metros: '))

km = (dm / 1000)
hm = (dm / 100)
dam = (dm / 10)
dm = (dm * 10)
cm = (dm * 100)
mm = (dm * 1000)

print('O valor \nem KM {}\nem HM {} \nem DAM {}\nem DM {}\nem CM {:.0f}\nem MN {:.0f}'
      .format(km, hm, dam, dm, cm, mm))
