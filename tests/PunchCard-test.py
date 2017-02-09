import os
import PunchCard
import sys
import unittest

sys.path.insert(0, os.path.abspath('..'))


class CaclWorkTimeTests(unittest.TestCase):

    def test_returnsTwo_givenEightAndTenOclock(self):
        self.assertEqual(PunchCard.calcWorkTime('8:00', '10:00'), 2)

    def test_returnsZero_givenEightAndEightOclock(self):
        self.assertEqual(PunchCard.calcWorkTime('8:00', '8:00'), 0)

    def test_returnsFour_givenTenAndTwoOclock(self):
        self.assertEqual(PunchCard.calcWorkTime('10:00', '2:00'), 4)

    def test_returnsTwoAndHalf_givenEightThirtyAndElevenOclock(self):
        self.assertEqual(PunchCard.calcWorkTime('8:30', '11:00'), 2.5)

    def test_throwsError_givenAnIncorrectTime(self):
        with self.assertRaises(ValueError):
            PunchCard.calcWorkTime('a', '10:00')


class CalculateDayTests(unittest.TestCase):

    def test_returnsZero_givenEmptyArray(self):
        self.assertEqual(PunchCard.calculateDay([]), 0.0)

    def test_returnsZero_givenTwoEqualTimeEntries(self):
        self.assertEqual(PunchCard.calculateDay(['8:00', '8:00']), 0.0)

    def test_returnsEight_givenFourEntries(self):
        dayEntry = ['8:00', '12:00', '1:00', '5:00']
        self.assertEqual(PunchCard.calculateDay(dayEntry), 8.0)

    def test_returnsEight_givenTwoEntries(self):
        self.assertEqual(PunchCard.calculateDay(['8:00', '4:00']), 8.0)

    def test_throwsError_givenAnIncorrectTime(self):
        with self.assertRaises(ValueError):
            PunchCard.calculateDay(['a', '10:00'])


if __name__ == '__main__':
    unittest.main()
