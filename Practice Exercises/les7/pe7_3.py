rapporten = {'Ahmad':7.0, 'Mike':10.0, 'Ben':4.4, 'Kees':2.6, 'Adriaan':6.6, 'Gijs':7.2, 'Johan':9.3, 'Dennis':9.8}
uitslag = rapporten.items()
for gegeven in uitslag:
    if gegeven[1] >= 9:
        print(gegeven[0], gegeven[1])
