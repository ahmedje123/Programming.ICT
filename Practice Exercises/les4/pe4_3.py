lengte = eval(input('Wat is je lengte in centimeters?'))


def lang_genoeg(lengte):
    if lengte >= 120:
        print('Je mag erin!')
    else:
        print('Helaas je mag er niet in.')


lang_genoeg(lengte)