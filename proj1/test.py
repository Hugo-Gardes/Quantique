from bolchClass import bolchSphereCalc
import numpy as np

def test(beta, teta):
    exCour = bolchSphereCalc(beta, teta)
    exCour.initAll()
    return (exCour)


def checkRes(res, expect):
    # print()
    # if ((round(res.X, 2) <= round(expect[0], 2) * 1.3 and round(res.X, 2) >= round(expect[0], 2) * 0.7) or (round(res.X, 2) * 1.3 <= round(expect[0], 2) and round(res.X, 2) * 0.7 >= round(expect[0], 2))):
    #     if ((round(res.Y, 2) <= round(expect[2], 2) * 1.3 and round(res.Y, 2) >= round(expect[2], 2) * 0.7) or (round(res.Y, 2) * 1.3 <= round(expect[2], 2) and round(res.Y, 2) * 0.7 >= round(expect[2], 2))):
    #         if ((round(res.Z) <= round(expect[1], 2) * 1.3 and round(res.Z, 2) >= round(expect[1], 2) * 0.7) or (round(res.Z, 2) * 1.3 <= round(expect[1], 2) and round(res.Z, 2) * 0.7 >= round(expect[1], 2))):
    #             print(f"test1 is passed: expected: [x: {expect[0]}, z: {expect[2]}, y: {expect[1]}]\nobtain: [x: {res.X}, z: {res.Z}, y: {res.Y}]")
    #         else:
    #             print(f"test1 failed: expected Z={expect[2]} but obtained Z={res.Z}")
    #     else:
    #         print(f"test1 failed: expected Y={expect[1]} but obtained Y={res.Y}")
    # else:
    #     print(f"test1 failed: expected X={expect[0]} but obtained X={res.X}")
    print(f"expected: [x: {expect[0]}, z: {expect[2]}, y: {expect[1]}]\nobtain: [x: {res.X}, z: {res.Z}, y: {res.Y}]")

res = test(np.sqrt(2/3), np.sqrt(1/3))
expect = [2 * np.sqrt(2) / 3, 0, 1 / 3]

checkRes(res, expect)