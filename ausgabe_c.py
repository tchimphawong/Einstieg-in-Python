x = 100/7
y = 7/2

print("Format f, Standard:   %f %f %f" % (x, x, y))
print("Format f, nach Komma: %.25f" % (x))
print("Format f, gesamt:     %15.10f" % (x))

print("Format e, Standard:   %e" %(x))
print("Format e, nach Komma: %.3e" % (x))
print("Format e, gesamt:     %12.3e" % (x))

print("Format %%, Standard:   %f%%" % (y*100))
print("Format %%, nach Komma: %.3f%%" % (y*100))
print("Format %%, gesamt:     %12.3f%%" % (y*100))


